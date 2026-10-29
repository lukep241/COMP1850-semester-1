# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not (isinstance(width, int) and isinstance(height, int)):
            raise TypeError("Type error - Non-integer value entered.")

        if not (width > 0 and height > 0):
            raise ValueError("Value error - value less than or equal to 0 entered.")

        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here

    def is_square(self):
        """
        returns true if the rectangle is actuallty a square. If not, returns false.
        """
        if (self.width == self.height):
            return True
        else:
            return False

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        return (self.width*2) + (self.height*2)

    # (See README.md for details of what they should do)
