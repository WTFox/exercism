const MAX_PER_HOUR: f64 = 221.0;

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let success_rate = match speed {
        0..=4 => 1.0,
        5..=8 => 0.9,
        9..=u8::MAX => 0.77,
    };
    return speed as f64 * MAX_PER_HOUR * success_rate;
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    return production_rate_per_hour(speed) as u32 / 60;
}
