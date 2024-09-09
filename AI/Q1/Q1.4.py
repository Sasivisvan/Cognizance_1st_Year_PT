
import numpy as np
# Creating a dataset with 15 students and 5 attributes
data = np.array([
    [170, 65, 19, 85, 5],
    [180, 75, 20, 90, 6],
    [160, 55, 18, 80, 4],
    [175, 70, 21, 88, 7],
    [155, 50, 19, 82, 5],
    [165, 62, 22, 89, 6],
    [178, 80, 23, 91, 7],
    [162, 58, 20, 78, 3],
    [172, 68, 19, 86, 5],
    [169, 66, 20, 84, 4],
    [171, 64, 22, 87, 6],
    [177, 72, 21, 90, 9],
    [174, 76, 24, 88, 8],
    [158, 52, 18, 75, 3],
    [164, 63, 19, 81, 4]
])
# Printing the dataset with student labels
# print("Student\tHeight\tWeight\tAge\tAvg Grade\tCourses")
# for index, student in enumerate(data):
#     print(f"Student {index + 1}\t{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t\t{student[4]}")

get_grades = data[:, 3]
more_than_85 = get_grades > 85
# print(more_than_85)

no = np.sum(more_than_85)
print("No of people who got above 85 is",no)
# abv_85 = np.where(get_grades > 85 )
# print(np.sum(abv_85[0]))
# print(TF_data_grade_abv_85)
