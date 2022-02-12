export class Clock {
  protected hour: number;
  protected minute: number;

  constructor(hour: number, minute: number = 0) {
    const totalMinutes = minute + hour * 60;
    [this.hour, this.minute] = this.hhmmFromTotalMinutes(totalMinutes);
  }

  protected hhmmFromTotalMinutes(totalMinutes: number): [number, number] {
    let minutes = (totalMinutes + 60) % 60;
    let hours = Math.floor((totalMinutes - minutes) / 60) % 24;

    if (minutes < 0) {
      minutes += 60;
      hours -= 1;
    }

    hours = hours < 0 ? hours + 24 : hours;
    return [hours, minutes];
  }

  public toString(): string {
    const hour = this.hour.toString().padStart(2, "0");
    const minute = this.minute.toString().padStart(2, "0");
    return `${hour}:${minute}`;
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
