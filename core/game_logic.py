from .player_io import ask_player_action

def int_by_suite(val):
    if val == "A":
        return 1
    elif val == "J" or val == "Q" or val == "K":
        return 10
    else:
        return int(val)


def calculate_hand_value(hand: list[dict]) -> int:
    count_hand = 0
    flag = False

    for card in hand:
        if card["rank"] == "A":
            flag = True
        count_hand += int_by_suite(card["rank"])
    
    if flag and count_hand <= 11:
        count_hand += 10

    return count_hand
    

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        player["hand"].append(deck.pop(0))
        dealer["hand"].append(deck.pop(0))

    print(f"hand dealer = {calculate_hand_value(dealer["hand"])}.  ---  player hand = {calculate_hand_value(player["hand"])}.")


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_hand = calculate_hand_value(dealer["hand"])

    while dealer_hand < 18:
        dealer["hand"].append(deck.pop(0))
        dealer_hand = calculate_hand_value(dealer["hand"])

    if dealer_hand > 21:
        print(f"hand dealer = {calculate_hand_value(dealer["hand"])}.")
        print("dealer lose")
        return False
    
    else:
        return True
    

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    choice = ask_player_action()

    while choice == "H":
        player["hand"].append(deck.pop(0))
        player_hand = calculate_hand_value(player["hand"])
        print(f"hand dealer = {calculate_hand_value(dealer["hand"])}.  ---  player hand = {calculate_hand_value(player["hand"])}.")
        if player_hand > 21:
            print("game over - player lose")
            break
        choice = ask_player_action()

    if choice == "S":
        dealer_rownd = dealer_play(deck, dealer)

        if dealer_rownd:
            dealer_hand = calculate_hand_value(dealer["hand"])
            player_hand = calculate_hand_value(player["hand"])

            if dealer_hand > player_hand:
                print(f"hand dealer = {calculate_hand_value(dealer["hand"])}.  ---  player hand = {calculate_hand_value(player["hand"])}.")
                print("dealer win")
            elif dealer_hand < player_hand:
                print(f"hand dealer = {calculate_hand_value(dealer["hand"])}.  ---  player hand = {calculate_hand_value(player["hand"])}.")
                print("player win")
            else:
                print(f"hand dealer = {calculate_hand_value(dealer["hand"])}.  ---  player hand = {calculate_hand_value(player["hand"])}.")
                print("win-win")

            







