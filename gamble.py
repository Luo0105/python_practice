#It's just coding, dont' do it for real
import random
import time

money = 1000
while money > 0:
    print("You have $" + str(money))
    while True:
        bet = int(input("How much do you want to bet? "))
        if 0 < bet <= money:
            break
        print("Invalid bet. Please enter a number between 1 and " + str(money) + ".")
    input("Press Enter to roll the dice...")
    print("Rolling the dice...")
    time.sleep(1)
    dice1 = random.randint(1, 6) + random.randint(1, 6)
    print("You rolled a " + str(dice1) + ".")
    if dice1 == 7 or dice1 == 11:
        print("You win!")
        input("Press Enter to continue...")
        time.sleep(1)
        money += bet
    elif dice1 == 2 or dice1 == 3 or dice1 == 12:
        print("You lose!")
        input("Press Enter to continue...")
        time.sleep(1)
        money -= bet
    else:
        print("You need to roll again.")
        input("Press Enter to roll again...")
        while True:
            print("Rolling the dice again...")
            time.sleep(1)
            dice2 = random.randint(1, 6) + random.randint(1, 6)
            print("You rolled a " + str(dice2) + ".")
            time.sleep(1)
            if dice2 == dice1:
                print("You win!")
                input("Press Enter to continue...")
                money += bet
                break
            elif dice2 == 7:
                print("You lose!")
                input("Press Enter to continue...")
                money -= bet
                break
            else:
                dice1 = dice2
                input("Press Enter to roll again.")

print("You are out of money! Game over.")
