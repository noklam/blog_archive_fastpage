class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        raise NotImplementedError
        print('Setter!')
        self._age = age 

p = Person('Bob', 23)
p.age = 100
