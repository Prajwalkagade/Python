# tuple is  same as string i.e. immutable (we cant change tuple) and written in '()' it contains different data types 

a=(1,22.20,"prajwal",True,'yash')
print(type(a)) #<class 'tuple'>
# indexing is allowed 
print(a[2])
print(a[:4]) #it prints 0 to len-1 ie.excluding last
print(a[0:]) # it prints o to end (including last)
