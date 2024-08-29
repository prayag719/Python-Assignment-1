def leap(year):
    if year % 400 ==0:
        print(f"The year {year} is Leap Year")
    elif year % 4 ==0 and year % 100 !=0:
        print(f"The year {year} is Leap Year")
    else:
        print(f"The year {year} is not leap year")

year = int(input("Enter the Year\n"))
leap(year)