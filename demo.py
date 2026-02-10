"""Demo module: circle area calculation"""

import math

def circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        return 0
    return math.pi * radius**2
