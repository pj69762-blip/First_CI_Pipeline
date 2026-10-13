
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1

    for i in range(2, number + 1):
        result *= i

    return result
