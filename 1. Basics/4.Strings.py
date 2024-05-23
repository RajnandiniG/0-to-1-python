#String
course = "Python is for 'all'"
print(course)
#Multi-line string
multi='''
Hello,
I am happy to connect!
See you around.
'''
print(multi)
#extract string value, [start,end index,skip step]
print(course[1:11]) #it skips last index

name='Thomas Peterson'
print(name[1:-3]) #by default will consider -1 last index

#Fuctions with String
course='Python is awesome to learn!'
print(len(course)) #To know the length of string
print(course.upper()) #Convert in uppercase
print(course.lower()) #Convert in lowercase
print(course.find('a')) #Returns index number
print(course.find('z')) #Returns -1 if not found
print(course.replace("Python","Go")) #replace the word
print(course.replace("a","M")) #Replace index value, can't use index no to replace

age=int(input('Enter your age:'))
print(f'Hi there, you are {age} years old!') #f-string, which is a way to format strings in Python
