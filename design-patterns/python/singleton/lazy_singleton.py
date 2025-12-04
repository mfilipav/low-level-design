class LazySingleton:
    """Lazy initialization singleton - not thread-safe"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("LazySingleton instance created")
        return cls._instance

    def get_message(self) -> str:
        return "Hello from LazySingleton!"


# alternative:
"""
class LazySingleton:
    _instance = None

    def __init__(self):
        if LazySingleton._instance is not None:
            raise Exception("Use get_instance() instead.")

    @staticmethod
    def get_instance():
        if LazySingleton._instance is None:
            LazySingleton._instance = LazySingleton()
        return LazySingleton._instance
"""
