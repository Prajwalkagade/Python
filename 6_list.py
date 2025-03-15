# lists are mutable that means you can change them and list contain different data types at same &its wriiten in '[]'
demo=["prajwal"," ajit",5,555.45,True,"yash","ram","aditya"]
print(demo)
# indexing
print(demo[0]) #prajwal
print(demo[0:5])#exclude last one (['prajwal', ' ajit', 5, 555.45, True])
#  we can replace the element of list
demo[1]="amit"
print(demo) #['prajwal', 'amit', 5, 555.45, True, 'yash', 'ram', 'aditya']
