#In an Employee class, we set names, emails and pay in our init method. 
#these are set for each instance of the employee
#Class variables are shared among all instances
#Instance variables can be unique for each instance such as names , email , pay
#Class variables should be the same for each instance
#Difference between instance variables and class variables

class Employee:
    num_of_emps = 0 #keeping track how many employees we have - it should be the same for all instances of our class
    raise_amount = 1.04  # class variable shared by all instances

    def __init__(self, first, last, pay):
        self.first = first # instance variables using self arguments
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
        Employee.num_of_emps += 1 #we add it to __init__ method because it runs every time we create a new employee

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): # create a method
        self.pay = int(self.pay * Employee.raise_amount)
        
print(Employee.num_of_emps) # it returns 0 because we do not create any employees
# Instances of class:
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps) # It returns 2 because it is incremented twice when we instantiated both employees

print(Employee.fullname(emp_1))
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
Employee.apply_raise(emp_1)
print(emp_1.pay)
print(emp_2.pay)
Employee.apply_raise(emp_2)
print(emp_2.pay)


#Test a new method in an instance
#print(emp_1.pay)
#emp_1.apply_raise() # we need to invoke it to make multiple
#print(emp_1.pay)


#print(Employee.raise_amount) # we can access this class variable from both my class itself
#print(emp_1.raise_amount) # we can also access this class variable from instances
#print(emp_2.raise_amount)

#print(emp_1.__dict__)

#print(Employee.__dict__) # this class has raise_amount attribute


#Employee.raise_amount = 1.05 # it changes a raise_amount value for class and all instances
#print(Employee.raise_amount) 
#print(emp_1.raise_amount) 
#print(emp_2.raise_amount)
#We use an instance instead of using class:
#emp_1.raise_amount = 1.05 # it changes a raise_amount value for only emp_1
#print(Employee.raise_amount) 
#print(emp_1.raise_amount) 
#print(emp_2.raise_amount)
#print(emp_1.__dict__) # it returns raise_amount 1.05 value

