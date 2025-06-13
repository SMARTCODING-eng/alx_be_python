def safe_divide(numerator, denominator):
    try:
        modify_numerator = float(numerator)
        modify_denominator = float(denominator)
        return f"The result of the division is {modify_numerator / modify_denominator}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
    


         

    # try:
    #     if 



    # except ZeroDivisionError:
        # print(f"Error: Cannot divide by zero.")