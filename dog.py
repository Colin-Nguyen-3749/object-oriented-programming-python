class Dog:
    dogs = []
    xc = 5

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # these are called decorators to 
    # indicate that they are a special 
    # type of method!
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
    
    # these don't need the class to be called
    # no self no class
    # use these as a function but they're 
    # just organized in a class for tidiness
    @staticmethod
    def bark(n):
        # bark n times
        for _ in range(n):
            print("Bark!")

# clifford = Dog("Clifford")
# # print(clifford.bark(5))

# print(clifford.num_dogs())

# # to access class variables, you don't need an instance!
# print(Dog.dogs)

Dog.bark(3) # call static method