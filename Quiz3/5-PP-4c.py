#Alexandra Montgomery
# 5/1/2016
#5-PP-4c

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
            w1 = print(word[0])
        else:
            continue
        if word[2] of
