# method chaining = it is used to call multiple methods sequentially
#                     each call performs on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine.")
        return self

    def drive(self):
        print("You drive the car.")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You stop the engine")
        return self


car = Car()

car.turn_on().drive().brake().turn_off()