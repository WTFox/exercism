const valueMaps: {[key: string]:number}= {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
}

export function decodedResistorValue(bands: string[]): string {
  const result = parseInt(bands.slice(0,2).reduce((prev, curr) => {
    return prev + valueMaps[curr];
  }, '') + '0'.repeat(valueMaps[bands[2]]));

  if (result > 1000) {
    return `${result / 1000} kiloohms`
  }

  return `${result} ohms`;
}
