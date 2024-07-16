#https://www.geeksforgeeks.org/python-property-decorator-property/
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property # we define our email in the class like a method but we're able to access it like an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    
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

del emp_1.fullname