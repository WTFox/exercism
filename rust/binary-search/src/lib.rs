use std::cmp::Ordering;

pub fn find<T: Ord>(array: &[T], key: T) -> Option<usize> {
    binary_search(array, key, 0)
}

fn binary_search<T: Ord>(array: &[T], key: T, _offset: i32) -> Option<usize> {
    if array.is_empty() {
        return None;
    }

    if array.len() == 1 {
        return if array[0] == key {
            Some(_offset as usize)
        } else {
            None
        };
    }

    let pivot = array.len() / 2;
    let (left, right) = array.split_at(pivot);
    match key.cmp(&right[0]) {
        Ordering::Equal => Some((_offset + pivot as i32) as usize),
        Ordering::Less => binary_search(left, key, _offset),
        Ordering::Greater => binary_search(right, key, _offset + pivot as i32),
    }
}
