import hashlib

import Chain
import BCNet
import RSA


class Node:
    def __init__(self, owner, ip, chain):
        super().__init__()
        self.owner_ = owner
        self.ip_ = ip
        self.chain_ = chain

    def Mine(self, db):
        proof = self.POW()
        amount = 128
        sha = db.GetSHA("0x0")
        sk = db.GetSK(sha)
        sign = RSA.RSA.Cipher(sk, sha)
        BCNet.BCNet.NewTransaction(sha, self.owner_, amount, sign, db)
        self.chain_.AddBlock(proof)
        self.chain_.GetLastBlock().transactions_ = BCNet.BCNet.transactions_.copy()
        BCNet.BCNet.transactions_.clear()
        BCNet.BCNet.Consistent()

    def POW(self):
        last_block = self.chain_.GetLastBlock()
        last_proof = last_block.proof_
        proof = 0
        while Node.ValidProof(last_proof, proof) == False:
            proof += 1
        return proof

    @staticmethod
    def ValidProof(last_proof, proof):
        difficulty = 4
        proof = f'{last_proof}{proof}'.encode()
        hashval = hashlib.sha256(proof).hexdigest()
        if hashval[:difficulty] == "0"*difficulty:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
