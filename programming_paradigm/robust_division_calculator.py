def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    
    Parameters:
        numerator (str or float): The numerator
        denominator (str or float): The denominator
    
    Returns:
        str: Result of division or an error message
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."