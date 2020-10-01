import json

import Block
import BCNet


class Chain:
    def __init__(self):
        # init
        super().__init__()
        self.chain_ = []

    def AddBlock(self, proof):
        # create a new block and add it to chain
        pre_hash = 0
        if len(self.chain_) > 0:
            pew_hash = hash(self.chain_[-1])
        index = len(self.chain_)
        transactions = []
        new_block = Block.Block(pre_hash, index, proof, transactions)
        self.chain_.append(new_block)

    def GetChain(self):
        chain = json.dumps(
            obj=self.chain_, default=lambda x: x.__dict__, sort_keys=False)
        return chain

    def GetLastBlock(self):
        # get last block
        if len(self.chain_) > 0:
            return self.chain_[-1]
        else:
            return None

    @staticmethod
    def ValidChain(chain):
        # check if chain is valid
        last_block = chain[0]
        for i in len(chain):
            cur_block = chain[i]

            # check hash
            last_block_hash = Block.Hash(last_block)
            if cur_block.pre_hash != last_block_hash:
                return False

            # check pow
            if not Node.Node.ValidProof(last_block.proof, cur_block.proof):
                return False

            last_block = cur_block
        return True


if __name__ == '__main__':
    pass
