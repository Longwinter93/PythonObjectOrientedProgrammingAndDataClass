#!/usr/bin/env python
# coding: utf-8

# # For Loop

# #### For Loop - It executes a block of code repeatedly

# In[1]:


for number in range(5):
    print("Thank you")


# In[2]:


for x in [0,1,2]:
    print(x)


# In[3]:


symbols = {'12123312123': 'APPL',
           '765757567756':'CSVO',
           '598918919':'ORCL'}

for k in symbols:
    print(symbols[k])


# In[4]:


for key, value in symbols.items():
    print(key, value)


# In[5]:


for x in 'ORACLE':
    print(x)


# In[6]:


languages = ['R', 'Python', 'Scala', 'Java',' Julia']


# In[7]:


for index in range(len(languages)):
    print("Current language:", languages[index])


# In[8]:


for index in range(5):
    print("Current language", languages[index])


# In[9]:


#Printing Thank you a 3 times

for number in range(3):
    print("Thank you")


# In[10]:


# it stops the iteration if we encounter 5
for i in range(10):
    print(i)
    if i == 5:
        break


# In[11]:


for i in range(20):
    if i % 2 == 0:
        continue
    print(i)


# In[12]:


# we ignore value for example 2
for x in [0,1,2,3]:
    if x == 2:
        continue
    print(x)


# In[13]:


nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)


# In[14]:


nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Skip 3')
        continue
    print(num)


# In[15]:


for i in range(10):
    print(i+1)


# In[16]:


for i in 'Datacamp':
    if i == 'a':
        print(i)


# In[17]:


sequence = [1,2,8,100,200,'datacamp','tutorial']


# In[18]:


for i in sequence:
    print(i)


# In[19]:


len(sequence)


# In[20]:


sequence[5]


# In[21]:


for i in range(len(sequence)):
    print(sequence[i])


# In[22]:


for i in range(len(sequence)):
    element = sequence[i]
    if type(element) == int:
        sequence[i] = element  + 1


# In[23]:


sequence


# In[24]:


for i in range(1,20,2):
    print(i)


# In[25]:


for i in range(11):
    for j in range(i):
        print(i, end= ' ')
    print()


# In[26]:


import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')


# In[27]:


iris.head()


# In[28]:


len(iris) # rows


# In[29]:


iris.iloc[1,2]


# In[30]:


iris.iloc[111,4] # we are on the 'species' column


# In[31]:


for i in range(len(iris)):
    Class = iris.iloc[i,4]
    if Class == 'versicolor' and i < 70:
        print(Class)


# In[32]:


for index, row in iris.iterrows():
    print(row["species"])


# In[33]:


iris.at[0,'sepal_length']


# In[34]:


columns =  ['sepal_length','sepal_width','petal_length','petal_width']

for indices, row in iris.iterrows():
    for column in columns:
        iris.at[indices, column] = row[column] + 2


# In[35]:


iris


# # Nested loops

# In[36]:


for number in range(3):
    print("---------------------------------------------")
    print("I am outer loop iteration "+str(number))
    #inner loop
    for another_number in range(5):
        print("*************************")
        print("I am inner loop iteration "+str(another_number))


# In[37]:


for i in range(5):
    print('*')
    for j in range(i + 1):
        print("*",end=' ')

for i in range(5,-1,-1):
    print('*')
    for j in range(i + 1):
        print("*",end=' ')
       


# In[38]:


for i in range(2):
    print('outer',i)


# In[39]:


for i in range(4):
    print('outer',i)
    for j in range(i + 1):
        print('inner',j)


# In[40]:


for i in range(4):
    print('outer',i)
    for j in range(i + 1):
        print('inner',j, end=" ")


# In[41]:


for i in range(4,-1,-1):
    print('outer',i)
    for j in range(i + 1):
        print('inner',j, end=" ")


# In[42]:


for i in range(5):
    print("*")
    for j in range(i+1):
        print("*", end=" ")


# In[43]:


for i in range(5,-1,-1):
    print("*")
    for j in range(i + 1):
        print("*", end=" ")


# In[44]:


for i in range(3):
    for j in range(3):
        print(i, j )


# In[45]:


for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)


# In[46]:


nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter) #for each number it will loop through every character in this string 'abc' 
                            #and print out the number and character, then move on to the next number and do it over again


# In[259]:


for x in range(3): #this for loop repeats this code 3 times
    for y in range(1,10):
        print(y, end="")
    print()


# In[260]:


rows = int(input('Enter the # of rows: '))
columns = int(input('Enter the # of columns: '))
symbol =  input("Enter a symbol to use: ")

for x in range(rows): #this for loop repeats this code 3 times
    for y in range(columns):
        print(symbol, end="")
    print()


