#Alexandra Montgomery
#5/1/2016
#5-PP-4a

def createSenateFile():
    infile = open("Senate113.txt", 'r')
    set1 = {line.rstrip() + "\n" for line in infile}
    infile.close()
    infile = open("RetiredSen.txt", 'r')
    set2 = {line.rstrip() + "\n" for line in infile}
    infile.close()
    infile = open("NewSen.txt", 'r')
    set3 = {line.rstrip() + "\n" for line in infile}
    infile.close()
    set1 = set1.difference(set2)
    set1 = set1.union(set3)
    listx = list(set1)
    listx.sort(key=lambda x: x.split(',')[1])
    outfile = open("Senate114.txt", 'w')
    outfile.writelines(listx)
    outfile.close()
    return


