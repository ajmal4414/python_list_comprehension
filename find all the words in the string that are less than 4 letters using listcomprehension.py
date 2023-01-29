#3.find all the words in the string that are less than 4 letters using listcomprehension
str='Welcome To India'

f=str.split()

res=[word for word in  f if len(word)<=4]
print(res)