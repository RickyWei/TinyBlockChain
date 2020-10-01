from urllib.parse import urlparse
from uuid import uuid4

import Chain
import Node


class BCNet:
    nodes_ = {}
    transactions_ = []
    fee_rate_ = 0.01

    def __init__(self):
        super().__init__()
        # genesis block
        self.node_ = Node.Node("0", "127.0.0.1:10000", Chain.Chain())
        self.node_.chain_.AddBlock(0)
        self.uid_ = str(uuid4())
        BCNet.nodes_[self.uid_] = self.node_

    def AddNode(self, owner, ip):
        ip = urlparse(ip)
        if ip.netloc:
            ip = ip.netloc
        elif ip.path:
            ip = ip.path
        else:
            raise ValueError('Invalid ip')
        chain = self.node_.chain_
        new_node = Node.Node(owner, ip, chain)
        uid = uuid4()
        uid = str(uid)
        BCNet.nodes_[uid] = new_node
        return uid

    def GetChain(self):
        if len(BCNet.nodes_) < 0:
            return {}
        else:
            chain = BCNet.nodes_[self.uid_].chain_.GetChain()
            return chain

    def Mine(self, uid):
        node = BCNet.nodes_[uid]
        node.Mine()

    @staticmethod
    def NewTransaction(sender, receiver, amount):
        # add a nre transaction to list of transactions
        transaction = {
            'sender': sender,
            'reveiver': receiver,
            'amount': amount,
        }
        if CheckDB == True:
            BCNet.transactions_.append(transaction)
            return True
        else:
            return False

    @staticmethod
    def CheckDB(db, transaction):
        balance = db.CheckBalance(transaction['sender'])
        if balance > transaction['amount']*BCNet.fee_rate_:
            return True
        else:
            return False

    @staticmethod
    def UpdateDB(db):
        pass

    @staticmethod
    def Coinsistent(bcnet):
        main_chain = []
        for nd in bcnet.nodes_:
            if len(nd.chain_) > len(main_chain):
                main_chain = nd.chain_
        for nd in bcnet.nodes_:
            nd.chain_ = main_chain


if __name__ == '__main__':
    pass
