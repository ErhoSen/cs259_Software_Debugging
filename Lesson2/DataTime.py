class Time:

    def __init__(self, h=0, m=0, s=0):
        assert 0 <= int(h) <= 23
        assert 0 <= int(m) <= 59
        assert 0 <= int(s) <= 60 # Leap second!

        self._hours = int(h)
        self._minutes = int(m)
        self._seconds = int(s)

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def __repr__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.get_hours(), self.get_minutes(), self.get_seconds())

t = Time(13, 0, 0)
print t

t1 = Time(1, 3.14, 2)
print t1