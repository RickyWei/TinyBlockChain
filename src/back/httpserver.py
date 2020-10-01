from flask import Flask, request, jsonify
import hashlib

import BCNet
import DB
import RSA

app = Flask(__name__)

bcnet = BCNet.BCNet()
db = DB.DB()


@app.route('/register/user', methods=['POST'])
def RegisterUser():
    info = request.get_json()
    user = info.get('user')
    passwd = info.get('passwd')
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


@app.route('/NewTransaction', methods=['POST'])
def NewTransaction():
    info = request.get_json()
    sender = info.get('sender')
    receiver = info.get('receiver')
    amount = info.get('amount')
    if db.HasUserSha(sender) and db.HasUserSha(receiver):
        sign = RSA.RSA.Cipher(sender)
        if bcnet.NewTransaction(sender, receiver, amount, sign):
            return info, 200
        else:
            return "wrong signature", 400
    else:
        return "no sender or receiver", 400


@app.route('/register/node', methods=['POST'])
def RegisterNode():
    info = request.get_json()
    owner = info.get('sha')
    ip = info.get('ip')
    if owner and ip:
        uid = bcnet.AddNode(owner, ip)
        rsps = {"uid": uid}
        return jsonify(rsps), 200
    else:
        return "error info", 400


@app.route('/mine', methods=['POST'])
def Mine():
    info = request.get_json()
    uid = info.get('uid')
    if uid != None:
        bcnet.Mine(uid, db)
    else:
        return "error uid", 400


@app.route('/getchain', methods=['GET', 'POST'])
def GetChain():
    return bcnet.GetChain()


if __name__ == '__main__':
    app.run(host="192.168.56.101", port=9999)
