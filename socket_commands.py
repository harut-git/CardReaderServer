players_list = []


def add_player(params):
    if len(players_list) == 4:
        return "Room is full"
    players_list.append(params['name'])
    return params


