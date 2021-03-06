import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def parsePage(lst, html, fpath):
    soup = BeautifulSoup(html, 'html.parser')
    keyList = soup.find_all('h2')
    num = soup.find_all('div',  attrs={'class': 'content'})
    # print(len(num))
    # infoDict = {}
    for i in range(len(num)):
        contentInfo = num[i]
        valList = contentInfo.find('span')
        val = valList.text
        val = val.replace("\n", "")
        key = keyList[i].text
        key = key.replace("\n", "")
        lst[key] = val

    with open(fpath, 'a', encoding='utf-8') as f:
        f.write(str(lst) + '\n')


def printInfo(lst):
    i = 1
    for key in lst.keys():
        print("用户" + str(i) + "：" + key + '\n', "留言： " + lst[key] + '\n')
        i += 1


def main():
    # depth = 2
    start_url = 'https://www.qiushibaike.com'
    infoList = {}
    fpath = 'F:/Crawler/精通python的网络爬虫/第六章/糗事百科/qiushi.txt'
    html = getHTMLText(start_url)
    parsePage(infoList, html, fpath)
    for i in range(2, 4):
        try:
            url = start_url + '/8hr/page/' + str(i)       # 这里的i一定要是str！！！！
            html = getHTMLText(url)
            parsePage(infoList, html, fpath)
            printInfo(infoList)
        except:
            continue

main()