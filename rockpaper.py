import random

def get_choice():
    player_choice = input("enter a choice : ")
    optoins = ["rock", "papper", "scissors"]
    computer_choice = random.choice(optoins)
    choice = {"player" : player_choice, "computer": computer_choice}
    return choice

def check_win(player, computer):
    print(f"player chose : {player} and computer chose : {computer}")
    if player == computer:
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return " rocks smashes scissors, you win!"
        else:
            return "paper covers rock, you lose"
    elif player == "paper":
        if computer == "scissors":
            return " scissors cuts paper, you lose"
        else:
            return "paper covers rock, you win!"
    elif player == "scissors":
        if computer == "paper":
            return " scissors cuts paper, you win!"
        else:
            return "rock smash scissors, you lose"
        
choice = get_choice()
result = check_win(choice["player"], choice["computer"])
print(result)
