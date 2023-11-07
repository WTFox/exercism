pub fn is_armstrong_number(num: u32) -> bool {
    let digits: Vec<_> = num.to_string().chars().map(|c| c.to_digit(10)).collect();
    let length = digits.len() as u32;
    let sum = digits
        .iter()
        .map(|x| x.unwrap().pow(length) as u64)
        .sum::<u64>();

    sum == (num as u64)
}
