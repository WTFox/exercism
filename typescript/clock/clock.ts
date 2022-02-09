export class Clock {
  private _hour: number;
  private _minute: number;

  constructor(hour: number, minute: number = 0) {
    this._minute = minute % 60;
    if (minute > 59) {
      hour += Math.floor(minute / 60);
    }
    this._hour = hour % 24;
  }

  public toString(): string {
    const hourString = this._hour.toString().padStart(2, "0");
    const minuteString = this._minute.toString().padStart(2, "0");
    return `${hourString}:${minuteString}`;
  }

  public plus(minutes: unknown): Clock {
    throw new Error("Remove this statement and implement this function");
  }

  public minus(minutes: unknown): Clock {
    throw new Error("Remove this statement and implement this function");
  }

  public equals(other: unknown): unknown {
    throw new Error("Remove this statement and implement this function");
  }
}
