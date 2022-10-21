import math
x = float(input('x='))
y = float(input('y='))
if x == 0 and y == 0:
    print("F does not exist")
else:
    F = (math.sin(math.pow((x + 0.4), 2))) / (math.pow(y, 2) + 7.325 * x)
    print(F)