# In[265]:


for x in range(5):
    for y in range(10):
        print(y, end ='')
    print()


# # While

# #### While loop - it executes a piece of code over and over again while a given condition still holds true

# In[47]:


number = 2

while number < 5:
    print('Thank you')
    number += 1 


# In[48]:


number = 0
while number < 5:
    print(f"The number is {number}")
    number += 1 


# In[49]:


number = 0

while number < 10:
    if number % 2 == 0:
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")
        
    number += 1
    


# In[50]:


number = 2

while number < 6:
    print(number)
    number += 1


# In[51]:


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1 
        print(result)
        return result 
    
n = input("Give me a number: ")

while n !=1:
    n = collatz(int(n))


# In[52]:


number = 0

while number < 3:
    print("Thank you ")
    number += 1


# In[53]:


number = 1

while number < 10:
    while number % 2 ==0:
        print("The number "+str(number)+" is even")
        break 
    number += 1


# In[54]:


for number in range(3) : 
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    for another_number in range(3):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))
        break


# In[55]:


error = 50.0

while error > 1:
    error = error / 4
    print(error)


# In[56]:


offset = 8

while offset != 0:
    print("Correcting")
    offset -= 1
    print(offset)
    


# In[57]:


while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        break
    print("Invalid input. Please try again")


# In[58]:


stock = 10 
num_of_purchases = 0

while num_of_purchases < stock:
    num_of_purchases += 1
    if stock - num_of_purchases > 7:
        print("Plenty of stock remaining")
    elif stock - num_of_purchases > 3:
        print("Some stock remaining")
    elif stock - num_of_purchases != 0:
        print("Low stock!")
    else:
        print("No stock")


# In[59]:


x = 0 

while x < 10:
    print(x)
    x += 1


# In[60]:


x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


# In[61]:


x = 0 

while True:
    if x == 5:
        break
    x += 1
    print(x)


# # range()

# In[62]:


range(10)


# In[63]:


for i in range(10):
    print(i)


# In[64]:


for i in range(5,10,2):
    print(i)


# In[65]:


for i in range(1,11):
    print(i)


# In[66]:


type(range(100))


# In[67]:


list(range(10))


# In[68]:


len(list(range(10)))


# In[69]:


for seq in range(-5,0):
    print(seq)


# In[70]:


for seq in range(50,1000,100):
    print(seq)


# In[71]:


for seq in range(100,10,-10):
    print(seq)


# In[72]:


list1 = [2,4,6,8,10,12,14,16,18,20]
counter = 0

for i in range(len(list1)):
    counter = counter + list1[i]
    print(counter)
print(f'Sum of the list : {counter}')

SumOfTheList = sum([x for x in list1])
print(f'List Comprehension SumOfTheList: {SumOfTheList}')


# In[73]:


from itertools import chain 

a1 = range(10,0, -2)
a2 = range(30,20,-2)
a3 = range(50,40,-2)
final = chain(a1, a2, a3)
print(final)
print(list(final))


# In[74]:


for a in final:
    print(a)


# In[75]:


a = list(range(0, 10, 3))
b = list(range(0, 11, 3))
c = list(range(0, 11, 2))
print(a == b)
print(a == c)


# # if elif else

# In[76]:


z = 4 

if z % 2 == 0:
    print('z is even')


# In[77]:


if z % 2 == 0:
    print('Checking ' + str(z))
    print('z is even')


# In[78]:


z = 5 
if z % 2 == 0: # False, no output
    print('Checking ' + str(z))
    print('z is even')
    


# In[79]:


z = 5 

if z % 2 == 0:
    print('z is even')
else:
    print('z is odd')


# In[80]:


z = 5

if z % 2 == 0:
    print('z is divisible by 2')
elif z % 3 == 0:
    print('z is divisible by 3')
else:
    print('z is neither divisible by 2 nor by 3')


# In[81]:


room = 'bed'
area = 14.0

if room == 'kit':
    print('Looking around in the kitchen')
elif room == 'bed':
    print('Looking around in the bedroom')
else:
    print('Looking around elsewhere')
    
if area > 15:
    print('It is a small place')
else:
    print('Pretty small')


# # Lambda function

# In[82]:


x = [20, 30, 40, 50, 60]
y = []


# In[83]:


x


# In[84]:


for v in x:
    y += [v * 5]


# In[85]:


x


# In[86]:


y = map(lambda x: x * 5, x)
y


# In[87]:


list(y)


# In[88]:


columns


# In[89]:


for column in columns:
    iris[column] = iris[column].apply(lambda row: row + 2)


# In[90]:


iris


# In[236]:


add = lambda x,y: x + y
add(10,10)


# In[239]:


nums = [48, 6, 9, 21, 1]

