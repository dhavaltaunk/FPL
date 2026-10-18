import functools
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017/"

@functools.lru_cache(maxsize=1)
def get_client() -> MongoClient:
    # 1. Connect to MongoDB (Local instance example)
    # For MongoDB Atlas, paste your "mongodb+srv://..." connection string here
    client = MongoClient(CONNECTION_STRING)
    print("Connected to MongoDB successfully!")
    return client

@functools.lru_cache(maxsize=1)
def get_fpl_db():
    client = get_client()
    return client.fpl_data


def test_connection():
    client = get_client()
    print(f'All DBs - {client.list_database_names()}')

    fpl_db = client.fpl_data
    print('Connected to fpl_data')
    collections = fpl_db.list_collection_names()
    print(f'Collections in fpl_data - {collections}')

def main():
    test_connection()

if __name__ == '__main__':
    main()
