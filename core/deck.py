from random import randint

def build_standard_deck() -> list[dict]:
    card_list = []
    nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suites = ["H", "C", "D", "S"]

    for num in nums:
        for suite in suites:
            card = {
                "rank": num,
                "suite": suite
            }
            card_list.append(card)

    return card_list
        

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    num_swaps = 0

    while num_swaps != swaps:

        flag = True
        while flag:

            i = randint(0, len(deck) -1)
            j = randint(0, len(deck) -1)

            if j != i:

                if deck[i]["suite"] == "H":
                    if j % 5 == 0:
                        deck[i], deck[j] = deck[j], deck[i]
                        flag = False

                elif deck[i]["suite"] == "C":
                    if j % 3 == 0:
                        deck[i], deck[j] = deck[j], deck[i]
                        flag = False

                elif deck[i]["suite"] == "D":
                    if j % 2 == 0:
                        deck[i], deck[j] = deck[j], deck[i]
                        flag = False

                elif deck[i]["suite"] == "S":
                    if j % 7 == 0:
                        deck[i], deck[j] = deck[j], deck[i]
                        flag = False
        
        num_swaps += 1

    return deck





