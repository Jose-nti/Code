import random as rm

tal1 = rm.randint(1,10)
tal2 = rm.randint(1,10)

answer = tal1 * tal2

svar = int(input(f"vad blir", {tal1}, "+", {tal2}, "?"))

if svar != answer:
    print("you bunz, is", answer)
elif svar == answer :
    print("good boy")