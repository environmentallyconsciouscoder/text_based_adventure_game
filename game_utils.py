from game_data import list_of_positions, found_cat, starting_position

def get_directions(position: str) -> dict:
    return list_of_positions[position]['directions']

def check_room(position: str) -> bool:
    return list_of_positions[position]['isThereCat']

def backtracking_required(position: str, found_cat: bool) -> bool:
    return (position in ('F', 'I', 'H')) and found_cat