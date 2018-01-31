#Alexandra Montgomery
#Exam Q3

def main():
    cars = textFileToDictionary("Mileage.txt")
    outputResult(cars)

# convert Mileage.txt into a dictionary named cars
def textFileToDictionary(fileName):
    infile = open(fileName, 'r')
    cars = {}
    for line in infile:
        split = line.split(',')
        cars[split[0]] = eval(split[1])
    return cars

#convert dictionary "cars" into list with average mpg, and display the list
def outputResult(cars):
    print("Model", "\t", "MPG")
    for line in cars:
        print(line)


main()
