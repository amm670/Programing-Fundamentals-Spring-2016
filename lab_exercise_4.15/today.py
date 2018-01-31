# Alexandra Montgomery
# Pres and VS Pres
# 4/15/2016

def main():
    createSetFromFile(filename)
    createIntersection(set1, set2)
    writeNamesToFile(setName, fileName)

def createSetFromFile(filename):
    importFile = open("uspres1.txt", "r")
    listPres = [uspres.rstrip() for uspres in importFile]
    importFile.close()
    importFile = open("vspres1.txt", "r")
    listVP = [vspres.rstrip() for vspres in importFile]
    importFile.close()
    return listPres, listVP
    
def createIntersection(set1, set2):
    set1 = listPres
    set2 = listVP
    intersection = set1.intersection(set2)
    return intersection
    
def writeNamesToFile(setName, fileName):
    create.file(
    
main()
