import math

class Shape:
    """Base class for geometric shapes."""

    def area(self):
        """Method to compute area — must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    """Rectangle shape class."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of a circle."""
        return math.pi * (self.radius ** 2)
