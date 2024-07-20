#https://www.programiz.com/python-programming/polymorphism
#We can use the concept of polymorphism while creating class methods as Python allows
#different classes to have methods with the same name 
class Polygon: #We create a Polygon class
    #method to render a shape
    def render(self):
        print("Rendering Polygon..")
        
class Square(Polygon): #Square subclasses
    #Renders Square
    def render(self): #the purpose of this method is to render the shape
        print("Rendering Square...")
        
class Circle(Polygon): #Circle subclasses
    #renders Circle
    def render(self): #the purpose of this method is to render the shape
        print("Rendering circle...")
        
#create an object of Square
s1 = Square()
s1.render()

#Create an object of Circle
c1 = Circle()
c1.render()
#Create an object of Polygon
p1 =Polygon()
p1.render()

#The purpose of this method is to render the shape, 
#The process of rendering a square is different from the process of rendering a circle.
#Hence, the render() method behaves differently in different classes. Or, we can say render() is polymorphic.

#Second example
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am cat. My name is {self.name}. I am {self.age} years old.")
        
    def make_sound(self):
        print("Meow")
        
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old")
    
    def make_sound(self):
        print("Bark")
#We have two classes (Cat and Dog). They share a similar structure and have the same method names info() and make_sound()         
#We pack these two different objects into a tuple and iterate thourgh it suing a common animal variable.
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()