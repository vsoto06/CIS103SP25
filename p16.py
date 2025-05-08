def recursive_sum(n, show_steps=False):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    if n == 1:
        return 1, "1" if show_steps else ""
    else:
        sum_of_smaller, steps = recursive_sum(n - 1, show_steps)
        current_sum = n + sum_of_smaller
        current_steps = f"{n}+{steps}" if show_steps else ""
        return current_sum, current_steps

def get_valid_input(prompt="enter number:"):
    user_input = input(prompt)
    if not user_input.strip():
        print("Input cannot be blank.")
        return get_valid_input(prompt)
    try:
        num = int(user_input)
        if num < 0:
            print("Number cannot be negative.")
            return get_valid_input(prompt)
        return num
    except ValueError:
        print("Invalid input detected.")
        return get_valid_input(prompt)

def process_number():
    num = get_valid_input()
    result, steps_string = recursive_sum(num, show_steps=True)
    print(f"{steps_string} = {result}")
    ask_again()

def ask_again():
    another = input("Another number (y/n): ").lower()
    if another == 'y':
        process_number()
    else:
        print("---done---")

def main():
    print("--- sum up numbers---")
    process_number()

if __name__ == "__main__":
    main()

