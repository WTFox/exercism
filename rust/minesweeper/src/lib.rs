fn count_surrounding_mines(row_i: usize, col_i: usize, minefield: &[&str]) -> usize {
    let mut count = 0;

    #[rustfmt::skip]
    let adjacent_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ];

    for &(row_offset, col_offset) in adjacent_offsets.iter() {
        let adjacent_row = row_i as isize + row_offset;
        let adjacent_column = col_i as isize + col_offset;

        if adjacent_row < 0 || adjacent_row >= minefield.len() as isize {
            continue;
        }
        if adjacent_row < 0 || adjacent_column >= minefield[0].len() as isize {
            continue;
        }

        let adjacent_cell = minefield[adjacent_row as usize]
            .chars()
            .nth(adjacent_column as usize)
            .unwrap_or(' ');

        if adjacent_cell == '*' {
            count += 1;
        }
    }

    count
}

pub fn annotate(minefield: &[&str]) -> Vec<String> {
    if minefield.is_empty() {
        return vec![];
    }

    let expected_length = minefield[0].len();
    for row in minefield.iter() {
        if row.len() != expected_length {
            panic!("Invalid minefield");
        }
    }

    let mut result = Vec::with_capacity(minefield.len());
    for (row_i, row) in minefield.iter().enumerate() {
        let mut new_row = String::from("");
        for (cell_i, cell) in row.chars().enumerate() {
            if cell != '*' {
                let count = count_surrounding_mines(row_i, cell_i, minefield);
                match count {
                    0 => new_row.push(' '),
                    _ => new_row.push(count.to_string().chars().next().unwrap()),
                }
            } else {
                new_row.push('*');
            }
        }
        result.push(new_row)
    }

    result
}
