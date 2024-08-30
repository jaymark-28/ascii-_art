from pyfiglet import Figlet
from termcolor import colored


figlet = Figlet(font='larry3d') 
ascii_art = figlet.renderText('jaymark')
colored_art = colored(ascii_art, 'cyan')

print(colored_art)