#A data class is a class that is designed to only hold data values. 
# They aren't different from regular classes, but they usually don't have any other methods. 
# They are typically used to store information that will be passed between different parts of a program or a system.
#Type annotations — also known as type 
# signatures — are used to indicate the datatypes of variables and input/outputs of functions and methods.
from dataclasses import dataclass, field 
from typing import ClassVar 
import random
import string

@dataclass #Python dataclass decorator it modifies what is defined below. We modify class
class Point: #we define two fields (x, y) and give the type annotation
    x: int
    y: int 
#dataclass reads these fields and populates three   common methods we have to write on our own:
#__init__
#__repr__
#__eq__
#They (these methods) provide special functionalities to our Python classes
    
p1 = Point(1, 2)
p2 = Point(2, 1)

print(p1, p2)
print(p1 == p2)

#Second example

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass 
class InventoryItem:
    #Class for keeping track of an item in Inventory
    name: str
    unit_price: float
    quantity_on_hand: int = 2
    sizes: list[str] = field(default_factory=list)
    class_var: ClassVar[int] = 100 #we define a class variable
    id: str = field(default_factory=generate_id) #we define a default value
    
    def total_cost(self) -> float: #implement a method
        return self.unit_price * self.quantity_on_hand
 
def main() -> None:
    inventory = InventoryItem(name='Items', unit_price=2.05 )  
    return print(inventory)

main()

#help(InventoryItem) # it show the definition of my class

#Inheritance

@dataclass
class Rectangle:
    width: int
    length: int 
    
@dataclass
class ColoredRectangle(Rectangle):
    color: str 
    
rect = ColoredRectangle(10, 10, 'green')

print(rect.color)

