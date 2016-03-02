class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)



start = Room("STARTROOM", "DWON & WEST.")

rooms = {"STARTROOM": start}

current = rooms["STARTROOM"]

print current.name
    
        