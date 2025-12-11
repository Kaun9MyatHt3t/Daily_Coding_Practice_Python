# Add a new row
import pandas as pd

from common_data import employee_df as df

new_row = pd.DataFrame([{
    "Name" : "Rosy",
    "Department" : "IT",
    "Salary" : 70000
}], index=["4"])

df = pd.concat([df, new_row])
print(df)

