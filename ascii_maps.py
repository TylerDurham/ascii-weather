from dataclasses import dataclass
from termcolor import colored, cprint
from collections import namedtuple

ColorMap = namedtuple("ColorMap", "index color")
Glyph = namedtuple("Glyph", "ascii colors")

sunny = Glyph(
    [
        "\\ | /",
        "- O -",
        "/ | \\"
    ],
    [
        "b b b",
        "b 9 b",
        "b b b"
    ]
)

colors = {
    "b": "yellow",
    "9": "red",
    "8": "black",
    "A": "green",
    "C": "blue",
    "D": "magenta",
    "E": "cyan",
    "F": "white",
    " ": ""
}

def print_glyph(glyph: Glyph):
    buffer = []
    lc = 0
    for line in glyph.ascii: 
        chc = 0
        for ch in line:
            ccode = glyph.colors[lc][chc]
            # print(f'Character: {ch}')
            # print(f'Color: {colors[ccode]}')
            if ccode == " ":
                buffer.append(ch)
            else:
                buffer.append(colored(ch, colors[ccode]))
            # Increment character count
            chc = chc + 1

        # Increment line count
        buffer.append("\n")                      
        lc = lc + 1

    #print(f'{index + 1} characters written')
    print("".join(buffer))                            

print_glyph(sunny)
