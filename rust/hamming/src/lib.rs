/// Return the Hamming distance between the strings,
/// or None if the lengths are mismatched.
pub fn hamming_distance(s1: &str, s2: &str) -> Option<usize> {
    if s1.len() != s2.len() {
        return None;
    }

    Some(
        s1.chars()
            .enumerate()
            .map(|(i, c)| match c == s2.chars().nth(i).unwrap() {
                true => 0,
                false => 1,
            })
            .sum(),
    )
}
