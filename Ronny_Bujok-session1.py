from faker import Faker  # Before running this script, run `pip install faker`
from numpy.random import normal
import numpy as np
import pandas as pd

# First, let me generate some fake data...
fake = Faker()
students = []
for i in range(100):
    students.append({
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address': fake.address(),
        'maths': np.clip(normal(3, .5), 0, 4),
        'linguistics': np.clip(normal(3, .5), 0, 4),
        'psychology': np.clip(normal(3, .5), 0, 4)
    })

# Now, let's try out some things!
first_names = []
last_names = []
addresses = []
maths_grades = []
linguistics_grades = []
psychology_grades = []





# Can you write a loop that fills the above lists with the corresponding values from the list of dictionaries (students)?

for student in students:
    first_names.append(student['first_name'])
    last_names.append(student['last_name'])
    addresses.append(student['address'])
    maths_grades.append(student['maths'])
    linguistics_grades.append(student['linguistics'])
    psychology_grades.append(student['psychology'])

# Now, can you turn this dataset into a pandas dataframe?
#   hint: use the list of dictionaries to initialize your dataframe

students_dataframe = pd.DataFrame(students)

# What if you wanted to create a 3x100 numpy array of all the grades? (excluding the other information)
#   hint: use the separate lists to create a list of lists to initialize your array

grades = [maths_grades, linguistics_grades, psychology_grades]
grades_array = np.array(grades)
print(grades_array)

# Now, try to do the following for all four data structures: list of dictionaries, separate lists, dataframe, array.
# Don't spend more than 20 minutes on any of these!
# Thinking about a solution is more important than actually programming it.
# 1. Get all the information belonging to the 20th student

# Python counts from 0 so 19 is equal to the 20th student
#Dict
print(students[19])
#lists
print(first_names[19], last_names[19], addresses[19], maths_grades[19], linguistics_grades[19], psychology_grades[19])
#DF
print(students_dataframe.iloc[19])
#didn't know how to do the array

# 2. Find the student with the highest linguistics grade

# lists
highest_grade = max(linguistics_grades)
index = linguistics_grades.index(highest_grade)
print(first_names[index], last_names[index], linguistics_grades[index])

# DF
highest_index = students_dataframe['linguistics'].argmax()
print(students_dataframe.iloc[highest_index])


# 3. Calculate the average grade per student; (maths + linguistics + psychology) / 3

# lists
average_grades = []
for i in range(len(linguistics_grades)):
    average_grades.append((maths_grades[i] + linguistics_grades[i] + psychology_grades[i]) / 3)
print(average_grades[0])

# DF
students_dataframe['average'] = (students_dataframe['maths'] + students_dataframe['linguistics'] + students_dataframe['psychology']) / 3


# What operations do you find easier to do in each of these four structures? And what operations harder?

#generally lists are the most intuitive to me because I am familiar with them. Dataframes seem to be very useful and straight forward to use
#I'm not very confident with arrays and dictionaries.