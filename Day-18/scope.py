#local scope
#global dec
#global keyword is used to declare outside all functions

"""def display():
    global n
    n=10
    print("inside:",n)

display()
print("outside:",n)"""

#non local-declared inside an outer fun
"""def display():
    course ="JFS"
    print("Starting:",course)
    def update():
        nonlocal course
        course = "PFS"
        print("updated:",course)
    update()
    print("final:",course)

display()"""

#build scope

s = "codegnan"

max = 10

print(max(s))

