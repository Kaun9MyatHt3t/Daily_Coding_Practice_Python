# extract the domain from an email column and store it in a new column Domain

import pandas as pd

df = pd.DataFrame({"Email": ['k@gmail.com', 'support@company.org']})

df['Domain'] = df['Email'].str.split('@').str[1]

print(df)