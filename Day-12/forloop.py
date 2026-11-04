#str list tuple set dict range()

#for i in seq:
    #stmt

"""s = 'codegnan'
for i in s:
    print(i)

a = input("Enter the word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i)"""

#list
"""s=[12,23,34,56,23,44]
for i in s:
    print(i)


a=list(map(int,input("Enter the nums: ").split()))
for i in a:
    if i%2==0:
        print(i)"""

#tuple
"""s = (10,23,45,89,56,34,85,12)
for i in s:
    print(i)

sumoftuple = 0
a = tuple(map(int,input("Enter the sums: ").split()))
for i in a:
    sumoftuple+=i

print("sum of tuple:",sumoftuple)"""

#set
"""s = {10,23,45,89,56,34,85,12}
for i in s:
    print(i)

max = 0
a = set(map(int,input("Enter the sums: ").split()))
for i in a:
    if i>max:
        max = i
print("Max of set:",max)"""

#dict
"""marks = {'python':90,'mysql':85,'fastapi':80,'html':85,'css':90}
for i in marks:
    print(i,marks[i])

sum = 0
marks = {'python':90,'mysql':85,'fastapi':80,'html':85,'css':90}
for i in marks:
    sum +=marks[i]
print("Total marks:",sum)"""
 
#range(start,end+1,step)
#range(0,,1)

"""for i in range(1,11):
    print(i,end=' ')

for i in range(20,0,-1):
    print(i,end=' ')

for i in range(2,101,2):
    print(i,end=' ')"""

"""n = int(input("Enter the table no: "))

for i in range(1,21):
    print(f'{n}*{i}={n*i}')"""

"""c = 'codegnan'
for i in range(len(c)):
    print(c[i],i,end=' ')"""

"""sum = 0
l = [12,34,45,10,78,43,80]
for i in range(len(l)):
    if l[i]%2==0:
        sum+=i

print(sum)"""

"""l=[12,34,633,44,75,99,67,22,19]
product=1
for i in range(len(l)):
    if l[i]%2!=0:
        product*=i
print(product)"""

"""for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)"""

for i in range(1,10):
    pass

if True:
    pass

class Booking:
    pass

def func():
    pass

    







