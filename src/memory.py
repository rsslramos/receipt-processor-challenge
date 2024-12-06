from receipt import Receipt

class MemoryStore:
    _instance: 'MemoryStore | None' = None
    receipts: dict[str, Receipt] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.receipts = {}
        return cls._instance
