def studList():

    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]


    for name in studentNames:
        print(f"{name} Evans")

    return studentNames

def addToList(studentNames):

    newName = input("请输入要添加的名字: ")


    studentNames.append(newName)


    for name in studentNames:
        print(f"{name} Evans")

    return studentNames


if __name__ == "__main__":

    studentNames = studList()


    studentNames = addToList(studentNames)
