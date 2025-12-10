from abc import ABC, abstractmethod


class Notification(ABC):
    """Product interface. An interface or abstract class for
    the objects the factory method creates.
    """

    @abstractmethod
    def send(self, message: str) -> None:
        pass
