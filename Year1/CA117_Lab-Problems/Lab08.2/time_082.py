class Time(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        return ((self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds))

    def __gt__(self, other):
        return self.time_to_seconds() > other.time_to_seconds()

    def __add__(self, other):
        return self.seconds_to_time(self.time_to_seconds() + other.time_to_seconds())

    def __iadd__(self, other):
        z = self + other
        self.hours, self.minutes, self.seconds = z.hours, z.minutes, z.seconds
        return self

    def __str__(self):
        return ("The time is {:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds))

    def time_to_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60 + self.seconds

    @classmethod
    def seconds_to_time(cls, s):
        minutes, seconds = divmod(s, 60)
        hours, minutes = divmod(minutes, 60)
        overflow, hours = divmod(hours, 24)
        return cls(hours, minutes, seconds)
