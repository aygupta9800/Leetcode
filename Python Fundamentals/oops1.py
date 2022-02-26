# 1. In python, dictionaries and list are mutable but tuple and dictionary is not.

# 2.  class attributes
#     They have same value for all class attributes. kind of static variable in java
#     must be initialized with initial value
#     we can access class attributes same way as instance attributes like obj.propertyName as well as classname.propertyName
class Dog:
    species = "Canis familiris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

d1 = Dog("abc", 23)
print(d1.species)
d2 = Dog("cde", 25)
s = f"{d1.name} and is {d2.age}"
print(s)
print(Dog.species)

# 4. we can implement method __str__ method in class so whenever we print class obj, that str function will be called
class Dog:
    species = "Canis familiris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
        
if __name__=="__main__":
    d1 = Dog("abc", 23)
    print(d1)

#5. Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.
    