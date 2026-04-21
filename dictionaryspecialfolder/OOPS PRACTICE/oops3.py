class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("New Speed:", self.speed)

c1 = Car("BMW", 50)
c1.accelerate()