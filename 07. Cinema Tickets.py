command = input()
counter = 0
kids = 0
stand = 0
stud = 0
while command != "Finish":
    seats = int(input())
    counter_per_film = 0
    while seats != counter_per_film:
        type = input()
        if type == "kid":
            kids += 1
        elif type == "standard":
            stand += 1
        elif type == "student":
            stud +=1
        elif type == "End":
            break
        counter_per_film += 1
        counter +=1
    full = counter_per_film / seats * 100
    print(f"{command} - {full:.2f}% full.")
    command = input()
if command == "Finish":
    k = kids / counter * 100
    sta = stand / counter * 100
    stu = stud / counter * 100
    print(f"Total tickets: {counter}")
    print(f"{stu:.2f}% student tickets.")
    print(f"{sta:.2f}% standard tickets.")
    print(f"{k:.2f}% kids tickets.")
