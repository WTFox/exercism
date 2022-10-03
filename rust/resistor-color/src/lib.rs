use enum_iterator::{all, cardinality, Sequence};
use int_enum::IntEnum;

#[repr(u32)]
#[derive(Copy, Clone, Debug, PartialEq, Eq, IntEnum, Sequence)]
pub enum ResistorColor {
    Black = 0,
    Brown = 1,
    Red = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Blue = 6,
    Violet = 7,
    Grey = 8,
    White = 9,
}

pub fn color_to_value(_color: ResistorColor) -> u32 {
    return _color.int_value();
}

pub fn value_to_color_string(value: u32) -> String {
    return if value >= cardinality::<ResistorColor>() as u32 {
        "value out of range".to_string()
    } else {
        format!("{:?}", ResistorColor::from_int(value).unwrap())
    };
}

pub fn other_thing(value: u32) -> String {
    ResistorColor::
}

pub fn colors() -> Vec<ResistorColor> {
    return all::<ResistorColor>().collect::<Vec<_>>();
}
