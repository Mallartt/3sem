from lab_python_oop.color import Color
from lab_python_oop.geometric import Geometric_Figure

class Rectangle(Geometric_Figure):
    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = Color(color)

    def square(self):
        return self.width * self.height

    def get_color(self):
        return self.color.color

    def set_color(self, value: str):
        self.color.color = value

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.get_color()}, square={self.square()})"
