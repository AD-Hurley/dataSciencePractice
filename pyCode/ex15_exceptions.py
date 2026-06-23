numericalGrade = round(float(input('Please enter the numerical grade:')),2)

try:
    if numericalGrade > 100 or numericalGrade < 0:
        raise ValueError("Grade must be between 0 and 100")
except ValueError as ve:
    print(f"⚠️ {ve}")
else:
    if numericalGrade >= 90:
        grade = 'A'
    if numericalGrade < 90:
        grade = 'B'
    if numericalGrade < 80:
        grade = 'C'
    if numericalGrade < 70:
        grade = 'D'
    if numericalGrade < 60:
        grade = 'F'

    print(grade)

finally:
    print("Congratulations or I'm sorry. Grades are meaningless in the grand scheme of it all anyway")