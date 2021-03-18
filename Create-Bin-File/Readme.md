# First we import pickle module which just helps us to serialize objects as file
import pickle
# then we created a dictionary called "stu", how we know its a dictionary because of {}(this implies a dictionary)
stu={}
# then we created a list called "stulist" which is empty as there is nothing in bracket () [] denotes a list)
stulist=[]
# here we are taking an input from user of how many names and roll no he/she wants to add
n = int(input("Enter the number of students: "))
# Now here we introduce a FOR loop in range of "n" (user input) and will repeat the code in the loop as many times as user inputted
for i in range(n):
# here we take another of roll no and store it in a list 'roll_no' in dictionary "stu"
    stu['roll_no']=int(input('Enter roll number of the student: '))
# here we take input of name and store it in a list 'name' in dictionary "stu"
# now there are 2 lists in stu i.e. name and roll_no
    stu['name']=input("Enter the name of the student: ")
# now we append(add without overwriting) stu in stulist(which we created at the beginning)
# now if user input '1' in roll_no and let say 'Ayush' in name then [{'roll_no': 1, 'name': 'Ayush'}{and so on...}] will be store in this manner in stulist
    stulist.append(stu)
# We empty stu(dictionary) as we have stored all its content in stulist(list)
    stu = {}
# here we make an object 'stufile' and open a file 'Student.BIN' in append binary+read mode(ab+) which will open the file or if the file is not present , it will create in the folder your code is saved as  because we opened it in append mode.
stufile = open("Student.BIN", 'ab+')
# here we store the date of stulist in stufile(object in which the file is opened) i.e. dump
pickle.dump(stulist, stufile)
# now we closed the file
stufile.close()
# This print is just to check if the code till now is correct and doesn't have any errors
print("Record added successfully")
# here to read the saved file we open it in object 'file' {we can also name the object stufile but just to make clear we named it different} in read mode because we just want to read it
file= open("Student.BIN", 'rb')
# then we load the file in a variable/object 'read' because we want to print it
read =pickle.load(file)
# we print 'read
print(read)
# then closed the file(object)
file.close()
