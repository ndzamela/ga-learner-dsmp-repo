# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here

data = pd.read_csv(path)

data.hist(column='Rating', bins=10, figsize=(10,10))
plt.show()

data = data[data['Rating'] <=5]
data.hist(column='Rating', bins=10, figsize=(10,10))
plt.show()

#Code ends here


# --------------
# code starts here

total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null], axis=1,keys=['Total','Percent'])

print(missing_data)

# Drop the null values from data
data1 = data.dropna()

total_null_1 = data1.isnull().sum()

percent_null_1 = (total_null_1/data1.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1,keys=['Total','Percent'])

print(missing_data_1)
# code ends here


# --------------

#Code starts here

g = sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)

g.set_titles("Rating vs Category")


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#print(data['Installs'].value_counts())

#Remove , and + from Installs column of 'data'
data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#print(data['Installs'].value_counts())

#Plot the regplot 
plt.figure(figsize =(10,10))
reg = sns.regplot(x="Installs", y="Rating", data=data)
plt.title("Rating vs Installs [RegPlot]", size = 20)
plt.show()

#Code ends here



# --------------
#Code starts here
#Removing the dollar sign from the column
data['Price'] = data['Price'].str.replace('$','')

#Converting the column to float
data['Price'] = data['Price'].astype(float)

#Setting the figure size
plt.figure(figsize = (10,10))

#print(data['Price'].value_counts())

#Using seaborn, plot the regplot
reg = sns.regplot(x="Price", y="Rating", data=data)
plt.title("Rating vs Price [RegPlot]", size = 20)
plt.show()
#Code ends here


# --------------

#Code starts here

print(len(data['Genres'].unique()), "genres")

#Splitting the column to include only the first genre of each app
data['Genres'] = data['Genres'].str.split(';').str[0]

#Grouping Genres and Rating
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean=gr_mean.sort_values('Rating')

print(gr_mean.head(1))

print(gr_mean.tail(1))


#Code ends here


# --------------

#Code starts here

#Converting the column to datetime format
data['Last Updated'] = pd.to_datetime(data['Last Updated'])

#Creating new column having `Last Updated` in days
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated']).dt.days 

#Setting the size of the figure
plt.figure(figsize = (10,10))

#Plotting a regression plot between `Rating` and `Last Updated Days`
sns.regplot(x="Last Updated Days", y="Rating", color = 'lightpink',data=data )

#Setting the title of the plot
plt.title('Rating vs Last Updated [RegPlot]',size = 20)



#Code ends here


