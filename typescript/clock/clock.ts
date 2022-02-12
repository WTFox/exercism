export class Clock {
  readonly minutes: number;

  constructor(hour: number, minute: number = 0) {
    this.minutes = hour * 60 + minute;
  }

  private get hour(): number {
    const h = Math.floor((this.minutes / 60) % 24);
    return h >= 0 ? h : h + 24;
  }

  private get minute(): number {
    const m = this.minutes % 60;
    return m >= 0 ? m : m + 60;
  }

  public toString(): string {
    const pad2 = (n: number): string => n.toString().padStart(2, "0");
    return `${pad2(this.hour)}:${pad2(this.minute)}`;
  }

  public plus(minutes: number): Clock {
    return new Clock(this.hour, this.minute + minutes);
  }

  public minus(minutes: number): Clock {
    return new Clock(this.hour, this.minute - minutes);
  }

  public equals(other: Clock): boolean {
    return this.hour === other.hour && this.minute === other.minute;
  }
}
