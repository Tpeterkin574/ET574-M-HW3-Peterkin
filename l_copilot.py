#list of three students named John, Kim and Lee
students = ['John', 'Kim', 'Lee']
students[1] = 'Kim'
students.append('Sara')
students.append('Miko')
#function to print ‘Hi name’ for each student in the list
def greet_students(student_list):
    for student in student_list:
        print(f'Hi {student}')
    print(f'Total students: {len(student_list)}')

#call the function
greet_students(students)

