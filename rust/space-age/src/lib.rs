#[derive(Debug)]
pub struct Duration {
    seconds: u64,
}

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Self { seconds: s }
    }
}

pub trait Planet {
    fn years_during(d: &Duration) -> f64 {
        todo!("convert a duration ({d:?}) to the number of years on this planet for that duration");
    }
}

macro_rules! impl_Planet {
    ($planet:ident, $year:expr) => {
        pub struct $planet;
        impl Planet for $planet {
            fn years_during(d: &Duration) -> f64 {
                d.seconds as f64 / $year
            }
        }
    };
}

impl_Planet!(Mercury, 7600543.81992);
impl_Planet!(Venus, 19414149.052176);
impl_Planet!(Earth, 31557600.0);
impl_Planet!(Mars, 59354032.69008);
impl_Planet!(Jupiter, 374355659.124);
impl_Planet!(Saturn, 929292362.8848);
impl_Planet!(Uranus, 2651370019.3296);
impl_Planet!(Neptune, 5200418560.032);
