#Python Object-Oriented-Programming
#In Python object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming.
# It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. 
# The main concept of object-oriented Programming (OOPs) or oops concepts in Python is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data.
#Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it for maintaining its state.
#Class instances can also have methods (defined by its class) for modifying its state. Methods - a function that is associated with a class
#A class is a collection of objects.
# A class contains the blueprints or the prototype from which the objects are being created. 
#It is a logical entity that contains some attributes and methods. 
#An Object is an element (or instance) of a class
#An Instance is an object of the class
#Initialize class attributes - __init__ method in Python is used to initialize objects of a class. It is also called a constructor.
#Class attributes are class variables that are inherited by every object of a class. 
#The value of class attributes remain the same for every new object.
# Task
#Creating an application for the company - it represents our employees 
#Using class because each individual employee has specific attributes and methods -
#Each employee is going to have a name, an email address. They can perform actions 
#We could use a blueprint to create each employee so that we didn't have to do this manually each time from scratch
class EmployeeOld:
    pass 

class A:
    brand = 'B' #class attribute it sets an attribute brand of the class

#A class - a blueprint to create instances. Instances are an object built from that blueprint
# each unique employee that we create to use our employee class wil be an instance of that class

emp_1 = EmployeeOld() 
emp_2 = EmployeeOld()
#Each of these are going to be their own unique instances of the employee class

print(emp_1)
print(emp_2)
# We can see that both of these are employee objects - they're both unique, because they have different locations in memory
#Instances variables contain data which is unique to each instance

#Creating instance variables for each employee:
emp_1.first = 'Lukasz'
emp_1.last = 'Longwinter'
emp_1.email = 'email@gmail.com'
emp_1.pay = 4000
#We provide another employee with attributes:
emp_2.first = 'Adam'
emp_2.last = 'Adamowski'
emp_2.email = 'email2@gmail.com'
emp_2.pay = 7000
#Each of these instances has attributes that are unique to them

print(emp_1.email)
print(emp_2.email)

# We do not want to set these variables for another employees everytime
#__init__ method in Python is used to initialize objects of a class. It is also called a constructor.
#The self parameter is a reference to the Speaker class 
# and it's a convention in Python to always have it as the first parameter in a __init__ method. 
class Employee: #we are going to create this special init method.We created a method within a class. 
    def __init__(self, first, last, pay): #It is like initialize - constructor. We specify arguments after self
        self.first = first # instance variable unique to each instance  & instance attribute
        self.last = last # access the class attribute with the self keyword
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        #we create a method in our class to put functionalities in one place
        #each method in class takes an instance for the first argument called self
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
        
#We created our instances of our employee class right now

emp_1 = Employee('Lukasz', 'Longwinter',5000 )
emp_2 = Employee('Adam', 'Adamowski',7000 )

print(emp_1)
print(emp_2)
print(emp_1.email)
print(emp_2.email)

#We need to add some methods to class

print('{} {}'.format(emp_1.first, emp_1.last))
#After adding methods in class we can print the first and last name. We print out method -
print(emp_1.fullname()) #we return the value of the method
#we print out methods
print(emp_1.fullname)
#We are going to use this method to print two employees full name
print(emp_1.fullname())
print(emp_2.fullname())
#These lines of codes below doing the same exact thing:
# we can run this methods using class method itself. We need to pass instance as an argument
print(Employee.fullname(emp_1)) 
# we use emp_1 which is an instance, then I call a method -I do not need to pass  in self
emp_1.fullname()


