from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.color import Color

class Square(Rectangle):
    def __init__(self, side: float, color: str):
        super().__init__(side, side, Color(color))
        self.side = side
        self.color=Color(color)

    def square(self):
        return self.width * self.height

    def get_color(self):
        return self.color.color

    def set_color(self, value: str):
        self.color.color = value

    def __repr__(self):
        return f"Square(side={self.side}, color={self.get_color()}, square={self.square()})"
