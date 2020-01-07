import shelve 


db = shelve.open("save_file.txt")
db["language"] = ["ru", "en"]
db["colors"] = ["red", "green", "blue"]

db.close()
