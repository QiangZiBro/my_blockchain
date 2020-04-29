from blockchain.app import app
from flask import Flask, render_template, g, session, request
from blockchain.app.mod_mysql.mysql_service import Mysql_service
from blockchain.app.mod_qrcode import QrcodeController
from blockchain.app.mod_blockchain.my_blockchain import blockchain


# 发布页面
@app.route('/signin_sailer_goods', methods=['POST', 'GET'])
def signin_sailer_goods():
    return render_template('signin_sailer_goods.html')


# 发布的结果
@app.route('/sigin_sailer_goods_result', methods=['GET', 'POST'])
def save_sail_goods():
    print(request.method)
    if request.method == 'GET':
        return render_template('signin_sailer_goods.html')
    else:
        print("saving")
        goodname = request.form['goodname']
        goodnumber = request.form['goodnumber']
        price = request.form['price']
        receiver = request.form['receiver']
        print(goodname, goodnumber, price, receiver)
        # 做一些数据判断
        pass  # 暂略
        # TODO 把货物存到数据库里
        blockchain.new_transaction(seller_name=session["username"], price=price, receiver=receiver, number=goodnumber, goods_name=goodnumber) #TODO
        return render_template('signin_sailer_goods.html')


# 物流
@app.route('/signin_sailer_trans')
def signin_sailer_trans():
    return render_template('signin_sailer_trans.html')


# 交易
@app.route('/signin_sailer_sails')
def signin_sailer_sails():
    path = QrcodeController.create_qrcode()
    return render_template('signin_sailer_sails.html', qrcode=path)


# 申诉
@app.route('/signin_sailer_system')
def signin_sailer_system():
    username = session['username']
    mysql = Mysql_service()
    [name, password, role, email, address, account, credit] = mysql.getUserInfoByUsername(username)
    return render_template('signin_sailer_system.html', username=username, credit=credit)
