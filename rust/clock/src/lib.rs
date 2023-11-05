use std::fmt;

#[derive(Debug, PartialEq)]
pub struct Clock {
    pub minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock {
            minutes: (hours * 60) + minutes,
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock {
            minutes: self.minutes + minutes,
        }
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // Ensure the minutes are within a day (0 to 1439)
        let minutes_in_a_day = 24 * 60;
        let mut normalized_minutes = self.minutes % minutes_in_a_day;

        // Handle negative minutes
        if normalized_minutes < 0 {
            normalized_minutes += minutes_in_a_day;
        }

        // Calculate hours and minutes
        let hours = normalized_minutes / 60;
        let minutes = normalized_minutes % 60;

        // Write to the provided formatter
        write!(f, "{:02}:{:02}", hours, minutes)
    }
}
