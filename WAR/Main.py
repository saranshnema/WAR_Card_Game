from WAR.Game import Game


def get_player_info():
    """
    This method is an interactive console application that takes in input from user
    regarding number of players in the game and their names.
    :return: List of player names
    """
    player_names = []
    while True:
        try:
            num_of_players = int(input("Enter number of players : "))
            if 1 < num_of_players <= 52:
                break
            else:
                print("*********Players can be in the range of 2 to 52*********")
        except ValueError:
            print("*********Please enter an integer value.*********")
    for number in range(1, num_of_players + 1):
        while True:
            name = str(input(("Enter Player {} name : ").format(str(number)))).strip()
            if name and name not in player_names:
                break
            else:
                print("*********Please provide a valid name that has not been used*********")
        player_names.append(name)
    return player_names


def main():
    """
    Driver method that helps populate player name and start the game.
    """
    while True:
        print("Welcome to WAR Game")
        player_names = get_player_info()
        game = Game(player_names=player_names)
        game.create_game()
        game.start_game()
        play_again = str(input("Would you like to play again? \n If No hit N else press any key to continue - ")).lower()
        if play_again == "n":
            print("Thanks for playing.\nGoodbye :)")
            break
if __name__ == '__main__':
    main()
