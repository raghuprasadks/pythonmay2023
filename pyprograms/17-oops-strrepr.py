class Person():
    def __init__(self, name):
        self.name = name
    """
    def __str__(self):
        return f'Name is {self.name}'
    """
    def __repr__(self):
        return f'Person(name={self.name})'


obj = Person('raghav')
print(obj)
#print(obj.__str__())
#print(obj.__repr__())
