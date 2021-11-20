""" Alejandro Madrigal, November 16 2021, Test #2"""
users =[]
""" Must look for Name, Gender, Height, Weight, Classes, Grades, GPA """
def adduser(students,name,gender,height,weight,grade,all_grades,average_gpa):
  students.append([name,gender,height,weight,grade,all_grades,average_gpa])
  return students

name = input("Name: ")
gender = input("Gender: ")
height = input("Height: ")
weight = input("Weight: ")
grade = input("Grade(9-12): ")
all_grades = input("Grades Per Class: ")
average_gpa = input("Average GPA from past years: ")
users=adduser(users,name,gender,height,weight,grade,all_grades,average_gpa)
print (users[-1])

def greeting():
  print("Please answer these questions for us.")

greeting()



classes = input("What classes have you attended:\n (a) Math \n (b) Science \n (c) English \n (d) History \n (e) Spanish \n (f) Theology \n")
#This function is the beginning of the code
def greeting():
  print("Please answer these questions for us.")

#Call the function to Run
"""
if (a) Math input = print("What's your GPA in Science?")
#person inputs GPA
if (b) Science input = print("What's your GPA in Science?")
#person inputs GPA
if (c) English input = print("What's your GPA in English?")
#person inputs GPA
if (d) History input = print("What's your GPA in History?")
#person inputs GPA
if (e) Spanish input = print("What's your GPA in Spanish?")
#person inputs GPA
if (f) Theology input = print("What's your GPA in Theology?")
#person inputs GPA
"""
