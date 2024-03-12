name = input("ENTER NAME OF A STUDENT: ")
marks = int(input("ENTER MARKS: "))
if(marks >= 87 and marks <= 100):
    print(name,"HAS OBTAINED A GRADE")

elif(marks >= 75 and marks <= 86):
    print(name,"HAS OBTAINED B GRADE")

elif(marks >= 65 and marks <= 74):
        print(name, "HAS OBTAINED C GRADE")

elif(marks >= 55 and marks <= 64):
    print(name,"HAS OBTAINED A GRADE")

elif(marks >= 0 and marks <= 54):
    print(name,"SORRY YOU ARE FAIL")
else:
    print("PLEASE ENTER CORRECT INFORMATION")