
import turtle
import math


def fractal_function(t, level, length):
    if level == 0:
        t.color('green')
        t.begin_fill()
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.end_fill()
        t.color('black')
        return

    t.forward(length)

    t.left(45)
    fractal_function(t, level - 1, length / math.sqrt(2))

    t.right(90)
    fractal_function(t, level - 1, length / math.sqrt(2))

    t.left(45)
    t.backward(length)


def main(level):

    turtle.setup(width=800, height=600)

    t = turtle.Turtle()
    t.speed('fastest')
    t.up()
    t.goto(0, -300)
    t.down()

    t.color('black')

    t.left(90)
    fractal_function(t, level, 100)

    t.hideturtle()
    turtle.done()


if __name__ == "__main__":

    while True:
        try:
            print("Пропонований проміжок для рівня рекурсії: від 3 до 8")
            recursion_level = int(input("Введіть рівень рекурсії (3 - 8): "))
            main(recursion_level)
        except ValueError:
            print("Будь ласка, введіть число.")
