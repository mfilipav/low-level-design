from abc import ABC, abstractmethod


class EnemyPrototype(ABC):
    """Prototype interface for enemy cloning"""

    @abstractmethod
    def clone(self) -> "EnemyPrototype":
        pass
