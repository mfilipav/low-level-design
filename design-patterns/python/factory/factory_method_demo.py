from .email_notification_creator import EmailNotificationCreator
from .sms_notification_creator import SMSNotificationCreator
from .push_notification_creator import PushNotificationCreator
from .simple_notification_factory import SimpleNotificationFactory
from .notification_service_naive import NotificationServiceNaive


def simple_factory_demo():
    """Demonstrate Simple Factory Pattern. Half good solution.

    Problem with Simple Factory: hardcoding the decision logic
    and centralizing creation in one place!
    Solution: need to give each type of notification its own responsibility
    for knowing how to create itself.
    """
    print("\n=== Simple Factory Pattern Demo ===")

    factory = SimpleNotificationFactory()

    email_notification = factory.create_notification("EMAIL")
    email_notification.send("Welcome via Simple Factory!")

    sms_notification = factory.create_notification("SMS")
    sms_notification.send("OTP via Simple Factory: 789012")

    push_notification = factory.create_notification("PUSH")
    push_notification.send("Push via Simple Factory!")


def factory_method_demo():
    """Demonstrate Factory Method Pattern -- excellent solution.

    Factory Method Pattern takes the idea of object creation and
    hands it off to subclasses.
    Instead of one central factory deciding what to create,
    you delegate the responsibility to specialized classes
    that know exactly what they need to produce.
    Creators know how to send notifications.
    """
    print("\n=== Factory Method Pattern Demo ===")

    # Send Email
    creator = EmailNotificationCreator()
    creator.send("Welcome to our platform!")

    # Send SMS
    creator = SMSNotificationCreator()
    creator.send("Your OTP is 123456")

    # Send Push Notification
    creator = PushNotificationCreator()
    creator.send("You have a new follower!")


def naive_implementation_demo():
    """Demonstrate naive implementation (anti-pattern)"""
    print("\n=== Naive Implementation Demo ===")

    service = NotificationServiceNaive()
    service.send_notification("EMAIL", "Email via naive service")
    service.send_notification("SMS", "SMS via naive service")
    service.send_notification("PUSH", "Push via naive service")


if __name__ == "__main__":
    simple_factory_demo()
    factory_method_demo()
    naive_implementation_demo()
