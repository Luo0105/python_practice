import random
import time
import os


def create_deck():
    return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4


def hand_deal(deck):
    hand = []
    for _ in range(2):
        card = deck.pop()
        hand.append(card)
    return hand


# 计算手牌总值
def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'A':
            total += 11
            aces += 1
        elif card in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


# 抽一张牌
def hit(hand, deck):
    card = deck.pop()
    hand.append(card)
    return hand


# 清屏
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# 是否blackjack
def blackjack_check(hand):
    return hand_total(hand) == 21


# 显示结果
def results(player_hand, dealer_hand):
    print(f"Your hand: {player_hand} Total: {hand_total(player_hand)}")
    print(f"Dealer's hand: {dealer_hand} Total: {hand_total(dealer_hand)}")


# 检查比分并返回结果和金额变化
def score_check(player_hand, dealer_hand):
    player_total = hand_total(player_hand)
    dealer_total = hand_total(dealer_hand)
    results(player_hand, dealer_hand)
    if dealer_total == 21:
        return "Dealer has blackjack! You lose!", -1
    if player_total == 21:
        return "Blackjack! You win!", 1.5
    if player_total > 21:
        return "You busted! You lose!", -1
    elif dealer_total > 21:
        return "Dealer busted! You win!", 1
    elif player_total > dealer_total:
        return "You win!", 1
    elif player_total < dealer_total:
        return "You lose!", -1
    else:
        return "It's a tie!", 0

def update_money(money, bet, result_code):
    if result_code == 1:
        return money + bet
    elif result_code == -1:
        return money - bet
    elif result_code == 1.5:
        return money + bet * 1.5
    return money


def play_again(money):
    while True:
        print()
        again = input(f"You have ${money}. Do you want to play again? (y/n) ").lower()
        if again == 'y':
            clear_screen()
            return True
        elif again == 'n':
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def game():
    money = 1000
    while money > 0:
        print(f"\nYou have ${money}")
        while True:
            try:
                bet = int(input("How much do you want to bet? "))
                if 0 < bet <= money:
                    break
                print(f"Invalid bet. Please enter a number between 1 and {money}.")
            except ValueError:
                print("Please enter a valid number.")

        input("Press Enter to deal the cards...")
        clear_screen()
        print("Dealing the cards...")
        time.sleep(1)

        deck = create_deck()
        random.shuffle(deck)
        player_hand = hand_deal(deck)
        dealer_hand = hand_deal(deck)

        print(f"Your hand: {player_hand} Total: {hand_total(player_hand)}")
        print(f"Dealer's hand: {dealer_hand[0]} ?")
        time.sleep(0.5)

        if blackjack_check(player_hand):
            print("Blackjack! You win!")
            money += bet
            input("Press Enter to continue...")
            continue

        if blackjack_check(dealer_hand):
            print("Dealer has blackjack! You lose!")
            money -= bet
            input("Press Enter to continue...")
            continue

        while True:
            action = input("Do you want to hit or stand? (h/s) ").lower()
            if action == 'h':
                player_hand = hit(player_hand, deck)
                print(f"Your hand: {player_hand} Total: {hand_total(player_hand)}")
                if hand_total(player_hand) > 21:
                    print("You busted! You lose!")
                    money -= bet
                    input("Press Enter to continue...")
                    break
            elif action == 's':
                time.sleep(1)
                while hand_total(dealer_hand) < 17:
                    dealer_hand = hit(dealer_hand, deck)
                message, result_code = score_check(player_hand, dealer_hand)
                print(message)
                money = update_money(money, bet, result_code)
                input("Press Enter to continue...")
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        if not play_again(money):
            break

    print("You're out of money! Game over.")

if __name__ == "__main__":
    game()
