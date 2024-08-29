def cal_bill(num):
    if num <= 100:
        print(f"Your bill for {num} calls = Rs.200")
    elif 100 < num < 150:
        print(f"Your bill for {num} calls = Rs.{num*0.60}")
    elif 150 < num < 200:
        print(f"Your bill for {num} calls = Rs.{num*0.50}")
    else:
        print(f"Your bill for {num} calls = Rs.{num*0.40}")

num = int(input("enter the number of calls\n"))
cal_bill(num)