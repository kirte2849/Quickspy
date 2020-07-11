def BLACK(text):
    print(f'\033[0;30;m{text}\033[0m')


def RED(text):
    print(f'\033[0;31;m{text}\033[0m')


def GREEN(text):
    print(f'\033[0;32;m{text}\033[0m')


def YELLOW(text):
    print(f'\033[0;33;m{text}\033[0m')


def BLUE(text):
    print(f'\033[0;34;m{text}\033[0m')



def PURPLISH_RED(text):#紫红色
    print(f'\033[0;35;m{text}\033[0m')



def TURQUOISE(text):#青蓝色
    print(f'\033[0;36;m{text}\033[0m')


def WHITE(text):
    print(f'\033[0;37;m{text}\033[0m')


def COLOR(col, text ):
    color={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'purplish_red':35,'turquoise':36,'white':37}
    print(f'\033[0;%s;m{text}\033[0m' % color[col])
