from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

import BCNet
import DB
import RSA

app = Flask(__name__)
CORS(app)

bcnet = BCNet.BCNet()
db = DB.DB()


@app.route('/register/user', methods=['POST'])
def RegisterUser():
    info = request.get_json()
    user = info.get('user')
    passwd = info.get('passwd')
    print(user, passwd)
    if db.HasUser(user) == True:
        return "User has existed", 400
    else:
        sha = hashlib.sha256((user+passwd).encode()).hexdigest()
        sk, pk = RSA.RSA.GenerateSKPK()

        if db.AddUser(user, passwd, sha, sk, pk) == True:
            rsps = {"sha": sha,
                    "sk": sk,
                    "pk": pk,
                    }
            return jsonify(rsps), 200
        else:
            rsps = {"sha": sha,
                    "sk": sk,
                    "pk": pk,
                    }
            return jsonify(rsps), 500


@app.route('/login', methods=['POST'])
def Login():
    info = request.get_json()
    user = info.get('user')
    passwd = info.get('passwd')
    # print(user, passwd)
    sha = db.Login(user, passwd)
    if sha != None:
        rsps = {"sha": sha}
        return jsonify(rsps), 200
    else:
        return "Wrong username or password", 400


@app.route('/checkbalance', methods=['POST'])
def CheckBalance():
    info = request.get_json()
    sha = info.get("sha")
    if sha != None:
        balance = db.CheckBalance(sha)
        if balance != None:
            rsps = {"balance": balance}
            return jsonify(rsps), 200
        else:
            return "error sha", 400


@app.route('/transaction', methods=['POST'])
def NewTransaction():
    info = request.get_json()
    sender = info.get('sender')
    receiver = info.get('receiver')
    amount = float(info.get('amount'))
    print(sender, "\n", receiver)
    if db.HasUserSha(sender) and db.HasUserSha(receiver):
        sk = db.GetSK(sender)
        sign = RSA.RSA.Cipher(sk, sender)
        if bcnet.NewTransaction(sender, receiver, amount, sign, db):
            return info, 200
        else:
            return "wrong signature", 400
    else:
        return "no sender or receiver", 400


@app.route('/alltransaction', methods=['GET'])
def GetAllTransaction():
    return jsonify(db.GetAllTransaction()), 200


@app.route('/register/node', methods=['POST'])
def RegisterNode():
    info = request.get_json()
    owner = info.get('sha')
    ip = info.get('ip')
    if owner and ip:
        uid = bcnet.AddNode(owner, ip)
        if uid != None:
            rsps = {"uid": uid}
            return jsonify(rsps), 200
        else:
            return "Node has been registered", 400
    else:
        return "error info", 400


@app.route('/mine', methods=['POST'])
def Mine():
    info = request.get_json()
    uid = info.get('uid')
    if uid != None:
        bcnet.Mine(uid, db)
        return "mine successfully", 200
    else:
        return "error uid", 400


@app.route('/getchain', methods=['GET', 'POST'])
def GetChain():
    return bcnet.GetChain(), 200


if __name__ == '__main__':
    app.run(host="192.168.56.101", port=9999)