square_all = map(lambda x: x **2, nums)
ListComprehension = [x ** 2 for x in nums]

print(square_all)
print(f'It is from map function {list(square_all)}, then it is from List Comprehension {ListComprehension}')





# In[240]:


def echo_world(words,echo):
    word = words * echo
    return word

echo_world('Lukasz',5)


# In[241]:


echo_worlds = lambda words, echo: words * echo 
echo_worlds('Lukasz', 5)


# In[242]:


add_1 = lambda x: x + 1
add_1(5)


# In[243]:


my_numbers = [1,2,3,4,5,6,7,8,9,10]

def square(x):
    return x ** 2

squares = list(map(square, my_numbers))

squares_lambda = list(map(lambda x: x**2, my_numbers))

squares_list_comprehesion = [x**2 for x  in my_numbers]

print(f'Result from function {squares}, result from lambda {squares_lambda}, result from list comprehension {squares_list_comprehesion}')


# In[245]:


evens = list(filter(lambda x: x % 2 == 0, my_numbers))
evensListComprehension = [x for x in my_numbers if x % 2 == 0]

print(f'Result from a filter {evens}, then result from a List Comprehension {evensListComprehension}')


# In[248]:


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda x: x[2])


# In[252]:


from functools import reduce
numbers = [1,2,3,4,5]

sum_of_numbers = reduce(lambda x, y: x+y, numbers)
print(sum_of_numbers)

max_value = reduce(lambda acc, x:acc  if acc > x else x, numbers)
print(max_value)

List_Comprehension = max([x for x in numbers])
Sum_List_Comprehension = sum([x for x in numbers])
print(List_Comprehension)
print(Sum_List_Comprehension)


# # List Comprehension

# In[121]:


numbers = range(10)

new_list = []

for n in numbers:
    if n % 2 == 0:
        new_list.append(n**2)

print(new_list)


# In[122]:


new_listcomprehension = [x**2 for x in numbers if x % 2 == 0]
print(new_listcomprehension)


# ## Instead of map() & filter() & reduce() &  lambda(), using List Comprehension

# In[158]:


kilometer = [39.2, 36.5, 37.3, 37.8]

feet = map(lambda x: float(3280.8399)*x, kilometer)
listfeet = list(feet)
print(listfeet)


# In[153]:


newfeetListComprehension = [x*float(3280.8399) for x in kilometer]
print(newfeetListComprehension)


# In[162]:


feet = list(map(int,listfeet))
print(feet)


# In[166]:


uneven = filter(lambda x: x%2, feet)
print(list(uneven))


# In[191]:


ListComprehensionInt = [int(x) for x in newfeetListComprehension]
print(ListComprehensionInt)


# In[173]:


ListComprehensionEvenTrue = [x % 2 for x in ListComprehensionInt]
print(ListComprehensionEvenTrue)
ListComprehensionEven = [x for x in ListComprehensionInt if x % 2 != 0]
print(ListComprehensionEven)


# In[174]:


from functools import reduce
reduced_feet = reduce(lambda x,y: x+y, feet)
print(reduced_feet)


# In[175]:


ListComprehensionSum = sum([x for x in feet])
print(ListComprehensionSum)


# ## List Comprehensions with Conditionals

# In[195]:


ListComprehensionInt


# In[192]:


uneven = [x/2 for x in ListComprehensionInt if x % 2 == 0]


# In[193]:


uneven


# In[196]:


uneven_list = []

for x in ListComprehensionInt:
    if x % 2 == 0:
        x = x/2
        uneven_list.append(x)

print(uneven_list)


# ## List Comprehensions with Multipe If Conditionals

# In[199]:


newdevided = []

for x in range(10):
    if x % 2 == 0:
        if x % 6 == 0:
            newdevided.append(x)
            
print(newdevided)
        


# In[202]:


devided = [x for x in range(10) if x % 2 == 0 if x % 6 == 0]
print(devided)


# ## List Comprehensions with If-Else Conditions

# In[212]:


feet


# In[221]:


newlistfeet = []

for x in feet:
    if x >= 120000:
        x = x + 1 
    else:
        x= x + 5
        
    newlistfeet.append(x)
        

print(newlistfeet)



# In[223]:


ListComprehensionFeetIfElse = [x+1 if x > 120000 else x + 5 for x in feet]
ListComprehensionFeetIfElse


# ## Nested List Comprehensions
# 

# In[231]:


list_of_list = [[1,2,3],[4,5,6],[7,8]]

flattened_list_of_list = [y for x in list_of_list for y in x]


# In[232]:


list(flattened_list_of_list)


# In[234]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = [[row[i] for row in matrix] for i in range(3)]

print(matrix)
print(new_matrix)



# In[ ]:




