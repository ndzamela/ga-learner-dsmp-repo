# --------------
# Code starts here

# Class 1 list
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
# Class 2 list
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
#Concatenate the 'class_1' and 'class_2'
new_class = class_1 + class_2
print(new_class)
# Append new_class
new_class.append('Peter Warden')
print(new_class)
#Deleter from new_class
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
#Courses dictionary fot Geoffrey Hinton
courses ={'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
total = sum(courses.values())
print(total)
percentage = (total/500)*100
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65, 'Yoshua Benjio': 50,'Hilary Mason': 70, 
'Corinna Cortes': 66, 'Peter Warden': 75 }
#max_marks_scored = max(mathematics.values())
max_marks_scored = max(mathematics.values())
print(max_marks_scored)
topper = max(mathematics, key = mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
# Code starts here
first_name = topper[:-3]
#print (first_name)
#last_name
last_name = topper[7:9]
#print(last_name)
full_name = last_name + ' '+ first_name
#print(full_name )
certificate_name = full_name.upper()
print(certificate_name)

# Code ends here


