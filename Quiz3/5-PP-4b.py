#Alexandra Montgomery
# 5/1/2016
#5-PP-4b

def main():
    importFile = open("Senate114.txt", "r")
    senateMembers = [Senate114.rsplit(",") for Senate114 in importFile]
    importFile.close()
    print("Party Affiliations:")
    countR(senateMembers)
    countD(senateMembers)
    countI(senateMembers)

def countR(senateMembers):
    countOfR = 0
    for word in senateMembers:
        if word[2] == "R\n":
            countOfR += 1
        else:
            continue
    print("\t", "Republicans: ", countOfR)

def countD(senateMembers):
    countOfD = 0
    for word in senateMembers:
        if word[2] == "D\n":
            countOfD += 1
        else:
            continue
    print("\t", "Democrats: ", countOfD)

def countI(senateMembers):
    countOfI = 0
    for word in senateMembers:
        if word[2] == "I\n":
            countOfI += 1
        else:
            continue
    print("\t", "Independents: ", countOfI)

main()
