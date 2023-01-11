import requests
import bs4

r = requests.get('https://www.loongson.cn/')
r.encoding = 'utf-8'
# 创建BeautifulSoup对象:soup
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# 图片下载
div = soup.find('div',class_='itemizecontent')
i = 0
for img in div.find_all('img'):
    try:
        pic_url = requests.get(img['src'], timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        continue
    path = 'pictures\\' + str(i) + img['src'][img['src'].rindex("."):]
    file = open(path, 'wb')
    file.write(pic_url.content)
    file.close()
    i += 1
print()

