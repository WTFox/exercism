use std::collections::HashMap;
use std::collections::HashSet;

fn char_frequency(word: &str) -> HashMap<String, usize> {
    word.chars().fold(HashMap::new(), |mut freq, c| {
        let lowered = c.to_lowercase().collect::<String>();
        *freq.entry(lowered).or_insert(0) += 1;
        freq
    })
}

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let word_freq = char_frequency(word);

    possible_anagrams
        .iter()
        .cloned()
        .filter(|&candidate| {
            word.to_lowercase().ne(&candidate.to_lowercase())
                && word_freq == char_frequency(candidate)
        })
        .collect()
}
