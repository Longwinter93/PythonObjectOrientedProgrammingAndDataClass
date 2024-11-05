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

# In[4]:


names = ['Alice', 'Bob', 'Charlie']

for index, name in enumerate(names, start=1):
    print(f'{index}. {name}')


# In[9]:


tasks = ['Write report', 'Attend Meeting', 'Review Code', 'Submit timesheet']

for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1 }. {task}")


# In[13]:


for index, task in enumerate(tasks, start=1):
    print(f'{index}. {task}')


# In[14]:


print(list(enumerate(tasks)))


# # dataclass

# In[5]:


from dataclasses import dataclass


# In[6]:


@dataclass 
class Person:
    name: str
    age: int
    job: str


# In[8]:


person = Person(name='Alice', age=30, job="Engineer")

print(person)


# # Try / Except

# In[16]:


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

