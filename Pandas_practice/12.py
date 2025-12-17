# Sort the dataframe by salary descending and then by name ascending

import pandas as pd
df = pd.DataFrame({
    'Salary' : [3999, 2939, 49030,348, 2940],
    'Name' : ["D", "A","C", "E","B"]
})

ans = df.sort_values(['Salary', 'Name'], ascending = [False, True])
print(ans)