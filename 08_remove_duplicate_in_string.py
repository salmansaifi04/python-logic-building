# How to remove duplicate character from the string

name = input("Enter a string : ")
temp = ""

for i in name:
    if i not in temp:
        temp+=i
print(temp)