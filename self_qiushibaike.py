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



def main():
    # depth = 2
    url = 'https://www.qiushibaike.com'
    infoList = {}
    fpath = 'F:/qiushibaike.txt'
    html = getHTMLText(url)
    parsePage(infoList, html, fpath)
    # for i in range(2, depth+2):
    #     try:
    #         url = start_url + '/8hr/page/' + i + '/'
    #         html = getHTMLText(url)
    #         parsePage(infoList, html, fpath)
    #     except:
    #         continue

main()