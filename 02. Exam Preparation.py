fails = int(input())
counter = 0
fail_counter = 0
grade = 0
name = ""
problem = ""
while name != "Enough":
    name = input()

    if name == "Enough":
        total_score = grade / counter
        print(f"Average score: {total_score:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {problem}")
        break

    score = int(input())
    problem = name
    if score <= 4:
        fail_counter += 1
        if fail_counter == fails:
            print(f"You need a break, {fail_counter} poor grades.")
            break
    counter += 1
    grade += score



