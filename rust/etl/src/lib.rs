use std::collections::BTreeMap;

pub fn transform(h: &BTreeMap<i32, Vec<char>>) -> BTreeMap<char, i32> {
    BTreeMap::from_iter(
        h.iter()
            .flat_map(|(point, letters)| {
                letters
                    .iter()
                    .map(|letter| (letter.to_ascii_lowercase(), *point))
            })
            .collect::<Vec<(char, i32)>>(),
    )
}
