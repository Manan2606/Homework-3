"""
This code snippet demonstrates how to define a class in Python that 
encapsulates a mathematical calculation, including two operands (a and b) 
and an operation (like add or subtract). 
The operation parameter is a higher-order function, meaning it takes 
functions as arguments or returns them. 
This approach leverages Python's first-class functions to create flexible 
and reusable code. The use of Decimal from the decimal 
module instead of floating-point numbers is crucial for 
financial and scientific calculations that require high precision. 
The __repr__ method provides a developer-friendly string representation 
of the object, useful for debugging and logging.
"""

# Import the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Import Callable from typing to specify the operation as a callable type hint
from typing import Callable

# Definition of the Calculation class with type annotations for improved readability and safety
class Calculation:
    """Class that encapsulates a mathematical calculation."""
    # pylint: disable=unnecessary-dunder-call, invalid-name
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initialize the Calculation instance.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform on the operands.
        """
        # Initialize the first operand of the calculation
        self.a = a
        # Initialize the second operand of the calculation
        self.b = b
        # Store the operation as a callable that takes two Decimals and returns a Decimal
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Create a new instance of Calculation.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable[[Decimal, Decimal], Decimal]): The operation to perform on the operands.

        Returns:
            Calculation: A new Calculation instance initialized with the provided arguments.
        """
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
