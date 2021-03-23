w = int(input())
l = int(input())
h = int(input())
room = w * l * h
command = input()
box = 0
while command != "Done":
    box = int(command)
    room -= box
    if room <=0:
        break
    command = input()
if command == "Done":
    print(f"{room} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(room)} Cubic meters more.")