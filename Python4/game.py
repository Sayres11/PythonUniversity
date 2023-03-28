import random
from getpass import getpass


def get_game_mode():
    while True:
        mode = input("Choose game mode: (1) Computer vs. Player or (2) Player vs. Player: ")
        if mode in ["1", "2"]:
            return mode
        else:
            print("Invalid input. Please enter 1 or 2.")


def get_num_rounds():
    while True:
        num_rounds = input("Enter the number of rounds: ")
        if num_rounds.isdigit():
            return int(num_rounds)
        else:
            print("Invalid input. Please enter a positive integer.")


def get_player_names(game_mode):
    if game_mode == "1":
        player_name = input("Enter your name: ")
        return [player_name, "Computer"]
    elif game_mode == "2":
        player1_name = input("Enter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")
        return [player1_name, player2_name]


def get_player_move(player_name):
    while True:
        player_move = getpass(f"{player_name}, choose your move: (P)aper, (R)ock, or (S)cissors: ").lower()
        if player_move in ["p", "r", "s"]:
            return player_move
        else:
            print("Invalid input. Please enter P, R, or S.")


def get_computer_move():
    moves = ["p", "r", "s"]
    computer_move = random.choice(moves)
    return computer_move


def get_round_winner(player1_name, player1_move, player2_name, player2_move):
    if player1_move == player2_move:
        return "Tie"
    elif player1_move == "p" and player2_move == "r":
        return player1_name
    elif player1_move == "r" and player2_move == "s":
        return player1_name
    elif player1_move == "s" and player2_move == "p":
        return player1_name
    else:
        return player2_name


def play_game():
    game_mode = get_game_mode()
    num_rounds = get_num_rounds()
    players = get_player_names(game_mode)
    player1_name = players[0]
    player2_name = players[1] if len(players) > 1 else "Computer"
    player1_score = 0
    player2_score = 0
    round_num = 1
    while round_num <= num_rounds:
        print(f"Round {round_num}:")
        if game_mode == "1":
            player1_move = get_player_move(player1_name)
            player2_move = get_computer_move()
        else:
            player1_move = get_player_move(player1_name)
            player2_move = get_player_move(player2_name)
        round_winner = get_round_winner(player1_name, player1_move, player2_name, player2_move)
        if round_winner == player1_name:
            player1_score += 1
            print(f"{player1_name} wins round {round_num}!")
        elif round_winner == player2_name:
            player2_score += 1
            print(f"{player2_name} wins round {round_num}!")
        else:
            print("Round was a tie.")
        round_num += 1
    print("\n--- Final Score ---")
    print(f"{player1_name}: {player1_score}")
    print(f"{player2_name}: {player2_score}")
    if player1_score > player2_score:
        print(f"{player1_name} wins the game!")
    elif player2_score > player1_score:
        print(f"{player2_name} wins the game!")
    else:
        print("Game was a tie.")

play_game()
