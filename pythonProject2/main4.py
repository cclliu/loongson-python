# 读取text文件
try:
    file = open("word\\1.txt", 'r',encoding='UTF-8')
except IOError:
    print("1.txt文件不存在,请先创建!")
else:
    text = file.read()
    print(text)
    file.close()
