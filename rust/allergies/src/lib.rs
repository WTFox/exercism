#[derive(Debug, PartialEq, Eq, Clone)]
pub enum Allergen {
    Eggs,
    Peanuts,
    Shellfish,
    Strawberries,
    Tomatoes,
    Chocolate,
    Pollen,
    Cats,
}

impl Allergen {
    pub fn to_array() -> [Allergen; 8] {
        [
            Allergen::Eggs,
            Allergen::Peanuts,
            Allergen::Shellfish,
            Allergen::Strawberries,
            Allergen::Tomatoes,
            Allergen::Chocolate,
            Allergen::Pollen,
            Allergen::Cats,
        ]
    }
}

pub struct Allergies {
    score: u32,
}

impl Allergies {
    pub fn new(score: u32) -> Self {
        Allergies { score }
    }

    pub fn is_allergic_to(&self, allergen: &Allergen) -> bool {
        let allergens = Allergen::to_array();
        let index = allergens
            .iter()
            .position(|a| a.clone() == *allergen)
            .unwrap_or(0);

        (1 << index) & self.score != 0
    }

    pub fn allergies(&self) -> Vec<Allergen> {
        Allergen::to_array()
            .iter()
            .enumerate()
            .filter(|(i, _)| 1 << i & self.score != 0)
            .map(|(_, a)| a.clone())
            .collect::<Vec<_>>()
    }
}
