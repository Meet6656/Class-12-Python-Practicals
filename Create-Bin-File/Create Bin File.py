import pickle
stu={}
stulist=[]
n = int(input("Enter the number of students: "))
for i in range(n):
    stu['roll_no']=int(input('Enter roll number of the student: '))
    stu['name']=input("Enter the name of the student: ")
    stulist.append(stu)
    stu = {}
stufile = open("Student.BIN", 'ab+')
pickle.dump(stulist, stufile)
stufile.close()
print("Record added successfully")
file= open("Student.BIN", 'rb')
list =pickle.load(file)
print(list)
file.close()
