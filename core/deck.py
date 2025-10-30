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
        