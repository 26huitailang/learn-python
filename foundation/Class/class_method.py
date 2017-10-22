#!/usr/bin/python
# coding: utf-8


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def average(self):
        print("{}".format(self))
        return sum(self.grades) / len(self.grades)

    @classmethod
    def go_to_school(cls):
        print("I'm going to school.")
        print("I'm a {}".format(cls))

    @staticmethod
    def go_to_home():
        print("HOME.")


s1 = Student('Amm', 'AA')
s2 = Student('Bee', 'BB')

s1.grades = [100, 90, 80]
s2.grades = [90, 90, 90]

print(s1.average())
s2.go_to_school()
s2.go_to_home()

Student.go_to_school()
Student.go_to_home()
