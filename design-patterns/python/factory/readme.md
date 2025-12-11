## python-patterns verdict: not good
### alternative: dependency injection
https://python-patterns.guide/gang-of-four/factory-method/

Does the class you’re designing really need to go around creating other classes?

If you know up front all the objects that the class will need, you should consider providing them to the class yourself through Dependency Injection.

### alternative: class attribute factory
https://python-patterns.guide/gang-of-four/factory-method/#instead-use-a-class-attribute-factory

### alternative: instance attribute factory
https://python-patterns.guide/gang-of-four/factory-method/#instead-use-an-instance-attribute-factory

Better than class attr factory -- because why should you have to subclass an object merely to customize its behavior?!

### alternative: object factory
https://realpython.com/factory-method-python/


## relations to other patterns
Comparison to other factory methods: https://refactoring.guru/design-patterns/factory-comparison

Many designs start by using Factory Method (less complicated and more customizable via subclasses) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, but more complicated).

Abstract Factory classes are often based on a set of Factory Methods, but you can also use Prototype to compose the methods on these classes.

You can use Factory Method along with Iterator to let collection subclasses return different types of iterators that are compatible with the collections.

Prototype isn’t based on inheritance, so it doesn’t have its drawbacks. On the other hand, Prototype requires a complicated initialization of the cloned object. Factory Method is based on inheritance but doesn’t require an initialization step.

Factory Method is a specialization of Template Method. At the same time, a Factory Method may serve as a step in a large Template Method.

