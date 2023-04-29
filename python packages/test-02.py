# using function f1() which is in module1.py file present in 'com' folder
# using function f2() which is in module2.py file present in 'goldd' folder inside 'com' folder


from com.module1 import f1
from com.goldd.module2 import f2
f1()
f2()


"""  =>> 

hello.. this is from module1 present in com package
hello.. this is from module2 present in com.goldd package

"""