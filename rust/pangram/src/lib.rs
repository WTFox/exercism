use std::collections::HashSet;

pub fn is_pangram(sentence: &str) -> bool {
    sentence
        .chars()
        .filter(|c| c.is_ascii_alphabetic())
        .flat_map(|c| c.to_lowercase())
        .collect::<HashSet<char>>()
        .len()
        == 26
}
