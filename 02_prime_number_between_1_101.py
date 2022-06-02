x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))

for i in range(x,y+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count+=1
    if count == 2:
        print(i, end=" ")