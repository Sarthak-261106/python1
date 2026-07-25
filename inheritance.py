class Vehicle:
    company='xyz motors'

    def __init__(self,n_wheels,n_seats,mileage):
        self.n_wheels=n_wheels
        self.n_seats=n_seats
        self.mileage=mileage

    def get_details(self):
        return f'this vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provide mileage of {self.mileage}'

# v1=Vehicle(4,5,20)
# print(v1.get_details())

class Car(Vehicle):
    def __init__(self,car_type,drive_type,wheels,seats,mileage):
        print('init of car')
        self.car_type=car_type
        self.drive_type=drive_type
        super().__init__(wheels,seats,mileage)

c1=Car('sidan','manual',4,7,22)
print(c1.get_details())
print(c1.__dict__)