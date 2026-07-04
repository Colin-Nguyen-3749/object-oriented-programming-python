

class Dog(object):

    # add a method
    # this is the constructor 
    # If you want anything to happen
    # initially when you first create a class
    # use __init__
    # always put self in the parameters!
    def __init__(self, name, age):

        # create an attribute
        # These are like variables that 
        # belong to a certain object 
        # self represents the instance 
        # that we're calling
        # name comes from the parameter!
        # in the example below, Clifford is the 
        # instance being represented by self
        self.name = name
        self.age = age
        self.li = [1,3,4]

        print("Nice, you made a dog")

    # methods look just like functions,
    # except you have to call them using an 
    # object
    def speak(self):
        print("Hi, I am", self.name, "and I am", self.age, "years old.")


    def change_age(self, age):
        self.age = age


    def add_weight(self, weight):
        self.weight = weight



clifford = Dog("Clifford", 4)
clifford.speak()
clifford.change_age(5)
clifford.speak()
clifford.add_weight(8)

print(clifford.age)
print(clifford.name)
print(clifford.li)
print(clifford.weight)