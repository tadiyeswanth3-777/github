def temperature(temp,unit):

    if unit == "C":
        farenheit = (temp * 9/5) +32
        kelvin = temp + 273
        print(f"Temperature in Farenheit:{farenheit} F")
        print(f"Temperature in Kelvin:{kelvin} K")

    elif unit == "F":
        celsius = (temp - 32 ) * 5/9
        kelvin = celsius + 273
        print(f"Temperature in Celsius:{celsius} C")
        print(f"Temperature in Kelvin:{kelvin} K")
    elif unit == "K":
        celsius = temp - 273
        farenheit = (celsius * 9/5) + 32
        print(f"Temperature in Celsius:{celsius} C")
        print(f"Temperature in Farenheit:{farenheit} F")
    else:
        print("invalid unit")



#temp = float(input("Enter Temperature: "))
#unit = input("enter units(K or F or C: ").upper()


temperature(50,"C")
temperature(40,"K")
temperature(60,"F")
