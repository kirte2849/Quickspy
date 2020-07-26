import random
from quickspy.color import *


BANNEL = '''                 _          _
  __ _   _   _  (_)   ___  | | __  ___   _ __    _   _
 / _` | | | | | | |  / __| | |/ / / __| | '_ \  | | | |
| (_| | | |_| | | | | (__  |   <  \__ \ | |_) | | |_| |
 \__, |  \__,_| |_|  \___| |_|\_\ |___/ | .__/   \__, |
    |_|                                 |_|      |___/
'''

FIRST_HELP = '''Welcome to quickspy console (0.1v)
Type "help", "copyright", "credits" or "license" for more information.'''

HELP = ''''''





def colorful_bannel():
    _bannel = ''
    for char in BANNEL:
        _bannel += COLOR(random.choice(['red', 'yellow', 'white', 'purplish_red', 'turquoise', 'green']), char)
    return _bannel

def random_color_bannel():
    return COLOR(random.choice(['red', 'yellow', 'white', 'purplish_red', 'turquoise', 'green']), BANNEL)

