'''
This Python code defines a Calculator class that provides a simple interface for performing arithmetic operations (addition, subtraction, multiplication, division) on Decimal numbers. The class uses static methods, demonstrating a functional approach within an object-oriented context. 
Each operation method creates a Calculation object, performs the calculation, adds it to a history of calculations, and then returns the result. 
Let's break down the code with detailed comments and highlight its design principles.

Design Principles Illustrated
Single Responsibility Principle (SRP): The Calculator class is focused solely on performing calculations using the provided operations. It delegates the responsibility of managing calculation history to the Calculations class, adhering to SRP by having a single reason to change.

Don't Repeat Yourself (DRY): The _perform_operation method abstracts the common process of creating a calculation, adding it to the history, and returning the result. This reduces repetition in the operation methods (add, subtract, multiply, divide), each of which only specifies the operation to perform.

Separation of Concerns: The Calculator class separates concerns by handling the calculation logic, while the Calculations class manages the history of calculations. This separation ensures that each class has a distinct responsibility, enhancing maintainability and scalability.

Encapsulation: While not encapsulating in the traditional sense of hiding data within an object, the Calculator class encapsulates the behavior of performing calculations and managing their lifecycle, showcasing functional encapsulation.

Polymorphism: The use of a Callable type hint for the operation parameter in _perform_operation method demonstrates polymorphism. It allows for any function that matches the specified signature to be passed in and executed, showcasing flexibility and reuse.

This code demonstrates effective use of object-oriented and functional programming principles to create a modular, maintainable, and easy-to-use calculator interface.
'''

# Standard imports
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Local imports
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation

# Definition of the Calculator class
class Calculator:
    """A class that provides basic arithmetic operations using Decimals."""

    @staticmethod
    # pylint: disable=invalid-name
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Create and perform a calculation, then return the result.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable): A function that takes two Decimal operands and returns a Decimal result.

        Returns:
            Decimal: The result of the calculation.
        """
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    # pylint: disable=invalid-name
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform addition by delegating to the _perform_operation method with the add operation.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of adding a and b.
        """
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    # pylint: disable=invalid-name
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform subtraction by delegating to the _perform_operation method with the subtract operation.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of subtracting b from a.
        """
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    # pylint: disable=invalid-name
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform multiplication by delegating to the _perform_operation method with the multiply operation.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of multiplying a and b.
        """
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    # pylint: disable=invalid-name
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform division by delegating to the _perform_operation method with the divide operation.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.

        Returns:
            Decimal: The result of dividing a by b.
        """
        return Calculator._perform_operation(a, b, divide)
