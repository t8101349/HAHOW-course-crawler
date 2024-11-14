
import requests
import time
import random
import sys
import json
import pandas as pd

url = "https://api.hahow.in/api/products/search?category=COURSE&limit=24&page=0&sort=TRENDING"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

response = requests.get(url, headers= headers)
if response.status_code == 200:
    data = response.json()
    sys.stdout.reconfigure(encoding='utf-8')
    course_list = []
    products = data["data"]["courseData"]['products']
    #products = data.get("data", {}).get("courseData", {}).get("products", [])
    for product in products:
        #course_data = {
        #    "title" : product['title'],
        #    "averageRating" : product['averageRating'],
        #    'price' : product['price'],
        #    'numSoldTickets' : product['numSoldTickets']
        #}

        #轉為excel
        course_data = [
            product['title'],
            product['averageRating'],
            product['price'],
            product['numSoldTickets']
            ]

        course_list.append(course_data)

        course_df = pd.DataFrame(course_list, columns = ["title","averageRating",'price','numSoldTickets'])
        course_df.to_excel('course.xlsx', index = False, engine= 'openpyxl')

        print(course_list)
else:
    print("no 無法取得網頁")


# 延遲下一次請求
time.sleep(random.uniform(1, 3)) 