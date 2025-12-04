class EagerSingleton:
    """Eager initialization singleton - instance created at class loading time.
    This implementation is one of the simplest and inherently thread-safe
    without needing explicit synchronization.
"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        print("EagerSingleton instance created")
        self._initialized = True

    def get_message(self) -> str:
        return "Hello from EagerSingleton!"


if __name__ == "__main__":
    singleton1 = EagerSingleton()
    singleton2 = EagerSingleton()

    print(singleton1.get_message())
    print(singleton2.get_message())
    print(f"Are both instances the same? {'Yes' if singleton1 is singleton2 else 'No'}")
