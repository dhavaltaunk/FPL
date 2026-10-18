from utils.official_fpl_endpoint import run_path
from utils.mongodb_conn import get_fpl_db
from utils.apis import get_player_id, get_all_players

ENDPOINT = 'element-summary/{}/'


def reload_player_stats():
    players = get_all_players()
    fpl_db = get_fpl_db()
    players_stats_collection = fpl_db.player_stats
    players_stats_collection.delete_many({})
    for player in players:
        _id = player['id']
        stats = get_player_stats_from_id(_id)
        stats['id'] = _id
        inserted_ids = players_stats_collection.insert_one(stats)
        print(f'Inserted {player['first_name']} {player['second_name']} to player_stats')


def get_player_stats_from_name(player_name: str):
    response = run_path(ENDPOINT.format(get_player_id(player_name)))
    status, data = response['Status'], response['Data']
    print(f'Response Status: {status}')
    return data


def get_player_stats_from_id(_id: str):
    response = run_path(ENDPOINT.format(_id))
    status, data = response['Status'], response['Data']
    print(f'Response Status: {status}')
    return data


def main():
    get_player_stats_from_name('Bryan Mbeumo')
    # reload_player_stats()


if __name__ == '__main__':
    main()
