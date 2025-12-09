# Filtering
import pandas as pd
from common_data import employee_df as df

print(df[df["Salary"] > 70000])