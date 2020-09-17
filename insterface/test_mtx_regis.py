'''
192.168.2.221
案例：请求码同学商城注册接口
'/mtx/index.php?s=/index/user/reg.html'
{'accounts': username, 'pwd': 123456, 'type': 'username', 'is_agree_agreement':1}
s_user
#python数据库交互  mysql关系型数据库---pymysql  交互模式
pip install pymysql
# mongodb进行操作---pymongo
'''
from insterface.pymysqltools import DataBaseHandle
from faker import Faker
import requests


class TestReg:
    # 前置脚本
    def setup_class(self):
        self.ip = 'http://192.168.1.102'
        self.db = DataBaseHandle()

    def test_reg(self):
        # 实例化Faker这个对象
        fake = Faker()
        url = self.ip + '/mtx/index.php?s=/index/user/reg.html'
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        # 对data数据进行构造
        username = fake.first_name()
        print(f'username的值是{username}')
        data = {'accounts': username, 'pwd': 123456, 'type': 'username', 'is_agree_agreement': 1}
        # 发起请求
        r = requests.post(url=url, data=data, headers=headers)
        print(r)
        res = r.json()
        print(res)

        print('返回的数据是:', res)
        # 进行一个断言：查询数据库 看一下刚才注册的数据是否成功的存入到数据库中
        sql = f'select pwd,username from s_user where username = "{username}"'
        data = self.db.selectDb(sql)
        print('返回的数据是', data)
        assert data[0][1] == username
