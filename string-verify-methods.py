### string verifying methods 



## checking type of character --> alphanumeric, numeric, etc...
#  isalnum() =>> alphanumeric =>> a-z,A-Z,0-9
#  isalpha() =>> only alphabets
#  isdigit() =>> only  digits
#  islower() =>> is it lowercase
#  isupper() =>> is it uppercase
#  istitle() =>> is it title case
#  isspace() =>> contains only spaces..


# print("kapil 88".isalnum())        # =>> False
# print("kapil88".isalnum())         # =>> True
# print("88.88".isdigit())           # =>> F
# print("88 88".isdigit())           # =>> F
# print("88088".isdigit())           # =>> T
# print("".isspace())                # =>> F
# print("    ".isspace())            # =>> T
# print("  38".isspace())            # =>> F
# print("Kapil Malviya".istitle())   # =>> T
# print("malviya kapil".islower())   # =>> T
# print("Kapil Malviya ".isupper())  # =>> F
# print("KAPIL   ".isupper())        # =>> T
# print("123".istitle())             # =>> F
# print("A1288".istitle())           # =>> T


xx = input('Enter any character : ')

if xx.isalnum() :
	print('Alpha numeric character')
	if xx.isalpha() :
		print('Alphabet character')
		if xx.islower() :
			print('Lower case Alphabet character')
		else :
			print('Upper case Alphabet character')
	else :
		print("It's a digit")
elif xx.isspace() :
	print("It's space character")
else :
	print("Non space special character")