'''

separating int values from string values :

'''


my_list = [10, "hello", 20, "world", 30]
int_list = []
str_list = []

for element in my_list:
    if isinstance(element, int):
        int_list.append(element)
    elif isinstance(element, str):
        str_list.append(element)

print('int list : ', int_list)  # Output: [10, 20, 30]
print('string list : ', str_list)  # Output: ["hello", "world"]
