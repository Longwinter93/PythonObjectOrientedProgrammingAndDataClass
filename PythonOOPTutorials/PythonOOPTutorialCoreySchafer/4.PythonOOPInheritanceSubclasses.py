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

#class Developer(Employee): #we would like to inherit all functionalities from Employee class a
    #pass #we can access the attributes that were actually set in our parent employee

class Developer(Employee): #we raise the raise amount to 10 %
    raise_amt = 1.10 
    
    def __init__(self, first, last, pay, prog_lang): #adding an argument for programming
        super().__init__(first, last, pay) #we let employee classes __init__ method handles first,last and pay
        self.prog_lang = prog_lang
        
class Manager(Employee): #we create a Manager class and inherit all functionalities from employee
    def __init__(self, first, last, pay, employees=None): #we add a list of employees that this manager supervises
        super().__init__(first, last, pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

#dev_1 = Employee('Corey', 'Schafer', 50000)
#dev_2 = Employee('Test', 'Employee', 60000)

#print(dev_1.email)
#print(dev_2.email)
#Task 1
#We are going to create a different kind of employees for example Developers & Managers
# We reuse this code by inherting from employee in order to create subclasses


#dev_1 = Developer('Corey', 'Schafer', 50000) 
#dev_2 = Developer('Test', 'Employee', 60000)

#print(dev_1.email)
#print(dev_2.email)

#print(help(Developer)) #help() function is a built-in function that provides information about modules, classes and functions
#We apply raise for current developer
#Task 2
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

#Task 3
#If we change an instance and back to employee, pay increases by 10%
#dev_1 = Employee('Corey', 'Schafer', 50000) 
# we can make changes to subclasses, without worrying breaking anything in the parent class

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

#Task 4
#Adding a new attribute to the class

#dev_1 = Developer('Corey', 'Schafer', 50000, 'Python') 
#dev_2 = Developer('Test', 'Employee', 60000, 'Java')  

#print(dev_1.first)
#print(dev_1.prog_lang)

#Task 5
#We create a Manager class
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python') 
dev_2 = Developer('Test', 'Employee', 60000, 'Java') 
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)
#Add an employee
mgr_1.add_emp(dev_2)
#Remove an employee from the list
mgr_1.remove_emp(dev_1)
#Print all employees that this manager supervises
mgr_1.print_emps()


print(isinstance(mgr_1, Manager))  #it tells us if an object is an instance of a class
print(isinstance(mgr_1, Employee))  #it tells us if an object is an instance of a class
print(isinstance(mgr_1, Developer))  #it tells us if an object is an instance of a class
print(issubclass(Developer, Employee)) # it tells uf if a class is a subclass of another class
print(issubclass(Manager, Employee)) # it tells uf if a class is a subclass of another class
print(issubclass(Manager, Developer)) # it tells uf if a class is a subclass of another class


