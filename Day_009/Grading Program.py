student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, value in student_scores.items():
    if value > 90:
        student_grades[key] = 'Outstanding'
    elif value > 80:
        student_grades[key] ='Exceeds Expectations'
    elif value > 70:
        student_grades[key] ='Acceptable'
    else:
        student_grades[key] = 'Fail'
print(student_grades)