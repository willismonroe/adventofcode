import cProfile
import day14


command = "day14.solve('abc')"
print(command)
cProfile.run(command)

command = "day14.solve('ngcjuoqr')"
print(command)
cProfile.run(command)

command = "day14.solve('abc', True)"
print(command)
cProfile.run(command)

command = "day14.solve('ngcjuoqr', True)"
print(command)
cProfile.run(command)

command = "day14.solve_v2('abc')"
print(command)
cProfile.run(command)

command = "day14.solve_v2('ngcjuoqr')"
print(command)
cProfile.run(command)

command = "day14.solve_v2('abc', True)"
print(command)
cProfile.run(command)

command = "day14.solve_v2('ngcjuoqr', True)"
print(command)
cProfile.run(command)