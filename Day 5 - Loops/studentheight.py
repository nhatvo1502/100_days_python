astring = "156 178 165 171 187"
student_height = astring.split(" ")
print(student_height)

number_of_student = 0
total_height_student = 0
for height in student_height:
    number_of_student+=1
    total_height_student+=int(height)

print(round(total_height_student/number_of_student))