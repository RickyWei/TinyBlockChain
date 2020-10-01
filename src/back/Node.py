import hashlib

import Chain
import BCNet


class Node:
    def __init__(self, owner, ip, chain):
        super().__init__()
        self.owner_ = owner
        self.ip_ = ip
        self.chain_ = chain

    def Mine(self):
        proof = POW()
        amount = 128
        BCNet.BCNet.NewTransaction("0x0", self.owner_, amount)
        self.chain_.AddBlock(proof)
        self.chain_.GetLastBlock().transactions_ = BCNet.transactions_
        BCNet.BCNet.transactions_.clear()
        BCNet.BCNet.Consistent()

    def POW(self):
        last_block = self.chain_.GetLastBlock()
        last_proof = last_block.proof
        proof = 0
        while Node.ValidProof(last_proof, proof) == False:
            proof += 1
        return proof

    @staticmethod
    def ValidProof(self, last_proof, proof):
        difficulty = 4
        proof = f'{last_proof}{proof}'.encode()
        hashval = hashlib.sha256(proof).hexdigest()
        if hashval[:difficulty] == "0"*difficulty:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
