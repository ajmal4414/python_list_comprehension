#1.find the common number in two cannot without using tuple or set

list1=[1,2,3,4]
list2=[2,3,4,5]

commonnum=[a for a in list1 if a in list2]
print(commonnum)