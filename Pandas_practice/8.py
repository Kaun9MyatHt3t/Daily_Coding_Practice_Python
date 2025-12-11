# Add a column Bonus which is 10% of the Salary

from common_data import employee_df as df

df['Bonus'] = df['Salary'] * 0.1

print(df.head())