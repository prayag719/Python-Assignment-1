def find(num):
    if num > 0:
        print("the number is positive")

    elif num == 0:
        print("the number is zero")

    else:
        print("the number is negative")

num = int(input("enter the number\n"))
find(num)