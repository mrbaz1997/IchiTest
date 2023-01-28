import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame()

# Create new data to add to the DataFrame
new_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Add new data to the DataFrame
df = pd.concat([df, new_data])
new_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

df = pd.concat([df,new_data], ignore_index=True)


print(df)
