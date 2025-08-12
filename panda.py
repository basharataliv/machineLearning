import pandas as pd

# Series: one-dimensional labeled array
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

# DataFrame from dict of lists
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'LA', 'SF']}
df = pd.DataFrame(data)
print(df)

# DataFrame from list of dicts
records = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob',   'Age': 30}
]
df2 = pd.DataFrame(records)
print(df2)
