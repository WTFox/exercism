/// Check a Luhn checksum.
pub fn is_valid(code: &str) -> bool {
    let clean_code = code.replace(' ', "");
    if clean_code.len() <= 1 || clean_code.chars().any(|c| !c.is_ascii_digit()) {
        return false;
    }

    clean_code
        .chars()
        .rev()
        .enumerate()
        .map(|(i, c)| {
            let mut digit = c.to_digit(10).expect("All characters should be digits");
            if i % 2 == 1 {
                digit *= 2;
                digit = if digit > 9 { digit - 9 } else { digit };
            }
            digit
        })
        .sum::<u32>()
        % 10
        == 0
}
