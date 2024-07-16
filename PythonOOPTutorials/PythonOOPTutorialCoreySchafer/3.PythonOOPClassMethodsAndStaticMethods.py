#Regular methods - it automatically pass the instance as the first argument - it is called self
#Class methods - it automatically pass the class as the first argument - it is called  cls 
#Static methods - it does not pass any methods automatically - they do not pass the instance or the class
#Decorator - Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class.
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
#Constructor -Constructors are generally used for instantiating an object.
#The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.
#In Python the __init__() method is called the constructor and is always called when an object is created.
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay): #body of the constructor
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self): # self - regular methods in a class automatically take the instance as the first argument - it is an instance variable called self
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod #adding a decorator - classmethod - it takes automatically class as the first argument. It turns a regular method to a class method
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount 
    
    @classmethod 
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod #does not take instance or class as a first argument, we pass any arguments that we work on it
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True
    
#Two employees instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(Employee.raise_amt) #classes raised amount
print(emp_1.raise_amt) #instances raised amount
print(emp_2.raise_amt)

#2
#Change raised amount to 5 %
Employee.set_raise_amt(1.05) #we use a classmethod set_raise_amt, now we work with class instead of the instance
#All raised amount is increased
print(Employee.raise_amt) #classes raised amount
print(emp_1.raise_amt) #instances raised amount
print(emp_2.raise_amt)

#3
#Alternative constructors
#A problem case - someone uses a class:
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
#We need to split a string on the hyphen
first, last, pay = emp_str_1.split('-')
#We create a new employee
new_emp_1 = Employee(first, last, pay) # we pass these values and run an init method

print(new_emp_1.email)
print(new_emp_1.pay)

#We are going to create a new classmethod
#We use a classmethod as an alternative constructor

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)


print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_2.email)
print(new_emp_2.pay)
print(new_emp_3.email)
print(new_emp_3.pay)


#Static method
#We are going to create a simple function that takes a date and returns whether or not it is a workday
#It does not depend on any specific instance or class variable
import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
my_date2 = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date2))