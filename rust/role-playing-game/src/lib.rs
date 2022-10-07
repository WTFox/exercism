pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        if self.health > 0 {
            return None;
        }

        return Some(Player {
            health: 100,
            mana: if self.level >= 10 { Some(100) } else { None },
            level: self.level,
        });
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        if self.level < 10 {
            self.health = if self.health >= mana_cost {
                self.health - mana_cost
            } else {
                0
            };
            return 0;
        }

        let available_mana = self.mana.unwrap();
        if available_mana >= mana_cost {
            self.mana = Some(available_mana - mana_cost);
            return mana_cost * 2;
        }

        return 0;
    }
}
