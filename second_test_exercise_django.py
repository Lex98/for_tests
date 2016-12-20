"""a)"""
Student.objects.all().count()

"""b)"""
Student.objects.filter(faculty__title='faculty1').count()

"""c)"""
students = []
for student in Student.objects.select_related('faculty').all():
    stud_dict = {'first name': student.first_name, 'last name': student.last_name, 'faculty': student.faculty.title}
    students.append(stud_dict)

"""d)"""
for faculty in Faculty.objects.prefetch_related('student_set'):
    print('Faculty name: {}, students count: {}'.format(faculty.title, faculty.student_set.all().count()))
