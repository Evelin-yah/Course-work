dog_food = int(input())
dog_food_gr = dog_food * 1000
command = input()
while command != "Adopted":
    daily_food = int(command)
    dog_food_gr -= daily_food
    command = input()
    if command == "Adopted":
        if dog_food_gr >= 0:
            print(f"Food is enough! Leftovers: {dog_food_gr} grams.")
            break
        elif dog_food_gr < 0:
            print(f"Food is not enough. You need {abs(dog_food_gr)} grams more.")
            break
