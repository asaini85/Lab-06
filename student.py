#!/usr/bin/env python3
# Author ID: asaini85

class Student:

    # Initialize with name and student number as string, and courses as a dictionary
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is a string
        self.courses = {}

    # Display student name and number as string
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add course and grade to student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate GPA, avoiding ZeroDivisionError if no courses are present
    def displayGPA(self):
        if len(self.courses) == 0:  # Check if no courses have been added
            return 'GPA of student ' + self.name + ' is 0.0'
        gpa = sum(self.courses.values()) / len(self.courses)  # GPA calculation
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # Display list of courses with grade > 0.0
    def displayCourses(self):
        passed_courses = []
        for course, grade in self.courses.items():
            if grade > 0.0:
                passed_courses.append(course)
        return passed_courses

# Testing code within this file (run only if this script is executed directly)
if __name__ == '__main__':
    # Create student1 and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create student2 and add grades
    student2 = Student('Jessica', 123456)  # Integer number will be converted to string
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display details for student1 and student2
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
