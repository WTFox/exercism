export class DnDCharacter {
  strength: number;
  dexterity: number;
  constitution: number;
  intelligence: number;
  wisdom: number;
  charisma: number;

  constructor() {
    this.strength = DnDCharacter.generateAbilityScore();
    this.dexterity = DnDCharacter.generateAbilityScore();
    this.constitution = DnDCharacter.generateAbilityScore();
    this.intelligence = DnDCharacter.generateAbilityScore();
    this.wisdom = DnDCharacter.generateAbilityScore();
    this.charisma = DnDCharacter.generateAbilityScore();
  }

  public static generateAbilityScore(): number {
    const rollSixSidedDice = () => Math.floor(Math.random() * 6) + 1;

    return new Array(4)
      .fill(0)
      .map(rollSixSidedDice)
      .sort((a, b) => a - b)
      .slice(1, 4)
      .reduce((prev, curr) => prev + curr);
  }

  public static getModifierFor(abilityValue: number): number {
    return Math.floor((abilityValue - 10) / 2);
  }

  public get hitpoints() {
    return Math.floor(10 + DnDCharacter.getModifierFor(this.constitution));
  }
}
