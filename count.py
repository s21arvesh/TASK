dict_students = [{'first_name': 'Rahul', 'last_name': 'chauhan', 'age': 21, 'dept': 'MECHANICAL'},
                 {'first_name': 'Sanket', 'last_name': 'Mhatre', 'age': 22, 'dept': 'IT'},
                 {'first_name': 'Yash', 'last_name': 'koli', 'age': 23, 'dept': 'MECHANICAL'},
                 {'first_name': 'Mihir', 'last_name': 'Patil', 'age': 24, 'dept': 'COMPUTER'},
                 {'first_name': 'Aditya', 'last_name': 'Mali', 'age': 25, 'dept': 'CIVIL'},
                 {'first_name': 'Sandeep', 'last_name': 'Gupta', 'age': 25, 'dept': 'CIVIL'}]
dept = [{'dept': 'MECHANICAL', 'phone_num': 11111}, {'dept': 'IT', 'phone_num': 22222},
        {'dept': 'COMPUTER', 'phone_num': 33333}]

final_student = {}
for i in dept:
    the_dictonary = {}
    # print(i['dept'].lower())
    final_list = []
    for students in dict_students:
        if i['dept'].lower() == students['dept'].lower():
            students['phone_num'] = i['phone_num']
            final_list.append(students)
    # print(final_list)
    count = (len(final_list))
    the_dictonary['STUDENT'] = final_list
    the_dictonary['count'] = count
    # print(the_dictonary)
    final_student[i['dept']] = the_dictonary
print(final_student)
