# property tax program calc
def getinput(msg):
    """Gets a float input from the user with the given message."""
    while True:
        try:
            xin = float(input(msg))
            return xin
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def main():
    """Calculates and prints the property tax due."""
    print('\n' * 1)  

    AssesmentLevel = 0.10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45

    PropertyValue = getinput('Enter value of property: ')
    LocalTaxRate = getinput('Enter local tax rate: ')
    StateEqualizer = getinput('Enter state equalizer rate: ')
    print('\n' * 5)  

    AssessedValue = PropertyValue * AssesmentLevel
    EqualizedValue = AssessedValue * StateEqualizer
    PropertyTaxBeforeExemption = EqualizedValue * LocalTaxRate /100
    TotalPropertyTax = PropertyTaxBeforeExemption - HomeOwnerEx - SeniorCEX

    print('\n' * 2)  
    print('Property tax due:', TotalPropertyTax)
    print('\n' * 3) 

if __name__ == "__main__":
    main()
