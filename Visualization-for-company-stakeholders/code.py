# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
#print(data)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind="bar")
#print(loan_status)
plt.show()

#Code starts here


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property_Area')
plt.ylabel('Loan_Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan= education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel('Education')
plt.ylabel('Loan_Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')

not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#For automatic legend display
#plt.legend()
plt.show()


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(15,8))

ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set(title ='ApplicantIncome vs LoanAmount')

ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set(title ='CoapplicantIncome vs LoanAmount')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
#data.head()
#data.plot.scatter(x='TotalIncome', y='LoanAmount', ax=ax_3)
#ax_2.set(title ='TotalIncome vs LoanAmount')
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set(title ='TotalIncome vs LoanAmount')

plt.show()


