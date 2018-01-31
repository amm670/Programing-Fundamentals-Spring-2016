# Alexandra Montgomery
# U.S. States Project 65 Page 181

# Sort states by the number of vowels in their name in desending order and displays first 6 states

states = [ ]

def main():

    importFile = open("states.txt", "r")
    listStates = [state.rstrip() for state in importFile]
    importFile.close()
    listStates.sort(key=numberOfVowels, reverse=True)

    for i in range(6):
            print(listStates[i])

def numberOfVowels(word):
    vowels = ("a", "e", "i", "o", "u")
    total = 0
    for vowel in vowels:
            total += word.count(vowel)
    return total

main()
