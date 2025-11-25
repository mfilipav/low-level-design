# LLD Intro
see https://algomaster.io/learn/lld/what-is-lld

### 1. Classes and Objects
  ```
    What are the key classes?
    What are their responsibilities?
    What data do they hold (attributes)?
    What operations do they perform (methods)?
  ```

### 2. Interfaces and Abstractions
Interfaces define contracts between components. They are critical to ensure loose coupling, allowing multiple components to interact without depending on each other's internal implementation details.

Ask yourself:
```
  What functionality should a class expose to the outside world?
  What details should remain hidden?
  Which parts of the system are likely to change or have multiple variations?
```

### 3. Relationships Between Classes
Classes don't exist in isolation. LLD defines these relationships clearly and precisely.

Key relationships include:

- **Association**: A general "uses-a" relationship. A Doctor uses a Stethoscope.
- **Aggregation** (Weak "has-a"): An object contains other objects, but they can exist independently. A Department has Professors. If the department is closed, the professors still exist.
- **Composition** (Strong "has-a"): An object is composed of other objects, and their lifecycles are tied. A House is composed of Rooms. If you demolish the house, the rooms are destroyed with it.
- **Inheritance** ("is-a"): A class inherits properties and behaviors from a parent. A Car is a Vehicle.

### 4. Method Signatures
Once your classes and relationships are defined, the next step is deciding how they behave using methods. A well-designed method signature is self-documenting and intuitive.

You’ll need to decide:
```
  What methods should each class expose?
  What are the method's input parameters, and return types?
  Should the method be public, private, or protected?
  What exceptions might they throw?
  Is it synchronous or asynchronous?
```

### 5. Design Patterns
LLD is also the stage where you apply proven solutions to common design problems using design patterns. These patterns provide reusable templates that bring structure, robustness, and maintainability to your code.

Some commonly used patterns in LLD include:
```
Singleton: useful when you need exactly one instance of a class across your system.
Factory: useful when you want to delegate object creation without exposing the instantiation details to the client.
Strategy: useful when you need to switch between multiple algorithms or behaviors at runtime.
Observer: useful for event-driven systems where you need to establish a publisher–subscriber relationship between objects.
Decorator: useful when you want to add new behavior to objects without altering existing code.
Adapter: useful when you need to bridge incompatible interfaces to work together.
Facade: useful when you want to provide a simplified interface to a complex subsystem.
```
