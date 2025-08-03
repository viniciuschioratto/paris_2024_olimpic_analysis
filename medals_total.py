import pandas as pd

df = pd.read_csv("dataset/medals_total.csv")

#print(type(data))
#print(data)

#print(df.head(10)) # Display the first 10 rows of the DataFrame

#print(df.columns) # Display the column names of the DataFrame

#print(df.tail(10)) # Display the last 10 rows of the DataFrame

#print(df.sort_values(by="Bronze Medal", ascending=False)) # Sort the DataFrame by the "Bronze Medal" column in descending order

#print(df.info()) # Display information about the DataFrame, including the number of non-null entries and data types of each column

#print(df[["country", "country_code"]]) # Display the "country" and "country_code" columns of the DataFrame


one_gold_medal = df[df["Gold Medal"] == 1] # Filter the DataFrame to include only rows where "Gold Medal" is equal to 1
#print(one_gold_medal)

only_u = df[df["country_code"].str.startswith("U")] # Filter the DataFrame to include only rows where "country_code" starts with "U"
#print(only_u)

more_than = df[df["Total"] > 25] # Get the rows where the "Total" column is greater than 25
#print(more_than)

complex_exp = df[(df["Gold Medal"] > 0) & (df["Total"] > 10)] # Get the rows where "Gold Medal" is greater than 0 and "Total" is greater than 25
print(complex_exp)
