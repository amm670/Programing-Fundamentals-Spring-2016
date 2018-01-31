#Alexandra Montgomery
# 5/1/2016
#5-PP-4d

def main():
    importFile = open("Senate114.txt", "r")
    senateMembers = [Senate114.rsplit(",") for Senate114 in importFile]
    importFile.close()
    state = input("Enter the name of a state: ")
    state.lower()
    findTheSenators(state, senateMembers)

def findTheSenators(state, senateMembers):
    for word in senateMembers:
        if word[1] == state:
            print(word[0])
        else:
            continue

main()
