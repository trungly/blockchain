import re

from block import Block
from prettytable import PrettyTable


class Chain:
    def __init__(self):
        genesis_block = Block(0, "n/a", "Initial data in Genesis block")
        self._chain = [genesis_block]

    def __str__(self):
        s = "Chain:\n"
        for block in self._chain:
            s += "\n" + "🔗" + "\n" + str(block)
        return s

    def height(self):
        return len(self._chain)

    def block(self, index):
        return self._chain[index]

    def add_block_with_data(self, data):
        nonce = 1
        while True:
            if nonce == 1:
                data += ":Nonce:1"
            else:
                data = re.sub(r":Nonce:\d+", ":Nonce:" + str(nonce), data)
            nonce += 1

            b = Block(self.height(), self.block(-1).get_hash(), data)
            if b.get_hash().startswith('0'):
                self._chain.append(b)
                break

    def is_valid(self):
        """
        Start with the last block and verify that the chain of hashes matches up
        """
        index = self.height() - 1
        while index > 0:
            curr = self.block(index)
            prev = self.block(index - 1)
            if curr.previous_hash != prev.get_hash():
                print("Houston, we have a problem!")
                print(f"Block {index}'s previous_hash does not equal Block {index-1}'s hash")
                t = PrettyTable(["field", "value"], align="l")
                t.add_row([f"Block {index}'s prev_hash", curr.previous_hash])
                t.add_row([f"Block {index-1}'s hash", prev.get_hash()])
                print(t)
                return False
            index -= 1
        return True
