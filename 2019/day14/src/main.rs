use std::collections::HashMap;
use std::fs;

struct ReactionDependency {
    name: String,
    count: u64,
}

struct Reaction {
    product_name: String,
    produced_quantity: u64,
    dependencies: Vec<ReactionDependency>,
}

fn get_input() -> HashMap<String, Reaction> {
    let mut mappings = HashMap::<String, Reaction>::new();
    let input = fs::read_to_string("input.txt").unwrap();

    let _split = |item: &str| {
        let mut rsplit = item.split(" ");
        let produced_quantity = rsplit.next().unwrap().parse::<u64>().unwrap();
        let product_name = rsplit.next().unwrap().to_owned();
        (product_name, produced_quantity)
    };

    input.trim().split("\n").for_each(|line| {
        let mut split = line.split(" => ");
        let lhs = split.next().unwrap();
        let rhs = split.next().unwrap();

        let (product_name, produced_quantity) = _split(rhs);
        let dependencies: Vec<ReactionDependency> = lhs
            .split(", ")
            .map(_split)
            .map(|(name, count)| ReactionDependency { name, count })
            .collect();

        mappings.insert(
            product_name.clone(),
            Reaction {
                product_name,
                produced_quantity,
                dependencies,
            },
        );
    });
    mappings
}

fn part1_recursive_helper(
    item: &str,
    quantity: u64,
    mappings: &HashMap<String, Reaction>,
    surplus_mapping: &mut HashMap<String, u64>,
    ore_count: &mut u64,
) {
    let mut quantity = quantity;

    if item == "ORE" {
        *ore_count += quantity;
        return;
    }

    let surplus = surplus_mapping.entry(item.to_string()).or_default();

    if *surplus >= quantity {
        *surplus -= quantity;
        return;
    } else {
        quantity -= *surplus;
        *surplus = 0;
    }

    let reaction = mappings.get(item).unwrap();

    let num_reaction: u64 = ((quantity as f64) / (reaction.produced_quantity as f64)).ceil() as u64;

    let surplus_produced = reaction.produced_quantity * num_reaction - quantity;

    *surplus_mapping.entry(item.to_string()).or_default() += surplus_produced;

    for dependency in reaction.dependencies.iter() {
        part1_recursive_helper(
            dependency.name.as_str(),
            dependency.count * num_reaction,
            &mappings,
            surplus_mapping,
            ore_count,
        );
    }
}

fn part1(mappings: &HashMap<String, Reaction>, c: u64) -> u64 {
    let mut surplus = HashMap::new();
    let mut ore_count = 0;
    part1_recursive_helper("FUEL", c, &mappings, &mut surplus, &mut ore_count);

    ore_count
}

fn part2(mappings: &HashMap<String, Reaction>, min_ores_per_fuel: u64) -> u64 {
    let max_ores = 1000000000000;

    let mut start = std::u64::MIN;
    let mut end = min_ores_per_fuel * 5;

    while start <= end {
        let mid = start + ((end - start) / 2);
        let ore_count = part1(&mappings, mid);
        if ore_count == max_ores {
            return mid;
        } else if ore_count > max_ores {
            end = mid - 1;
        } else if ore_count < max_ores {
            start = mid + 1;
        }
    }

    end
}

fn main() {
    let mappings = get_input();
    let p1 = part1(&mappings, 1);
    let p2 = part2(&mappings, p1);

    println!("Part 1: {}", p1);
    println!("Part 2: {}", p2);
}
