class Color:
    def __init__(self, color=None):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value
