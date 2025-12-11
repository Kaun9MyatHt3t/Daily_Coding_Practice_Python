import numpy as np

from common_data import employee_df as df

import pandas as pd

new_row = pd.DataFrame([{
    "Name" : "Rosy",
    "Department" : "IT",
    "Salary" : np.nan
}], index=["4"])

df = pd.concat([df, new_row])

avg_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(avg_salary)
print(df)
