#outdated
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:    
        date=input("Date: ")
        if date[0].isnumeric():
            month,day,year=date.split("/")
            if int(day)>31 or int(day)<1 or int(month)>12 or int(month)<1 or int(year)<0:
                continue
            print(year+"-"+f"{int(month):02}"+"-"+f"{int(day):02}")
            break
        else:
            month,day,year=date.split(" ")
            day=day[:-1]
            if int(day[:-1])>31 or int(day[:-1])<1:
                continue
            print(year+"-"+f"{months.index(month)+1:02}"+"-"+f"{int(day):02}")
            break
    except ValueError:
        pass