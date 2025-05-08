def convert_acres_to_hectares(acres):
    return acres * 0.40468564

def convert_quarts_to_liters(quarts):
    return quarts * 0.946352946

def convert_fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

again = 'y'

while again.lower() == 'y':
    print("Conversion Program")

    # Acres
    try:
        acres = float(input("Enter acres: "))
        hectares = convert_acres_to_hectares(acres)
        print(f"{acres} converts to {hectares:.4f} hectares")
    except:
        print("Input error - acres")
    
    print("----------")

    # Quarts
    try:
        quarts = float(input("Enter quarts: "))
        liters = convert_quarts_to_liters(quarts)
        print(f"{quarts} converts to {liters:.6f} liters")
    except:
        print("input error - quarts")

    print("----------")

    # Fahrenheit
    try:
        fahrenheit = float(input("Enter Fahrenheit: "))
        kelvin = convert_fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} converts to {kelvin:.2f} Kelvin")
    except:
        print("input error - Fahrenheit")

    print("----------")
    again = input("again y/n? ")
    print("===========")

print("done")
