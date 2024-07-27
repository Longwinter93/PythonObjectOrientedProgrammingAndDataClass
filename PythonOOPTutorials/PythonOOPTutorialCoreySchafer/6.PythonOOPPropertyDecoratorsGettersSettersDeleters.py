#https://www.geeksforgeeks.org/python-property-decorator-property/
#https://www.freecodecamp.org/news/python-property-decorator/
#The @property is a built-in decorator for the property() function in Python.
#It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters
#when we define properties in a class.
#@property decorator is a built-in decorator in Python 
#which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). 
#Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters. 
#Using @property decorator to define getters, setters, and delete
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
#Specifically, you can define three methods for a property:
#A getter - to access the value of the attribute.
#A setter - to set the value of the attribute.
#A deleter - to delete the instance attribute.
    
    @property # we define our email in the class like a method but we're able to access it like an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    #We are going to define a property
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #we have a setter method to decorate a function
    @fullname.setter 
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last 
        
    
    @fullname.deleter  #we use it to delete an attribute
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
        
#We create this simple Employee object
emp_1 = Employee('John', 'Smith')
#Property decorator allows us to define a method that we can access it like an attribute
#We do not write emp_1.fullname() for example thanks to property decorator

#Thanks to this setter, it works for this name:
emp_1.fullname = 'Corey Schafer' # this name Corey Schafer goes to this fullname.setter 

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
#the body, where we delete the instance attribute
del emp_1.fullname