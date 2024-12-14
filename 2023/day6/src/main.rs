use core::time;
use std::{fs, iter::zip};

fn main() {
    let data = fs::read_to_string("data.txt").expect("a file");

    //part1(&data);
    part2(&data);
}

fn part1(data: &str) {
    let (times, distances) = parse_input(data);

    let mut result = 1;
    for (time, distance) in zip(times, distances) {
        let mut count = 0;
        for t in 1..time {
            let total_dist = (time - t) * t;
            if total_dist > distance {
                count += 1;
            }
        }
        result *= count;
    }

    println!("{}", result);
}

fn part2(data: &str) {
    let (time, distance) = parse_input2(data);

    let mut result = 0;
    for t in 1..time {
        let d = (time - t) * t;
        if d > distance {
            result += 1;
        }
    }

    println!("{}", result);
}

fn parse_input(data: &str) -> (Vec<u32>, Vec<u32>) {
    let lines: Vec<_> = data.lines().collect();

    let times: Vec<u32> = lines[0]
        .split_whitespace()
        .skip(1)
        .map(|v| v.parse::<u32>().expect("a number"))
        .collect();

    let distances: Vec<u32> = lines[1]
        .split_whitespace()
        .skip(1)
        .map(|v| v.parse::<u32>().expect("a number"))
        .collect();

    return (times, distances);
}

fn parse_input2(data: &str) -> (u64, u64) {
    let lines: Vec<_> = data.lines().collect();

    let times: Vec<&str> = lines[0].split_whitespace().skip(1).collect();

    let distances: Vec<&str> = lines[1].split_whitespace().skip(1).collect();

    let time = times.join("").parse::<u64>().expect("a number");
    let distance = distances.join("").parse::<u64>().expect("a number");

    return (time, distance);
}
