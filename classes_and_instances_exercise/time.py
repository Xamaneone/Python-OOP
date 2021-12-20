class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if len(str(self.seconds)) == 1:
            self.seconds = "0" + str(self.seconds)
        if len(str(self.minutes)) == 1:
            self.minutes = "0" + str(self.minutes)
        if len(str(self.hours)) == 1:
            self.hours = "0" + str(self.hours)
        result = f"{self.hours}:{self.minutes}:{self.seconds}"
        self.hours = int(self.hours)
        self.minutes = int(self.minutes)
        self.seconds = int(self.seconds)
        return result

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0

        return self.get_time()



time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())