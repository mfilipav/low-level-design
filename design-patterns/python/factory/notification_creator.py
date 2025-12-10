from abc import ABC, abstractmethod
from .notification import Notification


class NotificationCreator(ABC):
    """Creator - abstract class / interface using Factory Method Pattern.

    It doesn't know what notification it's sending but it knows how to send it.
    It defers the choice of notification type to its subclasses.
    """

    @abstractmethod
    def create_notification(self) -> Notification:
        """Factory method - to be implemented by concrete creators"""
        pass

    def send(self, message: str) -> None:
        """Common logic using the factory method"""
        notification = self.create_notification()
        notification.send(message)
