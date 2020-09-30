import time
import json
import hashlib


class Block:
    def __init__(self, pre_hash, index, proof, transactions):
        # init
        super().__init__()
        self.pre_hash_ = pre_hash
        self.index_ = index
        self.timestamp_ = time.time()
        self.proof_ = proof
        self.transactions_ = transactions

    @staticmethod
    def Hash(block):
        # hash a block
        block = json.dumps(block, sort_keys=True).encode()
        hashval = hashlib.sha256(block).hexdigest
        return hashval


if __name__ == '__main__':
    pass
