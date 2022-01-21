#!/usr/bin/env python3
# Created by: Zack isingoma
# Created on: Jan 20th , 2022


def calc_mark(level):
    grades = {
        "4+": lambda: 98,
        "4": lambda: 88,
        "4-": lambda: 83,
        "3+": lambda: 78,
        "3": lambda: 75,
        "3-": lambda: 71,
        "2+": lambda: 68,
        "2" : lambda: 65,
        "2-": lambda: 61,
        "1+": lambda: 59,
        "1" : lambda: 55,
        "1-": lambda: 51,
        "0": lambda: 49,
        "R": lambda: 0,
    }
    return grades.get(level, lambda: -1)()


if __name__ == "__main__":
    user_grade = input("Enter the grade: ")

    percentage = calc_mark(user_grade)
    
    print("{}  represents to {}".format(user_grade, percentage))
