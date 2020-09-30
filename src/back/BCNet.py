from urllib.parse import urlparse

import Chain
import Node


class BCNet:
    nodes_ = set()
    transactions_ = []

    def __init__(self):
        super().__init__()
        # genesis block
        self.node_ = Node.Node("0", "127.0.0.1:10000", Chain.Chain())
        self.node_.chain_.AddBlock(0)

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
        BCNet.nodes_.add(new_node)

    @staticmethod
    def NewTransaction(sender, receiver, amount):
        # add a nre transaction to list of transactions
        transaction = {
            'sender': sender,
            'reveiver': receiver,
            'amount': amount,
        }
        BCNet.transactions_.append(transaction)

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
