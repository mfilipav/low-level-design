from .notification_creator import NotificationCreator
from .email_notification import EmailNotification
from .notification import Notification


class EmailNotificationCreator(NotificationCreator):
    """Concrete Creator, a subclass that extends the abstract creator to
    return an instance of a specific ConcreteProduct (EmailNotification).
    """

    def create_notification(self) -> Notification:
        return EmailNotification()
