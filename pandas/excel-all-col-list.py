
# exporting data (all column data) column wise from excel to the python list


import pandas as pd

data = pd.read_excel('example.xlsx')

column_data = {}

for col in data.columns:
    column_data[col] = data[col].tolist()


for col, data in column_data.items():
    print(col, data, '\n')
