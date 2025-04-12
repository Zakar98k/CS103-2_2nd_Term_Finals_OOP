class SchoolOne:
    students = []

    def average_grade(self):
        if not self.students:
            return 0
        total_grade = sum(student[1] for student in self.students)
        return total_grade / len(self.students)

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


zach = Student("Zach", 85)
peter = Student("Zach", 90)
quandale_dingle = Student("Quandale Dingle", 95)

ciit = SchoolOne()
ciit.add_student(zach)
ciit.add_student(peter)
ciit.add_student(quandale_dingle)

ciit.average_grade()
print(ciit.average_grade())
