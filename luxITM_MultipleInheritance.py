class ITM:
    subjects=["Hotel management","BTECH CSE","Design","Business"]
    teachers=["Sheetal ma'am","Sumit sir","Nidhi ma'am","Sai sir"]
    duration=["90 days","100 days","80 days","30 days"]
class LU:
    subjects=["AI/ML","AR/VR","Cloud Computing","Full Stack Developer"]
    teachers=["Sai Sir","Swapnil Sir","Vaibhav sir","Rohini ma'am"]
    duration=["60 days","30 days","50 days","55 days"]
class Courses(LU,ITM):
    print("Lets Upgrade courses:\n")
    luSubs=LU.subjects

    for i in range(len(luSubs)):
        print(i+1,LU.subjects[i],"by",LU.teachers[i],"for",LU.duration[i])

    lucourses=[]
    subNum=int(input("How many subjects you want to select: "))
    if subNum>4:
        print("Invalid number of subjects")
    else:
        for i in range(subNum):
            courseNum=int(input("Select your interested course: "))
            lucourses.append(courseNum)
    print("\nITM courses are:\n")

    itmSubs=ITM.subjects
    for i in range(len(itmSubs)):
        print(i+1,ITM.subjects[i],"by",ITM.teachers[i],"for",ITM.duration[i])

    itmCourses=[]
    subNum=int(input("How many subjects you want to select: "))
    if subNum>4:
        print("Invalid number of subjects")
    else:
        for i in range(subNum):
            courseNum=int(input("Select your interested course: "))
            itmCourses.append(courseNum)

    print("\nYour selected courses are:\n")
    for i in lucourses:
        print(i+1,LU.subjects[i-1],"by",LU.teachers[i-1],"for",LU.duration[i-1])

    for i in itmCourses:
        print(i+1,ITM.subjects[i-1],"by",ITM.teachers[i-1],"for",ITM.duration[i-1])


obj=Courses()