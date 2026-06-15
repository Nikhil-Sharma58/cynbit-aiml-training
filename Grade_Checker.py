marks = float(input("Enter your marks: "))
if(marks>=90):
    grade = "A"
elif(marks>=80):
    grade = "B"
elif(marks>=70):
    grade = "C"
else:
    grade = "Fail"

print("Your grade is:",grade)