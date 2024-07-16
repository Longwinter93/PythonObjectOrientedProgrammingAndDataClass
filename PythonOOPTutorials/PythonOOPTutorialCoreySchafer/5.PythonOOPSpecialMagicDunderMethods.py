# https://docs.python.org/3/reference/datamodel.html 3.3.8. Emulating numeric types
# https://www.geeksforgeeks.org/dunder-magic-methods-python/

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
   #Thanks to special methods we are able to change some of built-in behavior and operations     
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay) #it returns a string that we can use to  recreate this object
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other): #we adding all salaries from employees
        return self.pay + other.pay 
    
    def __len__(self):  # it returns the total number of fullname of employees
        return len(self.fullname())
    
    
#Employee Instances
emp_1 = Employee('Corey', 'Schafer', 50000) 
emp_2 = Employee('Test', 'Employee', 60000)
#1
#print(emp_1) without repr it returns an object
#2
#print(emp_1) # it returns the string that we specified in a repr method
#3 
#print(emp_1) # it returns the str that we specified in a str method

#print(repr(emp_1))
#print(str(emp_1))

#4 It returns the same object
#print(repr(emp_1.__repr__()))
#print(str(emp_1.__str__()))

# these two special methods allow us to change how our objects are printed and displayed
# we use Dunder Methods:
#print(1+2)

#print(int.__add__(1,2))
# a string object uses their own Dunder method
#print(str.__add__('a', 'b')) # str concates these two together

#We added two employees objects together we combined their salaries
print(emp_1 + emp_2)


print(len('test'))
#Using Dunder Method
print('test'.__len__())

#The total number of employees' characters
print(len(emp_1))