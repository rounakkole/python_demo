go = input("where to go? left or right \n")
go1 = go.lower()
if go1 == "left":
    print("go ahead")
    lake = input("wait for boat or swim? boat or swim \n")
    lake1 = lake.lower()
    if lake1 == "boat":
        print("go ahead")
        door = input("which door? green or yellow or red \n")
        door1 = door.lower()
        if door1 == "yellow":
            print("got key")
            print('''__________________________________________________
____________________________¶¶¶¶¶_________________
________________________¶¶¶¶¶¶¶¶¶¶¶¶______________
_______________________¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
_______________________¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
_______________________¶¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶¶__
________________________¶¶¶¶¶¶_______¶¶¶¶¶¶¶¶¶_¶¶_
_________________________¶¶¶¶¶¶________________¶¶_
__________________________¶¶¶¶__¶¶¶¶¶¶_________¶¶_
___________________________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
__________________________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
________________________¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___
_______________________¶¶__¶¶¶¶¶¶_________________
______________________¶___¶¶¶¶¶¶__________________
_____________________¶__¶¶¶¶¶¶¶___________________
___________________¶¶__¶¶¶¶¶¶¶____________________
__________________¶¶__¶¶¶¶¶¶______________________
_________________¶¶__¶¶¶¶¶¶_______________________
________________¶¶__¶¶¶¶¶¶________________________
_______________¶___¶¶¶¶¶¶_________________________
_____________¶¶__¶¶¶¶¶¶¶__________________________
____________¶¶__¶¶¶¶¶¶____________________________
___________¶___¶¶¶¶¶¶_____________________________
_________¶¶___¶¶¶¶¶¶______________________________
________¶¶_____¶¶¶________________________________
______¶¶_____¶¶¶¶_________________________________
_____¶¶_____¶¶¶¶¶¶¶¶¶¶____________________________
____¶¶______________¶¶____________________________
___¶___¶¶¶¶¶¶____¶¶¶¶_____________________________
__¶¶_¶¶¶¶¶¶¶¶¶___¶¶¶¶¶____________________________
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________________________
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________________________
___¶¶¶¶¶¶____¶¶¶¶¶________________________________
__________________________________________________
''')

        elif door1 == "red":
           print("fall in hole")
        elif door1 == "green":
            print("crocodiles")
        else : print("syntax error")

    elif lake1 == "swim":
        print("crocodiles")
    else : print("syntax error")
elif go1 == "right":
    print("fall in hole")
else : print("syntax error")
