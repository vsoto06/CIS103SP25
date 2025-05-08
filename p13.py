def create_roman_dictionary():
    """Creates a dictionary of decimal to Roman numerals."""
    roman_map = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII', 18: 'XVIII',
        19: 'XIX', 20: 'XX', 21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV'
    }
    return roman_map

def get_decimal_input(prompt):
    """Gets a decimal input from the user recursively."""
    decimal_input = input(prompt)
    if not decimal_input:
        print("Input cannot be blank.")
        return get_decimal_input(prompt)
    try:
        return int(decimal_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return get_decimal_input(prompt)

def translate_decimal_to_roman(roman_dict):
    """Translates decimal numbers to Roman numerals using recursion without while True."""
    def translate_recursive():
        number = get_decimal_input("Enter a positive integer (or 0 or negative to quit): ")
        if number <= 0:
            return 

        if number in roman_dict:
            print(f"Roman numeral for {number} is: {roman_dict[number]}")
        else:
            print(f"{number} not found in the current dictionary.")
            add_to_dictionary(roman_dict, number)
        return translate_recursive() 

    translate_recursive()

def add_to_dictionary(roman_dict, number):
    """Adds a decimal and its Roman numeral to the dictionary."""
    roman_numeral = input(f"Enter the Roman numeral for {number} (must be alphabetic): ").strip().upper()
    if roman_numeral.isalpha():
        roman_dict[number] = roman_numeral
        print(f"{number}: {roman_numeral} added to the dictionary.")
    else:
        print("Invalid Roman numeral. Must be alphabetic.")

def main():
    """Main function to run the decimal to Roman numeral translator without while True."""
    roman_dictionary = create_roman_dictionary()
    print("Initial Dictionary:", roman_dictionary)
    translate_decimal_to_roman(roman_dictionary)
    print("\nFinal Dictionary:", roman_dictionary)

if __name__ == "__main__":
    main()
