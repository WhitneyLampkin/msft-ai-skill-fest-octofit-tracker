from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Initialize the database
db = client["octofit_db"]

# Check and create collections if they do not exist
collections = db.list_collection_names()

if "users" not in collections:
    db.users.create_index("email", unique=True)

if "teams" not in collections:
    db.create_collection("teams")

if "activity" not in collections:
    db.create_collection("activity")

if "leaderboard" not in collections:
    db.create_collection("leaderboard")

if "workouts" not in collections:
    db.create_collection("workouts")

# List collections in the database
collections = db.list_collection_names()
print("Collections in octofit_db:", collections)

print("Database and collections initialized successfully.")