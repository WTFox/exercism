use std::cmp::Ordering;

pub fn find<T, U>(array: U, key: T) -> Option<usize>
where
    T: Ord,
    U: AsRef<[T]>,
{
    binary_search(array.as_ref(), &key, 0)
}

fn binary_search<T: Ord>(array: &[T], key: &T, offset: usize) -> Option<usize> {
    if array.is_empty() {
        return None;
    }

    let pivot = array.len() / 2;
    match key.cmp(&array[pivot]) {
        Ordering::Equal => Some(offset + pivot),
        Ordering::Less => binary_search(&array[..pivot], key, offset),
        Ordering::Greater => {
            if pivot + 1 < array.len() {
                binary_search(&array[pivot + 1..], key, offset + pivot + 1)
            } else {
                None
            }
        }
    }
}
