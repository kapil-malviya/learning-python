# Precedence order of operators

x=10+98/2-3*4
a=30
b=20
c=10
d=5


print(x)            # 47.0
print((a+b)*c/d)    # 100.0
print(a+(b*c)/d)    # 70.0



# The precedence order is described in the table below, 
#  starting with the highest precedence at the top:

#  Operators	                          Description	
#     ()	                                Parentheses	
#     **	                                Exponentiation	
#     +x  -x  ~x	                        Unary plus, unary minus, and bitwise NOT	
#     *  /  //  %	                        Multiplication, division, floor division, and modulus	
#     +  -	                                Addition and subtraction	
#     <<  >>	                            Bitwise left and right shifts	
#     &                                 	Bitwise AND	
#     ^	                                    Bitwise XOR	
#     |                                  	Bitwise OR	
#     ==  !=  >  >=  <  <=                 	Comparisons operators	
#     is  is not                            Identity operators 
#     in  not in                            Membership operators 
#     not	                                Logical NOT	
#     and	                                Logical AND	
#     or	                                Logical OR


# If two operators have the same precedence, the expression is evaluated from left to right.