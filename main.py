#Receving value from user
temp = float(input("What's the Celsius° temperature at your location? \n"))

#Converting to fahrenheit
fahr = float((temp * 1.8) + 32)

#Printing result to user
print(f"The temperature in Fahrenheit at you location is {fahr}°F")
