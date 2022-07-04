# Notes from Corey Schafer's Python Course
# https://www.youtube.com/c/Coreyms


student = {'name' : 'John', 'age' : 25, 'courses' : ['Math', 'CompSci']}

# Print all key value pairs
print(student)
# Output
# {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Print just student name
print(student['name'])
# Output
# John

# Create error, phone does not exist
# print(student['phone'])
# Throws exception

# To prevent errors from killing the program, you can use the dictionaires get method
# working example, if the key is not in the var, then non will be returned
print(student.get('name'))
# Output
# John

# This will output Not Found if the key is not listed, but name is
print(student.get('name', 'Not Found'))
# output
# John

# Example of missing key
print(student.get('phone', 'Not Found'))
# output
# Not Found

# Add new key to dictionary
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))
# output
# 555-5555

# Update value
student['name'] = 'Jane'
print(student.get('name', 'Not Found'))
# output
# Jane

print(student)
# output
# {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}

# Use the update method to update more the one value
student.update({'name' : 'Jane', 'age' : 26, 'phone' : '555-5554'})
print(student)
# output
# {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5554'}

# delete key with del
del student['age']
print(student)
# output
# {'name': 'Jane', 'courses': ['Math', 'CompSci'], 'phone': '555-5554'}

# delete key with pop methdo
fix_student = student.pop('phone')
print(fix_student)
print (student)
# output
# 555-5554
# {'name': 'Jane', 'courses': ['Math', 'CompSci']}


#reset student
student = {'name' : 'John', 'age' : 25, 'courses' : ['Math', 'CompSci']}

# list number of keys
print(len(student))
# output 
# 3 (total of 3 keys)

# print out all keys
print(student.keys())
# output
# dict_keys(['name', 'age', 'courses'])

# print out all values
print(student.values()) 
# output
# dict_values(['John', 25, ['Math', 'CompSci']])

# print out all keys and values
print(student.items())
# output
# dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

# loop through key value pair
for key, value in student.items():
    print(key, value)

# output
# name John
# age 25
# courses ['Math', 'CompSci']