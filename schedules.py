import pandas as pd

df = pd.read_csv("dataset/schedules.csv")

#grouped_by_day = df.groupby("day")  # Group the DataFrame by the "day" column

#print(grouped_by_day) # Display the grouped DataFrame
#print(type(grouped_by_day))  # Display the type of the grouped object

#for day, group in grouped_by_day:  # Iterate over each group in the grouped DataFrame
    #print(f"Day: {day}")  # Print the day
    #print(group)  # Print the group DataFrame for that day
    #print()  # Print a newline for better readability

grouped_by_day_status = df.groupby(["day", "status"])  # Group the DataFrame by both "day" and "status"

for value, dataFrame in grouped_by_day_status:  # Iterate over each group in the grouped DataFrame
    print(value)  # Print the day and status
    #print(dataFrame) # Print the group DataFrame for that day and status
    print()  # Print a newline for better readability
