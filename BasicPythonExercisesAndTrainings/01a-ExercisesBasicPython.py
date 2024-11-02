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


# In[47]:


for x in range(3): #this for loop repeats this code 3 times
    for y in range(1,10):
        print(y, end="")
    print()


# In[48]:


rows = int(input('Enter the # of rows: '))
columns = int(input('Enter the # of columns: '))
symbol =  input("Enter a symbol to use: ")

for x in range(rows): #this for loop repeats this code 3 times
    for y in range(columns):
        print(symbol, end="")
    print()


# In[49]:


for x in range(5):
    for y in range(10):
        print(y, end ='')
    print()


# # While

# #### While loop - it executes a piece of code over and over again while a given condition still holds true

# In[50]:


number = 2

while number < 5:
    print('Thank you')
    number += 1 


# In[51]:


number = 0
while number < 5:
    print(f"The number is {number}")
    number += 1 


# In[52]:


number = 0

while number < 10:
    if number % 2 == 0:
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")
        
    number += 1
    


# In[53]:


number = 2

while number < 6:
    print(number)
    number += 1


# In[54]:


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


# In[55]:


number = 0

while number < 3:
    print("Thank you ")
    number += 1


# In[56]:


number = 1

while number < 10:
    while number % 2 ==0:
        print("The number "+str(number)+" is even")
        break 
    number += 1


# In[57]:


for number in range(3) : 
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    for another_number in range(3):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))
        break


# In[58]:


error = 50.0

while error > 1:
    error = error / 4
    print(error)


# In[59]:


offset = 8

while offset != 0:
    print("Correcting")
    offset -= 1
    print(offset)
    


# In[60]:


while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        break
    print("Invalid input. Please try again")


# In[61]:


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


# In[62]:


x = 0 

while x < 10:
    print(x)
    x += 1


# In[63]:


x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


# In[64]:


x = 0 

while True:
    if x == 5:
        break
    x += 1
    print(x)


# # range()

# In[65]:


range(10)


# In[66]:


for i in range(10):
    print(i)


# In[67]:


for i in range(5,10,2):
    print(i)


# In[68]:


for i in range(1,11):
    print(i)


# In[69]:


type(range(100))


# In[70]:


list(range(10))


# In[71]:


len(list(range(10)))


# In[72]:


for seq in range(-5,0):
    print(seq)


# In[73]:


for seq in range(50,1000,100):
    print(seq)


# In[74]:


for seq in range(100,10,-10):
    print(seq)


# In[75]:


list1 = [2,4,6,8,10,12,14,16,18,20]
counter = 0

for i in range(len(list1)):
    counter = counter + list1[i]
    print(counter)
print(f'Sum of the list : {counter}')

SumOfTheList = sum([x for x in list1])
print(f'List Comprehension SumOfTheList: {SumOfTheList}')


# In[76]:


from itertools import chain 

a1 = range(10,0, -2)
a2 = range(30,20,-2)
a3 = range(50,40,-2)
final = chain(a1, a2, a3)
print(final)
print(list(final))


# In[77]:


for a in final:
    print(a)


# In[78]:


a = list(range(0, 10, 3))
b = list(range(0, 11, 3))
c = list(range(0, 11, 2))
print(a == b)
print(a == c)


# # if elif else

# In[79]:


z = 4 

if z % 2 == 0:
    print('z is even')


# In[80]:


if z % 2 == 0:
    print('Checking ' + str(z))
    print('z is even')


# In[81]:


z = 5 
if z % 2 == 0: # False, no output
    print('Checking ' + str(z))
    print('z is even')
    


# In[82]:


z = 5 

if z % 2 == 0:
    print('z is even')
else:
    print('z is odd')


# In[83]:


z = 5

if z % 2 == 0:
    print('z is divisible by 2')
elif z % 3 == 0:
    print('z is divisible by 3')
else:
    print('z is neither divisible by 2 nor by 3')


# In[84]:


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

# In[85]:


x = [20, 30, 40, 50, 60]
y = []


# In[86]:


x


# In[87]:


for v in x:
    y += [v * 5]


# In[88]:


x


# In[89]:


y = map(lambda x: x * 5, x)
y


# In[90]:


list(y)


# In[91]:


columns


# In[92]:


columns = ['sepal_length', 'sepal_width','petal_length','petal_width']

for column in columns:
    iris[column] = iris[column].apply(lambda row: row + 2)


# In[93]:


iris


