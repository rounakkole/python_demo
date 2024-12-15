height = input("your height in m? \n")
weight = input("your weight in kg? \n")
hei = int(height)
wei = int(weight)
print(type(hei))
bmi = wei / hei **  2
print(bmi)
bm = int(bmi)
if bm < 18.5:
    print("underweight")
elif bm < 25:
    print("good")
elif bm < 30:
    print("overweight")
elif bm < 35:
    print("clinically overweight")
else : print("not good")
