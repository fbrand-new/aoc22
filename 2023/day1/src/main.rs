use std::{fs, collections::{HashMap, hash_map}, hash::Hash};

fn main() {

    let contents = fs::read_to_string("data.txt").expect("Cant read file");
    let lines = contents.lines();
    let digits= vec!["one",
                            "two",
                            "three",
                            "four",
                            "five",
                            "six",
                            "seven",
                            "eight",
                            "nine",
                            "1",
                            "2",
                            "3",
                            "4",
                            "5",
                            "6",
                            "7",
                            "8",
                            "9"];

    let digit_map = HashMap::from([
        ("one",'1'),
        ("two",'2'),
        ("three",'3'),
        ("four",'4'),
        ("five",'5'),
        ("six",'6'),
        ("seven",'7'),
        ("eight",'8'),
        ("nine",'9'),
        ("1",'1'),
        ("2",'2'),
        ("3",'3'),
        ("4",'4'),
        ("5",'5'),
        ("6",'6'),
        ("7",'7'),
        ("8",'8'),
        ("9",'9'),
    ]);

    let mut calibrations = 0;
    for content in lines {
        let mut v = Vec::new();
        for mat in &digits {
            let v_: Vec<_> = content.match_indices(*mat).collect();
            v.extend(v_);
        }

        let mut min = content.len();
        let mut min_digit = "";
        let mut max = 0;
        let mut max_digit = "";

        for el in v {
            if el.0 < min {
                min = el.0;
                min_digit = el.1;
            }

            if el.0 >= max {
                max = el.0;
                max_digit = el.1;
            }
        }
        

        let first_digit = digit_map[min_digit];
        let second_digit = digit_map[max_digit];
        let mut calib = String::from("");
        calib.push(first_digit);
        calib.push(second_digit);
        

        let calib_int = calib.parse::<i32>().unwrap();
        calibrations += calib_int;
    }

    println!("{calibrations}");

    // let mut calib_final = 0;
    // for i in v {
    //     let calib = i.parse::<i32>().unwrap();
    //     calib_final += calib;
    //     // println!("{}",i);
    // }

    // println!("{}",calib_final);
}


// Old problem 
// for content in lines {
//     let mut v = Vec::new();
//     for mat in digits {
//         v.extend(content.match_indices(&mat).collect());
//     }

    // let mut calibration: String = String::from("");
    // for c in content.chars() {

    //     if c.is_digit(10) {
    //         calibration.push(c);
    //         break;
    //     }
    // }
    // for c in content.chars().rev(){
    //     if c.is_digit(10) {
    //         calibration.push(c);
    //         break;
    //     }
    // }

    // v.push(calibration);
