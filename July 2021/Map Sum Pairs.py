class MapSum:
    def __init__(self):
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        s = 0
        for key, value in self.map.items():
            if key.startswith(prefix):
                s += value
        return s  
