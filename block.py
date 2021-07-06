import time

from hashlib import sha256
from prettytable import PrettyTable


class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.data = data

    def __str__(self):
        t = PrettyTable(["field", "value"], align="l")
        t.add_row(["index", self.index])
        t.add_row(["previous_hash", self.previous_hash])
        t.add_row(["data", self.data])
        t.add_row(["timestamp", self.timestamp])
        t.add_row(["hash", self.get_hash()])
        return t.get_string()

    def get_hash(self):
        mushed_data = str(self.index) + self.previous_hash + str(self.timestamp) + self.data
        return sha256(mushed_data.encode()).hexdigest()
