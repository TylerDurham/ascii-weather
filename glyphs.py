from dataclasses import dataclass
from termcolor import colored, cprint
from collections import namedtuple

colors = {
    "B": "yellow",
    "9": "red",
    "8": "black",
    "A": "green",
    "C": "blue",
    "D": "magenta",
    "E": "cyan",
    "F": "white",
    " ": ""
}

@dataclass
class Glyph:
    text: []
    colors: []
        
    def fullcolor(self):
        lines = []
        lc = 0
        for line in self.text: 
            chc = 0
            segment = []
            for ch in line:
                ccode = self.colors[lc][chc]
                if ccode == " ":
                    segment.append(ch)
                else:
                    segment.append(colored(ch, colors[ccode]))
                # Increment character count
                chc = chc + 1

            # Increment line count
            lines.append("".join(segment))                      
            lc = lc + 1

        return lines                           

sunny = Glyph(
    [
        "  \\ | /  ",
        "  - O -   ",
        "  / | \\  "
    ],
    [
        "  B B B   ",
        "  B 9 B   ",
        "  B B B   "
    ]
)


partial_clouds = Glyph(
    [
        "  \\ /(  ) ",
        " - O(    )",
        "  / (  )  ",
    ],
    [
        "  B BC  C ",
        " B 9C    C",
        "  B C  C  "
    ]
)


clouds = Glyph(
    [
        "  ( )()_  ",
        " (      ) ",
        "  (  )()  "
    ],
    [
        "  C CCCC  ",
        " C      C ",
        "  C  CCC  "
    ]
)



drizzle = Glyph(
    [
        " '  '    '",
        "  '   ' ' ",
        " '   '   '"
    ],
    [
        " C  C    C",
        "  E   C E ",
        "E    C   C"
    ]
)

rain = Glyph(
    [
        " ' '' ' ' ",
        " '' ' ' ' ",
        " ' ' '' ' "
    ],
    [
        " C CE C E ",
        " EC E E C ",
        " C C EC C "
    ]
)


night = Glyph(
    [
        "   .   *  ",
        " *    . 🌕 ",
        " . . *  . "
    ],
    [
        "   F   B  ",
        " B    F F ",
        " F F B  F "
    ]
)


thunderstorm = Glyph(
    [
        " ''_/ _/' ",
        " ' / _/' '",
        " /_/'' '' "
    ],
    [   
        " CCBB BBC ",
        " C B BBC C",
        " BBBCC CC "
    ]
)


chaos = Glyph(
    [
        " c__ ''' '",
        " ' '' c___",
        " c__ ' 'c_"
    ],
    [
        " EEE CCC C",
        " C CC EEEE",
        " EEE C CEE"
    ]
)


snow = Glyph(
    [
        " * '* ' * ",
        " '* ' * ' ",
        " *' * ' * "
    ],
    [
        " F FF F F ",
        " FF E F F ",
        " FF F F F "
    ]
)


fog = Glyph(
    [
        " -- _ --  ",
        " -__-- -  ",
        " - _--__  "
    ],
    [
        " FF F FF  ",
        " FFFFF F  ",
        " F FFFFF  "
    ]
)

wind = Glyph(
    [
        " c__ -- _ ",
        " -- _-c__ ",
        " c --___c "
    ],
    [
        " FFF FF F ",
        " FF FFFFF ",
        " F FFFFFF "
    ]
)

def colorize(glyph: Glyph):
    lines = []
    lc = 0
    for line in glyph.text: 
        chc = 0
        segment = []
        for ch in line:
            ccode = glyph.colors[lc][chc]
            # print(f'Character: {ch}')
            # print(f'Color: {colors[ccode]}')
            if ccode == " ":
                segment.append(ch)
            else:
                segment.append(colored(ch, colors[ccode]))
            # Increment character count
            chc = chc + 1

        # Increment line count
        lines.append("".join(segment))                      
        lc = lc + 1

    return lines                           

