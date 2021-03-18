#First we import pickle module which just helps us to serialize objects as file
import pickle
#then we created a dictionary called "stu", how we know its a dictionary because of {}(this #implies a dictionary)
stu={}
#then we created a list called "stulist" which is empty as there is nothing in bracket
#([] denotes a list)
stulist=[]
#here we are taking an input from user of how many names and roll no he/she wants to #add
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
