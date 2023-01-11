import requests
import bs4

r = requests.get('https://www.loongson.cn/')
r.encoding = 'utf-8'
# 创建BeautifulSoup对象:soup
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# 导航文字获取
list = soup.find_all(class_='spanitem')

for a in list:
    print(a.text)
print()

