###  string case change & verify starts & end string



x = " Kapil Malviya from Indore Madhya Pradesh "

print(x.upper())       #  KAPIL MALVIYA FROM INDORE MADHYA PRADESH                   
print(x.lower())       #  kapil malviya from indore madhya pradesh
print(x.swapcase())    #  kAPIL mALVIYA FROM iNDORE mADHYA pRADESH
print(x.title())       #  Kapil Malviya From Indore Madhya Pradesh
print(x.capitalize())  #  kapil malviya from indore madhya pradesh



## checking starting and ending part of the string :

print(x.startswith('kapil'))             # False
print(x.startswith('Kapil '))            # False
print(x.startswith(' Kapil '))           # True
print(x.endswith('Madhya Pradesh '))     # True
