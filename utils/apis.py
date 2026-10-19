import functools
from utils.mongodb_conn import get_fpl_db
from utils.projections import TEAMS_DISPLAY_PROJECTION


@functools.lru_cache(maxsize=1)
def get_teams():
    '''
    Get names of all teams in the Premier League
    '''
    db = get_fpl_db()
    teams_collection = db.teams
    teams = teams_collection.find({}, TEAMS_DISPLAY_PROJECTION)
    return list(teams)


@functools.lru_cache(maxsize=1)
def get_team_names():
    '''
    Get names of all teams in the Premier League
    '''
    db = get_fpl_db()
    teams_collection = db.teams
    teams = teams_collection.find()
    team_names = []
    for team in teams:
        team_names.append(team['name'])
    return team_names


@functools.lru_cache(maxsize=1)
def get_team_codes():
    '''
    Get team codes of all teams in the Premier League
    '''
    db = get_fpl_db()
    teams_collection = db.teams
    teams = teams_collection.find()
    team_codes = dict()
    for team in teams:
        team_codes[team['name']] = team['code']
    return team_codes


@functools.lru_cache(maxsize=20)
def get_team_code_for(team_name):
    '''
    Get team code for team name
    '''
    return get_team_codes().get(team_name)


@functools.lru_cache(maxsize=20)
def get_all_players_for_team(team_name):
    '''
    Get summary of all players of a particular team
    '''
    team_code = get_team_code_for(team_name)
    if team_code:
        db = get_fpl_db()
        players_collection = db.players
        players = players_collection.find({'team_code': team_code})
        for player in players:
            print(f'{player['first_name']} {player['second_name']}')
        return players


def get_player(player_name: str):
    '''
    Get summary of a given player from player_name
    '''
    db = get_fpl_db()
    players_collection = db.players
    first_name, second_name = player_name.split(maxsplit=1)
    q = {'$and': [
        {'first_name': first_name},
        {'second_name': second_name},
    ]}
    player = players_collection.find_one(q)
    return player


def get_player_id(player_name: str):
    '''
    Get player id of a given player from player_name
    '''
    player = get_player(player_name)
    if player:
        return player['id']


def get_all_players():
    '''
    Get summary of all players
    '''
    db = get_fpl_db()
    players_collection = db.players
    return players_collection.find()


def main():
    # print(get_team_names())
    # print(get_team_codes())
    # print(get_team_code_for('Leeds'))
    # print(get_all_players_for_team('Man Utd'))
    print(get_player('Bryan Mbeumo'))

if __name__ == '__main__':
    main()
