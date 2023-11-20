# Finding the length of a string. Putting a limit amount of characters for the user to imput.

course = 'Python for noobs'
print(len(course))

# Printing things in upper case 
print(course.upper())

# printing with the regular way
print(course)

# printing something in all lower case
course_2 = 'PYTHON FOR NOOBS'
print(course.lower())

# finds the letter and says the position
# the find function id case sensitive  
print(course.find('P'))
print(course.find('o'))

# replace function will replace any word you like in the text you specify, you can also replace letters
print(course.replace('Python', 'Javascript')) 

# you can search for text words inside variables, also case sensitive
print('Python' in course)
