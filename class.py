

# class Dog(object):

#     # add a method
#     # this is the constructor 
#     # If you want anything to happen
#     # initially when you first create a class
#     # use __init__
#     # always put self in the parameters!
#     def __init__(self, name, age):

#         # create an attribute
#         # These are like variables that 
#         # belong to a certain object 
#         # self represents the instance 
#         # that we're calling
#         # name comes from the parameter!
#         # in the example below, Clifford is the 
#         # instance being represented by self
#         self.name = name
#         self.age = age

#         print("Nice, you made a dog")

#     # methods look just like functions,
#     # except you have to call them using an 
#     # object
#     def speak(self):
#         print("Hi, I am", self.name, "and I am", self.age, "years old.")

    
#     def talk(self):
#         print("Bark!")


# class Cat(Dog):
#     def __init__(self, name, age, color):

#         # in this case, the super class is 
#         # Dog since it's the class that we're
#         # inheriting from
#         super().__init__(name, age)
#         self.color = color

#     # override something from the parent class
#     # Instead of barking, we're going to meow
#     # basically using the same method name twice,
#     # the method in this class overrides the previous
#     # class everytime you call an instance for Cat
#     def talk(self):
#         print("Meow.")


    


# gumball = Cat('gumball', 5, 'blue')
# gumball.talk()


# try a more general class to practice inheritance!
class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = gas

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas
    

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

        def beep(self):
            print("HONK")

