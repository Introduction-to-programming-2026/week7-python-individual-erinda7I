# Project 1 — Temperature Converter
# Name: Erinda Ismani 
# Date: 3/31/2026

choice = input("Convert (C to F) or (F to C)? Enter C or F: ").upper()

if choice == "C":
    celsius = float(input("Enter temperature in Celsius: "))
    
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif choice == "F":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5/9
    
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

else:
    print("Invalid choice. Please enter C or F.")