# In[94]:


add = lambda x,y: x + y
add(10,10)


# In[95]:


nums = [48, 6, 9, 21, 1]

square_all = map(lambda x: x **2, nums)
ListComprehension = [x ** 2 for x in nums]

print(square_all)
print(f'It is from map function {list(square_all)}, then it is from List Comprehension {ListComprehension}')





# In[96]:


def echo_world(words,echo):
    word = words * echo
    return word

echo_world('Lukasz',5)


# In[97]:


echo_worlds = lambda words, echo: words * echo 
echo_worlds('Lukasz', 5)


# In[98]:


add_1 = lambda x: x + 1
add_1(5)


# In[99]:


my_numbers = [1,2,3,4,5,6,7,8,9,10]

def square(x):
    return x ** 2

squares = list(map(square, my_numbers))

squares_lambda = list(map(lambda x: x**2, my_numbers))

squares_list_comprehesion = [x**2 for x  in my_numbers]

print(f'Result from function {squares}, result from lambda {squares_lambda}, result from list comprehension {squares_list_comprehesion}')


# In[100]:


evens = list(filter(lambda x: x % 2 == 0, my_numbers))
evensListComprehension = [x for x in my_numbers if x % 2 == 0]

print(f'Result from a filter {evens}, then result from a List Comprehension {evensListComprehension}')


# In[101]:


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda x: x[2])


# In[102]:


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

# In[103]:


numbers = range(10)

new_list = []

for n in numbers:
    if n % 2 == 0:
        new_list.append(n**2)

print(new_list)


# In[104]:


new_listcomprehension = [x**2 for x in numbers if x % 2 == 0]
print(new_listcomprehension)


# In[105]:


num = range(11)
new_list = []

for n in num:
    new_list.append(n*n)
    
print(new_list)


# In[106]:


ListCom = [x*x for x in range(11)]
print(ListCom)


# In[107]:


even = []

for n in range(50):
    is_even = n % 2 == 0
    if is_even:
        even.append(n)
        
print(even)


# In[108]:


# I want a (letter, num) pair of each letter in 'abcd' and each number in '0123' foe example a0, A1
new_list = []

for letter in 'abcd':
    for number in [0,1,2,3]:
        #print(letter, number)
        new_list.append((letter,number))
print(new_list)


# In[109]:


my_new_list = [(a,b) for a in 'abcd' for b in range(4)]
print(my_new_list)


# ## Instead of map() & filter() & reduce() &  lambda(), using List Comprehension

# In[110]:


kilometer = [39.2, 36.5, 37.3, 37.8]

feet = map(lambda x: float(3280.8399)*x, kilometer)
listfeet = list(feet)
print(listfeet)


# In[111]:


newfeetListComprehension = [x*float(3280.8399) for x in kilometer]
print(newfeetListComprehension)


# In[112]:


feet = list(map(int,listfeet))
print(feet)


# In[113]:


uneven = filter(lambda x: x%2, feet)
print(list(uneven))


# In[114]:


nums = range(0,11)
my_list = filter(lambda x: x % 2 == 0, nums)
print(list(my_list))


# In[115]:


ListComprehensionInt = [int(x) for x in newfeetListComprehension]
print(ListComprehensionInt)


# In[116]:


ListComprehensionEvenTrue = [x % 2 for x in ListComprehensionInt]
print(ListComprehensionEvenTrue)
ListComprehensionEven = [x for x in ListComprehensionInt if x % 2 != 0]
print(ListComprehensionEven)


# In[117]:


from functools import reduce
reduced_feet = reduce(lambda x,y: x+y, feet)
print(reduced_feet)


# In[118]:


ListComprehensionSum = sum([x for x in feet])
print(ListComprehensionSum)


# ## List Comprehensions with Conditionals

# In[119]:


ListComprehensionInt


# In[120]:


uneven = [x/2 for x in ListComprehensionInt if x % 2 == 0]


# In[121]:


uneven


# In[122]:


uneven_list = []

for x in ListComprehensionInt:
    if x % 2 == 0:
        x = x/2
        uneven_list.append(x)

print(uneven_list)


# ## List Comprehensions with Multipe If Conditionals

# In[123]:


newdevided = []

for x in range(10):
    if x % 2 == 0:
        if x % 6 == 0:
            newdevided.append(x)
            
print(newdevided)
        


# In[124]:


devided = [x for x in range(10) if x % 2 == 0 if x % 6 == 0]
print(devided)


