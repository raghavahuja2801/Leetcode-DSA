def egyptian_fraction(numerator, denominator):
    """
    Represent a fraction as the sum of distinct unit fractions.
    
    Parameters:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.
    
    Returns:
        list: A list of denominators for the distinct unit fractions.
    """
    result = []

    while numerator != 0:
        x = (denominator + numerator - 1) // numerator  # Find the smallest unit fraction
        result.append(x)
        numerator = numerator * x - denominator
        denominator = denominator * x

    return result

# Example usage
numerator = 6
denominator = 14
print("Egyptian fraction representation:", egyptian_fraction(numerator, denominator))
