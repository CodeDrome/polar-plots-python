import math
from typing import Dict


def circle(radians: float, radius: float) -> Dict:

    return {"x": math.cos(radians) * radius,
            "y": math.sin(radians) * radius}


def cardioid(radians: float, radius: float) -> Dict:

    distance = (1 + math.cos(radians)) * radius

    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}


def spiral(radians: float, radius: float) -> Dict:

    """
    a - the rotation of the spiral
    b - distance between lines
    """

    a = 1
    b = 3

    distance = a + b * radians

    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}


def rose(radians: float, radius: float) -> Dict:

    n = 6

    distance = math.sin(radians * n) * radius

    return {"x": math.cos(radians) * distance,
            "y": math.sin(radians) * distance}