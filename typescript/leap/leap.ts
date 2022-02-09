/*
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
*/

export function isLeap(year: number): boolean {
  const divisibleBy = (n: number): boolean => year % n === 0;
  return divisibleBy(4) && (!divisibleBy(100) || divisibleBy(400))
}
