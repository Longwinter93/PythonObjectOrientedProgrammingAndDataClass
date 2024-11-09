#!/usr/bin/env python
# coding: utf-8

# # any()

# In[1]:


numbers = [0, 1, 2, 3, 4]

print(any(numbers))


# In[2]:


numbers2 = [-1, -2, 0, -4]
print(any(num > 0 for num in numbers2))


# # enumerate()

# In[3]:


names = ['Alice', 'Bob', 'Charlie']

for index, name in enumerate(names, start=1):
    print(f'{index}. {name}')


# In[4]:


tasks = ['Write report', 'Attend Meeting', 'Review Code', 'Submit timesheet']

for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1 }. {task}")


# In[5]:


for index, task in enumerate(tasks, start=1):
    print(f'{index}. {task}')


# In[6]:


print(list(enumerate(tasks)))


# # dataclass

# In[7]:


from dataclasses import dataclass


# In[8]:


@dataclass 
class Person:
    name: str
    age: int
    job: str


# In[9]:


person = Person(name='Alice', age=30, job="Engineer")

print(person)


# # Try / Except

# In[10]:


def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)


# # Fibonacci

# In[11]:


# Fn = F(n-1) + F(n-2)

def Fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibo(n-1) + Fibo(n-2)

Fibo(7)


# In[12]:


a, b = 0 , 1
n = 7

for i in range(n):
    print(a, end =' ')
    a, b = b, a + b
    


# In[13]:


a, b = 0 , 1 
n = 15

while b < n:
    print(a, end=' ')
    a, b = b, a + b


# # Ternary Operators

# In[14]:


# result_if_true if condition else result_if_false


# In[15]:


weather = 'sunny'

if weather == 'sunny':
    print('Go to the beach')
else:
    print('Stay at home')


# In[16]:


'Go to the beach' if weather == 'sunny' else 'Stay at home'


# In[17]:


x = 3
y = 5

result = x if x < y else y
print(result)


# In[18]:


my_list = list(range(1,6))
element = 5
print(my_list)
result = 'Element Present in The List' if element in my_list else 'It does not exist'
print(result)


# In[19]:


number = 2

result = 'Even' if number % 2 == 0   else 'Odd'
print(result)


# In[20]:


x = 5
y = 7

result = x + y if x < y  else x - y
print(result)


# In[21]:


def get_default_value():
    return 'Default'

x = None 

result = x if x is not None else get_default_value() 
print(result)


# In[22]:


def get_discount(customer):
    return 10 if customer == "VIP" else 5

customer_type = 'Regular'

discount = get_discount(customer_type) if customer_type != 'Regular' else 0 
print(discount)


# In[23]:


def Name(name):
    return 'A great name' if name =='Lukasz' else 'No Name'
name = 'Adam'
result = Name(name) if name == 'Lukasz' else 'An ugly name'

print(Name('Lukasz'))
print(Name('Adam'))
print(result)


# In[24]:


a = 100
b = 200
print(a, "is greater" if (a>b) else print(b, "is greater"))


# ## Nested Ternary Operators
# ### Multiple conditions

# In[25]:


num = 6 
result = 'A small number' if num < 5 else ('A medium number' if num < 15 else 'A large number')
print(result)


# ### Ternary Operators using Tuples
# #### (false_value, true_value) [condition]

# In[26]:


# value = (x if condition else y)
a, b = 1, 5

print((a, b)[a < b])


# In[27]:


t = 90
('Water is not boling', 'Water is boiling')[t >= 100]


# ### Ternary Operators using Dictionaries

# In[28]:


a , b = 1 , 5
result = {True: a, False: b} [a < b]
print(result)


# In[29]:


t = 90
{True: 'Water is boiling', False: 'Water is not boiling'}[t >= 100]


# ### Ternary Operators using Lambda

# In[30]:


t = 90 


# In[31]:


(lambda: 'Water is not boiling', lambda: 'Water is boiling')[t >= 100]()

