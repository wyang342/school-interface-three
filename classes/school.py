from posixpath import dirname
from classes.staff import Staff
from classes.student import Student
import os
import csv


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        new_student = Student(**student_data)
        self.students.append(new_student)
        self.update_csv()

    def remove_student(self, id):
        for student in self.students:
            if student.school_id == id:
                self.students.remove(student)
                break
        self.update_csv()

    def update_csv(self):
        current_dir_name = os.path.abspath(os.path.dirname(__file__))
        path_name = os.path.join(current_dir_name, "../data/students.csv")

        with open(path_name, "w") as csvfile:
            fields = ["name", "age", "role", "school_id", "password"]
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(fields)
            for student in self.students:
                csvwriter.writerow(
                    [student.name, student.age, student.role, student.school_id, student.password])
