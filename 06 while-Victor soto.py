CALORIES_PER_MINUTE = 4.33

print("Calorie Table Program")

again = "y"
while again.lower() == "y":
    minutes_input = input("Enter running minutes: ").strip()
    
    
    if minutes_input == "":
        print("Minutes cannot be blank")
    elif not minutes_input.lstrip("-").isdigit():
        print("Minutes must be a valid number")
    else:
        minutes = int(minutes_input)
        if minutes <= 5:
            print("Minutes must be greater than 5")
        else:
            for m in range(5, minutes + 1, 5):
                calories = round(m * CALORIES_PER_MINUTE, 2)
                print(f"minutes: {m}  calories: {calories}")

    again = input("Again y/n: ").strip().lower()
    print("-" * 30)

print("all done")
