from common_data import employee_df as df

print(df.loc[
          (df["Salary"] > 50000) &
          (df["Salary"] < 90000) &
          (df["Department"] == 'IT')
      ])

