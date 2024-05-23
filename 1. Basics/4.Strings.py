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

age=int(input('Enter your age:'))
print(f'Hi there, you are {age} years old!') #f-string, which is a way to format strings in Python
