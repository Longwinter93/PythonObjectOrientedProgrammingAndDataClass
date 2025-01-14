#!/usr/bin/env python
# coding: utf-8

# In[1]:


country_capitals = {
    'United States': 'Washington D.C',
    'Italy': 'Rome'
}

print(country_capitals)
# print dictionary keys one by one 

for country in country_capitals:
    print(country)
    
print()

# print dictionary values one by one 

for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
    
print()    

for key, values in country_capitals.items():
    print(key, values)


# In[2]:


#https://docs.python.org/3/library/re.html
import re 
text = 'lukasz'

a = re.compile('^l')
b = a.sub(r'',text)

print(b)


# In[3]:


#https://docs.python.org/3/library/collections.html#collections.Counter
# Total occurrences of words in a list 
from collections import Counter 
cnt = Counter()

words = ['red', 'blue', 'red', 'green', 'blue', 'blue']

for word in words:
    cnt[word] += 1

cnt



# In[4]:


print(Counter(words))


# In[5]:


#Explaining all functions  and libraries that are used here and learn it!
#https://docs.python.org/3/library/re.html
#https://www.programiz.com/python-programming/regex
#https://www.w3schools.com/python/python_regex.asp

