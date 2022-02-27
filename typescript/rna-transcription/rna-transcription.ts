export function toRna(input: string): string {
  const map = new Map([
    ["G", "C"],
    ["C", "G"],
    ["T", "A"],
    ["A", "U"],
  ]);

  if (input.toUpperCase().match("[^GCTA]")) {
    throw new Error("Invalid input DNA.");
  }

  return Array.from(input.toUpperCase())
    .map((c) => map.get(c))
    .join("");
}
