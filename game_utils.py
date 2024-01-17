from game_data import list_of_positions

def get_directions(position: str) -> dict:
    return list_of_positions[position]['directions']

def check_room(position: str) -> bool:
    return list_of_positions[position]['isThereCat']

def backtracking_required(position: str, found_cat: bool) -> bool:
    return (position in ('F', 'I', 'H')) and found_cat

def check_is_position_last(position: str) -> bool:
    return bool(list_of_positions[position]['positions'])

def check_permission(next_position: str, found_cat: bool) -> bool:
    return next_position == 'G' and found_cat is False