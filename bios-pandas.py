import pandas as pd
bios = pd.read_csv('bios.csv')

#print(bios.head())

filtered_data = bios.loc[bios['height_cm'] > 215, ['name','height_cm']]

f_data = bios[bios['height_cm'] > 215][['name','height_cm']]

usa_data = bios[(bios['height_cm'] > 215) & (bios['born_country']=='USA')][['name', 'born_country', 'height_cm']]

print(filtered_data)



coffee = pd.read_csv('coffee.csv')
print('count missing data per column\n',coffee.isnull().sum())

# axis=0 → check column-wise (down the rows)
print("\nMissing values in each column:")
print(coffee.isnull().any(axis=0))

# axis=1 → check row-wise (across columns)
print("\nMissing values in each row:")
print(coffee.isnull().any(axis=1))

# getrows where particular column value is missing
missing_customer = coffee[coffee["Customer"].isnull()]
print('get rows where particular column value is missing')
print(missing_customer)

# get rows where some value is missing
print('get rows where some value is missing')
rows_with_missing = coffee[coffee.isnull().any(axis=1)]
print(rows_with_missing)

# drop missing data
coffee.dropna(inplace=True)
# fill missing data
coffee.fillna(value=0, inplace=True)
print('count missing data per column\n',coffee.isnull().sum())

coffee["PricePlusFive"] = coffee["Price"].apply(lambda x: x + 5)


print(coffee['Customer'])

john_name = coffee[coffee['Customer'].str.contains('John')]
print(john_name)

ends_name = coffee[coffee['Customer'].str.endswith('n')]
print(ends_name)

print('Helo world')
