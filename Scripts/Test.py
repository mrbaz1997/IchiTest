import pandas as pd

# Read existing CSV file into a DataFrame
df = pd.read_csv("existing_data.csv")
print(df)
# Create new data to add to the DataFrame
new_data = pd.DataFrame({'dateTime': ['2023-01-23 10:00:00', '2023-01-23 11:00:00'],
                         'Open': [1.22, 1.23],
                         'Close': [1.25, 1.24]})

# Add new data to the existing DataFrame
df = pd.concat([df, new_data], ignore_index=True)

# Save the updated DataFrame back to the same CSV file
df.to_csv("existing_data.csv", index=False)