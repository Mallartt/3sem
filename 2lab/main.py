from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    N = 10
    rectangle = Rectangle(N, N, 'blue')
    circle = Circle(N, 'green')
    square = Square(N, 'red')

    print(rectangle)
    print(circle)
    print(square)

    response = requests.get("https://api.github.com", verify=False)
    print(f"GitHub API status: {response.status_code}")


if __name__ == "__main__":
    main()
