bill = input("how much bill? ")
people = input("how many people? ")
tip = input(f"how much tip? 12 or 15 or 18 perc ")
print(type(bill))
bill1 = float(bill)
people1 = float(people)
tip1 = float(tip)
each = (bill1 / 100 * tip1 + bill1) / people1
fprint = float(each)
print(f"each pearson {round(fprint, 1)} rs")