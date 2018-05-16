# from bs4 import BeautifulSoup
# import re
# import requests
# url = 'https://www.qiushibaike.com'
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     html = r.text
# except:
#     print('')
#
# soup = BeautifulSoup(html, 'html.parser')
# h2 = soup.find_all('h2')
# lst = []
# # print(h2)
# i = '''<h2>
# 在下张百忍
# </h2>'''
# print(i)
# data = (re.split("<h2>|</h2>", i))
# data1 = data[1]
# data1.replace("\n", "")
# print(data1)
#
# # lst.append(data1)
#
# print(lst)


import re

html = """ 
  <h2>多云</h2> 
"""

p = re.compile('<[^>]+>')
a = p.sub("", html)
print(a)

# print(p.sub("", html))


