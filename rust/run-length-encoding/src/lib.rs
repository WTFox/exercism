use std::iter::repeat;

pub fn encode(input: &str) -> String {
    let mut encoded = String::new();
    let mut chars = input.chars().peekable();

    while let Some(current_char) = chars.next() {
        let mut count = 1;
        while chars.peek() == Some(&current_char) {
            chars.next();
            count += 1;
        }
        if count > 1 {
            encoded.push_str(&count.to_string());
        }
        encoded.push(current_char);
    }

    encoded
}

pub fn decode(input: &str) -> String {
    let mut decoded = String::new();
    let mut chars = input.chars().peekable();

    while let Some(ch) = chars.next() {
        if ch.is_ascii_digit() {
            let mut count = ch.to_string();
            while let Some(&next_ch) = chars.peek() {
                if next_ch.is_ascii_digit() {
                    count.push(chars.next().unwrap());
                } else {
                    break;
                }
            }
            decoded.extend(repeat(chars.next().unwrap()).take(count.parse().unwrap()));
        } else {
            decoded.push(ch);
        }
    }

    decoded
}
