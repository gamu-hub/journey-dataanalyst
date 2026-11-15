"""
Exercise 8: Circle Class

Create a Circle class that can be defined using a radius
or diameter, calculate its area, add circles, compare
circles, and sort a list of circles.
"""

import math


class Circle:
    """Represent a circle using its radius."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        """Create a circle using its diameter."""
        return cls(diameter / 2)

    @property
    def diameter(self):
        """Calculate and return the diameter."""
        return self.radius * 2

    @property
    def area(self):
        """Calculate and return the circle's area."""
        return math.pi * self.radius ** 2

    def __str__(self):
        """Return a readable description of the circle."""
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __add__(self, other):
        """Add two circles and return a new circle."""
        if not isinstance(other, Circle):
            return NotImplemented

        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        """Check whether this circle is bigger than another."""
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius > other.radius

    def __eq__(self, other):
        """Check whether two circles have equal radii."""
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius == other.radius

    def __lt__(self, other):
        """Check whether this circle is smaller than another."""
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius < other.radius


# Create circles using radius and diameter
circle1 = Circle(5)
circle2 = Circle.from_diameter(10)
circle3 = Circle(3)
circle4 = Circle(8)


# Display circle information
print(circle1)
print("Area:", circle1.area)
print("Diameter:", circle1.diameter)


# Add two circles
circle5 = circle1 + circle3
print("Added circles:", circle5)


# Compare circles
print("Is circle1 bigger than circle3?", circle1 > circle3)
print("Are circle1 and circle2 equal?", circle1 == circle2)


# Store circles in a list and sort them
circles = [circle1, circle3, circle4, circle2]

circles.sort()

print("Sorted circles:")
for circle in circles:
    print(circle)