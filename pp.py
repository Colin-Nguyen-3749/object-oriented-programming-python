# there are no such things as private or public classes 
# in python, these are just examples
# the _ before the name is just to show that the
# methods are supposed to be private (that's the best we can do)
# and yes, it's a convention
class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hello")

    def display(self):
        print("HI")