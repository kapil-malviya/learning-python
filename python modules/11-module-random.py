# program to generate a 6 alphanumeric random value as otp :

"""
position 1, 3, 5 are alphabet symbols
position 2, 4, 6 are digits

ex =>> A7C8X3

"""

from random import *
for x in range (8) :
	print(chr(randint(65, 90)),randint(0, 9),chr(randint(65, 90)),randint(0, 9),chr(randint(65, 90)),randint(0, 9))


"""
P 2 Y 7 E 5
C 4 B 5 G 6
N 7 M 0 A 9
E 2 W 8 H 3
R 7 O 1 B 2
K 5 P 8 V 7
Q 7 S 3 G 7
E 4 T 4 J 1

"""
