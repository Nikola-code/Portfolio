#adieu, adieu
name_list=[]
while True:
    try:
        name=input("Name: ")
        name_list.append(name)
    except EOFError:
        print("Adieu, adieu, to ",end="")
        for name in name_list[:-1]:
            print(name,end=", ")
        if len(name_list)==1:
            print(name_list[0])
        else:
            print("and",name_list[-1])
        break