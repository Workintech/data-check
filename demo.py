
import math


def circle_area(radius: float) -> float:
    """Return the area of a circle. Negative radius returns 0."""
    if radius < 0:
        return 0
    return math.pi * (radius ** 2)