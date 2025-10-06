def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # (Redundant because we already check den == 0, but good practice)
        return "Error: Cannot divide by zero."
