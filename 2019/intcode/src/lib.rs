pub enum Parameter {
    Position(i64),
    Immediate(i64),
    Relative(i64),
}

pub enum Instruction {
    Add((Parameter, Parameter, Parameter)),
    Mul((Parameter, Parameter, Parameter)),
    Input(Parameter),
    Output(Parameter),
    JumpIfTrue((Parameter, Parameter)),
    JumpIfFalse((Parameter, Parameter)),
    LessThan((Parameter, Parameter, Parameter)),
    Equals((Parameter, Parameter, Parameter)),
    RelativeBaseOffset(Parameter),
    Halt,
}

#[derive(PartialEq)]
pub enum Signal {
    NeedsInput,
    ProducedOutput,
    Halt,
    None,
}

pub struct IntCodeComputer {
    memory: Vec<i64>,
    input: Vec<i64>,
    output: Option<i64>,
    relative_base_offset: i64,
    ip: usize,
}

impl IntCodeComputer {
    pub fn new() -> Self {
        IntCodeComputer {
            memory: Vec::new(),
            input: Vec::new(),
            output: None,
            relative_base_offset: 0,
            ip: 0,
        }
    }

    fn load_memory(&mut self, memory: Vec<i64>) -> &mut Self {
        self.memory = memory;
        self.ip = 0;
        self
    }

    fn roll_back_input_instruction(&mut self) {
        self.ip -= 2;
    }

    fn set_input(&mut self, input: Vec<i64>) -> &mut Self {
        self.input = input;
        self
    }

    fn try_resize_memory(&mut self, i: i64) {
        let i = i as usize;
        if self.memory.len() <= i {
            self.memory.resize(i + 1, 0);
        }
    }

    pub fn get_value_at_pos(&mut self, i: i64) -> i64 {
        if (i as usize) >= self.memory.len() {
            return 0;
        }
        self.memory[i as usize]
    }

    pub fn store_value_at_pos(&mut self, i: i64, value: i64) {
        self.try_resize_memory(i);
        self.memory[i as usize] = value;
    }

    fn fetch_word(&mut self) -> i64 {
        let word = self.get_value_at_pos(self.ip as i64);
        self.ip += 1;
        word
    }

    fn _fetch_parameter(&mut self, mode: i64) -> Parameter {
        let word = self.fetch_word();
        match mode {
            0 => Parameter::Position(word),
            1 => Parameter::Immediate(word),
            2 => Parameter::Relative(word),
            _ => panic!("unknown parameter mode"),
        }
    }

    fn fetch_param1(&mut self, opcode: i64) -> Parameter {
        self._fetch_parameter(opcode % 10)
    }

    fn fetch_param2(&mut self, mut opcode: i64) -> (Parameter, Parameter) {
        let p1 = self.fetch_param1(opcode);
        opcode /= 10;
        let p2 = self._fetch_parameter(opcode % 10);
        (p1, p2)
    }

    fn fetch_param3(&mut self, mut opcode: i64) -> (Parameter, Parameter, Parameter) {
        let (p1, p2) = self.fetch_param2(opcode);
        opcode /= 100;
        let p3 = self._fetch_parameter(opcode % 10);
        (p1, p2, p3)
    }

    fn unwrap_value(&mut self, param: Parameter) -> i64 {
        match param {
            Parameter::Immediate(val) => val,
            Parameter::Position(pos) => self.get_value_at_pos(pos),
            Parameter::Relative(pos) => self.get_value_at_pos(pos + self.relative_base_offset),
        }
    }

    fn store_val(&mut self, param: Parameter, val: i64) {
        match param {
            Parameter::Position(out) => {
                self.store_value_at_pos(out, val);
            }
            Parameter::Relative(out) => {
                self.store_value_at_pos(self.relative_base_offset + out, val);
            }
            _ => panic!("can not store to parameter in immediate mode"),
        }
    }

