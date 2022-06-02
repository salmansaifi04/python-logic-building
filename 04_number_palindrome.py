x = int(input("Enter a number : "))
temp = x
rev = 0

while x>0:
    dig = x%10
    rev = rev*10 + dig
    x = x//10

if temp == rev:
    print(f"{temp} is a palindrome")
else:
    print(f"{temp} is not a palindrome")