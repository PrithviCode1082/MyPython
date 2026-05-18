# Converting Celsius into Kelvin and Fahrenhite

#talking user input
temp_celsius = float(input("Enter temperature (in celsius): "))

# converting temperature
temp_kelvin = temp_celsius + 273.15
temp_Fahrenheit = (temp_celsius * (9/5)) + 32

# printing the temperatures
print(f"Temperature in Celsius: {temp_celsius:.2f}")
print(f"Temperature in Kelvin: {temp_kelvin:.2f}")
print(f"Temperature in Fahrenheit: {temp_Fahrenheit:.2f}")