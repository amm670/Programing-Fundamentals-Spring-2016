# Alexandra Montgomery
# U.S. Presidents Project 63 Page 180

presidents = [ ]
#sort list by length of their names and display 1st 6 names
def main():

    importFile = open("uspres.txt", "r")
    listPres = [uspres.rstrip() for uspres in importFile]
    importFile.close()
    listPres.sort(key=sortByFirstName)

    for i in range(6):
        print(listPres[i])
        
def sortByFirstName(pres):
    return len(pres.split() [0] )
    

main()

