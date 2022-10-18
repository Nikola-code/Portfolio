#little professor
import random
def main():
    score=0
    level=get_level()
    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)    
        for j in range(3):
            print(x,"+",y,"= ",end="")
            try:
                user_result=int(input(""))
            except ValueError:
                print("EEE")
                if j==2:
                    print(x,"+",y,"= ",(x+y))
                    break
            if user_result==(x+y):
                score+=1
                break
            else:
                print("EEE")
                if j==2:
                    print(x,"+",y,"= ",(x+y))
                    break
    print("Score:",score)

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level not in [1,2,3]:
                continue
            else:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    try:
        if level==1:
            n=random.randint(0,9)
        elif level==2:
            n=random.randint(10,99)
        elif level==3:
            n=random.randint(100,999)
    except ValueError:
        pass
    return n
if __name__ == "__main__":
    main()
