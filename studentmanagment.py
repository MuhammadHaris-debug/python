# class student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks

#     def display(Self):
#         print("Name:",Self.name)
#         print("Roll Number:",Self.rollno)
#         print("Mark",Self.marks)


# name=(input("Enter your Name:"))
# rollno=int(input("Enter your roll number:"))
# marks=int(input("Enter your marks"))

# result=student(name,rollno,marks)
# result.display()

class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate(self):
        percentage = sum(self.marks) / len(self.marks)

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"

        print("Percentage:", percentage)
        print("Grade:", grade)


# User input
name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))

marks = []
for i in range(3):
    mark = float(input("Enter mark: "))
    marks.append(mark)

# Object creation
student = Student(name, roll_no, marks)

# Calculate percentage and grade
student.calculate()