# ## List Comprehensions with If-Else Conditions

# In[125]:


feet


# In[126]:


newlistfeet = []

for x in feet:
    if x >= 120000:
        x = x + 1 
    else:
        x= x + 5
        
    newlistfeet.append(x)
        

print(newlistfeet)



# In[127]:


ListComprehensionFeetIfElse = [x+1 if x > 120000 else x + 5 for x in feet]
ListComprehensionFeetIfElse


# ## Nested List Comprehensions
# 

# In[128]:


list_of_list = [[1,2,3],[4,5,6],[7,8]]

flattened_list_of_list = [y for x in list_of_list for y in x]


# In[129]:


list(flattened_list_of_list)


# In[130]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = [[row[i] for row in matrix] for i in range(3)]

print(matrix)
print(new_matrix)



# ## Formatted String Literals or f-Strings

# In[131]:


year = 2024
name = 'Lukasz Dlugozima'
f'I am {name} was born {year}'


# In[132]:


a = 0.321321123
f"{a:.2%}"


# In[133]:


custom_string = 'String formatting'
print(f"{custom_string} is a powerful technique")


# In[134]:


animals = 'eels'
print(f'My hovercraft is full of {animals}.')


# ## .format() method

# In[135]:


value = ' a'
'text{}'.format(value)


# ### Positional formatting

# In[136]:


print("Machine learning provides {} the ability to learn {}".format("systems", "automatically"))


# In[137]:


my_string = "{} rely on {} datasets"
method = 'Supervised algorithms'
condition = 'labeled'

print(my_string.format(method, condition))


# ### Reordering values

# In[138]:


print('{} has a friend called {} and a sister called {}.'.format("Betty","Linda","Daisy"))


# In[139]:


print('{2} has a friend called {1} and a sister called {0}.'.format("Betty","Linda","Daisy"))


# ### Name Placeholders

# In[140]:


tool = 'Unsupervised algorithms'
goal = 'patterns'
print("{title} try to find {aim} in the dataset".format(title=tool, aim=goal))


# In[141]:


my_methods = {"tool":"Unsupervised algorithms", "goal":"patterns"}


# In[142]:


print("{data[tool]} try to find {data[goal]} in the dataset".format(data=my_methods))


# ### Format Specifier

# In[143]:


print('Only {0:f}% of the {1} produced worldwide is {2}'.format(0.51555675, "data", "analyzed"))


# In[144]:


print('Only {0:.2f}% of the {1} produced worldwide is {2}'.format(0.51555675, "data", "analyzed"))


# In[145]:


from datetime import datetime
print(datetime.now())


# In[146]:


print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now()))


# ### % operator

# In[147]:


name = 'Pete'

'Hello %s' %name


# In[148]:


number = 10

'I have %d years' %number


# In[149]:


a = 'We are'


'%s' %a


# ## print()

# In[150]:


print('Hello World')
type(print)


# In[151]:


print("Hello world!")
print()
print("Hello,world!")


# In[152]:


print('datacamp','tutorial','on','python','print','function')


# In[153]:


print('datacamp','tutorial','on','python','print','function', sep='\n')


# In[154]:


print('datacamp','tutorial','on','python','print','function', sep=',')
print('datacamp','tutorial','on','python','print','function', sep='/n/n')
print('datacamp','tutorial','on','python','print','function', sep=',+')


# In[155]:


int_list = [1,2,3,4,5,6]
print(int_list)


# In[156]:


str1 = 'datacamp tutorial on'
str2 = 'python print function'
print(str1)
print(str2)
print(str1, end = ' ')
print(str2)


# In[157]:


def value(items):
    for item in items:
        print(item, end=' ')


# In[158]:


value([1,2,3,4,5])


# In[159]:


file = open('print.txt', 'a+')


# In[160]:


def value(items):
    for item in items:
        print(item, file=file)
    file.close()


# In[161]:


value([1,2,3,4,5,6,7,8,9,10])


# In[162]:


a = 10
b = 'Datacamp'

print('We have only ',a,'PLN','for ',b)


# In[163]:


a = 10
b = 'Lukasz Dlugozima'
c ='the best'

print('%s is %s. He has %d years'%(b,c,10))


# In[164]:


print('{} is the best on the world'.format('Lukasz'))
a = 'Lukasz'
print('{} is the best on the world'.format(a))
name = 'Lukasz'
print(f'{name} is the best on the world')
a = 'Lukasz'
print('%s is the best on the world'%(a))


