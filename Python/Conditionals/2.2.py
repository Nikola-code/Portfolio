greeting = input("Greeting: ")

if greeting[0:5] == "Hello" or greeting[0:5] == "hello":
    print("0")
elif greeting[0] == "H" or greeting[0] == "h":
    print("20")
else:
    print("100")
