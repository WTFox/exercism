#[derive(Debug, PartialEq, Eq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

fn is_sublist<T: PartialEq>(a: &[T], b: &[T]) -> bool {
    b.windows(a.len()).any(|w| w == a)
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    match (_first_list.len(), _second_list.len()) {
        (0, 0) => Comparison::Equal,
        (0, _) => Comparison::Sublist,
        (_, 0) => Comparison::Superlist,
        (a, b) if a == b => {
            if is_sublist(_first_list, _second_list) {
                Comparison::Equal
            } else {
                Comparison::Unequal
            }
        }
        (a, b) if a < b => {
            if is_sublist(_first_list, _second_list) {
                Comparison::Sublist
            } else {
                Comparison::Unequal
            }
        }
        (a, b) if a > b => {
            if is_sublist(_second_list, _first_list) {
                Comparison::Superlist
            } else {
                Comparison::Unequal
            }
        }
        _ => Comparison::Unequal,
    }
}
