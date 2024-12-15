year = input("what year?\n")
yr = int(year)
if (yr % 400) == 0:
    print("leap year")
elif yr % 100 == 0:
    print("not leap year")
elif yr % 4 == 0:
    print("leap year")
else : print("not leap year")