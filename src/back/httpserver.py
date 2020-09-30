from flask import Flask
import hashlib

import BCNet
import DB

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
        db.AddUser(user, passwd, hashlib.sha256(user+passwd))
        return "Register successfully", 200


@app.route('/login', methods=['POST'])
def Login():
    info = request.get_json()
    user = info.get('user')
    passwd = info.get('passwd')
    if db.Login() == True:
        return "Login successfully", 200
    else:
        return "Wrong username or password", 400


@app.route('/register/node', methods=['POST'])
def RegisterNode():
    info = request.get_json()
    owner = info.get('owner')
    ip = info.get('owner')
    if owner and ip:
        bcnet.AddNode(owner, ip)
    else:
        return "error info", 400


if __name__ == '__main__':
    app.run(host="localhost", port=9999)
