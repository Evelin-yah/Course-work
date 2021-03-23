name = input()
grade = 0
year = 1
fails = 0
while year <= 12:
    score = float(input())
    if score >= 4.00:
        grade += score
        year += 1
    else:
        fails += 1
        if fails >1:
            print(f"{name} has been excluded at {year} grade")
            break
if not fails >1:
    total_score = grade / 12
    print(f"{name} graduated. Average grade: {total_score:.2f}")