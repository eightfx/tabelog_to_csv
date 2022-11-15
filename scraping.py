import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse    # 1. argparseをインポート
parser = argparse.ArgumentParser(
    description='食べログの検索結果をcsvに変換するツール')    # 2. パーサを作る

# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('-u', "--url", help='URL')    # 必須の引数を追加
args = parser.parse_args()

return_dic_list = []
for i in range(1, 60):
    url = args.url.replace("?", "{}/?".format(i))

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    elements = soup.find_all("div", class_="list-rst__body")
    for element in elements:

        # 夜料金取得
        price_info = element.find_all("ul", class_="list-rst__info")[0]
        dinner_price = price_info.text.strip().split("\n")[0].replace("￥", "")
        if dinner_price == "-":
            lowerst_price = 0
            highest_price = 0
        else:
            lowest_price, highest_price = dinner_price.strip().split("～")
            if lowest_price != "":
                lowest_price = int(lowest_price .replace(",", ""))
            else:
                lowest_price = 0
            if highest_price != "":
                highest_price = int(highest_price.replace(",", ""))
            else:
                highest_price = 0

        # 駅名取得
        area_info = element.find_all(
            "div", class_="list-rst__area-genre cpy-area-genre")[0]
        nearest_station, industry = area_info.text.strip().split("/")[:2]
        nearest_station = nearest_station.split(" ")[0]

        # 店名取得
        name_info = element.find_all(
            "a", class_="list-rst__rst-name-target cpy-rst-name")[0]
        name = name_info.text.strip()
        link = name_info.get("href")

        return_dic = {
            "name": name,
            "url": link,
            "lowest_dinner_price": lowest_price,
            "highest_dinner_price": highest_price,
            "nearest_station": nearest_station,
            "industry": industry
        }
        return_dic_list.append(return_dic)

df = pd.DataFrame(return_dic_list)
df = df.drop_duplicates()
df.to_csv("tabelog.csv", index=False, header=False, mode="a")
