class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        if new_value < self.limit:
            self.value = new_value

    def tick(self):
        self.value += 1
        if self.value == self.limit:
            self.value = 0
            return True
        return False

    def __str__(self):
        return str(self.value).zfill(2)

counter = Counter(30)

'''
# 0부터 5까지 센다
print("1부터 5까지 카운트하기")
for i in range(5):
    counter.tick()
    print(counter)

# 타이머 값을 0으로 바꾼다
print("카운터 값 0으로 설정하기")
counter.set(0)
print(counter)

# 카운터 값 27로 설정
print("카운터 값 27로 설정하기")
counter.set(27)
print(counter)

# 카운터 값이 30이 되면 0으로 바뀌는지 확인
print("카운터 값이 30이 되면 0으로 바뀝니다")
for i in range(5):
    counter.tick()
    print(counter)
'''

class Clock:
    HR = 24
    MIN = 60
    SEC = 60

    def __init__(self, hr, min, sec):
        self.hr = Counter(Clock.HR)
        self.min = Counter(Clock.MIN)
        self.sec = Counter(Clock.SEC)
        self.set(hr, min, sec)

    def __str__(self):
        return "{}:{}:{}".format(self.hr, self.min, self.sec)

    def tick(self):
        if self.sec.tick():
            if self.min.tick():
                self.hr.tick()

    def set(self, hr, min, sec):
        self.hr.set(hr)
        self.min.set(min)
        self.sec.set(sec)

# 1시 30분 48초인 시계 인스턴스 생성
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)