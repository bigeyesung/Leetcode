import pandas as pd
import numpy as np

def class_grades(students):
    """
    :param students: (list) Each element of the list is another list with the 
      following elements: Student name (string), class name (string), student grade (int).
    :returns: (list) Each element is a list with the following 
      elements: Class name (string), median grade for students in the class (float).
    """
    classes = []
    table = {}
    ret = []
    for student in students:
        if table.get(student[1])==None:
            table[student[1]] = [student[2]]
        else:
            table[student[1]].append(student[2])
    
    for key in table:
        marks = table[key]
        a = np.array(marks)
        median = np.median(a)
        tmp = [key,median]
        ret.append(tmp)
    return ret
# add lists to test
students = [["Ana Stevens", "1a", 5], ["Mark Stevens", "1a", 4], ["Jon Jones", "1a", 2], ["Bob Kent", "1b", 4]]
print(class_grades(students))


