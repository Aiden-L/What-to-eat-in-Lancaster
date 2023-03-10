import random
import re
import requests


def getresult():
    url = 'https://github.com/b1owcar/cooking_receipe/raw/c3267a01e24fb225a9ea474497d120482a2187b1/README.md'
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    # 获取md原始数据
    data = requests.get(url=url, headers=headers).text
    # 为获取到的数据分行
    lines = data.split('\n')
    # 用循环遍历菜谱，找到可以访问的菜品（同时去除 waiting list 中的菜）
    dishes_lines = []
    for line in lines:
        if 'dishes/' in line:
            pattern = r'\[(.*?)\]\((.*?)\)'
            match = re.search(pattern, line)
            if match:
                dish_name = match.group(1)
                dish_link = match.group(2)
                dishes_lines.append({
                    "name": dish_name,
                    "link": "https://github.com/b1owcar/cooking_receipe/blob/main/" + dish_link
                })
    # 随机选取的菜
    choice = random.choice(dishes_lines)
    return choice


if __name__ == '__main__':
    choice = getresult()
    print("今天吃: " + choice["name"])
    print(choice["link"])
