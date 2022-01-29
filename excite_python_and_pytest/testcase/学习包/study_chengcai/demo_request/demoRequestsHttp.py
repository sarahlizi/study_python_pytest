import requests

"""#1.发送get请求
response = requests.get(url='https://www.baidu.com')#发送请求

#2.获取响应体内容
    #方法一
res_body =response.text
print(res_body)
    #方法二
res_body=response.content.decode('utf-8')
print(res_body)"""

#通过requests，调我们自己的接口
    #get方法
response =requests.get(
    url='http://127.0.0.1:5000/register?username=xiaocheng&password=p123456&re_password=p123456&email=12345@qq.com&phone=13522223333'
)
res_body=response.content.decode('utf-8')
print(res_body) #{"code":9999,"msg":"恭喜你，注册成功"}
#print(type(res_body))#<class 'str'>
# post方法
response = requests.post(
    url='http://127.0.0.1:5000/register',
    data={
        "username":"xiaohua",
        "password":"p123456",
        "re_password":"p123456",
        "email":"123456@.com",
        "phone":"19221949381"
    }
                         )
res_body=response.content.decode('utf-8')
print(res_body)#{"code":9999,"msg":"恭喜你，注册成功"}