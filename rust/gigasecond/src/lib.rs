use time::PrimitiveDateTime as DateTime;

pub fn after(start: DateTime) -> DateTime {
    start + time::Duration::seconds(1_000_000_000)
}
