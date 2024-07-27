# PythonObjectOrientedProgramming

<br> **Object-oriented programming** (OOP) is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects. 
<br> In a Python, it is a programming paradigm that uses objects and classes in programming
<br> The main concept of object-oriented Programming (OOPs)  is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data.

It aims to implement real world entities and concepts in the programming such as:
- Class
- Object
- Inheritance - it allows to define a class that inherits all methods and properties from another class
- Polymorphism - it is the condition of occurrence in different forms. The same function name is being used for different types
- Encapsulation - it protects classes from accidental changes or deletions. It also promotes code reusability and maintainability


## Real world examples
<br> An object could represent a _person_ with **properties** like a name, age, and address and **behaviors** such as walking, talking, breathing, eating and running.
<br> What is more, it could represent an _email_ with **properties** like a recipient list, subject, and body and **behaviors** like adding attachments and sending.

<br>Therefore, **OOP** is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees or students and teachers.
<br>OOP models real-world entities as software objects that have some data associated with them and can perform certain operations.


### Definitions
<br> 1. **Classes** provide a means of bundling data and functionality together. A **class** is a collection of _objects_.
A **class** contains the blueprints or the prototype from which the objects are being created.
Creating a new **class** creates a new type of object. It allows new instances of that type to be made. 
Each **class instance** can have _attributes_ attached to it for maintaining its _state_.
**Class instances** can also have _methods_ (defined by its class) for modifying its _state_.
<br> 2. **Methods** - a function that is associated with a class
<br> 3. An **Object** is an element (or instance) of a class
<br> 4. An **Instance** is an object of the class
<br> 5. **Constructors** are generally used for instantiating an _object_. Initialize class attributes - a __init__ **method** in Python is used to *initialize* _objects_ of a _class_. 
<br> 6. **Class attributes** are class variables that are inherited by every object of a class. 
The value of **class attributes** remain the same for every new object.
<br> 7. **Class variables** are shared among all _instances_. They are useful for storing data that is shared among all _instances of a class_, such as constants or default values. Class variables should be the same for each instance
<br> 8. **Instance variables** can be unique for each instance such as names , email , pay. They are  used to store data that is _unique to each instance of a class_, such as object properties
<br> 9. **Regular (instance) methods** need a _class instance_ and can access the instance through self. They can read and modify an objects state freely. 
<br> 10. **Class methods** can access and modify class-level attributes. They have access to the class object and can modify class variables or create new instances of the class. **Class methods** are useful when you need to work with the class itself rather than any particular instance of it.
<br> 11. **Static methods**, on the other hand, do not have access to the class object and cannot modify any class-level attributes
<br> 12. **Decorators** are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. It allows us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
<br> 13. **@property** Decorator - is a built-in decorator for the property() function in Python. It is used to give "special" functionality to certain methods to make them act as _getters_, _setters_, or _deleters_ when we define properties in a class.

> [!IMPORTANT]
> <br> All steps and definitions are described and written in all Python scripts
> <br> This repo was created based on these sources:
> <br> [DataCamp Python OOP Tutorial](https://www.datacamp.com/tutorial/python-oop-tutorial)
> <br> [OOP FreeCodeCamp](https://www.freecodecamp.org/news/how-to-use-oop-in-python/)
> <br> [Python Class Variables](https://pynative.com/python-class-variables/)
> <br> [OOP Python GeeksforGeeks](https://www.geeksforgeeks.org/python-oops-concepts/)
> <br> [OOP Python](https://www.programiz.com/python-programming/object-oriented-programming)
> <br> [YouTube TutorialNeuralNine](https://www.youtube.com/@NeuralNine/playlists)
> <br> [Python OOP Tutorial Corey Schafer](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)


