###  string


email=input('Enter your email id : ')

print('Your email id is : ',email)   # if user input is in upper case it will return output in Upper case

# converting all characters of email id to lower case via ^^ lower function

email1=email.lower()

print('Your email id is : ',email1)  # here, with the help of lower(), it will retun in lower case


### string spliting  (index slicing & spliting)


part=email[:3]   # 0, 1, 2
print()
print(part)

part=email[2:5]
print()
print(part)

part1=email.split(',')
print()
print(part1)      ## return will be in list


