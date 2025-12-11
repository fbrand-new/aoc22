use std::fs;
use std::env;

fn main() {

    let curr_path = env::current_dir();

    let path: str = match curr_path {
        Ok(path) => path.string(),
        Err(_) => panic!("Could not retrieve current path")
    };


    let contents = fs::read_to_string(+ "test.txt")
        .expect("File exists");


    println!("Print contents: {contents}") 

}
