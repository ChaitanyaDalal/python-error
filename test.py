class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        total = 0
        for g in self.grades:
            total += g
        return total / len(self.grades)

s1 = Student("Alice")
s1.add_grade(90)
s1.add_grade("85")

print("Average grade:", s1.average())









