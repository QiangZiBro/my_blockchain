from flask import request,redirect,url_for,render_template,g,session
from blockchain.app import app
from blockchain.app.mod_blockchain.my_blockchain import blockchain

@app.route('/signin_sailer_index/getChain')
def getchain():
    responce={
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    blockchain.getchain()
    print(blockchain.chain)
    print(responce)
    return render_template('signin_sailer_index.html',chain=responce,index=blockchain.chain[1]['index'],transactions=blockchain.chain[1]['transactions'])