
def student(captain,*other_student):
    print('captain',captain)
    print('Other student: ',other_student)
student("kadir","shayan","ali")


#Arbitary keyword argumant
def student(captain,**other_student):
    print('captain',captain)
    print('Other student:',other_student)
student(captain="kadir",second_captain="shayan",third_captain="ali")


