from .notification import Notification
from .email_notification import EmailNotification
from .sms_notification import SMSNotification
from .push_notification import PushNotification


class SimpleNotificationFactory:
    """Simple Factory Pattern.
    Notification Factory has one job: centralize and encapsulate object
    creation. As such, the notification service no longer needs to know
    which concrete class to instantiate. It simply asks the factory for
    the right type of notification.
    Problem with Simple Factory: hardcoding the decision logic
    and centralizing creation in one place!
    Solution: need to give each type of notification its own responsibility
    for knowing how to create itself.
    """

    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        notification_type = notification_type.upper()

        if notification_type == "EMAIL":
            return EmailNotification()
        elif notification_type == "SMS":
            return SMSNotification()
        elif notification_type == "PUSH":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
