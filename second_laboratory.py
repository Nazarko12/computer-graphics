from math import sin
from math import cos
from matplotlib import pyplot as plt
import math


def main():
    x = 5
    max_x = 180
    step = 0.5

    x_list, y_list = [], []
    while x <= max_x:
        x_list.append(x)
        y_list.append(y(x))
        x += step

    ax = plt.figure(figsize=(5, 3.5)).gca()
    ax.plot(x_list, y_list)
    ax.set_xlabel('x')
    ax.set_ylabel('F(x)')
    plt.show()


def y(x):
    return 10 * (sin(x / 8.) + math.log(3 * x) * cos(x / 8.))


if __name__ == '__main__':
    main()
