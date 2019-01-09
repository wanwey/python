# -*- coding: utf-8 -*-

import re
import requests
import argparse
from bs4 import BeautifulSoup, Comment



HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def get_parser():
    parser = argparse.ArgumentParser(description='绿色网络，绿色资源！')
    parser.add_argument('-k', '--keyword', type=str, help='关键词')
    return parser


def run():
    print("正在为您打开新世界的大门...")
    print("\n")
    newworld = "http://www.btyunsou.co"
    parser = get_parser()
    kw = vars(parser.parse_args())["keyword"]
    magnets = []
    for p in range(1, 3):
        url = newworld + "/search/{kw}_ctime_{p}.html".format(kw=kw, p=p)
        try:
            resp = requests.get(url, headers=HEADERS).text.encode("utf-8")
            try:
                bs = BeautifulSoup(resp, "lxml").find(
                    'ul', class_='media-list media-list-set').find_all('li')
                if not bs:
                    print("姿势不对，没找到资源！")
                    return
                for b in bs:
                    name = str(b.find(
                        class_='media-body').find('h4').find('a', class_='title').text).strip()
                    if name:
                        item = b.find('div', class_='media-more')
                        time = item.find(class_='label label-success').text
                        size = item.find(class_='label label-warning').text
                        rank = item.find(class_='label label-primary').text
                        link = re.findall(r'href="(.*?)">', str(item.find(text=lambda text: isinstance(text, Comment))))[0]
                        magnets.append({
                            "magnet": link,
                            "magnet_name": name,
                            "magnet_date": time,
                            "magnet_size": size,
                            "magnet_rank": int(rank)
                        })
            except:
                pass
        except Exception as e:
            print(e)
       
    _magnets = sorted(magnets, key=lambda x: x["magnet_date"], reverse=True)    

    if not _magnets:
        return "没有找到资源！！"

    for row in _magnets:  
        print("资源名称:", row["magnet_name"])
        print("磁力链接:", row["magnet"], "资源大小：", row["magnet_size"], "资源日期:", row["magnet_date"])
        print('\n')
    return "查询完毕！！"


if __name__ == "__main__":
    run()


    


