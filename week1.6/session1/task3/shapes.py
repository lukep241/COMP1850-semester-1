# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!

class Circle(Shape) :
    """
    Subclass of Shape that represents a Circle
    """

    def __init__(self, radius, position, colour = "red"):
        """
        Creates a new circle with default colour red and a given radius and position
        """
  
        self.set_radius(radius)
        self.set_position(position)
        self.set_colour(colour)

    def set_radius(self, radius):

        if isinstance(radius, int) or isinstance(radius, float):
            if (radius > 0):
                self.radius = radius
            else:
                raise ValueError("Radius must be greater than 0")
        else:
            raise TypeError("Radius is not an int or float")

    def __str__(self):
        return f"{self.colour} circle, radius {self.radius}, at ({self.position.x},{self.position.y})"

    def area(self):
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        return self.radius * 2 * math.pi