def grading(sub1, sub2, sub3):
    avg = (sub1 + sub2 + sub3) / 3
    total = sub1 + sub2 + sub3
    if 0 <= avg < 59:
        return f"Average = {avg} and Grade F"
    elif 60 <= avg < 69:
        return f"Average = {avg} and Grade D"
    elif 70 <= avg < 79:
        return f"Average = {avg} and Grade C"
    elif 80 <= avg < 89:
        return f"Average = {avg} and Grade B"
    elif 90 <= avg < 100:
        return f"Average = {avg} and Grade A"

sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

result = grading(sub1, sub2, sub3)
print(result)
