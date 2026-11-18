#int float str list tuple set dict bool
#int float str tuple bool
#list set dict
#pass by value: refers to passing of immutable elements
#pass by reference: refers to passing of mutable elements

def display(n):
    n+=10
    print("Inside function:",n)

n=10
display(n)
print("Outside function:",n)

#float
def display(n):
    n+=10.3
    print("Inside function:",n)

n=10.3
display(n)
print("Outside function:",n)

#str
def display(n):
    n+="programming"
    print("Inside function:",n)

n="python"
display(n)
print("Outside function:",n)

#list
def display(n):
    n.append(5)
    print("Inside function:",n)

n=[1,2,3,4]
display(n)
print("Outside function:",n)

#tuple
def display(n):
    n+=(5,6,7)
    print("Inside function:",n)
   
n=(1,2,3,4)
display(n)
print("Outside function:",n)

#set
def display(n):
    n.update({5})
    print("Inside function:",n)

n={1,2,3,4}
display(n)
print("Outside function:",n)

#dict
def display(n):
    n[5]=50
    print("Inside function:",n)

n={1,2,3,4}
display(n)
print("Outside function:",n)

#bool
def display(n):
    n=False
    print("Inside function:",n)

n=True
display(n)
print("Outside function:",n)

