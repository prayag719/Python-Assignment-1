def maximum(first, second, third):
    if first > second and first > third:
        print(f"Maximum between {first}, {second}, and {third} = {first}")
    elif second > first and second > third:
        print(f"Maximum between {first}, {second}, and {third} = {second}")
    else:
        print(f"Maximum between {first}, {second}, and {third} = {third}")

print("Enter the first value:")
first1 = int(input())
print("Enter the second value:")
second2 = int(input())
print("Enter the third value:")
third3 = int(input())

maximum(first1, second2, third3)
