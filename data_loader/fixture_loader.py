from utils.official_fpl_endpoint import run_path
from utils.mongodb_conn import get_fpl_db
from utils.apis import get_player_id, get_all_players

ENDPOINT = 'fixtures/'


def reload_fixtures():
    fixtures = get_fixtures()
    fpl_db = get_fpl_db()
    fixtures_collection = fpl_db.fixtures
    fixtures_collection.delete_many({})
    for fixture in fixtures:
        inserted_ids = fixtures_collection.insert_one(fixture)
        print(f'Inserted to fixtures_collection')


def get_fixtures():
    response = run_path(ENDPOINT)
    status, data = response['Status'], response['Data']
    print(f'Response Status: {status}')
    return data


def main():
    reload_fixtures()


if __name__ == '__main__':
    main()
