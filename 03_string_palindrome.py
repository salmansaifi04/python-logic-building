x = input("Enter a string that you want to palindrome : ")

def str_pal(x):
    if x == x[::-1]:
        print(f"{x} is palindrome")
    else:
        print(f"{x} is not a palindrome")

str_pal(x)