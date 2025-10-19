astring = "78 65 89 86 55 91 64 89 99"
student_scores = astring.split(" ")
print(student_scores)
high_score = 0
low_score = 100
for score in student_scores:
    if int(score) > high_score:
        high_score=int(score)
    if int(score) < low_score:
        low_score=int(score)
print(f"Max score {high_score}")
print(f"Min score {low_score}")

