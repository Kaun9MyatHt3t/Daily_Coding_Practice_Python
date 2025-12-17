# Merge two dataframes : one containing employee details , another containing their project count

import pandas as pd

# Dataframe 1: Employee Details
df_employees = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Dept': ['Eng', 'Sales', 'HR', 'Eng']
})

# Dataframe 2: Project Counts
df_projects = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 105], # 105 is a ghost employee, 104 is missing
    'Project_Count': [5, 2, 8, 1]
})


merged_data = pd.merge(
    df_employees,
    df_projects,
    on= 'Employee_ID',
    how = "left"
)

merged_data['Project_Count'] = merged_data['Project_Count'].fillna(0).astype(int)

print(merged_data)