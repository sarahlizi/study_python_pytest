import json

import requests

url = "https://edu.51cto.com/center/appraise/index/get-lecturer-course-appraise?page=1&size=4&lecturer_id=13662582&essence_order_by=1&is_reply_list=1"

payload = {}
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://edu.51cto.com/lecturer/13662582.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'acw_tc=2760828316362117885248905ee390420fbde77ffb6b693c2cd4d666ecafab; PHPSESSID=nih8pqun65c3o8g62le10rasi8; _csrf=2bc0f309f0d6d676cd8e2bcb9d9c93baea3e63a1d1f575c83c36f5c013ffe847a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22%0B%15%0A6%14%D7%B2%9C-%3D%C3%8E%EC%27V%88%E4Z%07%84%EA%85%A5%D6%AE%3A%EFs%27A%8B%12%22%3B%7D; reg_sources=edu; UM_distinctid=17cf5d20489165-0187d75be8199-561a1053-e1000-17cf5d2048a366; CNZZDATA1279534624=46953273-1636203373-https%253A%252F%252Fwww.baidu.com%252F%7C1636203373; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217cf5d2057d33e-0307710dab7ad8-561a1053-921600-17cf5d2057ecdd%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22%24device_id%22%3A%2217cf5d2057d33e-0307710dab7ad8-561a1053-921600-17cf5d2057ecdd%22%7D; Hm_lvt_8c8abdb71d78d33dfdb885e0bc71dae0=1636211754,1636211811; Hm_lpvt_8c8abdb71d78d33dfdb885e0bc71dae0=1636211811; ssxmod_itna2=eq0OAIqArr7KGH=BD7wL4mOWKD7DUrq4YvqG9tLexBkixe7PjwBc3FX71PFGFWjk9N54glkiQsoMgdwiiYaImWUE2+Sl8cpHuIWdyv8676dxE8ryZCSvLxvjjUUCxVehOgBAvQTXmnx=SzwpvenihCYwecowf4QIxfS07Y0qHWmbh9WvAfebhiLbn+CWAiRq1mTaKcR2IfQq5nkKK5kNF4b=HALAbEdAbL2v3jnp1=Kb+Lo3dWRBb=UB7f+5O3ixQc2rm3bvq/herV27f/oAmR4nsYPu3sxiWdft1X46XNIzcTj=bMNovfdOD5BbbhLN2BNO8GRwQYl3uroBo3e4dIEioW+l3hqbo4uQruQeisTrm2hmk8ommNTWO6TotDmDgwVfC2WKCOsmlde31qDoR05RQKhkoTdqRY3aYtcGqa083SeD7QQxGcDG7ziDD===; BigUser=50dbff2770c3aaffe497a026a1193ac655f824372e88a1d248b8b63b21cc517fa%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22BigUser%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; ssxmod_itna=eqfO0KqmxG2DXDnQzY0Q5c7D0xxRrhLf4GX+5DZDiqAPGhDCSE=+wgErhGhqBIbljWrewb/8C+HEqF/WR7uYmDCPGnDBIPPNKxYA7Dt4DTD34DYDi2dGIDieDFty9ZODbxYQDmxAQDXha8DiPkDmROhxGCBxDCL7PDwx0CvgIaoR5mDivPU62OD7vmDlPxwR0OQbfEQYvk1Urd3CDDUnD6qexqrex6F0DqqW7ohgvsDCKDj2yODmeFibL8na7trW+4ThwYNi0oFn25S+2W5Bq0qG/iqjqq/e2xrBu5mGqtqYD==='
}

headers = {}
response = requests.request("POST", url, headers=headers, data=payload)
j = json.loads(response.text)
