student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    
    if score >= 91 and score < 100:
        student_grades[student]='Outstanding'
    elif score >= 81 and score < 90:
        student_grades[student]='Exceeds Expectations'
    elif score >= 71 and score < 80:
        student_grades[student]='Acceptable'
    else:
        student_grades[student]='Fail'