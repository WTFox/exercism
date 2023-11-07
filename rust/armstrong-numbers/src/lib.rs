pub fn is_armstrong_number(num: u32) -> bool {
    let num_str = num.to_string();
    num_str.chars().map(|c| c.to_digit(10)).fold(0, |acc, x| {
        acc + x.unwrap().pow(num_str.len() as u32) as u64
    }) == (num as u64)
}
