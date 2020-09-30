from flask import Flask

import BCNet

app = Flask(__name__)

bcnet = BCNet()


@app.route('/register/node', methods=['POST'])
def RegisterNode():
    info = request.get_json()
    owner = info.get('owner')
    ip = info.get('owner')
    if owner and ip:
        bcnet.AddNode(owner, ip)
    else:
        return "error info", 400
