#[derive(Clone, PartialEq, Eq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug,
}

pub fn log(level: LogLevel, message: &str) -> String {
    println!("\n\n{:?}", level.to_uppercase());
    return match level {
        LogLevel::Info => format!("[INFO]: {}", message),
        LogLevel::Warning => format!("[WARNING]: {}", message),
        LogLevel::Error => format!("[ERROR]: {}", message),
        LogLevel::Debug => format!("[DEBUG]: {}", message),
    };
}

pub fn info(message: &str) -> String {
    log(LogLevel::Info, message)
}

pub fn warn(message: &str) -> String {
    log(LogLevel::Warning, message)
}

pub fn error(message: &str) -> String {
    log(LogLevel::Error, message)
}
