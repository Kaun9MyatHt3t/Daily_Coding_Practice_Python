# Retrieve rows where the salary is greater than the average salary

from common_data import employee_df as df

avg_salary = df["Salary"].mean()
print(df[df["Salary"] > avg_salary])