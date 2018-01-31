# Alexandra Montgomery
# Crayon Colors Project 33 Page 163

colors = [ ]

def main():
    requestLetter()
    fillListWithColors(letter)
    print_colors()
    pass

def requestLetter():
    letter = input("Enter a letter: ")
    return letter.upper()

def fillListWithColors(letter):
    global colors
    for color in open("colors.txt", "r"):
        if color.startswith (letter):
            colors.append(color.rstrip()) 

def print_color():
    for color in colors:
        print(color)
main()
