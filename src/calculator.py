"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

import logging
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add(a, b):
    """Add two numbers together"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    logger.info(f"Multiplying {a} × {b}")
    result = a * b
    logger.info(f"Result: {result}")
    return result


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")

    result = a / b
    return result


def power(a, b):
    """Returns a raised to the power of b."""
    return a**b


def square_root(a):
    """Returns the square root of a number."""
    return math.sqrt(a)


if __name__ == "__main__":
    print("Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
