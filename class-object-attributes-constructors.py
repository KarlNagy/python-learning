
# Class: blueprint for an object
#   - define new types (like list, dictionaries, etc., but more complex)
#   -after defining w/name, define methods (.*) to associate with it
#
# Object: instance of a class
#
# Attributes: variables that belong to a particular object
#   -ex. Point object: has (x) and (y) as attributes
#
# Constructor: function that is called at the time of creating an object
#   -sets the parameters the function will accept
#   -(self) references the object created from that class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")



person1 = Person(age = 20, name = "frank")
person1.talk()

bob = Person("Bob Smith",30)
bob.talk()