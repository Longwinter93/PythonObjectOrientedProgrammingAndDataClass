#!/usr/bin/env python
# coding: utf-8

# # 101 Exercises for Python Fundamentals

# ## Orientation
# - Each *assert* line is both an example and a test that tests for the presence and functionality of the instructed exercise.
# 
# 
# ## Outline
# - Each cell starts with a problem statement that describes the exercise to complete.
# - Underneath each problem statement, learners will need to write code to produce an answer.
# - The **assert** lines test to see that your code solves the problem appropriately.
# - Do not alter or delete the assertion tests, since those are providing automated testing.
# - Many exercises will rely on previous solutions to be correctly completed
# - The `print("Exercise is complete")` line will only run if your solution passes the assertion test(s)
# - Be sure to create programmatic solutions that will work for all inputs:
# - For example, calling the `is_even(2)` returns `True`, but your function should work for all even numbers, both positive and negative.

# In[1]:


# Example problem:
# Uncomment the line below and run this cell.
# The hashtag "#" character in a line of Python code is the comment character.
doing_python_right_now = True

# The lines below will test your answer. If you see an error, then it means that your answer is incorrect or incomplete.
assert doing_python_right_now == True
print("Exercise 0 is correct") # This line will print if your solution passes the assertion above.


# In[2]:


# Exercise 1
# On the line below, create a variable named on_mars_right_now and assign it the boolean value of False
on_mars_right_now = False

assert on_mars_right_now == False
print("Exercise 1 is correct.")


# In[3]:


# Exercise 2
# Create a variable named fruits and assign it a list of fruits containing the following fruit names as strings:
# mango, banana, guava, kiwi, and strawberry.
fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]


assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry"]
print("Exercise 2 is correct.")


# In[4]:


# Exercise 3
# Create a variable named vegetables and assign it a list of fruits containing the following vegetable names as strings:
# eggplant, broccoli, carrot, cauliflower, and zucchini

vegetables = ['eggplant', 'broccoli', 'carrot', 'cauliflower', 'zucchini']

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"]
print("Exercise 3 is correct.")


# In[5]:


# Exercise 4
# Create a variable named numbers and assign it a list of numbers, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

numbers = [1,2,3,4,5,6,7,8,9,10]


assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Exercise 4 is correct.")


# ## List Operations
# **Hint** Recommend finding and using built-in Python functionality whenever possible.

# In[6]:


# Exercise 5
# Given the following assigment of the list of fruits, add "tomato" to the end of the list.
fruits = ["mango", "banana", "guava", "kiwi", "strawberry"]
fruits.append("tomato")
assert fruits == ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]
print("Exercise 5 is correct")


# In[7]:


# Exercise 6
# Given the following assignment of the vegetables list, add "tomato" to the end of the list.
vegetables = ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini"]
vegetables.append("tomato")

assert vegetables == ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini", "tomato"], "Ensure the variable contains all the strings in the provided order"
print("Exercise 6 is correct")


# In[8]:


# Exercise 7
# Given the list of numbers defined below, reverse the list of numbers that you created above.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()

assert numbers == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
print("Exercise 7 is correct.")


# In[9]:


# Exercise 8
# Sort the vegetables in alphabetical order
vegetables.sort()
assert vegetables == ['broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 8 is correct.")


# In[10]:


# Exercise 9
# Write the code necessary to sort the fruits in reverse alphabetical order
#fruits == ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]
fruits.sort(reverse = True)
assert fruits == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana']
print("Exercise 9 is correct.")


# In[11]:


# Exercise 10
# Write the code necessary to produce a single list that holds all fruits then all vegetables in the order as they were sorted above.
fruits.extend(vegetables)
fruits_and_veggies = fruits
assert fruits_and_veggies == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana', 'broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 10 is correct")


# ## Basic Functions
# ![](http://)**Hint** Be sure to `return` values from your function definitions. The assert statements will call your function(s) for you.

# In[12]:


# Run this cell in order to generate some numbers to use in our functions after this.
import random

positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)
print("We now have some random numbers available for future exercises.")
print("The random positive even number is", positive_even_number)
print("The random positive odd nubmer is", positive_odd_number)
print("The random negative even number", negative_even_number)
print("The random negative odd number", negative_odd_number)


# In[13]:


# Example function defintion:
# Write a say_hello function that adds the string "Hello, " to the beginning and "!" to the end of any given input.
def say_hello(name):
    return "Hello, " + name + "!"

assert say_hello("Jane") == "Hello, Jane!", "Double check the inputs and data types"
assert say_hello("Pat") == "Hello, Pat!", "Double check the inputs and data types"
assert say_hello("Astrud") == "Hello, Astrud!", "Double check the inputs and data types"
print("The example function definition ran appropriately")


# In[14]:


# Another example function definition:
# This plus_two function takes in a variable and adds 2 to it.
def plus_two(number):
    return number + 2

assert plus_two(3) == 5
assert plus_two(0) == 2
assert plus_two(-2) == 0
print("The plus_two assertions executed appropriately... The second function definition example executed appropriately.")


# In[15]:


# Exercise 11
# Write a function definition for a function named add_one that takes in a number and returns that number plus one.
def add_one(number):
    return number + 1

assert add_one(2) == 3, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(0) == 1, "Zero plus one is one."
assert add_one(positive_even_number) == positive_even_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(negative_odd_number) == negative_odd_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 11 is correct.")


# In[16]:


a = -1
if a > 0:
    print(True)
else:
    print(False)



# In[17]:


# Exercise 12
# Write a function definition named is_positive that takes in a number and returns True or False if that number is positive.
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
                         
