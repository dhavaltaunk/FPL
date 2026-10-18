from pymongo import MongoClient

def connect():
    # 1. Connect to MongoDB (Local instance example)
    # For MongoDB Atlas, paste your "mongodb+srv://..." connection string here
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)

    # 2. Access or create a database
    db = client["my_database"]

    # 3. Access or create a collection
    collection = db["my_collection"]

    print("Connected to MongoDB successfully!")


def main():
    connect()

if __name__ == '__main__':
    main()
