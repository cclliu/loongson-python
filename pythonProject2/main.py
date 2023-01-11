# 定义字符串
x = "好好学习,天天向上"

# 查看字符串的长度
print(len(x))
print("==================================")

# 查找字符串，返回字符串出现的下标位置，如果没有找到，返回-1
print(x.find('学'))
print(x.find('坏'))
print("==================================")

# 查找字符串出现的次数
print(x.count('学'))
print(x.count('好'))
print("==================================")

# 字符串分割方法
print(x.split(','))
print("==================================")

# 字符串连接方法
list1 = x.split(',')
print(list1)
print('-'.join(list1))
print("==================================")

# 字符串大小写转换
s = 'Good Good Study,Day Day Up!'
# 转小写
print(s.lower())
# 转大写
print(s.upper())
print("==================================")

# 字符串替换
print(s.replace('Good','好').replace('Day','天'))