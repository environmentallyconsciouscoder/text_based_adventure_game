from typing import Union
from game_data import list_of_positions, found_cat, starting_position
from game_utils import get_directions, backtracking_required, check_room, check_is_position_last, check_permission

def get_direction(user_input: str, position: str) -> Union[None, str]:
    directions = get_directions(position)
    valid_directions = [directions[direction] for direction in user_input if direction in directions]
    if valid_directions:
        return valid_directions[0]
    else:
        print("Invalid direction entered")
        return None

def find_cat(position: str) -> Union[None, bool]:
    global found_cat
    cat_in_room = check_room(position)
    if cat_in_room:
        print("you found the cat")
        found_cat = True

def give_instructions(question: str, position: str) -> str:
    if backtracking_required(position, found_cat):
        response = input('There is no way out from here. Please go back! Choose a direction to escape: N, E, S or E ')
    else:
        response = input(question)
    return response

def get_position(position: str = starting_position) -> None:

    keep_playing = check_is_position_last(position)
    print("Your current position: ",position)

    # If the game hasn't reached the last position, keep playing
    while keep_playing:
        user_input = give_instructions(list_of_positions[position]['question'], position)

        print("Direction given by you: ", user_input)
        next_position = get_direction(user_input, position)
        if next_position is not None:
            find_cat(next_position)
            is_movement_allowed = check_permission(next_position, found_cat)
            if is_movement_allowed:
                print("you need to find the cat before you can move on")
                get_position('F')
                continue
            else:
                get_position(next_position)
        else:
            print("The direction does not lead anywhere. Please try again.")
            continue
        break
    if not keep_playing:
        end_game()

def start_game() -> None:
    get_position()

def end_game() -> None:
    print('You have now escaped!')

if __name__ == "__main__":
    start_game()
