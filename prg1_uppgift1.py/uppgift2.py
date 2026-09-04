import random 

dice = input("Throw the dices")
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print("tärningarna du kastade är",dice1,"och",dice2)
choice = input("Vill du veta vad de blir när de läggs ihop? Yes/No ")
if choice == "Yes":
    x = dice1 + dice2
    print(x)
elif choice == "No":
    print("ok bye")
