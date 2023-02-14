### output types

# print() function



# form 1

# print() # without any arguments => new line will be inserted / line separator




# # form 2

# print(" Hello \n I'm Kapil I am from Indore")  
# #   \n in string will change the  line

# print(" SRK isn't from \t Bollywood")
# #   \t in string will add (tab) space

# print("kapil"+"malviya")  # kapilmalviya
# print('kapil'*3,'\n')     #kapilkapilkapil

#   + =>> both argument must be string type
#   * =>> one argument must be string type & another argument must be int type

# print('kapil'+'malviya\n')  # kapilmalviya
# print('kapil','malviya','\n\n')    # kapil malviya (comma(,) is adding space)

# a,b,c=8,18,88
# print('Three numbers are : ',a,b,c)  # =>> 8 18 88  (here bydefault space is the separator)


### form 3

###  sep attribute (sep=',') (sep=':') (sep="'")



# print(a,b,c,sep=',')  # =>> 8,18,88  (here comma(,) is the separator)
# print(a,b,c,sep="'")  # =>> 8'18'88  (here (') is the separator)




### end attribute (end='') (end=' ') (end=',') 



# print('Hello',end=' ')
# print('Kapil..',end='   ')
# print('Where',end=' ')
# print('are',end='')
# print('you',end=' ')
# print('from',end=' ')
# print('?',end='?')


#####  end & sep attribute difference


# print(10,20,30,40,50,sep=',',end='   ')
# print(160,170,180,190,200,sep=':')

# print(10,20,30,40,50,sep=',',end='... .. ...')
# print(160,170,180,190,200,sep=':',end='...')

## end attributes talks about line and sep attribute talks about (within print)

# e=[10,20,30,40]
# s=(10,20,30,40)
# a={10,20,30,40}

# print(e,end='')
# print(s,end='')
# print(a)
# print(e,s,a)



##$$ formate

name='munna'
salary=10000
gf='munni'
print('Hello {} your salary is {} and your girlfriend  {} is waiting.'.format(name,salary,gf))

print('Hello {1} your salary is {2} and your girlfriend  {0} is waiting.'.format(name,salary,gf))