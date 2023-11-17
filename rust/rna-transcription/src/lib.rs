#[derive(Debug, PartialEq, Eq)]
pub struct Dna<'a> {
    nucleotides: &'a str,
}

#[derive(Debug, PartialEq, Eq)]
pub struct Rna<'a> {
    nucleotides: &'a str,
}

impl<'a> Dna<'a> {
    pub fn new(dna: &str) -> Result<Dna, usize> {
        let invalid_index = dna
            .chars()
            .map(|c| matches!(c, 'G' | 'C' | 'T' | 'A'))
            .position(|x| !x);

        match invalid_index {
            None => Ok(Dna { nucleotides: dna }),
            _ => Err(invalid_index.unwrap()),
        }
    }

    pub fn into_rna(self) -> Rna<'a> {
        Rna {
            nucleotides: self
                .nucleotides
                .chars()
                .map(|c| match c {
                    'G' => 'C',
                    'C' => 'G',
                    'T' => 'A',
                    'A' => 'U',
                    _ => unreachable!(),
                })
                .collect::<String>()
                .as_str(),
        }
    }
}

impl<'a> Rna<'a> {
    pub fn new(rna: &str) -> Result<Rna, usize> {
        let invalid_index = rna
            .clone()
            .chars()
            .map(|c| matches!(c, 'G' | 'C' | 'U' | 'A'))
            .position(|x| !x);

        match invalid_index {
            None => Ok(Rna { nucleotides: rna }),
            _ => Err(invalid_index.unwrap()),
        }
    }
}
