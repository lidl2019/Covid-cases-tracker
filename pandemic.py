from lxml import html
import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; "
                         "Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/91.0.4472.106 Safari/537.36"}

def spider(i=0):
    url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
    response = requests.get(url, headers=headers)
    print(response.status_code)
    html_data = response.text
    with open('pandemic.html', mode='w', encoding='utf-8') as f:
             f.write(html_data)
    dict_data = json.loads(html_data)
    #print(dict_data)
    dict_list = dict_data['data']
    dict_list.sort(key=lambda x: x['confirmAdd'], reverse = False)
    print(type(dict_list))

    for dicts in dict_list:
        country = dicts['name']
        total = dicts['confirm']
        current_cases = dicts['nowConfirm']
        new_cases = dicts['confirmAdd']

        print(country + " 新增:" + str(new_cases) +
              " 当前病例: " + str(current_cases) + " 总共: "
              + str(total) + "\n")


spider()
