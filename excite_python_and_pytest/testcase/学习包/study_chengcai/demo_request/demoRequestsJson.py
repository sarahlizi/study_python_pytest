import requests,json

response=requests.post(
    url='http://127.0.0.1:5000/register',
    data={
        "username":"xiaohua",
        "password":"p123456",
        "re_password":"p123456",
        "email":"123456@.com",
        "phone":"19221949381"
    },
    headers={"Content-Type":"application/json"})
res_body=response.content.decode('utf-8')
print(res_body)#{"code":9999,"msg":"恭喜你，注册成功"}