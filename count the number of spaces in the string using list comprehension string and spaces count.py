#2.count the number of spaces in the string using list comprehension

str='Welcome To India'
spaces=[str for str in  str if str==' ']
print(len(spaces))