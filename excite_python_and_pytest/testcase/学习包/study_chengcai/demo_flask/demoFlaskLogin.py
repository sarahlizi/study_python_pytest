'''
flask框架介绍：该框架为后端服务框架，能够部署服务，这样我们的接口/代码就能够使用http协议来调用
'''

# 把我们写的代码（接口）发布成服务，让我们可以使用http协议调用

# 1.通过 pip install 导入该库


# 2.创建一个app的对象，把当前的python文件（模块）当成一个服务，__name__代表当前文件
import json

import flask as flask

from testcase.学习包.study_chengcai.demo_dbutils.DBUtils import DBUtils

app = flask.Flask(__name__)


# 3.我们写好的接口发布成服务，默认的接口地址是 127.0.0.1：5000
# @app.route('/', methods=['post', 'get'])  # route是路由的意思，methods用来指定接口访问的方式
# def demo():
#     return 'Hello World!'
@app.route('/user_login',methods=['get','post'])
def login():
    data = flask.request.values
    print(data)
    name=data.get('username')
    pwd=data.get('password')

    #登录接口的核心逻辑
    if len(name) ==0:
        return  json.dump({"code": 1001, "msg": "用户名不能为空"},ensure_ascii=False)
    elif len(pwd) == 0:
        return  json.dump({"code": 1002, "msg": "密码不能为空"},ensure_ascii=False)
    else:
        db=DBUtils()
        count=db.find_count('select * from tb_user where name=$s and passwd=%s',('name','pwd'))
        if count == 0:
            db.close()
            return json.dumps({"code": 1003, "msg": "用户名或密码错误"},ensure_ascii=False)
        else:
            db.close()
            return json.dumps({"code": 1000, "msg": "登录成功"},ensure_ascii=False)

if __name__== "__main__":
    app.run(debug=True)


