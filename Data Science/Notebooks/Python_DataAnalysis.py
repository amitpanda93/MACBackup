# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:07:53 2019

@author: Adminstrator
"""

#Data Analysis
#pandas
#numpy
data types - int, float, str
data structures - list, tuple, dict 
pandas, numpy  
#pandas
#advantages
#put cap on the amount of data it can hold 
#time-series functionality
#same ds handle both time-series and non-time series data 
#flexible handling of missing data
#arithmetic, merge, sort operations 

#2 data structures in pandas
#Series
#DataFrame

import pandas as pd
#or
#from pandas import Series, DataFrame

#create series data sctructure
#1-d array object
#creating series using array method
dat = pd.Series([1,2,3,4])
dat
dat.values
dat.index

#Series cannot take more than one data type 
dat2 = pd.Series([1,2,3,4],['a','b','c','d'])
dat2

dat3 = pd.Series([-4,9,12,5], index = ['a','b','c','d'])
dat3

dat3['a']
dat3['d']

dat3[['a','d']]
dat3[:]
dat3
dat4 = dat3 * 2
dat4

#check for conditions 
#display all values greater than 6
dat3[dat3 > 6]

'b' in dat3
12 in dat3

#creating series using dict method
sdata = {'Meghalaya' : 38,'Sikkim' :30 ,'Arunachal': 35,'Mizoram' : 42}
tempdata = pd.Series(sdata)
tempdata
states = ['Meghalaya','Sikkim','Arunachal','Mizoram','Nagaland']
tempdata2 = pd.Series(sdata, index = states)
tempdata2

#approach 1
tempdata2.isnull()
tempdata2.notnull()

#approach 2
pd.isnull(tempdata2)
pd.notnull(tempdata2)


tempdata
tempdata2

tempdata + tempdata2

tempdata.name = 'Temperature'
tempdata

tempdata.index.name = 'States'
tempdata

#index altered by assignment 
tempdata.index = ['Bob','Cathy','David','Freddy']
tempdata

#DataFrame
#represents a tabular, spread-sheet like data structure
#has both row index and column index
#it can thought of a dict of series or more than one series
#one or more 2d blocks

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year' : [2000,2001,2002,2001,2002],
                 'pop' :  [1.5,1.7,3.6,2.4,2.9]}

frame = pd.DataFrame(data)
frame

#rearrange columns
pd.DataFrame(frame,  columns = ['year','state','pop'])

frame2 = pd.DataFrame(data, columns = ['year','state','pop','debt'],
                      index = ['one','two','three','four','five'])

frame2
frame2.columns

#both give same result
frame2['state']
frame2.state

#rows can also be retrieved
frame2.ix['three']

#fill the null values
frame2['debt'] = 16.5   #assignment in dataframe of series changes the complete column or all rows
frame2['debt']

import numpy as np
np.arange(5.)
np.random.randn(5,4)

frame2['debt'] = np.arange(5.)
frame2['debt']

val = pd.Series([-1.2,-1.5,-1.7], index = ['two','four','five'])
frame2['debt'] = val
frame2
#Creating new column whose values are of type bool
frame2['eastern'] = frame2.state == 'Ohio'
frame2
      
#nested dict method 
pop = {'Nevada' : {2001 : 2.4, 2002 : 2.9},
       'Ohio' : {2000: 1.5, 2001 : 1.7, 2002 : 3.6}}      
pop      

frame3 = pd.DataFrame(pop)
frame3      
frame2
      
frame3.T
frame3.index.name = 'year'      
frame3
frame3.columns.name = 'state'
frame3


frame3.values
frame2.values

#input/ouput 
#data summary statistics
#merge,sort
#handling missing values
#groupby, aggregate
#data transformation
#visualization 

import pandas as pd
import os

#set working directory
os.chdir("C:\\Python Trainer\\mlarmy\\Online Class\\Python")

#read the dataset 
df_data = pd.read_csv('Data.csv')

#General dataframe functions
#Preprocessing-1
df_data.shape
df_data.head()
df_data.head(10)
df_data.tail()

df_data.columns
df_data.dtypes
df_data.info()
#gives summary statistics 
df_data.describe()
#null value check
df_data.Income.isnull().sum()
df_data.isnull().sum()
#access values index
#Preprocessing - 2
#iloc, loc
#iloc - select based on integer location
#: - all
df_data.iloc[0,4]
#4th row all cols
df_data.iloc[3]
#or
df_data.iloc[3,:]

#all rows 5th col
df_data.iloc[:,4]

df_data.iloc[:,:3]

df_data.iloc[2:5,8:]
#or
df_data.iloc[[2,3,4],[5,6,7]]

#loc
df_data.loc[2,"Income"]
df_data.loc[[4,5,6],["Income","Personal Loan"]]

#Income > 200
df_data.loc[df_data['Income'] > 200,["Income","Personal Loan"]]
#count of income > 200
(df_data.loc[df_data['Income'] > 200,["Income","Personal Loan"]]).count()

#count of income between 100 and 200 - assignment 
#what is the avg experience of customers whose income is greater than 200
#and what are your observations 
#how many rows where Age is greater than income 

#Boolean Indexing
#Group by
#filter
#query
#handling null values

#Boolean Indexing
#or - |
#and - &
sum((df_data.Experience > 10) | (df_data.Income > 100))
sum(df_data.Age.isnull())

#Display rows  based on or condition
df_data.loc[(df_data.Experience > 10) | (df_data.Income > 100),["Experience","Income"]][:10]

sum((df_data.Experience > 10) & (df_data.Income > 100))

df_data.loc[(df_data.Experience > 10) & (df_data.Income > 100),["Experience","Income"]][:10]

#not - ~
#displayrows where Income > 200 and still not gotten a loan
(df_data.Income > 200) & (~(df_data["Personal Loan"] == 1))
sum((df_data.Income > 200) & (~(df_data["Personal Loan"] == 1)))
#Total no of people whose income > 200
sum(df_data.Income > 200)
#displayrows where Income > 200 and still not gotten a loan
df_data.loc[(df_data.Income > 200) & (~(df_data["Personal Loan"] == 1)),["Family","CCAvg","Personal Loan","Income","Experience"]]
#displayrows where Income > 200 and gotten a loan
df_data.loc[(df_data.Income > 200) & (df_data["Personal Loan"] == 1),["Family","CCAvg","Personal Loan","Income","Experience"]]

#isin()
df_data.loc[df_data.Income.isin([21,193]),["CreditCard","Personal Loan"]]

#query
df_data.query('Income > Experience')
df_data.query('Income > Experience').loc[:,"ID"].count()
df_data.query('Income > Experience').shape[0]

#filter
df_data.filter(items = ['Income','Experience'])[:4]

#rename columns
df_data.rename(columns = {'Income' : 'Earnings','Family' : 'Dependants'})[:4]

#unique()
df_data.Family.unique()
df_data.Education.unique()

#duplicate
sum(df_data.Family.duplicated())
sum(df_data.ID.duplicated())

#groupby
df_data.groupby(by = ['Family']).count()
df_data.groupby(by = ['Family','Education']).count()
df_data.groupby(by = ['Family','Education']).mean().loc[:,['Age','Income']]


#checkout and compare the Education and Income of customers
#whose income > 200
df_data.loc[df_data.Income > 200,['Income','Education']]

#overal avg age of customers
df_data.Age.mean()

#average age of people who has 1 Family member and Education is 2
#without using groupby
df_data.loc[(df_data.Family == 1) & (df_data.Education == 2)].Age.mean()

#read a dataset with null values
df_na_data = pd.read_csv("DataWithMissingValues.csv")
#get null values for one column
sum(df_na_data.Age.isnull())
#get null values for all columns
df_na_data.isnull().sum()

#drop or fill 
#dropna() or fillna()

#dropna()
#how=any will delete row with any column = na
df_na_data.dropna(axis = 0, how = 'any').shape
#check the null values after dropna
df_na_data.dropna(axis = 0, how = 'any').isnull().sum()

#how=all deletes row with all columns = na
df_na_data.dropna(axis = 0, how = 'all').shape

df_na_data.isnull().sum()

df_na_data.Age.isnull().sum()
mean_age = df_na_data.Age.mean()
df_na_data.Age.fillna(mean_age, inplace = True)
df_na_data.Age.isnull().sum()

df_na_data.Experience.isnull().sum()
df_na_data.Experience.fillna(method = 'ffill', inplace = True)


#fill null values of other 3 columns 
#Income - calculate avg salary based on family 
#CCAvg - median
#Mortgage - Mode

#any() all()
df_na_data.isnull().sum()
df_na_data.isnull().any()
df_data.isnull().any()
df_data.notnull().all()
#extract records if there is atleast one null value
df_data.loc[:,df_data.notnull().any()][:4]
df_na_data.loc[:,df_na_data.notnull().any()][:4]
#Merge, Concatenation, joins 
os.chdir("C:\Python Trainer\mlarmy\Online Class\Python\Pandas\pandas - Introduction")

week1 = pd.read_csv("Restaurant - Week 1 Sales.csv")
week1.head()
week2 = pd.read_csv("Restaurant - Week 2 Sales.csv")
week2.head()
customers = pd.read_csv("Restaurant - Customers.csv")
customers.head()
customers.ID.duplicated().sum()
foods = pd.read_csv("Restaurant - Foods.csv")
foods.head()
foods["Food ID"].duplicated().sum()
pd.options.display.max_rows = 50

len(week1)
len(week2)
pd.concat([week1, week2], ignore_index = True, keys = ["1st Week", "2nd Week"])

#append() - works same as concat()
week2.append(week1, ignore_index = True)

#Joins
#inner join, outer join, left join, right join 
week1.head()
week2.head()
#merge on single column
pd.merge(week1, week2, how = "inner", on = "Customer ID", suffixes = ('-week1','-week2'))
#155 is duplicate - why
week1.loc[week1["Customer ID"] == 155]
week2.loc[week2["Customer ID"] == 155]
week1.loc[week1["Customer ID"] == 77]
week2.loc[week2["Customer ID"] == 77]

#example
df1 = pd.DataFrame({'A' : [2,3,4,2,2], 'B' : [5,6,7,8,9]})
df2 = pd.DataFrame({'A' : [2,2,3,14], 'B' : [15,16,17,18]})
df1
df2
pd.merge(df1, df2, how = 'inner', on = 'A')

#merge on multiple columns
pd.merge(week1, week2, how = "inner", on = ["Customer ID","Food ID"], suffixes = ('-week1','-week2'))
week1.loc[week1["Customer ID"] == 304]
week2.loc[week2["Customer ID"] == 304]

#outer join
merged = pd.merge(week1, week2, how = 'outer', on = ["Customer ID"], indicator = True)
#LIst of customers who visited my rest only once(either week1 or week2)
mask = merged[merged._merge.isin(["left_only","right_only"])]

#left join
pd.merge(week1, foods, how = "left", on = "Food ID", sort = True)
#right join
#try it

#left_on and right_on parameters
week2.head()
customers.head()
pd.merge(week2, customers, how = "left", left_on = "Customer ID", right_on = "ID")










