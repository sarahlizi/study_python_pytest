'''
flask框架介绍：该框架为后端服务框架，能够部署服务，这样我们的接口/代码就能够使用http协议来调用
'''

# 把我们写的代码（接口）发布成服务，让我们可以使用http协议调用

# 1.通过 pip install 导入该库
import flask, json



# 2.创建一个app的对象，把当前的python文件（模块）当成一个服务，__name__代表当前文件
from testcase.学习包.study_chengcai.demo_dbutils.DBUtils import DBUtils

app = flask.Flask(__name__)


# 3.我们写好的接口发布成服务，默认的接口地址是 127.0.0.1：5000
# @app.route('/', methods=['post', 'get'])  # route是路由的意思，methods用来指定接口访问的方式
# def demo():
#     return 'Hello World!'
@app.route('/register',methods=['get','post'])
def register():
    data = flask.request.values
    print(data)
    name=data.get('username')
    pwd=data.get('password')
    re_pwd=data.get('re_password')
    email= data.get('email')
    phone=data.get('phone')

    #登录接口的核心逻辑
    if len(name) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(pwd) == 0:
        return json.dumps({"code": 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    elif len(re_pwd) == 0:
        return json.dumps({"code": 1003, "msg": "重复密码不能为空"}, ensure_ascii=False)
    elif len(phone) == 0:
        return json.dumps({"code": 1004, "msg": "手机号码不能为空"}, ensure_ascii=False)
    elif len(email) == 0:
        return json.dumps({"code": 1005, "msg": "邮箱不能为空"}, ensure_ascii=False)
    elif pwd != re_pwd:
        return json.dumps({"code": 1006, "msg": "两次密码不一致"}, ensure_ascii=False)
    elif len(phone) != 11:
        return json.dumps({"code": 1007, "msg": "手机号码格式错误"}, ensure_ascii=False)
    elif not (6 <= len(name) <= 18 and 6 <= len(pwd) <= 18):
        return json.dumps({"code": 1008, "msg": '用户名或密码必须以字母开头，由字母和数字组成 6-8位的字符串'}, ensure_ascii=False)
    elif email.find('@') == -1 or email.find('.com') == -1:
        return json.dumps({"code": 1009, "msg": "邮箱格式错误"}, ensure_ascii=False)
    else:
        db = DBUtils()
        count = db.find_count('select * from tb_user where name=%s ', (name,))
        if count != 0:
            db.close()
            return json.dumps({"code": 1010, "msg": "该用户名已被注册"}, ensure_ascii=False)
        else:
            db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)', (name, pwd, email, phone))
            db.close()
            return json.dumps({"code": 9999, "msg": "注册成功"}, ensure_ascii=False)


# 第四步：启动服务器（使用debug模式启动服务，debug模式是可调模式）
if __name__ == '__main__':
    app.run(debug=True)