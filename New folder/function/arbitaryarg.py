

def student(*studentname):
    print(studentname,type(studentname))

    for i in studentname:
        print(i)

student("kadir","shayan","ali")

student()
student("rez")