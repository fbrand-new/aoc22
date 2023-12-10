use std::{fs, collections::{hash_map, HashMap}};
use regex::Regex;

fn main() {

    let data = fs::read_to_string("data.txt");
    if data.is_err() {
        println!("Could not read from file");
        return;
    }
    //part1(data.unwrap());
    part2(data.unwrap());
}

fn games(data: &str) -> Vec<Vec<&str>> {

    // Extract all the games
    let games: Vec<_> = data.lines()
                                .map(|v| { 
                                        let game: Vec<&str> = v.split(':').collect();
                                        let sets: Vec<_> = game[1].trim()
                                                                    .split(';')
                                                                    .collect();
                                        return sets;
                                    })
                                // .inspect(|v| {dbg!(v);})
                                .collect();

    return games;
}

fn part1(data: String) {
    
    let color_vec = [("blue",14),("red",12),("green",13)];
    let regex_color_vec = color_vec.map(|v| color_regex(v));
    
    let games = games(&data);

    // For every game extract every set
    // Run the regex and compare the result
    let mut num_games_valid = 0;
    for (id,sets) in games.iter().enumerate(){
        let mut is_game_valid = true;
        for set in sets {
            for regex in regex_color_vec.iter() {
                if let Some(boxes) = regex.0.captures(set) {
                    let cube_num = boxes["match"].parse::<i32>().expect("a number");
                    // println!("Cube num: {} for set {}",cube_num,set);
                    if cube_num > regex.1 {
                        is_game_valid = false;
                    }
                }
            }
        } 
        if is_game_valid {
            println!("id: {} is valid",id);
            num_games_valid += id+1;
        }
    }

    println!("sum of valid ids {}", num_games_valid);

}

fn part2(data: String) {
    let colors = [("green",0),("red",0),("blue",0)];
    let regex_color = colors.map(|v| (v.0,color_regex(v)));
    
    let games = games(&data);

    let mut result = 0;
    for sets in games.iter() {
        let mut max_cubes = HashMap::from([("red",0),("blue",0),("green",0)]) ;
        for set in sets {
            for regex in regex_color.iter() {
                if let Some(cube) = regex.1.0.captures(set) {
                    let cube_val = cube["match"].parse::<u32>().expect("is a number");
                    if cube_val > max_cubes[regex.0] {
                        if let Some(new_cub_val) = max_cubes.get_mut(regex.0) {
                            *new_cub_val = cube_val;
                        }
                    }
                }
            }
        }
        let mut set_result = 1;
        // println!("set--");
        for cube_val in max_cubes.iter() {
            // println!("cube_val {}: {}",cube_val.0,cube_val.1);
            set_result *= cube_val.1;
        }
        result += set_result;
    }

    println!("{}",result);
}

fn color_regex(color: (&str,i32)) -> (Regex,i32) {
    let regex = Regex::new(format!(r"(?<match>\d*?) {}",color.0)
                                .as_str())
                                .expect("is a regex");
    return (regex,color.1);
}