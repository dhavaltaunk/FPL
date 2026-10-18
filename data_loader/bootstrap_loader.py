from utils.official_fpl_endpoint import run_path
from utils.mongodb_conn import get_fpl_db

ENDPOINT = 'bootstrap-static/'

DATA_MAP = {
    'Teams'     : 'teams',
    'Players'   : 'elements',
}


def reload_teams(teams):
    fpl_db = get_fpl_db()
    teams_collection = fpl_db.teams
    teams_collection.delete_many({})
    inserted_ids = teams_collection.insert_many(teams)
    print(f'Inserted {len(inserted_ids.inserted_ids)} records to teams')


def reload_players(players):
    fpl_db = get_fpl_db()
    players_collection = fpl_db.players
    players_collection.delete_many({})
    inserted_ids = players_collection.insert_many(players)
    print(f'Inserted {len(inserted_ids.inserted_ids)} records to players')


def load():
    response = run_path(ENDPOINT)
    status, data = response['Status'], response['Data']
    print(f'Response Status: {status}')

    teams   = data[DATA_MAP['Teams']]
    reload_teams(teams)

    players = data[DATA_MAP['Players']]
    reload_players(players)


def main():
    load()

if __name__ == '__main__':
    main()
