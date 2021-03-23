import math
model = input()
sex = input()
cat_months = 0

if model == "British Shorthair":
    if sex == "m":
        cat_months = (13 * 12) / 6
    elif sex == "f":
        cat_months = (14 * 13) / 6
    print(f"{math.floor(cat_months)} cat months")
elif model == "Siamese":
    if sex == "m":
        cat_months = (15 * 12) / 6
    elif sex == "f":
        cat_months = (16 * 12) / 6
    print(f"{math.floor(cat_months)} cat months")
elif model == "Persian":
    if sex == "m":
        cat_months = (14 * 12) / 6
    elif sex == "f":
        cat_months = (15 * 12) / 6
    print(f"{math.floor(cat_months)} cat months")
elif model == "Ragdoll":
    if sex == "m":
        cat_months = (16 * 12) / 6
    elif sex == "f":
        cat_months = (17 * 12) / 6
    print(f"{math.floor(cat_months)} cat months")
elif model == "American Shorthair":
    if sex == "m":
        cat_months = (12 * 12) / 6
    elif sex == "f":
        cat_months = (13 * 12) / 6
    print(f"{math.floor(cat_months)} cat months")
elif model == "Siberian":
    if sex == "m":
        cat_months = (11 * 12) / 6
    elif sex == "f":
        cat_months = (12 * 12) / 6
    print(f"{math.floor(cat_months)} cat months")
else:
    print(f"{model} is invalid cat!")
