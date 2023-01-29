#use nested list comprehension to find all of the numbers from 1 to 1000 that are divisible by any single digit beside 1 using list comprehension
n=list[1,1001]
result=[n for n in range(1,1001)if True in [True for x in range(2,9) if n % x==0]]
print(result)