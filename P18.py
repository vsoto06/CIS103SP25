import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    kelvin_str = kelvin_entry.get()
    error_entry.delete(0, tk.END)
    
    # Input validation
    try:
        kelvin = float(kelvin_str)
        if kelvin <= 0:
            raise ValueError("Kelvin must be greater than 0")
    except ValueError as ve:
        kelvin_entry.config(bg="lightcoral")
        error_entry.insert(0, str(ve))
        return
    else:
        kelvin_entry.config(bg="white")

    # Conversion
    celsius = kelvin - 273.15
    fahrenheit = 9/5 * (kelvin - 273.15) + 32

    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)
    celsius_entry.insert(0, f"{celsius:.2f}")
    fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")

def clear_entries():
    for entry in [kelvin_entry, celsius_entry, fahrenheit_entry, error_entry]:
        entry.delete(0, tk.END)
        entry.config(bg="white")

def quit_app():
    root.destroy()


root = tk.Tk()
root.title("Temperature Conversion")

# Labels and Entries
tk.Label(root, text="Kelvin:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
kelvin_entry = tk.Entry(root)
kelvin_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Celsius:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Fahrenheit:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=2, column=1, padx=10, pady=5)

error_entry = tk.Entry(root, fg="red")
error_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Buttons
calc_button = tk.Button(root, text="CALC", command=convert_temperature)
calc_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="CLEAR", command=clear_entries)
clear_button.grid(row=4, column=1, padx=10, pady=10)

# Optional Quit Button
quit_button = tk.Button(root, text="QUIT", command=quit_app)
quit_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

