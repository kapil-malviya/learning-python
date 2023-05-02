
# separating int values in string from list =>> 


my_list = ['5 (Very effective)', '4 (Effective)', '3 (Satisfactory)', '5 (Very effective)', '3 (Satisfactory)']
int_list = []

for element in my_list:
    int_value = int(element[0])  # extracting the first character
    int_list.append(int_value)

print(int_list)  # Output: [5, 4, 3, 5, 3]