class Animal:
    def __init__(self):
        print('Animal Constructor')
        self.age = 1

    def eat(self):
        print('eat')

# Animal : Parnet, Base
# Mamal : Child, Sub


class Mammal(Animal):
    def __init__(self):
        print('Mammal Constructor')
        self.weight = 2
        super().__init__()  # this position responsibility with how parent being executed

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print('fly')


# class Chicken(Bird): # this is bad
#     pass


# m = Mammal()
# # m.eat()
# print(m.age)

# # print(isinstance(m, object))
# # print(issubclass(Mammal, Animal))
# # print(issubclass(Mammal, object))

# print(m.weight)
