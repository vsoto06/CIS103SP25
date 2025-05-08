def analyze_rainfall(rainfall_data):
    """
    Analyzes the rainfall data to find the highest, lowest, total, and average.

    Args:
        rainfall_data: A list of floats representing rainfall amounts.

    Returns:
        A tuple containing the highest rainfall, the month of highest rainfall (if available),
        the lowest rainfall, the month of lowest rainfall (if available),
        the total rainfall, and the average rainfall.
    """
    if not rainfall_data:
        return None, None, None, None, 0, 0

    highest = max(rainfall_data)
    lowest = min(rainfall_data)
    total = sum(rainfall_data)
    average = total / len(rainfall_data)

    highest_month = None
    lowest_month = None

    if len(rainfall_data) == 12:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        highest_index = rainfall_data.index(highest)
        lowest_index = rainfall_data.index(lowest)
        highest_month = months[highest_index]
        lowest_month = months[lowest_index]

    return highest, highest_month, lowest, lowest_month, total, average

def get_rainfall_from_input():
    """
    Gets rainfall data from user input without using any explicit while loop.
    """
    rainfall = []
    print("Enter rainfall amounts for each month (enter 'done' when finished):")

    def get_input_recursive(current_rainfall):
        entry = input("> ").strip()
        if entry.lower() == 'done':
            return current_rainfall
        try:
            amount = float(entry)
            if amount < 0:
                print("Rainfall amount cannot be negative.")
                return get_input_recursive(current_rainfall)
            return get_input_recursive(current_rainfall + [amount])
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_input_recursive(current_rainfall)

    return get_input_recursive(rainfall)

def get_rainfall_from_file(filename="rainfall_2017.txt"):
    """
    Gets rainfall data from a file without using while True for the main loop.
    Each line in the file should contain a rainfall amount (and optionally the
    month name separated by a space or comma).
    """
    rainfall = []
    try:
        with open(filename, 'r') as infile:
            for line in infile:
                parts = line.strip().split()  
                if parts:
                    try:
                        amount = float(parts[0].replace(',', '')) 
                        if amount < 0:
                            print(f"Warning: Negative rainfall amount found in file: {amount}. Ignoring.")
                        else:
                            rainfall.append(amount)
                    except ValueError:
                        print(f"Warning: Invalid rainfall amount in file: {parts[0]}. Ignoring.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please create it or use input from screen.")
        return get_rainfall_from_input()  
    return rainfall

def main():
    """
    Main function to get rainfall data and display the analysis without while True
    for the main program flow.
    """
    def main_loop():
        print("Choose the source for rainfall data:")
        print("1. Input from screen")
        print("2. Read from file (rainfall_2017.txt)")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            rainfall_data = get_rainfall_from_input()
        elif choice == '2':
            try:
                with open("rainfall_2017.txt", "r") as f:
                    pass
            except FileNotFoundError:
                with open("rainfall_2017.txt", "w") as f:
                    f.write("2.87 Jan\n")
                    f.write("1.52 Feb\n")
                    f.write("4.01 Mar\n")
                    f.write("6.43 Apr\n")
                    f.write("3.28 May\n")
                    f.write("3.44 Jun\n")
                    f.write("7.68 Jul\n")
                    f.write("2.51 Aug\n")
                    f.write("0.32 Sep\n")
                    f.write("8.70 Oct\n")
                    f.write("1.75 Nov\n")
                    f.write("0.59 Dec\n")
            rainfall_data = get_rainfall_from_file()
        elif choice == '3':
            print("Exiting program.")
            return False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            return True

        if rainfall_data:
            print("\nData list:", rainfall_data)
            highest, highest_month, lowest, lowest_month, total, average = analyze_rainfall(rainfall_data)

            print("Highest:", highest, end=" ")
            if highest_month:
                print(f"({highest_month})")
            else:
                print()

            print("Lowest:", lowest, end=" ")
            if lowest_month:
                print(f"({lowest_month})")
            else:
                print()

            print("Total:", total)
            print("Average:", f"{average:.1f}")
        else:
            print("No valid rainfall data to analyze.")
        return True

    while main_loop():
        pass

if __name__ == "__main__":
    main()
