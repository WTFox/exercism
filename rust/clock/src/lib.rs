use std::fmt;

#[derive(Debug, PartialEq)]
pub struct Clock {
    pub hours: i32,
    pub minutes: i32,
}

impl Clock {
    fn normalize(&mut self) -> Self {
        while self.minutes < 0 {
            self.minutes += 60;
            self.hours -= 1;
        }
        while self.minutes >= 60 {
            self.minutes -= 60;
            self.hours += 1;
        }
        while self.hours < 0 {
            self.hours += 24;
        }
        while self.hours >= 24 {
            self.hours -= 24;
        }

        Clock {
            hours: self.hours,
            minutes: self.minutes,
        }
    }

    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock { hours, minutes }.normalize()
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::new(self.hours, self.minutes + minutes)
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}
