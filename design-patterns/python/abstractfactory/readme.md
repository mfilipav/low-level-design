# verdict: not pythonic

The Abstract Factory is an awkward workaround for the lack of first-class functions and classes in less powerful programming languages. It is a poor fit for Python, where we can instead simply pass a class or a factory function when a library needs to create objects on our behalf.


## pythonic approach: callable factories
see https://python-patterns.guide/gang-of-four/abstract-factory/
