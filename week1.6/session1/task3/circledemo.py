# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from shapes import Circle, Point

c = Circle(10.45, Point(2,1), "purple")
print(c)
print(round(c.area(), 3))
print(round(c.perimeter(), 3))

c.set_position(Point(4,3))
print(c)

c.set_colour("green")
print(c)