import random, time
while True:
    yourmove = input("0 for Rock, 1 for Paper and 2 for Scissors")
    if yourmove == "0" or yourmove == "1" or yourmove == "2":
        yourmove = int(yourmove)
    else:
        break
    aimove = random.randint(0,2)
    if yourmove == 0 and aimove == 0:
        print("DRAW!")
    if yourmove == 0 and aimove == 1:
        print("YOU LOSE!")
    if yourmove == 0 and aimove == 2:
        print("YOU WIN!")
    if yourmove == 1 and aimove == 0:
        print("YOU WIN!")
    if yourmove == 1 and aimove == 1:
        print("DRAW!")
    if yourmove == 1 and aimove == 2:
        print("YOU LOSE!")
    if yourmove == 2 and aimove == 0:
        print("YOU LOSE!")
    if yourmove == 2 and aimove == 1:
        print("YOU WIN!")
    if yourmove == 2 and aimove == 2:
        print("DRAW!")
print("Sorry, but read the options!")
time.sleep(10)
