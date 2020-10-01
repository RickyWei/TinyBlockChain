from urllib.parse import urlparse
from uuid import uuid4

import Chain
import Node
import RSA


class BCNet:
    nodes_ = {}
    transactions_ = []
    tax_ = 0.01

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
        if ip in BCNet.nodes_.keys():
            return None
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

    def Mine(self, uid, db):
        node = BCNet.nodes_[uid]
        node.Mine(db)

    @staticmethod
    def NewTransaction(sender, receiver, amount, sign, db):
        # add a nre transaction to list of transactions
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'sign': sign
        }
        if BCNet.VerifyTransaction(transaction, db) == True:
            BCNet.UpdateDB(db, transaction)
            BCNet.transactions_.append(transaction)
            return True
        else:
            return False

    @staticmethod
    def VerifyTransaction(transaction, db):
        # check balance
        enough_balance = False
        balance = db.CheckBalance(transaction['sender'])
        enough_balance = balance > transaction['amount']*BCNet.tax_
        # check sign
        valid_sign = False
        pk = db.GetPK(transaction['sender'])
        valid_sign = RSA.RSA.Decipher(
            pk, transaction['sender'], transaction['sign'])
        if enough_balance and valid_sign:
            return True
        else:
            return False
        # print(transaction)
        # print(enough_balance)
        # print(valid_sign)
        # print(BCNet.transactions_)

    @staticmethod
    def UpdateDB(db, transaction):
        sender = transaction['sender']
        receiver = transaction['receiver']
        amount = transaction['amount']
        db.UpdateBalance(sender, -amount*(1+BCNet.tax_))
        db.UpdateBalance(receiver, amount)

    @staticmethod
    def Consistent():
        main_chain = []
        for nd in BCNet.nodes_.values():
            if len(nd.chain_) > len(main_chain):
                main_chain = nd.chain_
        for nd in BCNet.nodes_.values():
            nd.chain_ = main_chain


if __name__ == '__main__':
    pass
