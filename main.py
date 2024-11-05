import random


Rules = """
Rules:
1. 2-4 players can play
2. The player whose turn is can roll until he got 1
3. Player can stop rolling at any time.
4. If a player got 1 after rolling his score should become zero.
5. The player who hit 50 will win the game


"""
print(Rules,"\n")

def roll():
    roll_value = random.randint(min_value, max_value)
    return roll_value



while True:
    players = input("\nWelcome to PIG! How many players are you? (2-4) ")
    if players.isdigit():
        players = int(players)
        if(2<= players <= 4):
            print(f"{players} have been enrolled! ")
            break
        else:
            print("Players must be between 2-4!")
    else:
        print("Invalid Input! try Again")


min_value = 1
max_value = 6  
win_score = 50      
players_score = [0 for _ in range(players)]


while max(players_score) < win_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx+1}'s turn and your score is {players_score[player_idx]}!\n")
        while True:
            should_roll = input("Whould you like to roll? (y/n) ")
            if should_roll.lower() == "n":
                break
            elif should_roll.lower() == "y":
                value = roll()
                print(f"You rolled {value}")
                if value == 1:
                    players_score[player_idx] = 0
                    print(f" Players {player_idx+1}'s score is {players_score[player_idx]}")

                    break
                else:
                    players_score[player_idx] += value
                    print(f" Players {player_idx+1}'s score is {players_score[player_idx]}")
                    if(players_score[player_idx] >= win_score):
                        print(f"player {player_idx+1} Wins and its score is {players_score[player_idx]}! ")
                        exit()
            else:
                exit()
        
print(players_score)
        