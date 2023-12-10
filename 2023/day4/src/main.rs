use std::{fs, iter::zip};

fn main() {

    let data = fs::read_to_string("data.txt");

    //part1(&data.unwrap());
    part2(&data.unwrap());
}

fn part1(data: &str) {

    // 1. Obtain list of vec of winning numbers and ours numbers
    let winning_numbers = numbers_list(&data, true);
    let our_numbers = numbers_list(&data, false);

    // 2. Iterate through our numbers and check into winning numbers. Add one if found
    let mut result = 0;
    for (our_nums,winning_nums) in zip(our_numbers, winning_numbers) {
        let mut card_val = 0;
        for our_num in our_nums.iter() {
            if winning_nums.contains(our_num) {
                if card_val == 0 {
                    card_val = 1;
                } else {
                    card_val *= 2;
                }
            }
        }
        result += card_val;
    }

    
    println!("{}",result);
}

fn part2(data: &str) {



    // Think about the algorithm, then code

    // We cannot iterate over a vec and also insert data onto it (i think)
    // Dynamic programming approach:
    // 1. count the matching numbers for each card and save them in vec
    // 2. count the number of cards.
    // Card i-1 fully determines the amount of card i, so you can cycle exactly once for each card
    // Count the nums for card 1, update card2,3,.. if needed.
    // Count the nums for card 2, update cards ...

    // 1. Read the numbers
    let winning_numbers = numbers_list(data, true);
    let our_numbers = numbers_list(data, false);

    // 2. Define the vector of cards count 
    let n = winning_numbers.len();
    let mut cards = vec![1;n];

    // 3. Cycle through the cards, count the matches, update the cards count vector
    for (i,(our_nums, winning_nums)) in zip(our_numbers, winning_numbers).enumerate() {
        let mut matched_num = 0;
        for our_num in our_nums {
            if winning_nums.contains(&our_num) {
                matched_num += 1;
            }
        }
        let current_card_num = cards[i];

        // println!("matched_num: {}",matched_num);
        // We start iterating from the current card up to the matched number and update
        let mut k = i+1;
        while k < n && k < i+1+matched_num {
            cards[k] += current_card_num; //Sum current_card_num times to the current value of card k
            k=k+1
        }
    }

    // 4. Sum over the cards count vector and return\
    let result: i32 = cards.iter().sum();
    println!("{}",result);
}

fn numbers_list(data:&str, is_winning_numbers: bool) -> Vec<Vec<u32>> {

    let mut idx: usize = 0;
    if !is_winning_numbers {
        idx = 1;
    }
    let numbers: Vec<_> = data.lines()
        .map( |line| {
                let card: Vec<&str> = line.split(':').collect();
                let both_numbers_str: Vec<&str> = card[1].split('|').collect(); 
                let numbers: Vec<u32> = both_numbers_str[idx].split(' ')
                                                                //   .inspect(|v| {dbg!(v);})
                                                                  .filter(|num| !num.is_empty())
                                                                  .map(|num| num.parse::<u32>().expect("is a number"))
                                                                  .collect();
                return numbers;
            })
        .collect();

    return numbers;
}