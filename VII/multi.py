# class Employee:
#     def greet(self):
#         print("Employee Greet")

class Flyer:
    def fly(self):
        print("I'm Flying")


# class Person:
#     def greet(self):
#         print('Employee Guest')

class Swimmer:
    def swim(self):
        print("I'm Swimming")


# class Manager(Person, Employee):
#     pass

class FlyingFish(Flyer, Swimmer):
    pass


# manager = Manager()
# manager.greet()

fish = FlyingFish()
fish.fly()
fish.swim()
