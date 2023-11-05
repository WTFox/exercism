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
        let hours = self.minutes / 60;
        let minutes = self.minutes % 60;

        let normalized_minutes = if minutes < 0 { 60 + minutes } else { minutes };
        let normalized_hours = if hours < 0 { 24 + hours } else { hours };

        write!(f, "{:02}:{:02}", normalized_hours, normalized_minutes)
    }
}
