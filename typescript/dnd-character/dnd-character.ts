function rollDice(): number {
  return Math.floor(Math.random() * (7 - 1)) + 1;
}

export class DnDCharacter {
  strength: number = 0;
  dexterity: number = 0;
  constitution: number = 0;
  intelligence: number = 0;
  wisdom: number = 0;
  charisma: number = 0;
  hitpoints: number = 0;

  constructor() {
    this.strength = DnDCharacter.generateAbilityScore();
    this.dexterity = DnDCharacter.generateAbilityScore();
    this.constitution = DnDCharacter.generateAbilityScore();
    this.intelligence = DnDCharacter.generateAbilityScore();
    this.wisdom = DnDCharacter.generateAbilityScore();
    this.charisma = DnDCharacter.generateAbilityScore();

    this.hitpoints = Math.floor(10 + (this.constitution - 10) / 2);
  }

  public static generateAbilityScore(): number {
    return new Array(4)
      .fill(0)
      .map(() => rollDice())
      .sort((a, b) => a - b)
      .slice(1, 4)
      .reduce((prev, curr) => prev + curr, 1);
  }

  public static getModifierFor(abilityValue: number): number {
    return Math.floor((abilityValue - 10) / 2);
  }
}
