use std::{fs, collections::HashMap};

fn main() {

    let data = fs::read_to_string("data1.txt");
    if data.is_err() {
        println!("Could not read data file");
        return;
    }
    // part1(data.unwrap());

    let data2 = fs::read_to_string("data1.txt");
    if data2.is_err() {
        println!("Could not read data file");
        return;
    }
    part2(data2.unwrap());

}

fn part2(data: String) {
    let char_matrix = string_to_char_mat(data);
    let n = char_matrix[0].len();

    let mut symbols_vec: Vec<(usize,usize)> = Vec::new();
    for (i,line) in char_matrix.iter().enumerate() {
        for (j, ch) in line.iter().enumerate() {
            if *ch == '*' {
                symbols_vec.push((i,j));
            }
        }
    }

    let mut result = 0;
    for (i,j) in symbols_vec {
        let mut numbers_map: HashMap<(usize,usize), i32>= HashMap::new();
        for (u,v) in grid(i, j, n) {
            if char_matrix[u][v].is_digit(10) {
                //5. If number is already in the map then do not add it
                let (begin,num) = search_number(v, &char_matrix[u]);
                // println!("Num: {}, begins at {}. We are at line {}",num,begin,u);
                if !numbers_map.contains_key(&(u,begin)) {
                    numbers_map.insert((u,begin),num);
                    // nums_found += 1;
                }
            }
        }

        if numbers_map.len() == 2{
            let mut it = numbers_map.iter();
            let ((_,_),first_num) = it.next().unwrap();
            let ((_,_),second_num) = it.next().unwrap();
            // println!("Firstnum:{}, second num:{}",first_num,second_num);
            result += first_num*second_num;
        }
    }
    
    println!("{}",result);
}

fn part1(data: String) {
    //1. Create a matrix of chars from the lines
    // See https://stackoverflow.com/questions/47829646/how-do-i-convert-a-string-to-a-list-of-chars
    let char_matrix = string_to_char_mat(data);
    let n = char_matrix[0].len();

    //2. Iterate through data and look for symbols
    let mut symbols_vec: Vec<(usize,usize)> = Vec::new();
    for (i,line) in char_matrix.iter().enumerate() {
        for (j, ch) in line.iter().enumerate() {
            if !ch.is_digit(10) && *ch != '.' {
                symbols_vec.push((i,j));
            }
        }
    }

    //3. Use i,j of symbol and look at neighbours in the matrix at point 1
    // Create the grid to check as a vector of tuples
    //4. Create numbers map: <i,j,number_str> by first looking left where the number starts, then right until it ends
    let mut numbers_map: HashMap<(usize,usize), i32>= HashMap::new();
    for (i,j) in symbols_vec {
        for (u,v) in grid(i, j, n) {
            if char_matrix[u][v].is_digit(10) {
                //5. If number is already in the map then do not add it
                let (begin,num) = search_number(v, &char_matrix[u]);
                println!("Num: {}, begins at {}. We are at line {}",num,begin,u);
                if !numbers_map.contains_key(&(u,begin)) {
                    // println!()
                    numbers_map.insert((u,begin),num);
                }
            }
        }
    }

    //6. Iterate through the map and sum the result.
    let mut acc = 0;
    for ((i,j),num) in numbers_map {
        
        acc += num;
    }
    
    println!("{}",acc);
}

fn string_to_char_mat(s: String) -> Vec<Vec<char>> {
    let data_lines = s.lines();
    let char_matrix: Vec<Vec<_>> = data_lines.map(|x| x.chars().collect()).collect();
    return char_matrix;
}

fn search_number(i: usize, line: &Vec<char>) -> (usize,i32) {
    // We are guaranteed by design that we have a digit in i
    let mut number_char = String::from("");

    let mut k = i+1; //i+1 so that we don't overflow the subtraction
    while k>0 && line[k-1].is_digit(10) {
        number_char.insert(0, line[k-1]);
        // println!("{}",k);
        k-=1;
    }

    let begin = k;

    k = i+1;
    while k<line.len() && line[k].is_digit(10) {
        number_char.push(line[k]);
        k+=1;
    }

    return (begin,number_char.parse::<i32>().unwrap());

}

fn grid(i: usize, j: usize, N:usize) -> Vec<(usize, usize)> {
    let mut grid_: Vec<(usize,usize)> = Vec::new();
    if i>0 {
        grid_.push((i-1,j));
        if j > 0 {
            grid_.push((i,j-1));
            grid_.push((i-1,j-1));
        } 
        if j < N-1 {
            grid_.push((i,j+1));
            grid_.push((i-1,j+1));
        }
    }
    if i<N {
        grid_.push((i+1,j));
        if j > 0 {
            grid_.push((i+1,j-1));
        }
        if j < N {
            grid_.push((i+1,j+1));
        }
    }

    return grid_;
}
// fn part1(data: String) {

//     let mut symbols: Vec<(usize,usize)> = Vec::new();
//     let mut numbers: HashMap<(usize,usize),i32> = HashMap::new();

//     // Find symbols, char by char
//     for line in data.lines().enumerate() {
//         let ch_it = line.1.chars();
//         let nums = ch_it.scan("", |number,ch|{ 
//             number;
//             Some(ch)
//         });

//         // let nums = ch_it.filter(|x| x.is_digit(10)).collect();
//         for num in nums {
//             println!("{}",num);
//         }
//         // println!("{}",nums);
//         // for ch in ch_it {
//         //     // let mut ch = ch_it.next().unwrap();
//         //     let mut number_string = String::from("");
//         //     while ch.1.is_digit(10) {
//         //         number_string.push(ch.1);
//         //         ch_it.next();
//         //     }
    
//         //     if number_string != "" {
//         //         numbers.insert((ch.0-number_string.len(),number_string.len()), number_string.parse::<i32>().unwrap());
//         //     }
            
//         //     if ch.1 != '.' {
//         //         symbols.push((line.0,ch.0));
//         //     }
//         // }
//     }

//     // for symbol in symbols {
//     //     println!("Symbol in: {},{}",symbol.0,symbol.1);
//     // }
// }


