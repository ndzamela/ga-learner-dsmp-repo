# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data_file='path' # path for the file

data = np.genfromtxt(path, delimiter=",", skip_header=1,dtype=str)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

#New record
new_record = [[50, 9,4, 1,  0,  0, 40,  0]]
print(new_record)
#Code starts here
census = np.concatenate((new_record, data), axis=0)
print(census)


# --------------
#Code starts here
import numpy as np

#age = census[:,0]
#age = census[:,0:1]
#age=np.array(census[:,0])

age = np.asarray(census[:,0]).astype(np.float32)

max_age= np.max(age)

min_age = np.min(age)

age_mean = round(np.mean(age),2)+0

age_std = round(np.std(age),2)+0

print('The max age is: ',max_age)
print('The min age is: ',min_age)
print('The mean of age is: ',age_mean)
print('The std de of age is: ',age_std)


# --------------
#Code starts here

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0 = len(race_0)
print(len_0)
len_1 = len(race_1)
print(len_1)
len_2 = len(race_2)
print(len_2)
len_3 = len(race_3)
print(len_3)
len_4 = len(race_4)
print(len_4)

race_list = [len_0,len_1,len_2,len_3,len_4]

minority_race = race_list.index(min(race_list))
print(minority_race)    




# --------------
#Code starts here
import numpy as np

senior_citizens = census[census[:,0].astype(int) > 60] 
print(senior_citizens)
working_hours_sum = np.sum(senior_citizens[:,6].astype(int))
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len 

print(avg_working_hours)


# --------------
#Code starts here

high=census[census[:,1].astype(int) >10]
print(high)

low=census[census[:,1].astype(int) <=10]
print(low)

avg_pay_high = np.mean(high[:,7].astype(int))
avg_pay_low = np.mean(low[:,7].astype(int))

print(avg_pay_high.round(2))
print(avg_pay_low.round(2))


