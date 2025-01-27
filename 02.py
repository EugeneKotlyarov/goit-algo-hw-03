import turtle


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)


def koch_sf(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)


def main():
    level = int(input("Ей, користувач, вкажи рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("green")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400
    koch_sf(t, length, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
