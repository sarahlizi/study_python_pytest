import requests,json
#1.登录登录接口，获取token
response=requests.post(
    url='http://127.0.0.1:5000/register',
    data={
        "name":"xiaohua",
        "pwd":"p123456" 
    },
    headers={"Content-Type":"application/json"})
res_body=response.content.decode('utf-8')
print(res_body)#{"code":9999,"msg":"恭喜你，注册成功"}