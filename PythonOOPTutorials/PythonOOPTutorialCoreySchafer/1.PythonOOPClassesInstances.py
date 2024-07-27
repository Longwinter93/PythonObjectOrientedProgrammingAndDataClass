#Task
#Creating an application for the company - it represents our employees 
#Using class because each individual employee has specific attributes and methods -
#Each employee is going to have a name, an email address. They can perform actions 
#We could use a blueprint to create each employee so that we didn't have to do this manually each time from scratch
class EmployeeOld:
    pass 

class A:
    brand = 'B' #class attribute it sets an attribute brand of the class

#A class - a blueprint to create instances. Instances are an object built from that blueprint
#Each unique employee that we create to use our employee class will be an instance of that class

emp_1 = EmployeeOld() 
emp_2 = EmployeeOld()
#Each of these are going to be their own unique instances of the employee class

print(emp_1)
print(emp_2)
#We can see that both of these are employee objects - they're both unique, because they have different locations in memory
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


