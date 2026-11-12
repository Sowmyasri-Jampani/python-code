"""l=[12,9,3,4,5,10,2,4,5,2,4,5]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[j])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1"""

"""bill = 0

while True:
    product = input("Enter the product name(STOP): ")
    if product == 'STOP':
        print("Total Bill:",bill)
        break
    price = int(input("Enter the price: "))
    qua = int(input("Enter the quantity: "))
    bill+= price*qua"""

products={'sugar':65,'salt':25,'bread':20,'milk':45,'curd':25,'chocolate':50,'biscuits':10,'chips':15,'juice':50}
#Display menu
print("welcome to the store".center(50,'-'))
print("Product Name",'price')
for i in products:
    print(i.ljust(12,' '),':',products[i])

carts = {}
while True:
    cart = input("Enter the product Name(exit): ").lower()
    if cart == 'exit':
        break
    qua = int(input("Enter the quantity: "))
    carts[cart]=qua

print("Bill".center(50,'-'))
print('product Name Quantity (Rs)Price')
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
    bill += carts[i]*products[i]

print(f"Total bill: Rs{bill}")
print("Thanks for shopping")
