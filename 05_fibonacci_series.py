x = int(input("Enter a number : "))
a = 0
b = 1
if x == 0:
    print(a)
elif x == 1:
    print(b)
else:
    print(a,b, end=" ")
    for i in range(x-2):
        c = a+b
        a = b
        b = c
        print(b, end=" ")