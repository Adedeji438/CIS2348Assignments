'''


name: Adedeji Akingbola
PSID:1793979
'''


def part1():
    height = float(input("Enter wall height (feet): "))
    width = float(input("Enter wall width (feet): "))
    area = height * width
    print("Wall area: " + str(area) + " square feet")
    print("\n")


def part2():
    height = float(input("Enter wall height (feet): "))
    width = float(input("Enter wall width (feet): "))
    area = height * width
    print("Wall area: " + str(area) + " square feet")
    gallons = area / 350
    print("Paint needed: {:.2f} gallons".format(gallons))
    print("\n")


def part3():
    height = float(input("Enter wall height (feet): "))
    width = float(input("Enter wall width (feet): "))
    area = height * width
    print("Wall area: " + str(area) + " square feet")
    gallons = area / 350
    print("Paint needed: {:.2f} gallons".format(gallons))
    cans = round(gallons)
    print("Cans needed: %d can(s)" % cans)
    print("\n")

    
def part4():
    height = float(input("Enter wall height (feet): "))
    width = float(input("Enter wall width (feet): "))
    area = height * width
    print("Wall area: " + str(area) + " square feet")
    gallons = area / 350
    print("Paint needed: {:.2f} gallons".format(gallons))
    cans = round(gallons)
    print("Cans needed: %d can(s)" % cans)
    color = input("Choose a color to paint the wall: ")
    if(color == "red"):
        cost = 35 * cans
    elif(color == "blue"):
        cost = 25 * cans
    elif(color == "green"):
        cost = 23 * cans
    print("Cost of purchasing ", color, "paint:")
    print("$", cost)


if __name__ == '__main__':
   
    part1()
    part2()
    part3()
    part4()
    
