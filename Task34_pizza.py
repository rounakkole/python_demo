size = str(input("size of pizza? S, M, L \n"))
peppe = input("want peppe? Y, N \n")
cheese = input("want cheese? Y, N \n")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
        bill += 20
elif size == "L":
        bill += 25
if peppe == "Y":
        bill += 3
if cheese == "Y":
    bill += 1
    
print(f"your bill {bill} D")