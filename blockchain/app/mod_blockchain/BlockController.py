from flask import request, redirect, url_for, render_template, g, session
from blockchain.app import app
from blockchain.app.mod_blockchain.my_blockchain import blockchain


@app.route('/signin_sailer_index/getChain',methods=['POST', 'GET'])
def getchain():
    responce = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return render_template('home.html', name = responce)
    # return responce

