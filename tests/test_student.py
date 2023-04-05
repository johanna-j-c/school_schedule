import pytest
from school_schedule.student import Student

def test_new_valid_student():
    #Arrange
    name = "Felipe"
    grade = "Junior"
    classes = ["Art", "UWBW", "Algebra", "Computer Science"]

    #Act
    felipe = Student(name, grade, classes)

    #Assert
    assert felipe.name == name
    assert felipe.grade == grade
    assert felipe.classes == classes
    assert felipe.get_num_classes() == 4

def test_empty_list():
    #Arrange
    name = "Felipe"
    grade = "Junior"
    classes = []
    class_name = None

    #Act
    student = Student(name, grade, classes)
    class_list = student.add_class(class_name)

    #Assert
    assert class_list == classes

def test_get_num_classes_correct_len():
#     Arrange
    name = "Ada"
    grade = "Freshman"
    classes = ["Computer Science", "Calculus", "ELA"]

#     Act
    student = Student(name, grade, classes)
    class_list = student.get_num_classes()
    
#     Assert
    assert class_list == 3

def test_get_correct_student_summary():
#     Arrange
    name = "Ada"
    grade = "Freshman"
    classes = ["Computer Science", "Calculus", "ELA"]


#     Act
    student = Student(name, grade, classes)
    class_list = student.get_num_classes()  

#     Assert
    

    # def summary(self):
    #     return (f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes: {self.display_classes()}")

    