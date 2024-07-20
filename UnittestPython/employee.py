import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay): # we create Employee's instances __init__ is method
        #Of course, the __init__() method may have arguments for greater flexibility. 
        # In that case, arguments given to the class instantiation operator are passed on to __init__().
        self.first = first
        self.last = last
        self.pay = pay

    @property 
    def email(self): #methods
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self): #methods
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self): #methods
        self.pay = int(self.pay * self.raise_amt)
    
    #a new methon in our Employee class
    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
           return 'Bad Response!'