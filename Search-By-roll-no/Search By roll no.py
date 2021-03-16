
import pickle

stufile=open("Student.BIN", 'rb')
stulist=pickle.load(stufile)
roll=int(input("Enter the roll number you want to search: "))
find = False
for stu in stulist:
    if stu['roll_no']==roll:
        find=True
        print("Student name is", stu['name'])
if find==False:
    print("No such record found!!!")
print(stulist)