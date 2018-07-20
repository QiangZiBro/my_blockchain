from flask import request,redirect,url_for,render_template,g,session
from blockchain.app.mod_mysql.mysql_service import Mysql_service
from blockchain.app import app

# 主要用于注册
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        # add into the mysql
        mysql=Mysql_service()
        mysql.register(username,password,email,role)
        return redirect(url_for('login'))

# 主要用于登录
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        mysql = Mysql_service()
        name, real_pass, role, email, address, account, credit=mysql.getUserInfoByUsername(username)
        if password == real_pass:
            print(role)
            if role == 'Product':
                session['username'] = name
                return render_template('signin_sailer_index.html',username=name,email=email,address=address)
            if role == 'Transport':
                session['username'] = name
                return render_template('signin_trans_index.html',username=name,email=email,address=address)
            if role == 'Sale':
                session['username'] = name
                return render_template('signin_custs_index.html',username=name,email=email,address=address)
        else:
            print("======登录失败======")
            # 这里还没有考虑怎么样的返回界面
            return render_template('sign_in.html', res="fail")


# 主要用于修改个人信息
@app.route('/signin_sailer_index',methods=['POST','GET'])
def change_1():
    if request.method == 'GET':
        return render_template('signin_sailer_index.html')
    else:
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        # 不同的身份返回不同的界面所以要进行判断
        role = request.form['role']
        # 修改个人信息，这个界面只有在刚刚登陆成功之后才能成功运行，没有留有借口进行返回
        mysql = Mysql_service()
        mysql.modify_user_info(username=username,email=email,address=address)
        print("======成功修改======")
        if role == 'Product':
            return render_template('signin_sailer_index.html',username=username,email=email,address=address)



@app.route('/signin_trans_index',methods=['POST','GET'])
def change_2():
    if request.method == 'GET':
        return render_template('signin_trans_index.html')
    else:
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        # 不同的身份返回不同的界面所以要进行判断
        role = request.form['role']
        # 修改个人信息，这个界面只有在刚刚登陆成功之后才能成功运行，没有留有借口进行返回
        mysql = Mysql_service()
        mysql.modify_user_info(username=username,email=email,address=address)
        print("======成功修改======")
        if role == 'Transport':
            return render_template('signin_trans_index.html',username=username,email=email,address=address)

@app.route('/signin_custs_index',methods=['POST','GET'])
def change_3():
    if request.method == 'GET':
        return render_template('signin_trans_index.html')
    else:
        username = request.form['username']
        email = request.form['email']
        address = request.form['address']
        # 不同的身份返回不同的界面所以要进行判断
        role = request.form['role']
        # 修改个人信息，这个界面只有在刚刚登陆成功之后才能成功运行，没有留有借口进行返回
        mysql = Mysql_service()
        mysql.modify_user_info(username=username,email=email,address=address)
        print("======成功修改======")
        if role == 'Sale':
            return render_template('signin_custs_index.html',username=username,email=email,address=address)
