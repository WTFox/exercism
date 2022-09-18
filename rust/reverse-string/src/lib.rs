use unicode_segmentation::UnicodeSegmentation;

pub fn reverse(input: &str) -> String {
    let mut graphemes = input.graphemes(true).collect::<Vec<&str>>();
    graphemes.reverse();
    graphemes.join("")
}
