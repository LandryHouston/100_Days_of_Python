import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(deck)

def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def blackjack():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        print("\n"*50)
        print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/                            
        """)
        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]

        game_over = False

        while not game_over:
            player_score = calculate_score(player_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"\n\tYour cards: {player_cards}, current score: {player_score}")
            print(f"\tDealer's first card: {dealer_cards[0]}\n")

            if player_score == 21:
                print("Blackjack! You win! 🏆")
                game_over = True
                continue
            elif dealer_score == 21:
                print(f"Dealer has Blackjack! You lose! 😱\n\tDealer's final hand: {dealer_cards}")
                game_over = True
                continue
            elif player_score > 21:
                print("You went over 21. You lose! 😭")
                game_over = True
                continue

            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                player_cards.append(deal_card())
            else:
                while dealer_score < 17:
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)

                print(f"\n\tYour final hand: {player_cards}, final score: {player_score}")
                print(f"\tDealer's final hand: {dealer_cards}, final score: {dealer_score}")

                if dealer_score > 21 or player_score > dealer_score:
                    print("You Win! 🎉")
                elif player_score < dealer_score:
                    print("You Lose! 😤")
                else:
                    print("It's a Draw! 🙃")
                game_over = True

    print("Thanks for playing!")

blackjack()
