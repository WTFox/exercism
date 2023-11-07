/// Check a Luhn checksum.
pub fn is_valid(code: &str) -> bool {
    if code.trim().len() < 2 {
        return false;
    }

    if code
        .chars()
        .filter(|c| !c.is_whitespace())
        .any(|c| !c.is_ascii_digit())
    {
        return false;
    }

    code.trim()
        .chars()
        .rev()
        .filter(|c| !c.is_ascii_whitespace() || c.is_ascii_digit())
        .enumerate()
        .map(|(i, c)| {
            if i == 0 {
                return c.to_digit(10).unwrap();
            }

            if i % 2 == 1 {
                let mut result = c.to_digit(10).unwrap() * 2;
                if result > 9 {
                    result -= 9;
                }
                return result;
            }

            c.to_digit(10).unwrap()
        })
        .sum::<u32>()
        % 10
        == 0
}
