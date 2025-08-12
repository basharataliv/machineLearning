import pandas as pd
df = pd.DataFrame([[1,2,3],[3,4,5]], columns=['A','B','C'])

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
}

dfdata = pd.DataFrame(data)
print(dfdata)

#print(df)
#print(df.head(1))
#df.info()
#print(df.describe())

coffee = pd.read_csv('coffee.csv')
print(coffee.head())
print(coffee.tail())
print(coffee.sample(4))

# find rows and columns 
# loc[rows, columns] -> both params can passed as list as well with slice etc
# iloc[rows, columns] -> both params can passed as list as well with slice etc and 
# only workds with index

print(coffee.loc[[0,1]])
print(coffee.loc[0:])
print(coffee.loc[:10])
print(coffee.loc[5:10])
print(coffee.loc[[0,1],['Date','Customer']])

#coffee.index = coffee['Date']
#print(coffee.loc['2025-08-01':'2025-08-03', 'Customer'])

coffee.loc[0, 'Price']=5.50

print(coffee.iloc[0,2])

print(coffee.Date)
print(coffee['Date'])

sorted_coffe = coffee.sort_values(['Customer','Date'],ascending=False)
print(sorted_coffe)

for index,row in coffee.iterrows():
    print(index)
    print(row)
    print('\n\n\n')