import json
import random

# Load config
with open('config.json') as f:
    config = json.load(f)

# Configuration settings
username = config.get("username", "Player")
money = config.get("starting_money", 1000)
min_bet = config.get("min_bet", 10)
max_bet = config.get("max_bet", 100)
enable_double_down = config.get("enable_double_down", True)
enable_insurance = config.get("enable_insurance", True)

# Card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Function to create a deck of cards
def create_deck():
    deck = []
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for value in list(card_values.keys()):
            deck.append((value, suit))
    random.shuffle(deck)
    return deck

# Function to calculate the hand value
def calculate_hand(hand):
    value = sum(card_values[card[0]] for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Function to display hand
def display_hand(hand):
    return ', '.join(f'{card[0]} of {card[1]}' for card in hand)

# Function to check for Blackjack
def is_blackjack(hand):
    return calculate_hand(hand) == 21 and len(hand) == 2

# Main game loop
def play_blackjack():
    global money
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Initial dealing
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    print(f"Welcome, {username}! You have ${money} to start.")

    while True:
        if money < min_bet:
            print("You don't have enough money to continue playing.")
            break

        # Player's bet
        while True:
            try:
                bet = int(input(f"Place your bet (${min_bet}-${max_bet}): "))
                if bet < min_bet or bet > max_bet or bet > money:
                    raise ValueError
                break
            except ValueError:
                print(f"Invalid bet. Bet must be between ${min_bet} and ${max_bet} and not exceed your current money (${money}).")

        print(f"\nDealer's hand: {dealer_hand[0][0]} of {dealer_hand[0][1]} and [hidden]")
        print(f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand(player_hand)})\n")

        if enable_insurance and dealer_hand[0][0] == 'A':
            insurance = input("Dealer has an Ace. Do you want to buy insurance? (y/n): ").lower()
            if insurance == 'y':
                insurance_bet = bet / 2
                if is_blackjack(dealer_hand):
                    print("Dealer has a blackjack. You win the insurance bet.")
                    money += insurance_bet * 2
                else:
                    print("Dealer does not have a blackjack. You lose the insurance bet.")
                    money -= insurance_bet

        # Check for Blackjack
        if is_blackjack(player_hand):
            if is_blackjack(dealer_hand):
                print(f"Both you and the dealer have blackjack! It's a tie.")
            else:
                print(f"Blackjack! You win ${bet * 1.5}.")
                money += bet * 1.5
        elif is_blackjack(dealer_hand):
            print(f"Dealer has blackjack! You lose your bet of ${bet}.")
            money -= bet
        else:
            # Player's turn
            while calculate_hand(player_hand) < 21:
                move = input("Do you want to (h)it, (s)tand, or (d)ouble down? ").lower() if enable_double_down else input("Do you want to (h)it or (s)tand? ").lower()
                if move == 'h':
                    player_hand.append(deck.pop())
                    print(f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand(player_hand)})")
                    if calculate_hand(player_hand) > 21:
                        print("You bust! Dealer wins.")
                        money -= bet
                        break
                elif move == 's':
                    break
                elif move == 'd' and enable_double_down:
                    if bet * 2 > money:
                        print("You don't have enough money to double down.")
                    else:
                        bet *= 2
                        player_hand.append(deck.pop())
                        print(f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand(player_hand)})")
                        if calculate_hand(player_hand) > 21:
                            print("You bust! Dealer wins.")
                            money -= bet
                        break
                else:
                    print("Invalid input. Please enter 'h', 's', or 'd'.")

            # Dealer's turn
            if calculate_hand(player_hand) <= 21:
                while calculate_hand(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                print(f"\nDealer's hand: {display_hand(dealer_hand)} (Value: {calculate_hand(dealer_hand)})")

                # Determine winner
                player_value = calculate_hand(player_hand)
                dealer_value = calculate_hand(dealer_hand)

                if dealer_value > 21 or player_value > dealer_value:
                    print(f"You win! You gain ${bet}.")
                    money += bet
                elif player_value < dealer_value:
                    print(f"Dealer wins. You lose ${bet}.")
                    money -= bet
                else:
                    print("It's a tie!")

        print(f"\nCurrent money: ${money}\n")

        # Ask if the player wants to play again
        while True:
            play_again = input("Do you want to play again? (y/n/t for tip the dealer): ").lower()
            if play_again == 't':
                while True:
                    try:
                        tip_amount = input("Enter tip amount or type 'cancel' to cancel tipping: ").lower()
                        if tip_amount == 'cancel':
                            print("Tipping canceled.")
                            break
                        tip_amount = int(tip_amount)
                        if tip_amount > money or tip_amount < 0:
                            raise ValueError
                        money -= tip_amount
                        print(f"Thanks for the tip! Here's a 🍹 on the house!")
                        break
                    except ValueError:
                        print(f"Invalid tip amount. Please enter a positive number not exceeding your current balance (${money}).")
            elif play_again == 'y' or play_again == 'n':
                break
            else:
                print("Invalid input. Please enter 'y', 'n', or 't'.")

        if play_again == 'n':
            break
        
        player_hand = []
        dealer_hand = []
        deck = create_deck()
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    print(f"Thank you for playing, {username}! You finished with ${money}.")

if __name__ == "__main__":
    play_blackjack()