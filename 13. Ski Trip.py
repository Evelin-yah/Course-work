vacantion_days = int(input())
room = input()
rating = input()
room_price = 0
total = 0
if room == "apartment":
    if vacantion_days <= 10:
        room_price = (25.00 * (vacantion_days - 1)) * 0.70
    elif 10 < vacantion_days <= 15:
        room_price = (25.00 * (vacantion_days - 1)) * 0.65
    elif vacantion_days > 15:
        room_price = (25.00 * (vacantion_days - 1)) * 0.50
elif room == "president apartment":
    if vacantion_days <= 10:
        room_price = (35.00 * (vacantion_days - 1)) * 0.90
    elif 10 < vacantion_days <= 15:
        room_price = (35.00 * (vacantion_days - 1)) * 0.85
    elif vacantion_days > 15:
        room_price = (35.00 * (vacantion_days - 1)) * 0.80
elif room == "room for one person":
    room_price = 18.00 * (vacantion_days - 1)
if rating == "positive":
    total = (room_price * 0.25) + room_price
elif rating == "negative":
    total = room_price * 0.90
print(f"{total:.2f}")