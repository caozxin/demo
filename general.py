words = ["zebra", "fat", "apply", "lion", "ink"]

words.sort()

nums = [40, 100, 1, 5, 25, 10]

nums.sort() 

nums.sort(reverse=True) 

tasks = [
    ('Cook dinner', 5),
    ('Buy grocery', 3)
]

sorted_tasks = sorted(tasks, key=lambda task: task[1])

# sorted_tasks = sorted(tasks, key=cmp_to_key(lambda t1, t2: t1[1] - t2[1])) --> this one is not common


# another example of built-in sort:
from typing import List

class Student:
    def __init__(self, name, math_grade, english_grade):
        self.name = name
        self.math_grade = math_grade
        self.english_grade = english_grade

    def get_total_grade(self):
        return self.math_grade + self.english_grade

def print_student_names(students):
    for i in range(len(students)):
        if i == len(students) - 1:
            print(students[i].name)
        else:
            print(students[i].name, end=" ")

def print_sorted_students(students: List[Student]):
    # sort students by their total grade in ascending order
    students.sort(key=lambda student: student.get_total_grade())
    print_student_names(students)
    # sort students by their total grade in descending order
    students.sort(reverse=True, key=lambda student: student.get_total_grade())
    print_student_names(students)

if __name__ == '__main__':
    # print(sorted_tasks )

  
  
    input = ["6", "Sally 50 80", "Moon 68 22", "Brown 36 71"]
    students = []
    for each_item in input:
        if len(each_item.split()) == 3:
            print(each_item)
            students.append(each_item.split())
            
    print(students)
    updated_students = []
    for each_record in students:
        
        updated_students.append(Student(each_record[0], int(each_record[1]), int(each_record[2])))
    print_sorted_students(updated_students)
    # for each_updated_record in updated_students:
    #     print(each_updated_record)
    #     print_sorted_students(each_updated_record)