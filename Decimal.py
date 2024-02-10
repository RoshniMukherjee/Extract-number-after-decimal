def extract_digit_after_decimal(number):
    # Convert number to string
    number_string = str(number)
    
    # Find the position of the decimal point
    decimal_point_position = number_string.find('.')
    
    # Extract the digit after the decimal point
    digit_after_decimal = number_string[decimal_point_position + 1]
    
    # Return the digit after the decimal point
    return digit_after_decimal

# Example usage:
number = 123.54
print("Digit immediately following the decimal point:", extract_digit_after_decimal(number))
