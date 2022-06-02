x = int(input("Enter a number : "))
temp = x
sum = 0
order = len(str(x))

while x>0:
    dig = x%10
    sum = sum + dig**order
    x = x//10

if temp == sum:
    print(f"{temp} is a armstrong number")
else:
    print(f"{temp} is not a armstrong number")