use std::fs;

fn main() {
  
    let file_path = "test.txt";

    let weights = fs::read_to_string(file_path)
        .expect("Should have read the file");

    let mut sum: i32 = 0;

    for line in weights.lines() {
        if line.
       sum += line.parse::<i32>().unwrap(); 
    }
    
    println!("{}", weights);
}
