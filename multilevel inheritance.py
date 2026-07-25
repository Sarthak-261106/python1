class Vehicle:
    company='xyz motors'

    def __init__(self,n_wheels,n_seats,mileage):
        print('init of vehicle')
        self.n_wheels=n_wheels
        self.n_seats=n_seats
        self.mileage=mileage

    def get_details(self):
        return f'this vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provide mileage of {self.mileage}'

class Car(Vehicle):
    def __init__(self,car_type,drive_type,wheels,seats,mileage):
        print('init of car')
        self.car_type=car_type
        self.drive_type=drive_type
        super().__init__(wheels,seats,mileage)

    def display_info(self):
        print(f'car type is {self.car_type}, drive type is {self.drive_type}')

class ElectricCar(Car):
    print('init of ElectricCar')
    def __init__(self,car_type,drive_type,wheels,seats,mileage,battery_capacity,range):
        self.battery_capacity=battery_capacity
        self.range=range
        super().__init__(car_type,drive_type,wheels,seats,mileage)

    def charge(self):
        print(f'charging to {self.battery_capacity}%')



ec1=ElectricCar('sedan','manual',4,5,22,100,400)

print(ec1.__dict__)

