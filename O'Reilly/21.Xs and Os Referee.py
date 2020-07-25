from typing import List

def checkio(game_result: List[str]) -> str:
    for i in range(3):
        if game_result[0][i] == game_result[1][i] == game_result[2][i] == 'O':
            return 'O'
        elif game_result[0][i] == game_result[1][i] == game_result[2][i] == 'X':
            return 'X'
    if 'OOO' in game_result or game_result[0][0] == game_result[1][1] == game_result[2][2] == 'O' or game_result[0][2] == game_result[1][1] == game_result[2][0] == 'O':
        return 'O'
    elif 'XXX' in game_result or game_result[0][0] == game_result[1][1] == game_result[2][2] == 'X' or game_result[0][2] == game_result[1][1] == game_result[2][0] == 'X':
        return 'X'
    else:
        return 'D'
