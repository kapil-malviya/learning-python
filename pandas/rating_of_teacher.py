# extracting data from the excel file (column wise) 


import pandas as pd 


data = pd.read_excel('Anand_Singhai.xlsx')

communication_data_ = data['Communication Skill '].tolist()
quality_data_ = data['Quality of lecture '].tolist()
competency_data_ = data['Competency in Subject '].tolist()
usefulness_data_ = data['Usefulness of Topic/s '].tolist()

#data = pd.read_excel('feedback.xlsx', usecols="D")
#data = pd.read_excel('feedback.xlsx', usecols=[3, 5])



# for communication skill :


print('\n')
print(communication_data_)
print('\n')

communication_data = []
for intiger1 in communication_data_ :
	int_value1 = int(intiger1[0])
	communication_data.append(int_value1)

print(communication_data,'\n')
communication_length = len(communication_data)
print(communication_length)
communication_sum = sum(communication_data)
print(communication_sum)
rating_average_1 = communication_sum / communication_length
print("Average Rating of communication : ", rating_average_1)
rounded_average_1 = round(rating_average_1, 2)
print("Rounded Average Rating of Communication Skill : ",rounded_average_1)


print('-----------------------------------------------------------------------------')
# for quality of lecture : 


print('\n')
print(quality_data_)
print('\n')

quality_data = []
for intiger2 in quality_data_ :
	int_value2 = int(intiger2[0])
	quality_data.append(int_value2)

print(quality_data,'\n')
quality_length = len(quality_data)
print(quality_length)
quality_sum = sum(quality_data)
print(quality_sum)
rating_average_2 = quality_sum / quality_length
print("Average Rating of Quality of lecture : ", rating_average_2)
rounded_average_2 = round(rating_average_2, 2)
print("Rounded Average Rating of Quality of lecture : ",rounded_average_2)



print('-----------------------------------------------------------------------------')

# for competency in subject : 


print('\n')
print(competency_data_)
print('\n')

competency_data = []
for intiger3 in competency_data_ :
	int_value3 = int(intiger3[0])
	competency_data.append(int_value3)

print(competency_data,'\n')
competency_length = len(competency_data)
print(competency_length)
competency_sum = sum(competency_data)
print(competency_sum)
rating_average_3 = competency_sum / competency_length
print("Average Rating of Competency in subject : ", rating_average_3)
rounded_average_3 = round(rating_average_3, 2)
print("Rounded Average Rating of Competency in subject : ",rounded_average_3)




print('-----------------------------------------------------------------------------')

# for Usefulness of Topic/s : 


print('\n')
print(usefulness_data_)
print('\n')

usefulness_data = []
for intiger4 in usefulness_data_ :
	int_value4 = int(intiger4[0])
	usefulness_data.append(int_value4)

print(usefulness_data,'\n')
usefulness_length = len(usefulness_data)
print(usefulness_length)
usefulness_sum = sum(usefulness_data)
print(usefulness_sum)
rating_average_4 = usefulness_sum / usefulness_length
print("Average Rating of Usefulness of Topics : ", rating_average_4)
rounded_average_4 = round(rating_average_4, 2)
print("Rounded Average Rating of Usefulness of Topics : ",rounded_average_4)



print('-----------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------')


# final rating of teacher :

parameters_no = 4
final_sum = (rounded_average_1 + rounded_average_2 + rounded_average_3 + rounded_average_4)
final_rating = final_sum / parameters_no
print('Final Rating of Teacher : ',final_rating)