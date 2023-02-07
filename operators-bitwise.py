# Bitwise operators

#  ( &, |, ^, ~, <<, >> )
    # applicable only for  int and boolean value

a=4
b=5
c=0
d=True
e=False

#  & (and)  => if both bits are 1, then only 1 otherwise 0
#  |  (or)  => if atleast one bit is 1 then 1 otherwise 0
#  ^ (x-or) => (exclusive or operator means either first-one or second-one but not both)
#              if both arguments(bits) are different then 1 otherwise 0 (zero)
#  ~    => (bitwise compliment operator) 1 replaced with 0 and 0 replaced with 1
#  <<   => (bitwise left shift operator)
#  >>   => (bitwise right shift operator)

print('4 & 5 = ',a&b)   # 4      =>  better understand with the
print('4 | 5 = ',a|b)   # 5         help of truth table with given
print('4 ^ 5 = ',a^b)   # 1         laws for different operators
print()

#  ~ => bitwise compliment operator

print(~a)          # -5  (memory level)
print(~d)          # -2
print(~e)          # -1
print()
print()
print()



## shift operators 
#   <<  => left shift operator
#   >>  => right shift operator

print('10<<2 = ',10<<2)  # left shift 2 means => right hand side vaccant cells fill with 0s (here 00)two zeros   
#  representation of 10 in binary internally
#    => 00000.....0001010 => 10 => shift first two(00) to the last
#    =>   000.....0001010_0_0_ 
#                   32+8      => 40 (output)

print('10>>2 = ',10>>2)  # left hand side vacant cells sign bit
                         # for +ve no. => 0
                         # for -ve no. => 1

#  representation of 10 in binary internally
#    =>   00000.....0001010 => 10 => last two(10) cell will be vacant and in first two vacant cells will be
#                                     added with (00) two zeros because ten(+10) is +ve, so for +ve no. (0)   
#                                     zero is added and for -ve numbers (1) is added
#    =  0000000.....00010_ _ 
#                      2**1  => 2 (output)

print()
print('True << 2 = ',True<<2)     # 4 (1<<2)(same logic)
print('True >> 2 = ',True>>2)     # 0 (1>>2)    ----