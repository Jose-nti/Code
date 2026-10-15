import random as rm
import time as tm

ezlista = ["katt","hund","hus","sol","bil","stol","bord","fisk","båt","glass"]
medlista = ["äpple","skola","blomma","fågel","skog","berg","sjö","choklad","vinter","sommar"]
halista = ["regnbåge","snögubbe","krokodil","elefant","giraff","pingvin","blixt","åska"]

guessed = []
wlong = 0
maxg = 5

print("Hello welcome to my game")
tm.sleep(0.5)
print("Please choose the difficulty:")
tm.sleep(0.5)
print("EASY        MEDIUM      HARD")
tm.sleep(0.5)


start = input("skriv ditt svar här: ").lower()

if start == "easy":
    guessez = rm.choice(ezlista)

    while wlong < maxg:
        print(" ".join([letter if letter in guessed else "_" for letter in guessez]))
        guess = input("skriv ett bokstav: ").strip().lower()
        if len(guess) != 1:
            print("inte ord, bara bokstav")
        elif guess in guessed:
            print("du redan gissade den bokstav")
        elif guess in guessez:
            print("Rätt!!!")
            guessed.append(guess)
            if all(letter in guessed for letter in guessez):
                print(" ".join(guessez))
                print("du vann bro")
                break
        else:
            print("fel bro")
            wlong += 1
        if wlong >= maxg:
            print(guessez)

if start == "medium":
    guessed = []
    wlong = 0
    guessez = rm.choice(medlista)
    while wlong < maxg:
        print(" ".join([letter if letter in guessed else "_" for letter in guessez]))
        guess = input("skriv ett bokstav: ").strip().lower()

        if len(guess) != 1:
            print("inte ord, bara bokstav")
        elif guess in guessed:
            print("du redan gissade den bokstav")
        elif guess in guessez:
            print("Rätt!!!")
            guessed.append(guess)
            if all(letter in guessed for letter in guessez):
                print(" ".join(guessez))
                print("du vann bro")
                break
        else:
            print("fel bro")
            wlong += 1
        if wlong >= maxg:
            print(guessez)

if start == "hard":
    guessed = []
    wlong = 0
    guessez = rm.choice(halista)
    while wlong < maxg:
        print(" ".join([letter if letter in guessed else "_" for letter in guessez]))
        guess = input("skriv ett bokstav: ").strip().lower()
        if len(guess) != 1:
            print("inte ord, bara bokstav")
        elif guess in guessed:
            print("du redan gissade den bokstav")
        elif guess in guessez:
            print("Rätt!!!")
            guessed.append(guess)
            if all(letter in guessed for letter in guessez):
                print(" ".join(guessez))
                print("du vann bro")
                break
        else:
            print("fel bro")
            wlong += 1
        if wlong >= maxg:
            print(guessez)