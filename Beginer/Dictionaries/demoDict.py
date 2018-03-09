student = {'name': 'John','age':25,'courses':['Math','Programming']}

#student['phone'] = '555-660'
student.update({'name': 'Jane','age': 26,'phone':'333-222'})
del student['age']

print(student)