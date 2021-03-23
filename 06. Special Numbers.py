n = int(input())
special_number = 0
for current_number in range(1111, 9999 + 1):
    for index, value in enumerate(str(current_number)):
        if int(value) != 0:
            if n % int(value) == 0:
                special_number = current_number
                print(current_number, end=" ")