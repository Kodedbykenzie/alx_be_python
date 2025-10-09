class Calculator:
    """Demonstrates class and static methods."""

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Perform addition — no access to class or instance attributes."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Perform multiplication — accesses class attribute via cls."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
