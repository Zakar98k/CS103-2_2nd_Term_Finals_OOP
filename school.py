class SchoolOne:
    def __init__(self) -> None:
        self.students = []

    def average_grade(self):
        if not self.students:
            return 0
        total_grade = sum(student.grade for student in self.students)
        return total_grade / len(self.students)

    def add_student(self, student):
        self.students.append(student)


class SchoolTwo(SchoolOne):
    def __init__(self) -> None:
        super().__init__()


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


zach = Student("Zach", 85)
peter = Student("Peter", 90)
quandale_dingle = Student("Quandale Dingle", 95)

ciit = SchoolOne()
ciit.add_student(zach)
ciit.add_student(peter)
ciit.add_student(quandale_dingle)

ciit2 = SchoolTwo()
ciit2.add_student(zach)
ciit2.add_student(peter)

ciit.average_grade()
print(ciit.average_grade())

ciit2.average_grade()
print(ciit2.average_grade())
