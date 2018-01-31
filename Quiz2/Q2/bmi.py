#Alexandra Montgomery
#BMI
#4/1/2016


def main():
    weight = eval(input("Enter weight in pounds: "))
    height = eval(input("Enter height in inches: "))
    takeOutputOfCheck = checkInput(weight, height)
    if takeOutputOfCheck [0]:
        category = convertBmiToCategory(weight, height)
        print("For weight {0:.2f}".format(takeOutputOfCheck[1]),"and height {0:.2f} ".format(takeOutputOfCheck[2]) +\
              "the category is " + category)
    else:
        print("Invalid input.")

def checkInput(weight, height, times = 3):
    flag = False
    counter = 1
    while counter < times:
        if (weight >= 100 and weight <= 400 and height >= 48 and height <= 84):
            flag = True
            break
        else:
            counter += 1
            weight = eval(input("Enter weight in pounds: "))
            height = eval(input("Enter height in inches: "))
    if (weight >= 100 and weight <= 400 and height >= 48 and height <= 84):
        flag = True
    return [flag, weight, height]
    
def convertBmiToCategory(weight, height):
    bmi = ( weight / ( height ** 2 ) ) * 703
    category = " "
    if (bmi < 18.5):
        category = "Underweight"
    elif (bmi >= 18.5 and bmi < 25):
        category= "Normal Weight"
    elif (bmi >= 25 and bmi < 30):
        category = "Overweight"
    elif (bmi >= 30):
        category = "Obesity"
    return category


main()
