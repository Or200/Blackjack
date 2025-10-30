
def ask_player_action() -> str:
    while True:
        try:
            act = input("enter 's' or 'h': ").upper()
            if act == "S" or act == "H":
                return act
        except:
            pass


