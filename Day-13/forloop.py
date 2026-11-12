"""pin=1234

for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("Login successful")
        break
    else:
        print("Invalid Pin")

else:
    print("Max attempts reached! Try again after 30 secs")"""

"""l = [2,4,6,7,24,90,24,45,34,56,40]
search = int(input("Enter the num: "))

for i in range(len(l)):
    if l[i]  == search:
        print(f"{search} is found at {i}")
        break

else:
    print(f"{search} is not found")"""

"""c = {1,2,34,5,6,567,58}
for i in enumerate(c):
    print(i[0],i[1])"""

"""c = (1,2,34,5,6,567,58)
for i in enumerate(c):
    print(i[0],i[1])"""

"""c = [1,2,34,5,6,567,58]
for i in enumerate(c):
    print(i[0],i[1])"""

c = {"k1":"v1","k2":"v2","k3":"v3"}
for i in enumerate(c):
    print(i[0],i[1],c[i[1]])


