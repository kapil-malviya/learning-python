
# exporting single column data of excel file to the python list


import pandas as pd

data = pd.read_excel('example.xlsx')

column_data = data['Communication Skill '].tolist()

print(column_data)