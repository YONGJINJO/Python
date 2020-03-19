from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass

    def stop(self):
        self._speed = 0
        pass

    @property
    @abstractmethod
    def speed(self):
        pass

class Bicycle(Vehicle):
    max_speed = 15

    def __init__(self, value):
        self._speed = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        self.speed = self.max_speed / 3
        print("자전거 페달 돌리기 시작합니다.")

    def __str__(self):
        return "이 자전거는 현재 {}km/h로 주행 중입니다.".format(self.speed)

class NormalCar(Vehicle):
    def __init__(self, speed, max_speed):
        self.now = True
        self._speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self.speed = new_value if 0 <= new_value <= self.max_speed else 0


    def start(self):
        self._speed = self.max_speed / 2
        print("일반 자동차 시동겁니다.")

    def __str__(self):
        return "이 일반 자동차는 현재 {}km/h로 주행 중입니다.".format(self._speed)

class SportsCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed

    def start(self):
        self._speed = self.max_speed
        print("스포츠카 시동겁니다.")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 < new_value <= self.max_speed else 0

    def __str__(self):
        return "이 스포츠카는 현재 {}km/h로 주행 중입니다.".format(self._speed)

class DrivingSimulator:
    def __init__(self):
        self.vehicles = []


    def add_vehicle(self, new_vehicle):
        if isinstance(new_vehicle, Vehicle):
            self.vehicles.append(new_vehicle)
        else:
            print("{}은 교통 수단이 아니기 때문에 추가할 수 없습니다.".format(new_vehicle))

    def start_all_vehicles(self):
        print("모든 교통 수단을 주행 시작시킵니다!")
        for vehicle in self.vehicles:
            vehicle.start()

    def stop_all_vehicles(self):
        print("모든 교통 수단을 주행 정지시킵니다!")
        for vehicle in self.vehicles:
            vehicle.stop()

    def __str__(self):
        self.speed_info = ""
        for vehicle in self.vehicles:
            self.speed_info += (str(vehicle) + "\n")
        return self.speed_info


# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)


# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)

'''
# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스
car = NormalCar(0, 100)

# 스포츠카 인스턴스
sports_car = SportsCar(0, 200)

# 정의한 인스턴스들을 모두 주행 시작시킨다
bicycle.start()
car.start()
sports_car.start()

# 자전거의 속도를 출력한다
print(bicycle)

# 자전거만 주행을 멈춰준다
bicycle.stop()

# 결과 값을 출력한다
print(bicycle)
print(car)
print(sports_car)
'''