use std::{collections::HashMap, fs, process::Output};

fn main() {
    let data = fs::read_to_string("data.txt").expect("A file");

    //part1(&data);
    part2(&data);
}

fn part1(data: &str) {
    //1. Parse data and create
    // - List of seeds
    // - Map of seed(key) to soil(val)
    // - ...
    let (seeds, maps) = parse_input(data);

    // for map in maps {
    //     let a = map.iter().inspect(|v| {
    //         dbg!(v);
    //     });
    // }
    //2. Crete the location vector:
    // - For each map, if the key is present we return the value, else we return the key.
    let locations: Vec<_> = seeds
        .iter()
        .map(|seed| {
            let mut val = seed.clone();
            for map in maps.iter() {
                // Check if val is in range
                for m in map.iter() {
                    if val <= m.1 + m.2 && val >= m.1 {
                        val = m.0 + (val - m.1);
                        break;
                    }
                }
            }
            return val;
        })
        .inspect(|v| {
            dbg!(v);
        })
        .collect();

    // 3. Take the minimum location
    println!("{}", locations.iter().min().unwrap());
}

fn part2(data: &str) {
    //1. Parse data and create
    // - List of seeds
    // - Map of seed(key) to soil(val)
    // - ...
    let (seeds, maps) = parse_input(data);

    // for map in maps {
    //     let a = map.iter().inspect(|v| {
    //         dbg!(v);
    //     });
    // }
    //2. Crete the location vector:
    // - For each map, if the key is present we return the value, else we return the key.

    // 2bis seeds need to be zipped: (first val,range)

    let locations: Vec<_> = seeds
        .chunks(2)
        .map(|v| {
            let seed = v[0];
            let seed_range = v[1];
            let mut min_val = u64::MAX;
            for i in 0..seed_range {
                let mut val = seed.clone() + i;
                for map in maps.iter() {
                    // Check if val is in range
                    for m in map.iter() {
                        if val <= m.1 + m.2 && val >= m.1 {
                            val = m.0 + (val - m.1);
                            break;
                        }
                    }
                }
                if val < min_val {
                    min_val = val;
                }
            }
            return min_val;
        })
        .inspect(|v| {
            dbg!(v);
        })
        .collect();

    // 3. Take the minimum location
    println!("{}", locations.iter().min().unwrap());
}

fn parse_input(data: &str) -> (Vec<u64>, Vec<Vec<(u64, u64, u64)>>) {
    let seeds = seeds(data);

    let mut it = data.lines();

    let mut maps = Vec::new();

    let mut line = it.next();
    while line.is_some() {
        if line.unwrap().contains("map:") {
            // Forward iterator until space
            // Create a map
            // Push every line created on the map
            let mut map_vec = Vec::new();
            let mut new_line = it.next().unwrap();
            while !new_line.is_empty() {
                map_vec.push(add_to_map(new_line));
                new_line = it.next().unwrap();
            }
            maps.push(map_vec);
        }
        line = it.next();
    }

    return (seeds, maps);
}

fn seeds(input: &str) -> Vec<u64> {
    let seeds_line: Vec<&str> = input
        .lines()
        .filter(|line| line.contains("seeds:"))
        .map(|v| v.split_once(':').unwrap().1)
        .collect();

    let seeds: Vec<u64> = seeds_line[0]
        .split_whitespace()
        .map(|v| v.parse::<u64>().expect("a number"))
        .collect();

    return seeds;
}

fn add_to_map(line: &str) -> (u64, u64, u64) {
    let v: Vec<u64> = line
        .split_whitespace()
        .map(|v| v.parse::<u64>().expect("a number"))
        .collect();

    return (v[0], v[1], v[2]);
}
