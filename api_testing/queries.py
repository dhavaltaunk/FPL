from utils.mongodb_conn import get_fpl_db
from bson.objectid import ObjectId
from pprint import pprint

def query_teams():
    db = get_fpl_db()
    teams = db.teams
    teams = teams.find()
    for team in teams:
        pprint(team)

def query2():
    db = get_fpl_db()
    teams = db.teams
    
    arsenal = teams.find_one({'name':'Arsenal'})
    pprint(arsenal)

    _teams = teams.find({'points':0})
    for team in _teams:
        pprint(team['name'])

    n = teams.count_documents(filter={})
    print(f'Num of records in teams collection - {n}')

    _id = ObjectId('6ad3f9b98f3f5064aa8ec812')
    man_utd = teams.find_one({'_id':_id})
    pprint(man_utd)

def query3():
    db = get_fpl_db()
    players = db.players
    q = {'$and': [
            {'total_points': {"$gte": 20}},
            {'goals_conceded': {"$lte": 10}}
        ]}
    p = players.find(q)
    for _p in p:
        print(f'{_p['first_name']} {_p['second_name']}')


def main():
    # query_teams()
    # query2()
    query3()

if __name__ == '__main__':
    main()
