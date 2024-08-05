from datetime import datetime, timedelta

class Clock:
    def __init__(self):
        self.current_time = datetime.now()

    def set_time(self, new_time: datetime):
        self.current_time = new_time

    def get_time(self) -> datetime:
        return self.current_time

    def tick(self):
        """Simulate the passage of time."""
        self.current_time += timedelta(seconds=1)

class Alarm:
    def __init__(self):
        self.alarm_time = None
        self.is_snoozed = False
        self.snooze_duration = timedelta(minutes=5)

    def set_alarm(self, alarm_time: datetime):
        self.alarm_time = alarm_time
        self.is_snoozed = False

    def snooze(self):
        if self.alarm_time:
            self.alarm_time += self.snooze_duration
            self.is_snoozed = True

    def turn_off(self):
        self.alarm_time = None
        self.is_snoozed = False

    def get_alarm_time(self) -> datetime:
        return self.alarm_time

    def is_alarm_set(self) -> bool:
        return self.alarm_time is not None

class AlarmClock:
    def __init__(self):
        self.clock = Clock()
        self.alarm = Alarm()

    def set_time(self, new_time: datetime):
        self.clock.set_time(new_time)

    def get_time(self) -> datetime:
        return self.clock.get_time()

    def set_alarm(self, alarm_time: datetime):
        self.alarm.set_alarm(alarm_time)

    def snooze_alarm(self):
        self.alarm.snooze()

    def turn_off_alarm(self):
        self.alarm.turn_off()

    def check_alarm(self):
        """Check if the current time matches the alarm time."""
        if self.alarm.is_alarm_set() and self.clock.get_time() >= self.alarm.get_alarm_time():
            print("Alarm ringing!")
            self.alarm.turn_off()  # Automatically turn off the alarm after ringing
            return True
        return False

    def tick(self):
        """Simulate the passage of time in the clock and check for alarm."""
        self.clock.tick()
        if self.check_alarm():
            # If alarm triggered, you might want to handle snoozing or other actions
            pass

# Example usage
alarm_clock = AlarmClock()
alarm_clock.set_time(datetime(2024, 8, 5, 7, 0, 0))  # Set current time
alarm_clock.set_alarm(datetime(2024, 8, 5, 7, 5, 0))  # Set alarm time

# Simulate time passing and alarm checking
for _ in range(300):  # Simulate 300 seconds (5 minutes)
    alarm_clock.tick()