    fn emit_output(&mut self, param: Parameter) {
        self.output = Some(self.unwrap_value(param));
    }

    fn jump(&mut self, param: Parameter) {
        self.ip = self.unwrap_value(param) as usize;
    }

    pub fn feed_input(&mut self, inp: i64) {
        self.input.push(inp);
    }

    fn fetch_instruction(&mut self) -> Instruction {
        let mut opcode = self.fetch_word();
        let inst = opcode % 100;
        opcode /= 100;

        match inst {
            1 => Instruction::Add(self.fetch_param3(opcode)),
            2 => Instruction::Mul(self.fetch_param3(opcode)),
            3 => Instruction::Input(self.fetch_param1(opcode)),
            4 => Instruction::Output(self.fetch_param1(opcode)),
            5 => Instruction::JumpIfTrue(self.fetch_param2(opcode)),
            6 => Instruction::JumpIfFalse(self.fetch_param2(opcode)),
            7 => Instruction::LessThan(self.fetch_param3(opcode)),
            8 => Instruction::Equals(self.fetch_param3(opcode)),
            9 => Instruction::RelativeBaseOffset(self.fetch_param1(opcode)),
            99 => Instruction::Halt,
            _ => panic!("unknown instruction"),
        }
    }

    pub fn get_output(&mut self) -> Option<i64> {
        let ret = self.output;
        self.output = None;
        ret
    }

    pub fn tick(&mut self) -> Signal {
        let inst = self.fetch_instruction();
        match inst {
            Instruction::Add((param1, param2, param3)) => {
                let op1 = self.unwrap_value(param1);
                let op2 = self.unwrap_value(param2);
                self.store_val(param3, op1 + op2);
                return Signal::None;
            }
            Instruction::Mul((param1, param2, param3)) => {
                let op1 = self.unwrap_value(param1);
                let op2 = self.unwrap_value(param2);
                self.store_val(param3, op1 * op2);
                return Signal::None;
            }
            Instruction::Input(param) => {
                if self.input.is_empty() {
                    self.roll_back_input_instruction();
                    return Signal::NeedsInput;
                }
                let inp = self.input.remove(0);
                self.store_val(param, inp);
                return Signal::None;
            }
            Instruction::Output(param) => {
                self.emit_output(param);
                return Signal::ProducedOutput;
            }
            Instruction::JumpIfTrue((param1, param2)) => {
                if self.unwrap_value(param1) != 0 {
                    self.jump(param2);
                }
                return Signal::None;
            }
            Instruction::JumpIfFalse((param1, param2)) => {
                if self.unwrap_value(param1) == 0 {
                    self.jump(param2);
                }
                return Signal::None;
            }
            Instruction::LessThan((param1, param2, param3)) => {
                let op1 = self.unwrap_value(param1);
                let op2 = self.unwrap_value(param2);
                self.store_val(param3, if op1 < op2 { 1 } else { 0 });
                return Signal::None;
            }
            Instruction::Equals((param1, param2, param3)) => {
                let op1 = self.unwrap_value(param1);
                let op2 = self.unwrap_value(param2);
                self.store_val(param3, if op1 == op2 { 1 } else { 0 });
                return Signal::None;
            }
            Instruction::RelativeBaseOffset(offset) => {
                self.relative_base_offset += self.unwrap_value(offset);
                return Signal::None;
            }
            Instruction::Halt => return Signal::Halt,
        }
    }

    pub fn run_till_signal(&mut self, signal: Signal) {
        while self.tick() != signal {}
    }

    pub fn run(&mut self) -> Signal {
        let mut s = self.tick();
        while s == Signal::None {
            s = self.tick();
        }
        s
    }
}

pub fn get_computer(mem: &Vec<i64>, input: Vec<i64>) -> IntCodeComputer {
    let mut computer = IntCodeComputer::new();
    computer.load_memory(mem.clone()).set_input(input);
    computer
}