# OOP Fundamentals

## Classes and Objects
### 1. What is a Class?

A class is a blueprint, template, or recipe for creating objects. It defines what an object will contain (its data) and what it will be able to do (its behavior).

A **class is not an object itself**, it’s a template used to create many objects with similar structure but independent state.

```python
class Car:
    # Constructor
    def __init__(self, brand, model):
        # Attributes (private by convention with underscore)
        self._brand = brand
        self._model = model
        self._speed = 0

    # Method to accelerate
    def accelerate(self, increment):
        self._speed += increment

    # Method to display info
    def display_status(self):
        print(f"{self._brand} is running at {self._speed} km/h.")
```

### 2. What is an Object?
An object is an **instance of a class**.
It’s a real-world manifestation of the class blueprint, something you can interact with, store data in, and invoke methods on.

When you create an object, you’re essentially saying:

“Take this blueprint (class) and build one actual thing (object) out of it.”

Each object:
```
Has its own copy of the data defined in the class.
Shares the same structure and behavior as defined by the class.
Operates independently of other objects.
```


## Enums
```python
from enum import Enum

# Simple Enum
class OrderStatus(Enum):
    PLACED = "PLACED"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
```


## Interfaces: `what` a component should do, not `how`
See https://algomaster.io/learn/lld/interfaces

In object-oriented design, interfaces play a foundational role in building systems that are extensible, testable, and loosely coupled.

**An interface defines "what" the component should do, while classes implement the "how".**

This separation of **definition** and **implementation** allows different parts of your system to work together through **well-defined contracts**, without needing to know each other’s internal details.


### Interface example
Consider a remote control. It exposes a standard set of buttons:
```
play()
pause()
volumeUp()
powerOff()
```

The person using the remote doesn’t care if it controls a TV, a soundbar, or a projector, they all understand the same set of commands.


The `remote` is the `interface`. The `devices` (TV, soundbar, projector) are the `implementations`.

Each device behaves differently when you press play(), but the contract remains consistent.

### Loose Coupling with Interface Injection
`StripePayment` implements `PaymentGateway` interface. Both StripePayment and RazorpayPayment implement the same interface, but the actual logic for processing the payment is different.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass

class StripePayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Stripe: ${amount}")

class RazorpayPayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Razorpay: ₹{amount}")
```

Now let’s say you have a `CheckoutService` that processes payments. Instead of hardcoding a specific payment gateway, you inject the interface:

```python
class CheckoutService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)
```

Notice that CheckoutService **depends only on the interface, not the implementation**. This makes it easy to swap or extend payment providers without changing the checkout logic.

Now you can plug in any payment gateway at runtime:
```python
if __name__ == "__main__":
    stripe_gateway = StripePayment()
    checkout_service = CheckoutService(stripe_gateway)
    checkout_service.checkout(120.50)  # Output: Processing payment via Stripe: $120.5
    
    # Switch to Razorpay
    razorpay_gateway = RazorpayPayment()
    checkout_service.set_payment_gateway(razorpay_gateway)
    checkout_service.checkout(150.50)  # Output: Processing payment via Razorpay: ₹150.5
```