# # apply() method

# In[165]:


import pandas as pd
import numpy as np
from IPython.display import display

students = pd.Series(data=[180, 175, 168, 190],
                     index=['Vik', 'Mehdi', 'Bella', 'Chriss'])
display(students)
print(type(students))


# In[166]:


def cm_to_feet(h):
    return np.round(h/30.48,2)

print(students.apply(cm_to_feet))


# In[167]:


data = pd.DataFrame({'EmployeeName': ['Callen Dunkley', 'Sarah Rayner', 'Jeanette Sloan', 'Kaycee Acosta', 'Henri Conroy', 'Emma Peralta', 'Martin Butt', 'Alex Jensen', 'Kim Howarth', 'Jane Burnett'],
                    'Department': ['Accounting', 'Engineering', 'Engineering', 'HR', 'HR', 'HR', 'Data Science', 'Data Science', 'Accounting', 'Data Science'],
                    'HireDate': [2010, 2018, 2012, 2014, 2014, 2018, 2020, 2018, 2020, 2012],
                    'Sex': ['M', 'F', 'F', 'F', 'M', 'F', 'M', 'M', 'M', 'F'],
                    'Birthdate': ['04/09/1982', '14/04/1981', '06/05/1997', '08/01/1986', '10/10/1988', '12/11/1992', '10/04/1991', '16/07/1995', '08/10/1992', '11/10/1979'],
                    'Weight': [78, 80, 66, 67, 90, 57, 115, 87, 95, 57],
                    'Height': [176, 160, 169, 157, 185, 164, 195, 180, 174, 165],
                    'Kids': [2, 1, 0, 1, 1, 0, 2, 0, 3, 1]
                    })
display(data)


# In[168]:


x = 'Lukasz Adamski'

print(x.split()[0])
print(x.split()[1])


# In[169]:


data['FirstName'] = data['EmployeeName'].apply(lambda x: x.split()[0])
data['LastName'] = data['EmployeeName'].apply(lambda x: x.split()[1])


# In[170]:


display(data)


# In[171]:


from datetime import datetime, date

def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate,'%d/%m/%Y')
    today = date.today()
    return today.year - birthdate.year 


# In[172]:


data['Age'] = data['Birthdate'].apply(calculate_age)
display(data)


# In[173]:


print(data['Age'].mean())


# In[174]:


def calc_bmi(weight, height):
    return np.round(weight/(height/100)**2, 2)


# In[175]:


calc_bmi(90,190)


# In[176]:


data['BMI'] = data.apply(lambda x: calc_bmi(x['Weight'], x['Height']), axis=1)


# In[177]:


display(data)


# In[178]:


date.today().year


# In[179]:


mask = data['HireDate'].apply(lambda x: date.today().year - x >= 10)
print(mask)


# In[180]:


data[data.apply(lambda x: True if x['Sex'] == 'F' and x['Kids'] > 0 else False, axis=1)]


# In[181]:


data


# # Generator Expressions

# ### It returns new generator objects,
# ### Generator is iterable it does not store values, 
# ### but it generates values when you loop over.

# In[182]:


numbers = [2,1,3,4,7,11,8]
squares = (n**2 for n in numbers) # Generator Expression
squares


# In[183]:


next(squares)


# In[184]:


next(squares)


# In[185]:


next(squares)


# In[186]:


for n in squares:
    print(n)


# In[187]:


numbers = [2,1,3,4,7,11,8]
numbers[3] = 5
squares = (n**2 for n in numbers)
squares


# In[188]:


for n in squares:
    print(n)


# In[189]:


list(squares)


# In[190]:


numbers = [2,1,3,4,7,11,8]
squares = (n**2 for n in numbers)
squares


# In[191]:


for n in squares:
    print(n)
    if n > 10:
        break


# In[192]:


list(squares)


# In[193]:


result = (num for num in range(6))
print(list(result))


# In[194]:


even_numbs = (num for num in range(10) if num % 2 == 0)


# In[195]:


print(list(even_numbs))


# ### Generator Functions

# In[196]:


def num_sequence(n):
    i = 0
    while i < n:
        yield i #instead of return
        i += 1


# In[197]:


result = num_sequence(6)
print(type(result))

for item in result:
    print(item)


# In[198]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[199]:


def gen_func(n):
    for n in nums:
        yield n * n
        
gen_exp = gen_func(nums)



