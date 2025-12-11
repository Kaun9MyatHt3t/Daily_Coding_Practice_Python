# Using .iloc , select rows 2 to 4 and columns 1 to 4

from common_data import employee_df as df
print(df)
print(df.iloc[2:4, 1:4])