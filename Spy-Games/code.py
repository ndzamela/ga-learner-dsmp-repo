# --------------
##File path for the file 
file_path 

#with open(file_path) as f:
    #first_line = f.readline()
#print(first_line)
# function that reads the file content
def read_file(path):
    file = open(file_path,"r")
    sentence = file.readline()
    return sentence
    file.close 
# call function
sample_message = read_file(file_path)
print(sample_message)
#Code starts here


# --------------
#Code starts here
# Path for files
file_path_1
file_path_2

#Call function read_file() and read the paths
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1)
print(message_2)

#Function that implements integer(floor) division
def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return str(quotient)
#Call function 
secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)


# --------------
#Code starts here
#Path for file
file_path_3
#Call funtion to read_file() and read path
message_3 = read_file(file_path_3)
print(message_3)
# Function that substitute message
def substitute_msg(message_c):
    if message_c == 'Red':
        sub ='Army General'
    elif message_c == 'Green':
        sub ='Data Scientist'
    elif message_c == 'Blue':
        sub ='Marine Biologist'
    return sub
 #Call function substitute_msg
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#Call function read_file() to read the file paths
message_4 = read_file(file_path_4)
print(message_4)
message_5 = read_file(file_path_5)
print(message_5)


#Function that compare messages
def compare_msg(message_d, message_e):
    a_list = message_d.split(" ") 
    b_list = message_e.split(" ") 
    c_list = filter(lambda x: x not in b_list, a_list)
    final_msg =  " ".join(c_list)
    return final_msg
secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3 )




# --------------
#Code starts here
# File path for message 4  and message 5
file_path_6

#Code starts here

def extract_msg(message_f):

    a_list=message_f.split() 
    
    even_word=lambda x: (len(x)%2==0)
    
    b_list=filter(even_word, a_list)
    
    final_msg =" ".join(b_list)
    
    return final_msg
#Testing the function
message_6 =read_file(file_path_6)
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)
  


# --------------
#Secret message parts in the correct order
message_parts = [secret_msg_3,secret_msg_1,secret_msg_4,secret_msg_2]
print(message_parts)

final_path = user_data_dir + '/secret_message.txt'

#Code starts here
#with open(path,'a+') as f:
    #first_line = f.append(message_parts)
#print(first_line)

secret_msg = " ".join(message_parts)
#Function that writes a message
def write_file(secret_msg,path):
    file = open(path,'a+')
    file.write(secret_msg)
    file.close
 
#Call function that reads function
write_file(secret_msg, final_path)
print(secret_msg)

#secret_msg = list(extract_msg(secret_msg))



