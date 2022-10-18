#grocery list
list={}

while True:
    try:
        item=input("").upper()
        if item in list:
            list[item]+=1  
        else:
            list[item]=1
    except EOFError:
        break
for i in sorted(list):
    print(list[i],i)
#for i in list(list):
#    print(i.upper())