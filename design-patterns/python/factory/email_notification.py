from .notification import Notification


class EmailNotification(Notification):
    """Concrete Product. Concrete classes that implement the
    Product (aka Notification) interface.
    """

    def send(self, message: str) -> None:
        print(f"Sending email: {message}")
