#https://www.programiz.com/python-programming/object-oriented-programming
#https://www.datacamp.com/tutorial/encapsulation-in-python-object-oriented-programming
# Encapsulation is a fundamental object-oriented principle in Python. 
# It protects your classes from accidental changes or deletions and promotes code reusability and maintainability.
class Computer:
    
    def __init__(self): #we use this method to store the maximum selling price of Computer
        self.__maxprice = 900  #we define a private variable
        
    def sell(self):
        print("Selling Price : {}".format(self.__maxprice))
        
    def setMaxPrice(self, price):
        self.__maxprice = price 
        
        
c = Computer()
c.sell()

# change the price 
#We try to modify the value of __maxprice outside of the class. this modification is not seen on the output because __maxprice is a private variable
c.__maxprice = 1500
c.sell()

#Using setter function which takes price as a parameter to change the value
c.setMaxPrice(1000)
c.sell()


#Second example:


class Person:
    def __init__(self, name, age, gender):
        #defining a private attribute due to two underscores __
        self.__name = name
        self.__age = age
        self.__gender = gender
     
    @property    
    def Name(self):
        return self.__name
    
    @Name.setter #we create a setter thanks to this, we can control it
    def Name(self, value):
        if value =="Lukasz":
            self.__name = "Default Name"
        else:
            self.__name = value    
            
    
    
        
#1.It does not work, because we have a private attribute and the attribute name is automatically mangled to prevent accidental access      
#p1 = Person('Lukasz', 15, 'Male')
#print(p1.__name)
#p1.__name = 'Adam'   
  
#2.After creating properties
#We can create propreties to allows us to manipulate these values  through properties getters and setters for example.

p1 = Person("Mike", 20, "n") 
print(p1.Name)
#We can change this name to Bob

p1.Name = "Bob"
print(p1.Name)

#Using condition
p1.Name = "Lukasz"
print(p1.Name)

