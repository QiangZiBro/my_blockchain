# my_blockchain

环境配置

```bash
conda create -n blockchain_flask python=3.6
conda activate blockchain_flask
pip install -r requirements.txt
```


## 运行
-  运行方法1

用pycharm打开my_blockchain，进行下列配置，注：可能pycharm专业版才有此功能

![屏幕快照 2020-04-28 下午9.07.32](assets/屏幕快照 2020-04-28 下午9.07.32.png)



- 运行方法2
还没完成,代码引用需要调整
```
export FLASK_APP=app.py
flask run
```



## 手册
单个交易的数据结构
```python
'sales_time': time(),
# 卖家姓名
'seller_name': kargs['seller_name'],
# double 价格
'price': kargs['price'],
# 买家姓名
'buyer_name': kargs['receiver'],
# int交易数量
'amount': kargs['number'],
# 货物名称
'goods_name': kargs['goods_name']
```

区块的数据结构
> 注意第一块区块默认生成，为1
```python
# int
'index': len(self.chain) + 1,
# str
'previous_hash': previous_hash or self.hash(self.chain[-1]),
'timestamp': time(),
# 数组
'transactions': self.cur_transactions,
```

## 如何开始
`blockchain`是一个已经实例化的对象，其中chain属性就是整个区块链，所以演示的时候将里面的
数据显示出来就好


