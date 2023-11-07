fn count_surrounding_mines(row_i: usize, col_i: usize, minefield: &[&str]) -> usize {
    #[rustfmt::skip]
    let adjacent_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ];

    adjacent_offsets
        .iter()
        .filter_map(|&(row_offset, col_offset)| {
            let adjacent_row = row_i as isize + row_offset;
            let adjacent_column = col_i as isize + col_offset;

            if adjacent_row >= 0
                && adjacent_row < minefield.len() as isize
                && adjacent_column >= 0
                && adjacent_column < minefield[0].len() as isize
            {
                return minefield[adjacent_row as usize]
                    .chars()
                    .nth(adjacent_column as usize);
            } else {
                None
            }
        })
        .filter(|&c| c == '*')
        .count()
}

pub fn annotate(minefield: &[&str]) -> Vec<String> {
    if minefield.is_empty() {
        return Vec::new();
    }

    let mut result = Vec::with_capacity(minefield.len());
    for (row_i, row) in minefield.iter().enumerate() {
        let mut new_row = String::with_capacity(row.len());
        for (cell_i, &cell) in row.as_bytes().iter().enumerate() {
            if cell != b'*' {
                let count = count_surrounding_mines(row_i, cell_i, minefield);
                match count {
                    0 => new_row.push(' '),
                    _ => new_row.push(char::from_digit(count as u32, 10).unwrap()),
                }
            } else {
                new_row.push('*');
            }
        }
        result.push(new_row)
    }

    result
}
