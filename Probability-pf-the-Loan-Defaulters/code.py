# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

# Load the dataframe
df = pd.read_csv(path)

# probability of  fico score greater than 700

p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)

# probability of purpose == debt_consolidation
p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

# Create new dataframe for condition ['purpose']== 'debt_consolidation' 
df1 = df[df['purpose']== 'debt_consolidation']

# Calculate the P(A|B)
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)

# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
#code starts here

# probability of paid_back_loan is Yes
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0] / df.shape[0]
print(prob_lp)

# probability of the credit policy is Yes
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]  / df.shape[0]
print(prob_cs)
# create new dataframe for paid.back.loan == 'Yes'
new_df = df[df['paid.back.loan'] == 'Yes']

# Calculate the P(B|A)
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]

print(prob_pd_cs)

# bayes theorem 

bayes = (prob_pd_cs * prob_lp)/ prob_cs

# print bayes
print(bayes)

# code ends here


# --------------
# code starts here

df.purpose.value_counts(normalize=True).plot(kind="bar")
plt.title("Pobalility Distribution of purpose")
plt.ylabel("Probability")
plt.xlabel("Number of purpose")
plt.show()

df1= df[df['paid.back.loan']=='No']

df1.purpose.value_counts(normalize=True).plot(kind="bar")
plt.title("Pobalility Distribution of purpose")
plt.ylabel("Probability")
plt.xlabel("Number of purpose")
plt.show()
# code ends here


# --------------
# code starts here

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].hist(normed = True, bins=50)
plt.axvline(x=inst_median,color='r')
plt.axvline(x=inst_mean,color='g')
plt.show()

df['log.annual.inc'].hist(normed = True, bins=50)
plt.show()
# code ends here


