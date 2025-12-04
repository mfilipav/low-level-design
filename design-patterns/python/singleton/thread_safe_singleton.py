import threading


class ThreadSafeSingleton:
    """Thread-safe singleton using lock"""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    print("ThreadSafeSingleton instance created")
        return cls._instance

    def get_message(self) -> str:
        return "Hello from ThreadSafeSingleton!"


if __name__ == "__main__":
    singleton1 = ThreadSafeSingleton()
    singleton2 = ThreadSafeSingleton()

    print(singleton1.get_message())
    print(singleton2.get_message())
    print(f"Are both instances the same? {'Yes' if singleton1 is singleton2 else 'No'}")
