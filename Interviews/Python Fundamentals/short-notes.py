"""
    

1. In python, dictionaries and list are mutable but tuple and dictionary is not.

2.  class attributes
    They have same value for all class attributes. kind of static variable in java
    must be initialized with initial value
    we can access class attributes same way as instance attributes like obj.propertyName as well as classname.propertyName
    
3. Different ways to print in python
print(f"{self.name} is {self.age} years old")
print("My name is {}".format(self.name))
we can just return whole this f"{} {}" type string from a function and print later

4. we can implement method __str__ method in class so whenever we print class obj, that str function will be called

we can also use __repr__() method in class to print object with string, then we can call it using print([obj])

if no __str__() method is defined, print(obj) will use __repr__() method
if no __repr__() method is defined then default is used

5. Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.

6. Inheritance in python:
you can pass parent class as argument
class blackDog(Dog):
    pass
Instances of child classes inherit all of the attributes and methods of the parent class:

7. to know the type of object we can use type(obj) which will give us class name which it belongs to
8. a child class object is also a instance of parent class.
so to check whether an obj is an instance of a class or not we can use isinstance(obj, className) which return Boolean

9. changes in parent class automatically propogates to child class unless method or attribute is overridden.

10. You can access the parent class from inside a method of a child class by using super().fn(parametrs)
you can also fn of parent class in child class method by className.fnname(self, parameters)

11. we can create a variable private by declaring variable say as __a
# printing obj.a directly will then give error


12. In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.

13. issubclass(Derived, Base), isinstance(d, Base)


14. TO access parentclass property we can use:
    BaseClassName.propertyName = value
    super
"""