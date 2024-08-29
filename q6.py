def eligible(age):
    if age >= 18:
        print("ELIGIBLE TO VOTE")
    else:
        print("NOT ELIGIBLE")

age = int(input("enter the age\n"))
eligible(age)