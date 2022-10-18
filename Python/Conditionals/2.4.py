expression = input("Expression ")

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "/":
    if z == "0":
        print("you can't divide by 0")
    else:
        result = (x / z)
elif y == "*":
    result = (x * z)
elif y == "+":
    result = (x + z)
elif y == "-":
    result = (x - z)

print(round(result,1))
