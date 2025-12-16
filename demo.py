"""
Demo module for circle area calculation.
"""

import math


def circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (int or float): Radius of the circle

    Returns:
        float: Area of the circle or 0 if radius is negative
    """
    if radius < 0:
        return 0

    return math.pi * radius ** 2
