import time as tm
påse = [

]

while True: 
    print("Welcom bro to påse")
    print("[V] Visa innehållet i påsen")
    print("[S] Spara i påsen")
    print("[F] Leta (finns) i påsen")
    print("[Q] Avsluta programmet")

    choice = input("What you choose bro: ")
    if choice.upper() == "V":
        if påse == []: 
            print("nothing in påse bro")
            tm.sleep(2)
        else:
            print(påse)
        tm.sleep(2)
    elif choice.upper() == "S":
        addlist = input("what you add list? if nothing type exit: ")
        påse.append(addlist)
        tm.sleep(2)
    elif choice.upper() == "F":
        search = input("what you look for bro?: ")
        if search in påse:
            print("Found in påse bro!")
            tm.sleep(2)
        else:
            print("Not in påse")
            tm.sleep(2)
    elif choice.upper() == "Q":
        print("ok bye bro")
        break
    else:
        print("Invalid choice bro")