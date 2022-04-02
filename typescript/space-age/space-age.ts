const orbitalPeriods = new Map<string, number>([
  ["earth", 1],
  ["mercury", 0.2408467],
  ["venus", 0.61519726],
  ["mars", 1.8808158],
  ["jupiter", 11.862615],
  ["saturn", 29.447498],
  ["uranus", 84.016846],
  ["neptune", 164.79132],
]);

const earthYearInSeconds: number = 31557600;
const earthYearsFromSeconds = (seconds: number): number =>
  seconds / earthYearInSeconds;

export function age(planet: string, seconds: number): number {
  const orbitalPeriod = orbitalPeriods.get(planet.toLowerCase()) ?? 1;
  const age = earthYearsFromSeconds(seconds) / orbitalPeriod;
  return Number(age.toFixed(2));
}
