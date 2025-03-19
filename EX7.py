def studList():

    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]


    for name in studentNames:
        print(f"{name} Evans")

    return studentNames

def addToList(studentNames):

    newName = input("Please enter the name: ")


    studentNames.append(newName)


    for name in studentNames:
        print(f"{name} Evans")

    return studentNames


if __name__ == "__main__":

    studentNames = studList()


    studentNames = addToList(studentNames)
