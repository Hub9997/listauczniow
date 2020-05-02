data = []
#data=[{'name':name,

def add_student(data, name, surname):
    student = {
        'name': name,
        'surname': surname,
        'grades': {}
    }

    data.append(student)


def print_students_console(data):
    for student in data:
        print(f" Name:{student['name']} Surname:{student['surname']}")


def print_student_grades(data, name, surname, course):
    for student in data:
        if name == student['name'] and surname == student['surname']:
            if student['grades'].get(course) is not None:
                print(student['grades'][course])
            else:
                print(f"No course {course}")

            return
    print(f'No such student: {name},{surname}')


def add_grade_to_course(data, name, surname, course, grade):
    for student in data:
        if name == student['name'] and surname == student['surname']:
            if student['grades'].get(course) is not None:
                student['grades'] = {course:grade}


            else:

                  student['grades'].update({course:grade})



add_student(data, name="Mateusz", surname="B")
add_student(data, name='Hubert', surname='K')
add_student(data, name = 'Ewelina', surname = 'O')
add_grade_to_course(data, name='Mateusz', surname='B', course='biology', grade=5)
add_grade_to_course(data,name='Ewelina',surname='O',course = 'religia',grade=1)
add_grade_to_course(data,name='Ewelina',surname='O',course = 'math',grade=6)
add_grade_to_course(data,name='Hubert',surname='K',course = 'math',grade=6)
add_grade_to_course(data,name='Hubert',surname='K',course = 'wf',grade=6)
add_grade_to_course(data,name='Hubert',surname='K',course = 'informatyka',grade=5)


print(print_students_console(data))
print(data)