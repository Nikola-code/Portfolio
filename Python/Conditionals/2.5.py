
def main():
    user_time = input("what time is it? ")
    user_time = convert(user_time)

    if user_time >= 7.00 and user_time <= 8.00:
        print("breakfat time")
    elif user_time >= 12.00 and user_time <= 13.00:
        print("lunch time")
    elif user_time >= 18.00 and user_time <= 19.00:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    converted_minutes = float(minutes)/60
    return float(hours) + converted_minutes

if __name__ == "__main__":
    main()
