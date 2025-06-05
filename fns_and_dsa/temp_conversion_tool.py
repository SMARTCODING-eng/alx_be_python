FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celcius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR  + 32
    return fahrenheit

def main():
    user_temp = float(input("Enter the temperature to convert: "))
    temp_type = input("Is this temperature in Celsius of Farhrenheit? (C/F): ").upper()

    if temp_type == 'F':
       result = convert_to_celcius(user_temp)
       print(f"{user_temp}°{temp_type} is {result}°C")

        
    elif temp_type == 'C':   
        result = convert_to_fahrenheit(user_temp)
        print(f"{user_temp}°{temp_type} is {result}°F")
    
    else:
        return "Invalid Temperature type"
    
if __name__ == "__main__":
    # result = main()
    # 
    
    main()

