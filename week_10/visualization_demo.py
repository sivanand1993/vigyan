import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# I generally prefer to use seaborn to plot my data, it's nice to be able to put everything into just one line

# import the data and get a feel for what the structure of the dataset is
data = pd.read_csv('CollegeScoreCard_Project.csv')
# I like to start by looking at the head of the data just to see what it's looking like.
print("Head of data:", data.head())

""" Data cleaning section"""
# First we will remove all NA values and fill in any missing data with zeros
# Then we will manipulate some of the data to see correlations and possible points of interest
# to focus on for our plotting.
data.replace({'PrivacySuppressed': 0}, inplace=True)
data.dropna()
data.fillna(0, inplace=True)
print(data.head())
print(data.info())
# Now that we've gotten rid of the invalid values we can analyze the data a bit
# Let's mess around looking at some cities act scores
def max_act(series):
    return series['sat_avg'].max()

def columns(series):
    return series.columns

# Testing a couple types of selections to get specific data about the set.
print(data[data['city'] == 'Boston']['act_med'])

# Curious as to the min and max tuition average by city
print(columns(data))
cities = data.groupby('city')
print('Max SAT = ', max_act(cities))
print(cities.mean()['tuition'].min())
print(cities.mean()['tuition'].max())

"""Using Pandas for insights"""
# I want to group up the cities and do some analysis on those,
# I also want to do some general analysis regarding tuition rates per city and their potential correlations.
print('# of unique cities', data['city'].nunique())
print(data.corr())
cities = data.groupby('city')
print('Max SAT = ', max_act(cities))
print(cities.mean()['tuition'].min())
print(cities.mean()['tuition'].max())
print('Mean tuition rate', data['tuition'].mean())
print('Mean SAT_Score', data['sat_avg'].mean())



"""Graphs"""
# Tuition is on a normal distribution with a bunch of values at 0 which is expected
# Univariate plot
sns.distplot(data['tuition'])
plt.show()
# There are a handful of men_only universities
# Univariate plot
sns.countplot(data['men_only'])
plt.show()
# Univariate plot
sns.distplot(data['non_resident'])
plt.show()
# Bivariate plot
sns.boxplot(x='men_only', y='tuition', data=data, palette='rainbow')
plt.show()

# This plot is pretty messy not ideal for analysis but it looks like men only schools may have a slightly
# higher sat_avg, but that may just be a product of the difficulty to get into the school.
# Bivariate plot
sns.boxplot(x='men_only', y='sat_avg', data=data)

plt.show()

# This shows some really good info, it seems like ACT and SAT scores heavily influence tuition rate
# along with Race surprisingly.
# multivariate plot
sns.heatmap(data.corr(), cmap='coolwarm')
plt.show()
