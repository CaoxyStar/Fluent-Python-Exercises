class ParentA:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f'Name: {self.name}')


class ParentB:
    def __init__(self, age):
        self.age = age
    
    def info(self):
        print(f'Age: {self.age}')


class Child(ParentA, ParentB):
    def __init__(self, name, age):
        ParentA.__init__(self, name)
        ParentB.__init__(self, age)
    
    def info(self):
        ParentA.info(self)
        ParentB.info(self)


child = Child('Curry', 37)
child.info()