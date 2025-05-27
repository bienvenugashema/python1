class Student:
    def __init__(self, name, marks: str):
        self.name = name
        self.marks = marks

    def average(self):
            average = sum([int(mark) for mark in self.marks.split(" ")])/len(self.marks.split(" "))

            return f"Average marks of {self.name} is {average}"

marks = input("Marks separated by space: ")
student = Student("Bienvenu", marks)

print(student.average())