goal = 10000
step_counter = 0
command = input()
while command != "Going home":
    step = int(command)
    step_counter += step
    if step_counter > goal:
        total = step_counter - goal
        print("Goal reached! Good job!")
        print(f"{abs(total)} steps over the goal!")
        break
    command = input()
if command == "Going home":
    command = input()
    step = int(command)
    step_counter += step
    total = step_counter - goal
    if step_counter > goal:
        print("Goal reached! Good job!")
        print(f"{abs(total)} steps over the goal!")

    elif step_counter < goal:
        print(f"{abs(total)} more steps to reach goal.")