assert is_positive(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(0) == False, "Zero is not a positive number."
print("Exercise 12 is correct.")


# In[18]:


# Exercise 13
# Write a function definition named is_negative that takes in a number and returns True or False if that number is negative.
def is_negative(number):
    if number < 0:
        return True 
    else:   
        return False 
    
assert is_negative(positive_odd_number) == False 
assert is_negative(positive_even_number) == False 
assert is_negative(negative_odd_number) == True
assert is_negative(negative_even_number) == True
assert is_negative(0) == False 
print("Exercise 13 is correct.")


# In[19]:


a = [2, 4, 5]

a = [num for num in a if num % 2 != 0]
print(a)


# In[20]:


# Exercise 14
# Write a function definition named is_odd that takes in a number and returns True or False if that number is odd.
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False




assert is_odd(positive_odd_number) == True 
assert is_odd(positive_even_number) == False 
assert is_odd(negative_odd_number) == True 
assert is_odd(negative_even_number) == False 
print("Exercise 14 is correct.")


# In[21]:


# Exercise 15
# Write a function definition named is_even that takes in a number and returns True or False if that number is even.

def is_even(number):
    result = True if number % 2 == 0 else False
    return result


assert is_even(2) == True 
assert is_even(positive_odd_number) == False 
assert is_even(positive_even_number) == True 
assert is_even(negative_odd_number) == False 
assert is_even(negative_even_number) == True 
print("Exercise 15 is correct.")


# In[22]:


# Exercise 16
# Write a function definition named identity that takes in any argument and returns that argument's value. Don't overthink this one!

def identity(argument):
    return argument

assert identity(fruits) == fruits
assert identity(vegetables) == vegetables 
assert identity(positive_odd_number) == positive_odd_number 
assert identity(positive_even_number) == positive_even_number
assert identity(negative_odd_number) == negative_odd_number
assert identity(negative_even_number) == negative_even_number
print("Exercise 16 is correct.")


# In[23]:


# Exercise 17
# Write a function definition named is_positive_odd that takes in a number and returns True or False if the value is both greater than zero and odd
def is_positive_odd(number):
    if number % 2 != 0 and number > 0:
        return True 
    else:
        return False


#def is_positive_odd(number):
    #result = True if number % 2 != 0 and number > 0 else False 
    #return result


assert is_positive_odd(3) == True, "Double check your syntax and logic"
assert is_positive_odd(positive_odd_number) == True, "Double check your syntax and logic"
assert is_positive_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 17 is correct.")


# In[24]:


# Exercise 18
# Write a function definition named is_positive_even that takes in a number and returns True or False if the value is both greater than zero and even
def is_positive_even(number):
    result = True if number % 2 == 0 and number > 0 else False 
    return result


assert is_positive_even(4) == True, "Double check your syntax and logic"
assert is_positive_even(positive_odd_number) == False, "Double check your syntax and logic"
assert is_positive_even(positive_even_number) == True, "Double check your syntax and logic"
assert is_positive_even(negative_odd_number) == False, "Double check your syntax and logic"
assert is_positive_even(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 18 is correct.")


# In[25]:


# Exercise 19
# Write a function definition named is_negative_odd that takes in a number and returns True or False if the value is both less than zero and odd.

def is_negative_odd(number):
    result = True if number % 2 != 0 and number < 0 else False
    return result

assert is_negative_odd(-3) == True, "Double check your syntax and logic"
assert is_negative_odd(positive_odd_number) == False, "Double check your syntax and logic"
assert is_negative_odd(positive_even_number) == False, "Double check your syntax and logic"
assert is_negative_odd(negative_odd_number) == True, "Double check your syntax and logic"
assert is_negative_odd(negative_even_number) == False, "Double check your syntax and logic"
print("Exercise 19 is correct.")


# In[26]:


# Exercise 20
# Write a function definition named is_negative_even that takes in a number and returns True or False if the value is both less than zero and even.

def is_negative_even(number):
    if number % 2 == 0 and number < 0:
        return True 
    else:
        return False

assert is_negative_even(-4) == True, "Double check your syntax and logic"
assert is_negative_even(positive_odd_number) == False, "Double check your syntax and logic"
assert is_negative_even(positive_even_number) == False, "Double check your syntax and logic"
assert is_negative_even(negative_odd_number) == False, "Double check your syntax and logic"
assert is_negative_even(negative_even_number) == True, "Double check your syntax and logic"
print("Exercise 20 is correct.")


# In[27]:


# Exercise 21
# Write a function definition named half that takes in a number and returns half the provided number.
def half(number):
    return number / 2


assert half(4) == 2
assert half(5) == 2.5
assert half(positive_odd_number) == positive_odd_number / 2
assert half(positive_even_number) == positive_even_number / 2
assert half(negative_odd_number) == negative_odd_number / 2
assert half(negative_even_number) == negative_even_number / 2
print("Exercise 21 is correct.")


# In[28]:


# Exercise 22
# Write a function definition named double that takes in a number and returns double the provided number.

def double(number):
    return number * 2


assert double(4) == 8
assert double(5) == 10
assert double(positive_odd_number) == positive_odd_number * 2
assert double(positive_even_number) == positive_even_number * 2
assert double(negative_odd_number) == negative_odd_number * 2
assert double(negative_even_number) == negative_even_number * 2
print("Exercise 22 is correct.")


# In[29]:


# Exercise 23
# Write a function definition named triple that takes in a number and returns triple the provided number.

def triple(number):
    return number * 3

assert triple(4) == 12
assert triple(5) == 15
assert triple(positive_odd_number) == positive_odd_number * 3
assert triple(positive_even_number) == positive_even_number * 3
assert triple(negative_odd_number) == negative_odd_number * 3
assert triple(negative_even_number) == negative_even_number * 3
print("Exercise 23 is correct.")


# In[30]:


# Exercise 24
# Write a function definition named reverse_sign that takes in a number and returns the provided number but with the sign reversed.

def reverse_sign(number):
    return number * (-1)

assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5
assert reverse_sign(positive_odd_number) == positive_odd_number * -1
assert reverse_sign(positive_even_number) == positive_even_number * -1
assert reverse_sign(negative_odd_number) == negative_odd_number * -1
assert reverse_sign(negative_even_number) == negative_even_number * -1
print("Exercise 24 is correct.")


# In[31]:


# Exercise 25
# Write a function definition named absolute_value that takes in a number and returns the absolute value of the provided number
def absolute_value(number):
    return abs(number)

assert absolute_value(4) == 4
assert absolute_value(-5) == 5
assert absolute_value(positive_odd_number) == positive_odd_number
assert absolute_value(positive_even_number) == positive_even_number
assert absolute_value(negative_odd_number) == negative_odd_number * -1
assert absolute_value(negative_even_number) == negative_even_number * -1
print("Exercise 25 is correct.")


# In[32]:


# Exercise 26
# Write a function definition named is_multiple_of_three that takes in a number and returns True or False if the number is evenly divisible by 3.

def is_multiple_of_three(number):
    if number % 3 == 0:
        return True
    else:
        return False


assert is_multiple_of_three(3) == True
assert is_multiple_of_three(15) == True
assert is_multiple_of_three(9) == True
assert is_multiple_of_three(4) == False
assert is_multiple_of_three(10) == False
print("Exercise 26 is correct.")


# In[33]:


# Exercise 27
# Write a function definition named is_multiple_of_five that takes in a number and returns True or False if the number is evenly divisible by 5.

def is_multiple_of_five(number):
    result = True if number % 5 == 0 else False 
    return result


assert is_multiple_of_five(3) == False
assert is_multiple_of_five(15) == True
assert is_multiple_of_five(9) == False
assert is_multiple_of_five(4) == False
assert is_multiple_of_five(10) == True
print("Exercise 27 is correct.")


# In[34]:


# Exercise 28
# Write a function definition named is_multiple_of_both_three_and_five that takes in a number and returns True or False if the number is evenly divisible by both 3 and 5.
def is_multiple_of_both_three_and_five(number):
    if number % 3 == 0 and number % 5 == 0:
        return True 
    else:
        return False


assert is_multiple_of_both_three_and_five(15) == True
assert is_multiple_of_both_three_and_five(45) == True
assert is_multiple_of_both_three_and_five(3) == False
assert is_multiple_of_both_three_and_five(9) == False
assert is_multiple_of_both_three_and_five(4) == False
print("Exercise 28 is correct.")


# In[35]:


# Exercise 29
# Write a function definition named square that takes in a number and returns the number times itself.

def square(number):
    return number ** 2


assert square(3) == 9
assert square(2) == 4
assert square(9) == 81
assert square(positive_odd_number) == positive_odd_number * positive_odd_number
print("Exercise 29 is correct.")


# In[36]:


# Exercise 30
# Write a function definition named add that takes in two numbers and returns the sum.
def add(first, second):
    return first + second


assert add(3, 2) == 5
assert add(10, -2) == 8
assert add(5, 7) == 12
print("Exercise 30 is correct.")


# In[37]:


# Exercise 31
# Write a function definition named cube that takes in a number and returns the number times itself, times itself.

def cube(number):
    return number ** 3

assert cube(3) == 27
assert cube(2) == 8
assert cube(5) == 125
assert cube(positive_odd_number) == positive_odd_number * positive_odd_number * positive_odd_number
print("Exercise 31 is correct.")


# In[38]:


# Exercise 32
# Write a function definition named square_root that takes in a number and returns the square root of the provided number

def square_root(number):
    return number ** 0.5


assert square_root(4) == 2.0
assert square_root(64) == 8.0
assert square_root(81) == 9.0
print("Exercise 32 is correct.")


# In[39]:


# Exercise 33
# Write a function definition named subtract that takes in two numbers and returns the first minus the second argument.

def subtract(a, b):
    return a - b

assert subtract(8, 6) == 2
assert subtract(27, 4) == 23
assert subtract(12, 2) == 10
print("Exercise 33 is correct.")


# In[40]:


# Exercise 34
# Write a function definition named multiply that takes in two numbers and returns the first times the second argument.

def multiply(a, b):
    return a * b

assert multiply(2, 1) == 2
assert multiply(3, 5) == 15
assert multiply(5, 2) == 10
print("Exercise 34 is correct.")


# In[41]:


# Exercise 35
# Write a function definition named divide that takes in two numbers and returns the first argument divided by the second argument.
def divide(a, b):
    return a / b 


assert divide(27, 9) == 3
assert divide(15, 3) == 5
assert divide(5, 2) == 2.5
assert divide(10, 2) == 5
print("Exercise 35 is correct.")


# In[42]:


# Exercise 36
# Write a function definition named quotient that takes in two numbers and returns only the quotient from dividing the first argument by the second argument.

def quotient(a,b):
    return a // b

assert quotient(27, 9) == 3
assert quotient(5, 2) == 2
assert quotient(10, 3) == 3
print("Exercise 36 is correct.")


# In[43]:


# Exercise 37
# Write a function definition named remainder that takes in two numbers and returns the remainder of first argument divided by the second argument.

def remainder(a,b):
    return a % b

assert remainder(3, 3) == 0
assert remainder(5, 2) == 1
assert remainder(7, 5) == 2
print("Exercise 37 is correct.")


# In[44]:


# Exercise 38
# Write a function definition named sum_of_squares that takes in two numbers, squares each number, then returns the sum of both squares.

def sum_of_squares(a,b):
    return (a**2 + b**2)

assert sum_of_squares(3, 2) == 13
assert sum_of_squares(5, 2) == 29
assert sum_of_squares(2, 4) == 20
print("Exercise 38 is correct.")


# In[45]:


# Exercise 39
# Write a function definition named times_two_plus_three that takes in a number, multiplies it by two, adds 3 and returns the result.

def times_two_plus_three(number):
    return (number * 2) + 3


assert times_two_plus_three(0) == 3
assert times_two_plus_three(1) == 5
assert times_two_plus_three(2) == 7
assert times_two_plus_three(3) == 9
assert times_two_plus_three(5) == 13
print("Exercise 39 is correct.")


# In[46]:


# Exercise 40
# Write a function definition named area_of_rectangle that takes in two numbers and returns the product.

def area_of_rectangle(a, b):
    return a * b

assert area_of_rectangle(1, 3) == 3
assert area_of_rectangle(5, 2) == 10
assert area_of_rectangle(2, 7) == 14
assert area_of_rectangle(5.3, 10.3) == 54.59
print("Exercise 40 is correct.")


# In[47]:


import math
# Exercise 41
# Write a function definition named area_of_circle that takes in a number representing a circle's radius and returns the area of the circl
def area_of_circle(a):
    return math.pi  * a**2


assert area_of_circle(3) == 28.274333882308138
assert area_of_circle(5) == 78.53981633974483
assert area_of_circle(7) == 153.93804002589985
print("Exercise 41 is correct.")


# In[48]:


import math
# Exercise 42
# Write a function definition named circumference that takes in a number representing a circle's radius and returns the circumference.
def circumference(a):
    return 2 * math.pi * a


assert circumference(3) == 18.84955592153876
assert circumference(5) == 31.41592653589793
assert circumference(7) == 43.982297150257104
print("Exercise 42 is correct.")


# ## Functions working with strings
# If you need some guidance working with the next few problems, recommend reading through [this example code](https://gist.github.com/ryanorsinger/f758599c886549e7615ec43488ae514c)

# In[49]:


# Exercise 43
# Write a function definition named is_vowel that takes in value and returns True if the value is a, e, i, o, u in upper or lower case.

# def is_vowel(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if string.lower() in vowels:
#         return True
#     else:
#         return False

def is_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if string.lower() in vowels else False



assert is_vowel("a") == True
assert is_vowel("e") == True
assert is_vowel("i") == True
assert is_vowel("o") == True
assert is_vowel("u") == True
assert is_vowel("A") == True
assert is_vowel("E") == True
assert is_vowel("I") == True
assert is_vowel("O") == True
assert is_vowel("U") == True
assert is_vowel("banana") == False
assert is_vowel("Q") == False
assert is_vowel("y") == False
assert is_vowel("aei") == False
assert is_vowel("iou") == False
print("Exercise 43 is correct.")


# In[50]:


# Exercise 44
# Write a function definition named has_vowels that takes in value and returns True if the string contains any vowels.

# def has_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char in string.lower():
#         if char in vowels:
#             return True
#     return False

def has_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = any([char for char in string.lower() if char in vowels])
    return result


assert has_vowels("banana") == True
assert has_vowels("ubuntu") == True
assert has_vowels("BANANA") == True
assert has_vowels("QQQQ") == False
assert has_vowels("wyrd") == False
print("Exercise 44 is correct.")


# In[51]:


# Exercise 45
# Write a function definition named count_vowels that takes in value and returns the count of the nubmer of vowels in a sequence.
# def count_vowels(string):
#     count = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char in string.lower():
#         if char in vowels:
#             count += 1
#     return count

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = len([char for char in string if char in vowels])
    return result

assert count_vowels("banana") == 3
assert count_vowels("ubuntu") == 3
assert count_vowels("mango") == 2
assert count_vowels("QQQQ") == 0
assert count_vowels("wyrd") == 0
print("Exercise 45 is correct.")


# In[52]:


# Exercise 46
# Write a function definition named remove_vowels that takes in string and returns the string without any vowels

# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for char in string:
#         if char in vowels:
#             string = string.replace(char, '')
#     return string

def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''.join([char for char in string if char not in vowels])
    return result

assert remove_vowels("banana") == "bnn"
assert remove_vowels("ubuntu") == "bnt"
assert remove_vowels("mango") == "mng"
assert remove_vowels("QQQQ") == "QQQQ"
print("Exercise 46 is correct.")


# In[53]:


# Exercise 47
# Write a function definition named starts_with_vowel that takes in string and True if the string starts with a vowel

# def starts_with_vowel(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if string[0] in vowels:
#         return True
#     else:
#         return False

def starts_with_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if string[0] in vowels else False

assert starts_with_vowel("ubuntu") == True
assert starts_with_vowel("banana") == False
assert starts_with_vowel("mango") == False
print("Exercise 47 is correct.")


# In[54]:


# Exercise 48
# Write a function definition named ends_with_vowel that takes in string and True if the string ends with a vowel

# def ends_with_vowel(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if string[-1] in vowels:
#         return True 
#     else:
#         return False

def ends_with_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if string[-1] in vowels else False

 
assert ends_with_vowel("ubuntu") == True
assert ends_with_vowel("banana") == True
assert ends_with_vowel("mango") == True
assert ends_with_vowel("spinach") == False
print("Exercise 48 is correct.")


# In[55]:


# Exercise 49
# Write a function definition named starts_and_ends_with_vowel that takes in string and returns True if the string starts and ends with a vowel

# def starts_and_ends_with_vowel(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     if string[0] in vowels and string[-1] in vowels:
#         return True 
#     else:
#         return False

def starts_and_ends_with_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if string[0] in vowels and string[-1] in vowels else False

assert starts_and_ends_with_vowel("ubuntu") == True
assert starts_and_ends_with_vowel("banana") == False
assert starts_and_ends_with_vowel("mango") == False
print("Exercise 49 is correct.")


# ## Accessing List Elements

# In[56]:


# Exercise 50
# Write a function definition named first that takes in sequence and returns the first value of that sequence.

def first(string):
    return string[0]


assert first("ubuntu") == "u"
assert first([1, 2, 3]) == 1
assert first(["python", "is", "awesome"]) == "python"
print("Exercise 50 is correct.")


# In[57]:


# Exercise 51
# Write a function definition named second that takes in sequence and returns the second value of that sequence.

def second(string):
    return string[1]

assert second("ubuntu") == "b"
assert second([1, 2, 3]) == 2
assert second(["python", "is", "awesome"]) == "is"
print("Exercise 51 is correct.")


# In[58]:


# Exercise 52
# Write a function definition named third that takes in sequence and returns the third value of that sequence.

def third(string):
    return string[2]


assert third("ubuntu") == "u"
assert third([1, 2, 3]) == 3
assert third(["python", "is", "awesome"]) == "awesome"
print("Exercise 52 is correct.")


# In[59]:


# Exercise 53
# Write a function definition named forth that takes in sequence and returns the forth value of that sequence.

def forth(string):
    return string[3]

assert forth("ubuntu") == "n"
assert forth([1, 2, 3, 4]) == 4
assert forth(["python", "is", "awesome", "right?"]) == "right?"
print("Exercise 53 is correct.")


# In[60]:


# Exercise 54
# Write a function definition named last that takes in sequence and returns the last value of that sequence.

def last(string):
    return string[-1]

assert last("ubuntu") == "u"
assert last([1, 2, 3, 4]) == 4
assert last(["python", "is", "awesome"]) == "awesome"
assert last(["kiwi", "mango", "guava"]) == "guava"
print("Exercise 54 is correct.")


# In[61]:


# Exercise 55
# Write a function definition named second_to_last that takes in sequence and returns the second to last value of that sequence.

def second_to_last(string):
    return string[-2]

assert second_to_last("ubuntu") == "t"
assert second_to_last([1, 2, 3, 4]) == 3
assert second_to_last(["python", "is", "awesome"]) == "is"
assert second_to_last(["kiwi", "mango", "guava"]) == "mango"
print("Exercise 55 is correct.")


# In[62]:


# Exercise 56
# Write a function definition named third_to_last that takes in sequence and returns the third to last value of that sequence.

def third_to_last(string):
    return string[-3]


assert third_to_last("ubuntu") == "n"
assert third_to_last([1, 2, 3, 4]) == 2
assert third_to_last(["python", "is", "awesome"]) == "python"
assert third_to_last(["strawberry", "kiwi", "mango", "guava"]) == "kiwi"
print("Exercise 56 is correct.")


# In[63]:


# Exercise 57
# Write a function definition named first_and_second that takes in sequence and returns the first and second value of that sequence as a list

# def first_and_second(string):
#     return list((string[0], string[1]))

# def first_and_second(string):
#     return list(string[0:2])

def first_and_second(string):
    return [char for char in string[0:2]]

# def first_and_second(string):
#     for char in string[0:2]:
#         string = list(string[0:2])
#     return string

assert first_and_second([1, 2, 3, 4]) == [1, 2]
assert first_and_second(["python", "is", "awesome"]) == ["python", "is"]
assert first_and_second(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "kiwi"]
print("Exercise 57 is correct.")


# In[64]:


# Exercise 58
# Write a function definition named first_and_last that takes in sequence and returns the first and last value of that sequence as a list

# def first_and_last(string):
#     return list((string[0], string[-1]))

# def first_and_last(string):
#     return string[::len(string)-1]

def first_and_last(string):
    return [string[i] for i in (0,-1)]

assert first_and_last([1, 2, 3, 4]) == [1, 4]
assert first_and_last(["python", "is", "awesome"]) == ["python", "awesome"]
assert first_and_last(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "guava"]
print("Exercise 58 is correct.")


# In[65]:


# Exercise 59
# Write a function definition named first_to_last that takes in sequence and returns the sequence with the first value moved to the end of the sequence.

# def first_to_last(string):
#     a = string[0]
#     b = string[1:]
#     b.append(a)
#     return b

def first_to_last(string):
    string = string[1:] + [string[0]]
    return string

assert first_to_last([1, 2, 3, 4]) == [2, 3, 4, 1]
assert first_to_last(["python", "is", "awesome"]) == ["is", "awesome", "python"]
assert first_to_last(["strawberry", "kiwi", "mango", "guava"]) == ["kiwi", "mango", "guava", "strawberry"]
print("Exercise 59 is correct.")


# ## Functions to describe data

# In[66]:


# Exercise 60
# Write a function definition named sum_all that takes in sequence of numbers and returns all the numbers added together.
from functools import reduce

# def sum_all(numbers):
#     return sum(numbers)


def sum_all(numbers):
    return reduce(lambda p,q: p+q, numbers)

assert sum_all([1, 2, 3, 4]) == 10
assert sum_all([3, 3, 3]) == 9
assert sum_all([0, 5, 6]) == 11
print("Exercise 60 is correct.")


# In[67]:


# Exercise 61
# Write a function definition named mean that takes in sequence of numbers and returns the average value
import statistics 

def mean(numbers):
    return statistics.mean(numbers)



assert mean([1, 2, 3, 4]) == 2.5
assert mean([3, 3, 3]) == 3
assert mean([1, 5, 6]) == 4
print("Exercise 61 is correct.")


# In[68]:


# Exercise 62
# Write a function definition named median that takes in sequence of numbers and returns the average value

def median(numbers):
    return statistics.median(numbers)

assert median([1, 2, 3, 4, 5]) == 3.0
assert median([1, 2, 3]) == 2.0
assert median([1, 5, 6]) == 5.0
assert median([1, 2, 5, 6]) == 3.5
print("Exercise 62 is correct.")


# In[69]:


# Exercise 63
# Write a function definition named mode that takes in sequence of numbers and returns the most commonly occuring value

def mode(numbers):
    return statistics.mode(numbers)

assert mode([1, 2, 2, 3, 4]) == 2
assert mode([1, 1, 2, 3]) == 1
assert mode([2, 2, 3, 3, 3]) == 3
print("Exercise 63 is correct.")


# In[70]:


# Exercise 64
# Write a function definition named product_of_all that takes in sequence of numbers and returns the product of multiplying all the numbers together
import math

def product_of_all(numbers):
    return math.prod(numbers)


assert product_of_all([1, 2, 3]) == 6
assert product_of_all([3, 4, 5]) == 60
assert product_of_all([2, 2, 3, 0]) == 0
print("Exercise 64 is correct.")


# ## Applying functions to lists

# In[71]:


# Exercise 65
# Write a function definition named get_highest_number that takes in sequence of numbers and returns the largest number.

def get_highest_number(numbers):
    return max(numbers)


assert get_highest_number([1, 2, 3]) == 3
assert get_highest_number([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == 5
assert get_highest_number([-5, -3, 1]) == 1
print("Exercise 65 is correct.")


# In[72]:


# Exercise 66
# Write a function definition named get_smallest_number that takes in sequence of numbers and returns the smallest number.

def get_smallest_number(numbers):
    return min(numbers)


assert get_smallest_number([1, 3, 2]) == 1
assert get_smallest_number([5, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == -5
assert get_smallest_number([-4, -3, 1, -10]) == -10
print("Exercise 66 is correct.")


# In[73]:


# Exercise 67
# Write a function definition named only_odd_numbers that takes in sequence of numbers and returns the odd numbers in a list.

def only_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 !=0, numbers))

# def only_odd_numbers(numbers):
#     only_odd_numbers = []
#     for number in numbers:
#         if number % 2 != 0:
#             only_odd_numbers.append(number)
            
#     return only_odd_numbers 


    
# def only_odd_numbers(numbers):
#     result = [number for number in numbers if number % 2 != 0]
#     return result


assert only_odd_numbers([1, 2, 3]) == [1, 3]
assert only_odd_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert only_odd_numbers([-4, -3, 1]) == [-3, 1]
assert only_odd_numbers([2, 2, 2, 2, 2]) == []
print("Exercise 67 is correct.")


# In[74]:


# Exercise 68
# Write a function definition named only_even_numbers that takes in sequence of numbers and returns the even numbers in a list.

# def only_even_numbers(numbers):
#     return list(filter(lambda x: x % 2 == 0,numbers))

# def only_even_numbers(numbers):
#     even_numbers = [] 
#     for number in numbers:
#         if number %2 == 0:
#             even_numbers.append(number)
#     return even_numbers 

def only_even_numbers(numbers):
    return [number for number in numbers if number % 2== 0]

assert only_even_numbers([1, 2, 3]) == [2]
assert only_even_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert only_even_numbers([-4, -3, 1]) == [-4]
assert only_even_numbers([1, 1, 1, 1, 1, 1]) == []
print("Exercise 68 is correct.")


# In[75]:


# Exercise 69
# Write a function definition named only_positive_numbers that takes in sequence of numbers and returns the positive numbers in a list.

# def only_positive_numbers(numbers):
#     positive_number = []
#     for number in numbers:
#         if number > 0:
#             positive_number.append(number)
#     return positive_number

# def only_positive_numbers(numbers):
#     return list(filter(lambda x: x > 0,numbers))

def only_positive_numbers(numbers):
    return [number for number in numbers if number > 0]


assert only_positive_numbers([1, 2, 3]) == [1, 2, 3]
assert only_positive_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert only_positive_numbers([-4, -3, 1]) == [1]
print("Exercise 69 is correct.")


# In[76]:


# Exercise 70
# Write a function definition named only_negative_numbers that takes in sequence of numbers and returns the negative numbers in a list.

# def only_positive_numbers(numbers):
#     positive_number = []
#     for number in numbers:
#         if number < 0:
#             positive_number.append(number)
#     return positive_number

# def only_positive_numbers(numbers):
#     return list(filter(lambda x: x < 0,numbers))

def only_negative_numbers(numbers):
    return list(filter(lambda x: x < 0, numbers))



assert only_negative_numbers([1, 2, 3]) == []
assert only_negative_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
assert only_negative_numbers([-4, -3, 1]) == [-4, -3]
print("Exercise 70 is correct.")


# In[77]:


# Exercise 71
# Write a function definition named has_evens that takes in sequence of numbers and returns True if there are any even numbers in the sequence

def has_evens(numbers):
    result = any([number for number in numbers if number % 2 ==0])
    return result

# def has_evens(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             return True 
#     else:
#         return False
 

assert has_evens([1, 2, 3]) == True
assert has_evens([2, 5, 6]) == True
assert has_evens([3, 3, 3]) == False
assert has_evens([]) == False
print("Exercise 71 is correct.")


# In[78]:


# Exercise 72
# Write a function definition named count_evens that takes in sequence of numbers and returns the number of even numbers

# def count_evens(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0:
#             count += 1
#     return count 

def count_evens(numbers):
    return len([number for number in numbers if number % 2== 0])

assert count_evens([1, 2, 3]) == 1
assert count_evens([2, 5, 6]) == 2
assert count_evens([3, 3, 3]) == 0
assert count_evens([5, 6, 7, 8] ) == 2
print("Exercise 72 is correct.")


# In[79]:


# Exercise 73
# Write a function definition named has_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence

# def has_odds(numbers):
#     for number in numbers:
#         if number % 2 != 0:
#             return True 
#     return False

def has_odds(numbers):
    return any(number for number in numbers if number %2 !=0)

assert has_odds([1, 2, 3]) == True
assert has_odds([2, 5, 6]) == True
assert has_odds([3, 3, 3]) == True
assert has_odds([2, 4, 6]) == False
print("Exercise 73 is correct.")


# In[80]:


# Exercise 74
# Write a function definition named count_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence

# def count_odds(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 != 0:
#             count += 1
#     return count

def count_odds(numbers):
    return len([number for number in numbers if number %2 !=0])

assert count_odds([1, 2, 3]) == 2
assert count_odds([2, 5, 6]) == 1
assert count_odds([3, 3, 3]) == 3
assert count_odds([2, 4, 6]) == 0
print("Exercise 74 is correct.")


# In[81]:


# Exercise 75
# Write a function definition named count_negatives that takes in sequence of numbers and returns a count of the number of negative numbers

# def count_negatives(numbers):
#     count = 0
#     for number in numbers:
#         if number < 0:
#             count += 1
#     return count
def count_negatives(numbers):
    return len([number for number in numbers if number < 0]) 


assert count_negatives([1, -2, 3]) == 1
assert count_negatives([2, -5, -6]) == 2
assert count_negatives([3, 3, 3]) == 0
print("Exercise 75 is correct.")


# In[82]:


# Exercise 76
# Write a function definition named count_positives that takes in sequence of numbers and returns a count of the number of positive numbers

# def count_positives(numbers):
#     count = 0
#     for number in numbers:
#         if number > 0:
#             count += 1      
#     return count

def count_positives(numbers):
    return len([number for number in numbers if number > 0])

assert count_positives([1, -2, 3]) == 2
assert count_positives([2, -5, -6]) == 1
assert count_positives([3, 3, 3]) == 3
assert count_positives([-2, -1, -5]) == 0
print("Exercise 76 is correct.")


# In[83]:


# Exercise 77
# Write a function definition named only_positive_evens that takes in sequence of numbers and returns a list containing all the positive evens from the sequence

# def only_positive_evens(numbers):
#     only_positive_evens = []
#     for number in numbers:
#         if number > 0 and number % 2 == 0:
#             only_positive_evens.append(number)
#     return only_positive_evens


def only_positive_evens(numbers):
    return [number for number in numbers if number > 0 and number % 2 == 0]

assert only_positive_evens([1, -2, 3]) == []
assert only_positive_evens([2, -5, -6]) == [2]
assert only_positive_evens([3, 3, 4, 6]) == [4, 6]
assert only_positive_evens([2, 3, 4, -1, -5]) == [2, 4]
print("Exercise 77 is correct.")


# In[84]:


# Exercise 78
# Write a function definition named only_positive_odds that takes in sequence of numbers and returns a list containing all the positive odd numbers from the sequence

# def only_positive_odds(numbers):
#     only_positive_odds = []
#     for number in numbers:
#         if number > 0 and number % 2 != 0:
#             only_positive_odds.append(number)
#     return only_positive_odds

def only_positive_odds(numbers):
    return [number for number in numbers if number > 0 and number % 2 != 0]

assert only_positive_odds([1, -2, 3]) == [1, 3]
assert only_positive_odds([2, -5, -6]) == []
assert only_positive_odds([3, 3, 4, 6]) == [3, 3]
assert only_positive_odds([2, 3, 4, -1, -5]) == [3]
print("Exercise 78 is correct.")


# In[85]:


# Exercise 79
# Write a function definition named only_negative_evens that takes in sequence of numbers and returns a list containing all the negative even numbers from the sequence

# def only_negative_evens(numbers):
#     only_negative_evens =[]
#     for number in numbers:
#         if number < 0 and number % 2 == 0:
#             only_negative_evens.append(number)
            
#     return only_negative_evens

def only_negative_evens(numbers):
    return [number for number in numbers if number < 0 and number %2 == 0]

assert only_negative_evens([1, -2, 3]) == [-2]
assert only_negative_evens([2, -5, -6]) == [-6]
assert only_negative_evens([3, 3, 4, 6]) == []
assert only_negative_evens([-2, 3, 4, -1, -4]) == [-2, -4]
print("Exercise 79 is correct.")


# In[86]:


# Exercise 80
# Write a function definition named only_negative_odds that takes in sequence of numbers and returns a list containing all the negative odd numbers from the sequence

# def only_negative_odds(numbers):
#     only_negative_odds = []
#     for number in numbers:
#         if number < 0 and number %2 != 0:
#             only_negative_odds.append(number)
#     return only_negative_odds

def only_negative_odds(numbers):
    return [number for number in numbers if number < 0 and number %2 != 0]

assert only_negative_odds([1, -2, 3]) == []
assert only_negative_odds([2, -5, -6]) == [-5]
assert only_negative_odds([3, 3, 4, 6]) == []
assert only_negative_odds([2, -3, 4, -1, -4]) == [-3, -1]
print("Exercise 80 is correct.")


# In[87]:


# Exercise 81
# Write a function definition named shortest_string that takes in a list of strings and returns the shortest string in the list.

# def shortest_string(string):
#     return min(string, key=len)

# def shortest_string(string):
#     letters = [len(letter) for letter in string]
#     index = letters.index(min(letters))
#     return string[index]

from functools import reduce

def shortest_string(string):
    return reduce(lambda x,y: x if len(x) < len(y) else y, string)

assert shortest_string(["kiwi", "mango", "strawberry"]) == "kiwi"
assert shortest_string(["hello", "everybody"]) == "hello"
assert shortest_string(["mary", "had", "a", "little", "lamb"]) == "a"
print("Exercise 81 is correct.")


# In[88]:


# Exercise 82
# Write a function definition named longest_string that takes in sequence of strings and returns the longest string in the list.

# def longest_string(string):
#     return max(string, key=len)

# def longest_string(string):
#     characters = [len(char) for char in string]
#     index = characters.index(max(characters))
#     return string[index]

def longest_string(string):
    return reduce(lambda x,y: x if len(x) > len(y) else y, string)

assert longest_string(["kiwi", "mango", "strawberry"]) == "strawberry"
assert longest_string(["hello", "everybody"]) == "everybody"
assert longest_string(["mary", "had", "a", "little", "lamb"]) == "little"
print("Exercise 82 is correct.")


# ## Working with sets
# **Hint** Take a look at the `set` function in Python, the `set` data type, and built-in `set` methods.

# In[89]:


# Example set function usage
print(set("kiwi"))
print(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))


# In[90]:


# Exercise 83
# Write a function definition named get_unique_values that takes in a list and returns a set with only the unique values from that list.

def get_unique_values(string):
    return set(string)


assert get_unique_values(["ant", "ant", "mosquito", "mosquito", "ladybug"]) == {"ant", "mosquito", "ladybug"}
assert get_unique_values(["b", "a", "n", "a", "n", "a", "s"]) == {"b", "a", "n", "s"}
assert get_unique_values(["mary", "had", "a", "little", "lamb", "little", "lamb", "little", "lamb"]) == {"mary", "had", "a", "little", "lamb"}
print("Exercise 83 is correct.")


# In[91]:


# Exercise 84
# Write a function definition named get_unique_values_from_two_lists that takes two lists and returns a single set with only the unique values

def get_unique_values_from_two_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)

assert get_unique_values_from_two_lists([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 3, 4, 5}
assert get_unique_values_from_two_lists([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_unique_values_from_two_lists(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato", "mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 84 is correct.")


# In[92]:


# Exercise 85
# Write a function definition named get_values_in_common that takes two lists and returns a single set with the values that each list has in common

def get_values_in_common(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

assert get_values_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {3, 5}
assert get_values_in_common([1, 2], [2, 2, 3]) == {2}
assert get_values_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato"}
print("Exercise 85 is correct.")


# In[93]:


# Exercise 86
# Write a function definition named get_values_not_in_common that takes two lists and returns a single set with the values that each list does not have in common

def get_values_not_in_common(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    return list1.symmetric_difference(list2)


assert get_values_not_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 4}
assert get_values_not_in_common([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_values_not_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 86 is correct.")


# ## Working with Dictionaries
# 

# In[94]:


# Run this cell in order to have these two dictionary variables defined.
tukey_paper = {
    "title": "The Future of Data Analysis",
    "author": "John W. Tukey",
    "link": "https://projecteuclid.org/euclid.aoms/1177704711",
    "year_published": 1962
}

thomas_paper = {
    "title": "A mathematical model of glutathione metabolism",
    "author": "Rachel Thomas",
    "link": "https://www.ncbi.nlm.nih.gov/pubmed/18442411",
    "year_published": 2008
}


# In[95]:


print(tukey_paper['title'])
print(thomas_paper['title'])
print(tukey_paper.keys())
print(tukey_paper.values())
print(tukey_paper.items())


# In[96]:


for k,v in tukey_paper.items():
    print(k, v)


# In[97]:


for i, v in enumerate(tukey_paper):
    print(i, v)


# In[98]:


for key, value in tukey_paper.items():
    print('{0} correspond to {1}'.format(key, value))


# In[99]:


for a, b in zip(tukey_paper.keys(), tukey_paper.values()):
    print('There are {0} corresponds to {1}'.format(a,b))


# In[100]:


[(key, value) for key,value in tukey_paper.items()]


# In[101]:


favsDict = { 'Tim': ['red', 'pizza', 'soda'],
             'Jake': ['green', 'burger', 'juice'],
             'Mary': ['blue', 'salad', 'water']    }


# In[102]:


print(favsDict['Tim'][1])
print(favsDict['Mary'][1])


# In[103]:


# Exercise 87
# Write a function named get_paper_title that takes in a dictionary and returns the title property

def get_paper_title(dicionary):
    return dicionary['title']


assert get_paper_title(tukey_paper) == "The Future of Data Analysis"
assert get_paper_title(thomas_paper) == "A mathematical model of glutathione metabolism"
print("Exercise 87 is correct.")


# In[104]:


# Exercise 88
# Write a function named get_year_published that takes in a dictionary and returns the value behind the "year_published" key.

def get_year_published(dictionary):
    return dictionary['year_published']


assert get_year_published(tukey_paper) == 1962
assert get_year_published(thomas_paper) == 2008
print("Exercise 88 is correct.")


# In[105]:


# Run this code to create data for the next two questions
book = {
    "title": "Genetic Algorithms and Machine Learning for Programmers",
    "price": 36.99,
    "author": "Frances Buontempo"
}


# In[106]:


# Exercise 89
# Write a function named get_price that takes in a dictionary and returns the price

def get_price(dictionary):
    return dictionary['price']

assert get_price(book) == 36.99
print("Exercise 89 is complete.")


# In[107]:


# Exercise 90
# Write a function named get_book_author that takes in a dictionary (the above declared book variable) and returns the author's name

def get_book_author(dictionary):
    return dictionary['author']


assert get_book_author(book) == "Frances Buontempo"
print("Exercise 90 is complete.")


# ## Working with Lists of Dictionaries
# **Hint** If you need an example of lists of dictionaries, see
# - [Getting Started With a List of Dictionaries](https://colab.research.google.com/github/ryanorsinger/list_of_dictionaries/blob/main/getting_started.ipynb)
# - [Practice Exercises for List of Dictionaries](https://colab.research.google.com/github/ryanorsinger/list_of_dictionaries/blob/main/exercises.ipynb)
# - [Companion Video](https://www.youtube.com/watch?v=pPdEahZgv8U)
# 

# In[108]:


# Run this cell in order to have some setup data for the next exercises
books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "price": 36.99,
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "price": 38.00,
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "price": 30.47
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "price": 17.44
    }
]


# In[109]:


# Exercise 91
# Write a function named get_number_of_books that takes in a list of objects and returns the number of dictionaries in that list.


def get_number_of_books(ListOfDictionaries):
    return len(ListOfDictionaries)

assert get_number_of_books(books) == 4
print("Exercise 91 is complete.")


# In[110]:


# Exercise 92
# Write a function named total_of_book_prices that takes in a list of dictionaries and returns the sum total of all the book prices added together

def total_of_book_prices(dictionaries):
    return sum(dictionary['price'] for dictionary in dictionaries)

# def total_of_book_prices(dictionary):
#     price_total = 0
#     for book in books:
#         price_total += book['price']
#     return price_total 


assert total_of_book_prices(books) == 122.9
print("Exercise 92 is complete.")


# In[111]:


books


# In[112]:


sum_of_price = 0
counter = 0

for book in books:
    sum_of_price += book['price']
    quantity_of_item = len(books)
    counter += 1
print(sum_of_price)
print(quantity_of_item)
print(counter)
    


# In[113]:


# Exercise 93
# Write a function named get_average_book_price that takes in a list of dictionaries and returns the average book price.

# import statistics 

# def get_average_book_price(dictionaries):
#     return statistics.mean(dictionary['price'] for dictionary in dictionaries)

def get_average_book_price(listofdicionaries):
    sum_of_price = 0
    quantityofbooks = 0
    for listofdictionary in listofdicionaries:
        sum_of_price += listofdictionary['price']
        quantityofbooks += 1
    return   sum_of_price / quantityofbooks


assert get_average_book_price(books) == 30.725
print("Exercise 93 is complete.")


# In[114]:


# Exercise 94
# Write a function called highest_price_book that takes in the above defined list of dictionaries "books" and returns the dictionary containing the title, price, and author of the book with the highest priced book.
# Hint: Much like sometimes start functions with a variable set to zero, you may want to create a dictionary with the price set to zero to compare to each dictionary's price in the list


def highest_price_book(dictionary):
    return max(dictionary, key=lambda x:x['price'])

assert highest_price_book(books) == {
    "title": "The Visual Display of Quantitative Information",
    "price": 38.00,
    "author": "Edward Tufte"
}

print("Exercise 94 is complete")


# In[115]:


# Exercise 95
# Write a function called lowest_priced_book that takes in the above defined list of dictionaries "books" and returns the dictionary containing the title, price, and author of the book with the lowest priced book.
# Hint: Much like sometimes start functions with a variable set to zero or float('inf'), you may want to create a dictionary with the price set to float('inf') to compare to each dictionary in the list

def lowest_price_book(dictionary):
    return min(dictionary, key=lambda x:x['price'])


assert lowest_price_book(books) == {
    "title": "Weapons of Math Destruction",
    "author": "Cathy O'Neil",
    "price": 17.44
}
print("Exercise 95 is complete.")


# In[116]:


shopping_cart = {
    "tax": .08,
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "chocolate",
            "price": 0.75,
            "quantity": 9
        }
    ]
}


# In[117]:


# Exercise 96
# Write a function named get_tax_rate that takes in the above shopping cart as input and returns the tax rate.
# Hint: How do you access a key's value on a dictionary? The tax rate is one key of the entire shopping_cart dictionary.

def get_tax_rate(listofdictionary):
    return listofdictionary['tax']

assert get_tax_rate(shopping_cart) == .08
print("Exercise 96 is complete")


# In[118]:


# Exercise 97
# Write a function named number_of_item_types that takes in the shopping cart as input and returns the number of unique item types in the shopping cart.
# We're not yet using the quantity of each item, but rather focusing on determining how many different types of items are in the cart.

def number_of_item_types(listofdictionary):
    return len(listofdictionary['items'])

# def number_of_item_types(listofdictionary):
#     counter = 0
#     for quantity in listofdictionary['items']:
#         counter += 1
#     return counter 


assert number_of_item_types(shopping_cart) == 5
print("Exercise 97 is complete.")


# In[119]:


# Exercise 98
# Write a function named total_number_of_items that takes in the shopping cart as input and returns the total number all item quantities.
# This should return the sum of all of the quantities from each item type

def total_number_of_items(dictionary):
    dictionary = dictionary['items'] 
    return sum(values['quantity'] for values in dictionary)

# def total_number_of_items(listofdictionaries):
#     listofdictionaries = listofdictionaries['items']
#     sumofquantity = 0
#     for quantity in listofdictionaries:
#         sumofquantity += quantity['quantity']
#     return sumofquantity

assert total_number_of_items(shopping_cart) == 17
print("Exercise 98 is complete.")


# In[120]:


# Exercise 99
# Write a function named get_average_item_price that takes in the shopping cart as an input and returns the average of all the item prices.
# Hint - This should determine the total price divided by the number of types of items. This does not account for each item type's quantity.

def get_average_item_price(listofdictionary):
    listofdictionary = listofdictionary['items']
    sumofprice = 0
    counter = 0
    for item in listofdictionary:
        sumofprice += item['price']
        counter += 1
    return sumofprice /  counter
    
# import statistics 
# def get_average_item_price(listofdictionary):
#     listofdictionary = listofdictionary['items']
#     return statistics.mean(values['price'] for values in listofdictionary)


assert get_average_item_price(shopping_cart) == 2.1420000000000003
#assert get_average_item_price(shopping_cart) == 2.142

print("Exercise 99 is complete.")


# In[121]:


itemsdict = shopping_cart['items']

a = sum(item['price'] * item['quantity'] for item in itemsdict)
b = sum(item['quantity'] for item in itemsdict)


a / b


# In[122]:


# Exercise 100
# Write a function named get_average_spent_per_item that takes in the shopping cart and returns the average of summing each item's quanties times that item's price.
# Hint: You may need to set an initial total price and total total quantity to zero, then sum up and divide that total price by the total quantity

# def get_average_spent_per_item(listofdictionaries):
#     listofdictionaries = listofdictionaries['items']
#     total_spent = 0
#     quantity_of_items = 0
#     for listofdictionary in listofdictionaries:
#         total_spent += listofdictionary['price'] * listofdictionary['quantity']
#         quantity_of_items += listofdictionary['quantity']
#     average_per_item = total_spent /  quantity_of_items
    
#     return average_per_item
    
def get_average_spent_per_item(listofdictionaries):
    listofdictionaries = listofdictionaries['items']
    TotalRevenue = sum(item['price'] * item['quantity'] for item in listofdictionaries)
    QuantityOfItem = sum(item['quantity'] for item in listofdictionaries)
    return TotalRevenue / QuantityOfItem
    

assert get_average_spent_per_item(shopping_cart) == 1.333529411764706
print("Exercise 100 is complete.")


# In[123]:


# Exercise 101
# Write a function named most_spent_on_item that takes in the shopping cart as input and returns the dictionary associated with the item that has the highest price*quantity.
# Be sure to do this as programmatically as possible.
# Hint: Similarly to how we sometimes begin a function with setting a variable to zero, we need a starting place:
# Hint: Consider creating a variable that is a dictionary with the keys "price" and "quantity" both set to 0. You can then compare each item's price and quantity total to the one from "most"

def most_spent_on_item(listofdictionaries):
    listofdictionaries = listofdictionaries['items']
    return max(listofdictionaries, key=lambda x:x['price']*x['quantity'])

assert most_spent_on_item(shopping_cart) == {
    "title": "chocolate",
    "price": 0.75,
    "quantity": 9
}
print("Exercise 101 is complete.")


# In[124]:


#https://colab.research.google.com/github/ryanorsinger/list_of_dictionaries/blob/main/getting_started.ipynb#scrollTo=NW30XiyIOas9
#https://github.com/ryanorsinger/list_of_dictionaries/blob/main/getting_started.ipynb
fruits = [
    {
        "item": "apple",
        "quantity": 5,
        "price": 0.95
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    }
]


# In[125]:


# How do we access the first dictionary in the list?
fruits[0]


# In[126]:


# How would we get the number of apples?
fruits[0]['quantity']


# In[127]:


# How would we determine the total spent on apples where we multiply price * quantity?
fruits[0]['quantity'] * fruits[0]['price']


# In[128]:


# What's one way to determine the total quantity of all items in the fruist list of dictionaries?
fruits[0]['quantity'] + fruits[1]['quantity']


# In[129]:


# What about if we have a longer list than only two? What if we need this to be programmatic? Use a loop!
total_quantity = 0 
for fruit in fruits:
    total_quantity += fruit['quantity']
total_quantity


# In[130]:


sum(fruit['quantity'] for fruit in fruits)


# In[131]:


# What's one way to determine the total spent on both apples and oranges? (this is the "brute force" way)
(fruits[0]['quantity'] * fruits[0]['price']) + (fruits[1]['quantity'] * fruits[1]['price'])


# In[132]:


# What's a programmatic way to determine the total spend? Use a loop! Then access each dictionary's values inside the loop
total_spend = 0

for fruit in fruits:
    total_spend += fruit['quantity'] * fruit['price']
   
    
total_spend


# In[133]:


sum(fruit['price'] * fruit['quantity'] for fruit in fruits)


# In[134]:


# How would we determine the average price spent per item?
total_spent = 0
quantity = 0

for fruit in fruits:
    total_spent += fruit['price'] * fruit['quantity']
    quantity += fruit['quantity']
    
total_spent / quantity  


# In[135]:


Total_Spent = sum(fruit['price'] * fruit['quantity'] for fruit in fruits)
Quantity = sum(fruit['quantity'] for fruit in fruits)

Total_Spent / Quantity


# In[136]:


# https://colab.research.google.com/github/ryanorsinger/list_of_dictionaries/blob/main/exercises.ipynb
#https://www.youtube.com/watch?v=pPdEahZgv8U
#https://github.com/ryanorsinger/list_of_dictionaries/blob/main/exercises.ipynb
drinks = [
    {
        "type": "water",
        "calories": 0,
        "number_consumed": 7,
        "caffeinated": False
    },
    {
        "type": "orange juice",
        "calories": 220,
        "number_consumed": 4,
        "caffeinated": False
    },
    {
        "type": "gatorade",
        "calories": 140,
        "number_consumed": 1,
        "caffeinated": False
    },
    {
        "type": "cappuccino",
        "calories": 350,
        "number_consumed": 2,
        "caffeinated": True
    },
    {
        "type": "hot tea",
        "calories": 5,
        "number_consumed": 3,
        "caffeinated": True
    }
]


# In[137]:


# Exercise 1
# How many different kinds of drinks?
len(drinks)


# In[138]:


quantity_of_drinks = 0
for drink in drinks:
    quantity_of_drinks += 1
    
quantity_of_drinks


# In[139]:


# Exercise 2
# How many total consumed drinks?
total_consumed_drinks = 0
for drink in drinks:
    total_consumed_drinks += drink['number_consumed']
    
total_consumed_drinks


# In[140]:


sum(drink['number_consumed'] for drink in drinks)


# In[141]:


# Exercise 3
# How many total consumed calories

total_consumed_calories = 0


for drink in drinks:
    total_consumed_calories += drink['calories'] * drink['number_consumed']
    
total_consumed_calories
    


# In[142]:


sum(drink['calories'] * drink['number_consumed'] for drink in drinks)


# In[143]:


# Exercise 4a
# How many types of drinks are caffieinated?
drinks_caffeinated = 0
 
for drink in drinks:
    if drink['caffeinated'] == True:
        drinks_caffeinated += 1
        
drinks_caffeinated   


# In[144]:


drink_caffeinated = [drink for drink in drinks if drink['caffeinated'] == True]
len(drink_caffeinated)


# In[145]:


# Exercise 4b
# How many types of drinks are non-caffieinated?
drinks_no_caffeinated = 0

for drink in drinks:
    if drink['caffeinated'] == False:
        drinks_no_caffeinated += 1

drinks_no_caffeinated    


# In[146]:


drink_no_caffeinated = [drink for drink in drinks if drink['caffeinated'] == False]
len(drink_no_caffeinated)


# In[147]:


# Exercise 5a
# How many total consumed drinks were non-caffeinated?
total_consumed_drinks_non_caffeinated = 0
for drink in drinks:
    if drink['caffeinated'] == False:
        total_consumed_drinks_non_caffeinated += drink['number_consumed']

total_consumed_drinks_non_caffeinated
        


# In[148]:


sum(drink['number_consumed'] for drink in drinks if drink['caffeinated'] == False)


# In[149]:


# Exercise 6
# Which drink has the most calories?
max(drinks, key=lambda x:x['calories'])


# In[150]:


# Exercise 7
# Which drink was consumed the least?
min(drinks, key=lambda x:x['calories'])


# In[151]:


# Exercise 8
# Average calorie count per consumed drink, if all beverages are consumed
total_calories = 0
quantity = 0

for drink in drinks:
    total_calories += drink['calories'] * drink['number_consumed']
    quantity += 1
    
total_calories / quantity


# In[152]:


Total_calories = sum(drink['calories'] * drink['number_consumed'] for drink in drinks)
Quantity = len(drinks)
Total_calories / Quantity


# In[153]:


#https://github.com/ryanorsinger/list_of_dictionaries/blob/main/how-to-solve-looping-problems.ipynb
#https://www.youtube.com/watch?v=Mk-N_iGJIAc&t=1555s
#https://www.youtube.com/watch?v=-IeZJhZkvjc&t=1435s
#https://www.youtube.com/watch?v=-IeZJhZkvjc
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# In[154]:


students[0]


# In[155]:


student = students[0]


# In[156]:


name = student['student']
pet = student['pets']
QuantityOfPets = len(student['pets'])


# In[157]:


name


# In[158]:


pet


# In[159]:


QuantityOfPets


# In[160]:


f'{name} has {QuantityOfPets} pet'


# In[161]:


for student in students:
    pets = len(student['pets'])
    name = student['student']
    print(f'{name} has {pets} pet(s)')
    


# In[162]:


for student in students:
    pets = len(student['pets']) 
    name = student['student']
    if pets == 0:
        print(f'{name} has no pets at all')
    if pets == 1:
        print(f'{name} has only {pets} pets')
    if pets > 1:
        print(f'{name} has only {pets} pets')


# In[163]:


number = 5
number


# In[164]:


numbers = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10]
numbers


# In[165]:


for number in numbers:
    print(number)


# In[166]:


number


# In[167]:


# First time through the for loop
number = numbers[0]
# Second time through the loop
number = numbers[1]
# etc...


# In[168]:


numbers[0]


# In[169]:


numbers[3]


# In[170]:


#Solving Iteration And Looping Problems
#1. What's the average of all student grades. -> 82.92857
#Loop and List Comprehension
students


# In[171]:


student = students[0]
student


# In[172]:


NewGradeList = []
for grade in student['grades']:
    NewGradeList.append(grade)


SumOfGradeNewStudent = sum(NewGradeList)
QuantityOfGradeEachStudent = len(NewGradeList)
Average = SumOfGradeNewStudent /  QuantityOfGradeEachStudent

SumOfGradeNewStudent, QuantityOfGradeEachStudent,  Average


# In[173]:


NewListStudentsGrade = []

for student in students:
    for grade in student['grades']:
        NewListStudentsGrade.append(grade)

SumEachStudentGrades = sum(NewListStudentsGrade)
QuantityOfGrades = len(NewListStudentsGrade)
AverageGradesOfEachStudent = SumEachStudentGrades / QuantityOfGrades

print(f'The average of all student grades {AverageGradesOfEachStudent}')


# In[174]:


#List Comprehension
GradeOfEachStudent = [student['grades'] for student in students]
GradeOfEachStudent


# In[175]:


#Flattening  lists of lists
from functools import reduce

NewGradeOfEachStudent= list(reduce(lambda x, y: x + y, GradeOfEachStudent, []))
NewGradeOfEachStudent


# In[176]:


SumNewListGradeStudents = sum(NewGradeOfEachStudent)
QuantityOfElement = len(NewGradeOfEachStudent)
AverageOfAllStudentGrades = SumNewListGradeStudents /  QuantityOfElement

print(f'The average of all student grades {AverageOfAllStudentGrades}')


# In[177]:


#Flattening  lists of lists

FlatteningGradeOfEachStudent = sum(GradeOfEachStudent, [])
FlatteningGradeOfEachStudent


# In[178]:


#2. Count the number of pets from data science students in the above data -> 9
#Loop and List Comprehension
student = students[3]   
student   


# In[179]:


len(student['pets'])  


# In[180]:


QuantityOfPetsStudentDS = []

for student in students:
    if student['course'] == 'data science':
        QuantityOfPets = len(student['pets'])
        QuantityOfPetsStudentDS.append(QuantityOfPets)
        
sum(QuantityOfPetsStudentDS)    


# In[181]:


QuantityOfPetsStudentDS2 = 0

for student in students:
    if student['course'] == 'data science':
        QuantityOfPetsStudentDS2 += len(student['pets'])
        
QuantityOfPetsStudentDS2        


# In[182]:


QuantityOfPetsDSStudent3 = [len(student['pets']) for student in students if student['course'] == 'data science']
QuantityOfPetsDSStudent3


# In[183]:


SumOfPetsStudentDSS = sum(QuantityOfPetsDSStudent3)
SumOfPetsStudentDSS


# In[184]:


#Breaking Problems Down, Building Solutions Up
#1. What is the average grade for students with 0 pets? ->  82.125, sum -> 657, number of student without pets 8
#Loop and List Comprehension


# In[185]:


student = students[2]
student


# In[186]:


sum(student['grades'])


# In[187]:


len(student['grades'])


# In[188]:


len(student['pets'])


# In[189]:


SumOfGrades = 0
QuantityOfGrades = 0

for student in students:
    SumOfGrades += sum(student['grades'])
    QuantityOfGrades += len(student['grades'])
    Average = SumOfGrades / QuantityOfGrades
    
print(f'Sum Of Grades for all students {SumOfGrades}')
print(f'Quantity of Grades for all students {QuantityOfGrades}')
print(f'Average of Grades for all students {Average}')


# In[190]:


def AverageGrade(students):
    SumOfGrades = 0
    QuantityOfGrades = 0
    for student in students:
        SumOfGrades += sum(student['grades'])
        QuantityOfGrades += len(student['grades'])
        Average = SumOfGrades / QuantityOfGrades
    #return Average    
    a = print(f'Sum Of Grades for all students {SumOfGrades}')
    b = print(f'Quantity of Grades for all students {QuantityOfGrades}')
    c = print(f'Average of Grades for all students {Average}')
    
     
AverageGrade(students)


# In[191]:


TotalGrades = 0
QuantityGrades = 0

for student in students:
    if len(student['pets']) == 0:
        TotalGrades += sum(student['grades'])
        QuantityGrades += len(student['grades'])
        AverageGrade = TotalGrades /  QuantityGrades
        

print(f'Sum Of Grades for all students {TotalGrades}')
print(f'Quantity of Grades for all students {QuantityGrades}')
print(f'Average of Grades for all students {AverageGrade}')


# In[192]:


#List Comprehension
GradesForAllStudentsWithoutPets = [student['grades'] for student in students if len(student['pets']) == 0]


# In[193]:


NewListGradesForAllStudentsWithoutPets = sum(GradesForAllStudentsWithoutPets, [])

SumOfGradesForAllStudentsWithoutPets = sum(NewListGradesForAllStudentsWithoutPets)
QuantityOfGradesForAllStudentsWithoutPets = len(NewListGradesForAllStudentsWithoutPets)
AverageGradesForAllStudentsWithoutPets =  SumOfGradesForAllStudentsWithoutPets / QuantityOfGradesForAllStudentsWithoutPets

print(f'Sum Of Grades for all students without pets {SumOfGradesForAllStudentsWithoutPets}')
print(f'Quantity of Grades for all students without pets {QuantityOfGradesForAllStudentsWithoutPets}')
print(f'Average of Grades for all students without pets {AverageGradesForAllStudentsWithoutPets}')


# Write a loop that adds one to every number in the list of numbers

# In[194]:


numbers = [5, 6, 7, 8, 9, 10]
number = numbers[0] + 1
number


# In[195]:


AddedNumbers = []

for number in numbers:
    number = number + 1
    AddedNumbers.append(number)
AddedNumbers


# In[196]:


AddedNumbers = [number + 1 for number in numbers]
AddedNumbers


# Created by [Ryan Orsinger](https://ryanorsinger.com)
# 
# Source code on [https://github.com/ryanorsinger/101-exercises](https://github.com/ryanorsinger/101-exercises)
