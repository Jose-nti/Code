hola = input("Hello bro write text pls no virus: ")
i = 0
pepe = -1
for c in hola:
    if c == ' ':
        pepe = i
    i = i + 1

if pepe != -1:
    print(f"Last white space is at position {pepe}")
else:
    print("inga.......zzzzzz")  