# In[200]:


for i in gen_exp:
    print(i)


# In[201]:


sum_of_squares = sum(x**2 for x in range(1000000))


# In[202]:


print(sum_of_squares)


# # Dictionary

# In[203]:


a = {'apple':'fruit','beetroot':'vegetable','cake':'dessert'}


# In[204]:


a


# In[205]:


a['doughnut'] = 'snack'


# In[206]:


a


# In[207]:


a = {'one': 1, 'two':'to', 'three': 3.0, 'four':[4,4.0]}
print(a)


# In[208]:


del a['one']


# In[209]:


a


# In[210]:


a.clear()
print(a)


# In[211]:


sweet_dict ={'a1':'cake', 'a2':'cookie', 'a1':'icecream'}
print(sweet_dict['a1'])


# In[212]:


for k, v in sweet_dict.items():
    print(k, v)


# In[213]:


for i, v in enumerate(sweet_dict):
    print(i, v)


# In[214]:


print(sweet_dict.items())
print(sweet_dict.keys())
print(sweet_dict.values())


# In[215]:


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q,a))


# # Dictionary Comprehension

# In[216]:


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dict1.keys())
print(dict1.values())
print(dict1.items())


# In[217]:


dict_variable = {key:value for (key,value) in dict1.items()}


# In[218]:


dict_variable


# In[219]:


dict1 = {'a':1, 'b':2, 'c':3, 'd':4,'e':5}
print(dict1)
dictDictionaryComprehensionV = {k:v*2 for (k,v) in dict1.items()}
print(dictDictionaryComprehensionV)
dictDictionaryComprehensionK = {k*2:v for (k,v) in dict1.items()}
print(dictDictionaryComprehensionK)


# In[220]:


numbers = range(10)
new_dict_for = {}

for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n**2

print(new_dict_for)


# In[221]:


new_dict_for2 = {n:n**2 for n in numbers if n % 2 ==0}
print(new_dict_for2)


# In[222]:


fahrenheit = {'t1':-30, 't2':-20,'t3':-10,'t4':0}
fahrenheit


# In[223]:


fahrenheit
new_celcius = list(map(lambda x:(float(5)/9)*(x-32) , fahrenheit.values()))
dictfahrenheit = dict(zip(fahrenheit.keys(), new_celcius))
print(dictfahrenheit)


# In[224]:


fahrenheit
dictfahrenheit = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(dictfahrenheit)


# In[225]:


fahrenheit


# In[226]:


names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpole']

print(dict(zip(names, heros)))


# In[227]:


# I want a dict{'name':'hero'} for each name, hero in zip(names, heros)
my_dict = {}

for name, hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)


# In[228]:


DictComp = {k:v for k,v in zip(names,heros)}
print(DictComp)


# In[229]:


DictComp = {k:v for k,v in zip(names,heros) if k != 'Peter'}
print(DictComp)


# ### Adding Conditionals to Dictionary Comprehension
# #### If conditions & Multpie If Conditions

# In[230]:


dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,'f':6}
print(dict1)
dict1Conditional = {k:v for (k,v) in dict1.items() if v > 2}
print(dict1Conditional)


# In[231]:


dict2Conditional = {k:v for (k,v) in dict1.items() if v > 2 if v % 2 ==0}
print(dict2Conditional)


# In[232]:


dict3Conditional = {k:v for (k,v) in dict1.items() if v > 2 if v % 2 == 0 if v % 3 == 0}
print(dict3Conditional)


# In[233]:


dict4Conditional = {}


for k,v in dict1.items():
    if (v > 2 and v % 2 == 0 and v % 3 == 0):
        dict4Conditional[k]=v
print(dict4Conditional)


# #### If-Else Conditions

# In[234]:


print(dict1)

ifelsedict ={k:('even' if v % 2 == 0 else 'odd') for (k,v) in dict1.items()}

print(ifelsedict)


# # List of Dictionary

# In[235]:


data = [{7058:'sravan', 7079: 'jyothika',
         7072:'harsha', 7075:'deepika'}]

print(data)
print(len(data))
print(type(data))


# In[236]:


print(data[0][7058])
print(data[0][7075])


# In[237]:


data = [{7058: 'sravan', 7059: 'jyothika', 
         7072: 'harsha', 7075: 'deepika'},
         
        {7051: 'fathima', 7089: 'mounika', 
         7012: 'thanmai', 7115: 'vasavi'},
         
        {9001: 'ojaswi', 1289: 'daksha', 
         7045: 'parvathi', 9815: 'bhavani'}]
 
