#Alexandra Montgomery
#Exam Q1

def main():
    fileExistFlag = False
    try:
        infile = open('text.txt', 'r')
        fileExistFlag = True
        list2 = [line.rstrip() for line in infile]
        infile.close()
    except Exception as e1:
        print('This is the error: ' + str(type(e1)), end = ' ')
        print('opps!')
    finally:
        if fileExistFlag:
            print("The file was opened sucessfully")
            print(list2)
        else:
            infile1 = open('text.txt', 'w')
            print('A file namely text.txt with default content is opened')
            list1 = ['It is default content,\n', 'It is default content']
            print(list1)
            infile1.writelines(list1)
            infile1.close()

main()

