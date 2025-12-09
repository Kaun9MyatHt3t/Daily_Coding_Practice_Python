# Select multiple columns from a DataFrame and return as a new DataFrame
from common_data import employee_df

b = employee_df[["Name", "Salary"]]
print(b)