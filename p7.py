def miles_to_kilometers(miles):
  """Converts miles to kilometers."""
  kilometers = miles * 1.609344
  return kilometers

def pounds_to_kilograms(pounds):
  """Converts pounds to kilograms."""
  kilograms = pounds * 0.45359237
  return kilograms

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

# distance conversion
miles_input = float(input("Enter distance in miles: "))
kilometers_output = miles_to_kilometers(miles_input)
print(f"{miles_input} miles is equal to {kilometers_output} kilometers")

# weight conversion
pounds_input = float(input("Enter weight in pounds: "))
kilograms_output = pounds_to_kilograms(pounds_input)
print(f"{pounds_input} pounds is equal to {kilograms_output} kilograms")

# temperature conversion
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_output = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input} Fahrenheit is equal to {celsius_output} Celsius")
