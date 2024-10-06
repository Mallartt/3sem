from lab_python_oop.color import Color
from lab_python_oop.geometric import Geometric_Figure
import math

class Circle(Geometric_Figure):
    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = Color(color)

    def square(self):
        return math.pi * self.radius ** 2

    def get_color(self):
        return self.color.color

    def set_color(self, value: str):
        self.color.color = value

    def __repr__(self):
        return f"Circle(radius={self.radius}, color={self.get_color()}, square={self.square()})"
