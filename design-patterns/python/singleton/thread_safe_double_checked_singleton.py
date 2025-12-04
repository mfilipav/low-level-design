import threading


class DoubleCheckedSingleton:
    """Double-checked locking singleton pattern.
    This approach minimizes performance overhead from synchronization
    by only synchronizing when the object is first created.
"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        # First check (without locking)
        if cls._instance is None:
            with cls._lock:
                # Second check (with locking)
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print("DoubleCheckedSingleton instance created")
        return cls._instance

    def get_message(self) -> str:
        return "Hello from DoubleCheckedSingleton!"
