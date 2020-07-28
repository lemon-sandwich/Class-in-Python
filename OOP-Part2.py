# You will be wondering what is the use of creating var in classes. Why can't we just instantiate var in the main function
# Well that's because what if you wanted to list 500 students. What would you do? Now making an array is also a bad idea because of all the accessing
# and stuff. To keep things clean and make the code understandable for ourselves and others, we make classes

class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade # 1 - 100


class Course():
    def __init__(self,name,max_students):
        self.name = name
        self.students = []
        self.max_students = max_students
    def addStudent(self,student):
        if(len(self.students) < self.max_students):
            self.students.append(student)
            return True
        return False

s1 = Student("Tim",19,50)
s2 = Student("Billy",20,70)
s3 = Student("Ali",19,67)
max = 2
cs = Course("Computer Science",max)
if(cs.addStudent(s1.name)):
    print("Student Added!")
else:
    print("Student Wans't Added")

if(cs.addStudent(s2.name)):
    print("Student Added!")
else:
    print("Student Wans't Added")
if(cs.addStudent(s3.name)):
    print("Student Added!")
else:
    print("Student Wans't Added")

# You can also pass the whole object s1 in the cs object

math = Course("Mathematics",1)
math.addStudent(s1)
print("Name of the first student is: " + math.students[0].name)

# You can also ask the user for the values

s4 = Student(input("Name: "),int(input("Age: ")),int(input("Grade: ")))

print(s4.name)
print(s4.age)
print(s4.grade)

    
