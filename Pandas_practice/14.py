# create a pivot table showing average salary for each department and gender

import pandas as pd

df = pd.DataFrame({
    'Department': ['Engineering', 'Engineering', 'Sales', 'Sales', 'HR', 'HR', 'Engineering', 'Sales'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'F', 'M'],
    'Salary': [120000, 115000, 85000, 92000, 70000, 72000, 110000, 88000]
})

pivot = df.pivot_table(
    index = 'Department',
    columns = 'Gender',
    values = 'Salary',
    aggfunc = 'mean'
)

print(pivot)