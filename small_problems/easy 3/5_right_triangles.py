def triangle(height):
    for item in range(1, (height + 1)):
        print(((" " * (height - item))) + ("*" * item))

triangle(5)
triangle(9)