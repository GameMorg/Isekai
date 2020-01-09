import shelve 


db = shelve.open("save_file.txt")
db["language"] = ["ru", "en"]
db["colors"] = ["red", "green", "blue"]
print(db["language"])
db.close()


class Save:
    """save settings game, 
    1- download
    2- save
    3- show
    """
    def __init__(self):
        self.sf = shelve.open("save_file.txt")

    def save_set(self, key, loading):
        self.sf[key] = [loading]

    def show(self, key):
        self.show_save = self.sf[key]
        print(self.show_save)


test_sf = Save()

test_sf.save_set("run", "programm")

test_sf.show("run")
