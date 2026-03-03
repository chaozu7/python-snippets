import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
available = figlet.getFonts()
len_available = len(available)



if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 1:
        font_random = random.randint(0,len_available)
        font_name = available[font_random]
        figlet.setFont(font=font_name)
    elif len(sys.argv) == 3:
        if sys.argv[1] != '-f'and sys.argv[1] != '-font':
            sys.exit("Invalid usage")
        else:
            if sys.argv[2] in available:
                font_name = sys.argv[2]
                figlet.setFont(font=font_name)
            else:
                sys.exit("Invalid usage")
    words = input("Please give me a text ")
else:
    sys.exit("Invalid usage")





print(figlet.renderText(words))



