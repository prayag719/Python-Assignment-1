print("enter the number")
num = int(input())

first = num // 1000
second = (num // 100) % 10
third = (num // 10) % 10
forth = num % 10


print( f"Face value of each decimal is  {first} {second} {third} {forth} ")
print(f"{num} = {first*1000} + {second*100} + {third *10} + {forth}")
print(f"{(forth*1000)+(third*100)+(second*10)+(first)}")