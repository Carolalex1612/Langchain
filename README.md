# Object-Oriented Programming (OOP)

## 1. Class
- User-defined template for creating objects.
- Bundles data and functions together, making it easier to manage and use them.
- Created using the `class` keyword.
- **Attributes** are variables defined inside the class and represent the properties of the class.  
- Attributes can be accessed using the dot (`.`) operator (e.g., `MyClass.my_attribute`).

## 2. Object
- Instance of a **Class**.
- Represents a specific implementation of the class and holds its own data.
- `__init__()` function automatically initializes object attributes when an object is created.

### Self Parameter
- `self` parameter is a reference to the current instance of the class.
- It allows access to the attributes and methods of the object.

## 3. Inheritance
### Types of Inheritance:
- **Single Inheritance**: A child class inherits from a single parent class.
- **Multiple Inheritance**: A child class inherits from more than one parent class.
- **Multilevel Inheritance**: A child class inherits from a parent class, which in turn inherits from another class.
- **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.
- **Hybrid Inheritance**: A combination of two or more types of inheritance.

## 4. Polymorphism
Polymorphism allows methods to have the same name but behave differently based on the object’s context. It can be achieved through **method overriding** or **overloading**.

### Types of Polymorphism:
- **Compile-Time Polymorphism**:  
  - Determined during compilation.  
  - Allows methods or operators with the same name to behave differently based on input parameters or usage.  
  - Commonly referred to as **method overloading** or **operator overloading**.
- **Run-Time Polymorphism**:  
  - Determined during program execution.  
  - Occurs when a subclass provides a specific implementation for a method already defined in its parent class (**method overriding**).

## 5. Encapsulation
Encapsulation is the bundling of **data (attributes) and methods (functions)** within a class, restricting access to some components to control interactions.

- A class is an example of encapsulation as it encapsulates all **data members, functions, variables, etc.**

### Types of Encapsulation:
- **Public Members**: Accessible from anywhere.
- **Protected Members**: Accessible within the class and its subclasses.
- **Private Members**: Accessible only within the class.

## 6. Data Abstraction
Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on **“what to do”** rather than **“how to do it.”**

### Types of Abstraction:
- **Partial Abstraction**: Abstract class contains both abstract and concrete methods.
- **Full Abstraction**: Abstract class contains only abstract methods (like interfaces).
