# Group employees by Department and compute the average and maximum salary in each department

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary': [120000, 85000, 95000, 70000, 90000, 110000]
}

df = pd.DataFrame(data)

grouped_df = df.groupby(['Department'])
new_df = grouped_df['Salary'].agg(['mean', 'max'])

print(new_df)