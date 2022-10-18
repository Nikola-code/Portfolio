#fuel gauge
def main():
    while True:
        fuel=input("Fraction: ")
        try:
            percentage=convert(fuel)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x,y=fraction.split("/")
            x,y=int(x),int(y)
            f=round(x/y*100)
            if y>=x:
                return f
            else:
                raise ValueError
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError
def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()
