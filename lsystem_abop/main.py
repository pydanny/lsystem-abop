import string
import sys

import turtle

SYMBOLS = "Ff+-^&\\/|$[]{G.}~!'%"


def remove_non_commands(text):
    output = ""
    for i in tuple(text):
        if i in SYMBOLS + string.digits:
            output += i
    return output


def preprocessor(raw_string):
    result = []
    for line in raw_string.splitlines():
        line = line.strip()
        line = line.split("#")[0]
        line = remove_non_commands(line)
        if len(line):
            result.append(line.strip())
    return "".join(result)


def parser(symbols):
    symbols = preprocessor(symbols)
    elements = []
    command = ""
    for index, e in enumerate(symbols.strip()):
        if e in SYMBOLS:

            if index != 0:
                elements.append(command)
            command = e

        else:
            command += e
    elements.append(command)
    return elements


def turtle_renderer(commands):
    pass
    # SWITCH = {"F": lambda x: turtle.forward(x), "+": lambda x: turtle.left(x)}

    # for command in commands:
    #     SWITCH.get(command)

    # turtle.done()


def main(symbols):
    commands = parser(symbols)
    print(commands)
    turtle_renderer(commands)


if __name__ == "__main__":
    # main("F30+30F30")

    text = """
    F30
    +90
    F30 
    -60  # Turn right 60 degrees
    # This is a comment
    aergq394t89
    """
    main(text)
