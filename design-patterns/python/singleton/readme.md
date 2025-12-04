# singleton is not a thing in Python - use global object pattern instead!
- https://python-patterns.guide/python/module-globals/

A “singleton” is a class instance that has been assigned a global name through The Global Object Pattern. For example, the official Python Programming FAQ answers the question “How do I share global variables across modules?” with the assertion that in Python “using a module is also the basis for implementing the Singleton design” — because not only can a module’s global namespace store constants (the FAQ’s example is x = 0 shared between several modules), but mutable class instances as well.

