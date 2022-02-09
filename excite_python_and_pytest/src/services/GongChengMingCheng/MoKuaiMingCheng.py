import pytest
import json
import requests
from src.common.envConfig import *



#接口地址配置
demoPostUrl=DemoPostUrl #+'.json'

def demo_post(param):
    response = requests.post(demoPostUrl, param, headers=headerParams)
    # 判断response返回情况
    assert response.status_code == 200, "接口调用失败,状态码：" + str(response.status_code)
    resp = json.loads(response.text)
    print(json.dumps(resp, sort_keys=True, indent=2, ensure_ascii=False))
    return resp