print(data)


# In[238]:


print(data[0][7058])
print(data[1][7051])
print(data[2][9001])


# ## Append a Dictionary to Python List of Dictionary
# 

# In[239]:


data = [{1: 'Geeks', 2:'GeeksforGeeks'}]
print(data)


# In[240]:


new_data = [{1: 'Python', 2:'Programming'}]

data.append(new_data)
print(data)


# In[241]:


data = [{1: 'Geeks', 2:'GeeksforGeeks'}, {1: 'Python', 2:'Programming'},{'A':'B'}]
print(data)


# In[242]:


data[0][3] = "World"
data[0][2] = "Hello"


# In[243]:


data


# In[244]:


data[1][1] = 'SQL'


# In[245]:


data


# In[246]:


data[2]['A']


# In[247]:


data[2]['A'] = 'C'


# In[248]:


data


# # Set Comprehensions

# In[249]:


nums = [1,1,2, 2, 3,4,5,5,6,7,8,10,4,4,4, 4, 5, 6, 7, 8, 9, 10]

my_set = set()

for n in nums:
    my_set.add(n)
    
print(my_set)


# In[250]:


SetComprehensions = {x for x in nums}
print(SetComprehensions)


# # Python List Functions & Methods

# In[251]:


prices = [238.11,237.81, 289.91]
prices.sort()
print(prices)


# In[252]:


fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
fam2 = [["liz", 1.73],
        ["emma", 1.68],
        ["mom", 1.71],
        ["dad", 1.89]]


# In[253]:


type(fam)


# In[254]:


type(fam2)


# In[255]:


months = ['January','February','March']
months.append('April')
print(months)


# In[256]:


x = [1, 2, 3]
x.extend([4,5])
x


# In[257]:


months = ['January', 'February', 'March']
prices = [238.11, 237.81, 238.91]


# In[258]:


months.index('February')


# In[259]:


prices[1]


# In[260]:


prices = [159.54, 37.13, 71.17] 
prices_max = max(prices)
print(prices_max)


# In[261]:


months = ['January', 'February', 'March']
prices = [238.11, 237.81, 238.91]


# In[262]:


min_prices = min(prices)


# In[263]:


index_prices = prices.index(min_prices)
index_prices


# In[264]:


print(months[index_prices])


# In[265]:


stock_price_1 = [50.23]
stock_price_2 = [75.14, 85.64, 11.28]

print('stock_price_1 length is {}'.format(len(stock_price_1)))
print('stock_price_2 length is {}'.format(len(stock_price_2)))


# In[266]:


print(list())

stocks = ('238.11', '237.81', '238.91')
print(list(stocks))


# In[267]:


def filter_price(price):
    if(price > 350):
        return True
    else:
        return False 
    
item_price = [230, 400, 450, 350, 370] 

filtered_price = filter(filter_price,item_price)


# In[268]:


print(list(filtered_price))


# In[269]:


LambdaFilter = list(filter(lambda x: x > 350, item_price))
print(LambdaFilter)


# # count() & counter()

# In[270]:


list = [1,2,3,4,5,5,5,5,1,1]


# In[271]:


print(list.count(1))
print(list.count(5))


# In[272]:


from collections import Counter
x = Counter(list)
print(x)


# # mutable & immutable types

# In[273]:


print('Mutable types in Python are: {}, {}, {}'.format('list','set','dict'))
print('Immutable types in Python are: {}, {}, {}, {}, {}, {}'.format('str','int','float','bool','bytes','tuple'))


# In[274]:


x= (1,2)

# x[0] = 1 # TypeError: 'tuple' object does not support item assignment
x


# In[275]:


y = x # we add assignment that we create a real copy of immutable object
x = (1, 2, 3) # reassign a new value to x 
print(x, y)


# In[276]:


x = [1, 2]
y = x 
x[0] = 100
print(x, y)


# # local()

# In[277]:


def demo1():
    print("Here no local variable  is present : ", locals())

# here local variables are present
def demo2():
    name = "Ankit"
    name2 = "Lukasz"
    print("Here local variables are present : ", locals())

# driver code
demo1()
demo2()


# In[278]:


phones = ['Apple', 'Samsung', 'Oneplus']
phones_iter = iter(phones)

print(next(phones_iter))
print(next(phones_iter))
print(next(phones_iter))

