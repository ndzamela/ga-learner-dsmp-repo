# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#print(data)

data['Gender'].replace('-','Agender',inplace=True)
#print(data)
gender_count = data['Gender'].value_counts()
print(gender_count)

plot_gender_count = gender_count.plot(kind='bar', title="Total number per gender", figsize=(7,5))
plt.xticks(fontsize=10, rotation=45)
plt.show()

#Code starts here 




# --------------
#Code starts here

alignment = data['Alignment'].value_counts()
plot = alignment.plot.pie(title='Character Alignment', figsize=(5, 5))


# --------------
#Code starts here
sc_df=data[['Strength','Combat']].copy()

sc_covariance=sc_df.cov().iloc[0,1]

sc_strength=sc_df['Strength'].std()

sc_combat=sc_df['Combat'].std()

sc_pearson=sc_covariance/(sc_combat*sc_strength)
print(sc_pearson)

ic_df=data[['Intelligence','Combat']].copy()

ic_covariance=ic_df.cov().iloc[0,1]

ic_intelligence=ic_df['Intelligence'].std()

ic_combat=ic_df['Combat'].std()

ic_pearson=ic_covariance/(ic_combat*ic_intelligence)
print(ic_pearson)





# --------------
#Code starts here

total_high = data['Total'].quantile(q=0.99)
#print(total_high)

super_best =data[data['Total'] > total_high]
#print(super_best)

super_best_names = ['Amazo','Geneal Zod','Martuan Manhunter','Stardust','Superboy-Prime','Superman']
print(super_best_names)


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3,figsize=(20,8))

ax_1.boxplot(super_best['Intelligence'])
ax_1.set(title='Intelligence')

ax_2.boxplot(super_best['Speed'])
ax_2.set(title='Speed')

ax_3.boxplot(super_best['Power'])
ax_3.set(title='Power')


