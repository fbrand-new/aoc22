use std::fs;
use regex::Regex;

fn main() {

    let data = fs::read_to_string("test.txt");
    if data.is_err() {
        println!("Could not read from file");
        return;
    }
    part1(data.unwrap());
}

fn part1(data: String) {
    
    // Define the three regexs
    // let blue_regex = Regex::new(r"(?<blue>\d?) blue").expect("is a regex");
    // let green_regex = Regex::new(r"(?<green>\d?) green").expect("is a regex");
    // let red_regex = Regex::new(r"(?<red>\d?) red").expect("is a regex");
    let color_vec = ["blue","red","green"];
    let regex_color_vec = color_vec.map(|v| color_regex(v));
    
    let games: Vec<_> = data.lines()
                                .map(|v| { 
                                        let game: Vec<&str> = v.split(':').collect();
                                        let sets: Vec<_> = game[1].trim()
                                                                    .split(';')
                                                                    .collect();
                                        return sets;
                                    })
                                .inspect(|v| {dbg!(v);})
                                .collect();
    
    for regex in regex_color_vec {
        for sets in games.iter() {
            for set in sets {
                let regex.captures(set);
            }
        }
    }

    // for line in data.lines() {
    //     let game: Vec<_> = line.split(':')
    //                             .collect();
    //     let sets: Vec<_> = game[1].trim()
    //                                 .split(';')
    //                                 .collect();
    //     for set in sets.iter() {
    //         // let colors = regex_color_vec.map(|v| v.captures(set));
            // regex_color_vec.
            // let mut blue: i32 = 0;

                            // .unwrap()["blue"]
                            // .parse::<i32>())
                            // .map(|v| v.expect("an integer"));
            // // for regex in regex_color_vec {
            // //     if let Some(v) = regex.captures(set) {
            // //         blue = v["blue"].parse::<i32>().unwrap();
            // //     }
            // // }
}

fn color_regex(color: &str) -> Regex {
    let regex = Regex::new(format!(r"(?<{}>\d?) {}",color,color).as_str()).expect("is a regex");
    return regex;
}