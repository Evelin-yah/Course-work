income = float(input())
grade = float(input())
minimal_salary = float(input())
grade_scholarship = int(grade * 25)
social_scholarship = int(minimal_salary * 0.35)
if grade >= 5.50:
    if social_scholarship > grade_scholarship and income <= minimal_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {grade_scholarship} BGN")
elif 4.50 < grade < 5.50:
    if income < minimal_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")