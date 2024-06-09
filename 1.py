import random

def initialize_game():
    holes = [0, 0, 0, 0, 0]
    fox_position = random.randint(0, 4)
    holes[fox_position] = 1
    return fox_position, 0

def move_fox(fox_position):
    if fox_position == 0:
        fox_position += 1
    elif fox_position == 4:
        fox_position -= 1
    else:
        fox_position += random.choice([-1, 1])
    return fox_position

def play_game(max_steps=3):
    fox_position, attempts = initialize_game()
    while attempts < max_steps:
        print(f"Attempt {attempts + 1}:")
        player_guess = int(input("Choose a hole (0-4): "))
        if player_guess == fox_position:
            print("Congratulations! You caught the fox!")
            break
        else:
            print("No fox in this hole.")
            fox_position = move_fox(fox_position)
            attempts += 1
    else:
        print("Sorry, you've used all attempts. The fox got away!")

if __name__ == "__main__":
    play_game()
