class time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s
    def __add__(self, t):
        h = self.__hour + t.__hour
        m = self.__minute + t.__minute
        s = self.__second + t.__second
        if s >= 60:
            m = m + s // 60
            s = s % 60
        if m >= 60:
            h = h + m // 60
            m = m % 60
        return time(h, m, s)
    def display(self):
        print("Time:", self.__hour, ":", self.__minute, ":", self.__second)

t1 = time(2, 45, 50)
t2 = time(1, 30, 20)
t3 = t1 + t2
t3.display()

