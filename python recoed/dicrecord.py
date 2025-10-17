student={"name":"Anu","roll number":"MCA0010","register number":19852,"department":"Computer science","semester":"s1"}
print(student)
student["total mark"]=980
print(student)
if student["total mark"]>=90:
    student["grade"]="A"
elif student["total mark"]>=82:
    student["grade"]="B"
elif student["total mark"]>=75:
    student["grade"]="C"
elif student["total mark"]>=60:
    student["grade"]="D"
elif student["total mark"]>=50:
    student["grade"]="P"
else:
    student["grade"]="F"
print(student)
student.pop("roll number")
print(student)
