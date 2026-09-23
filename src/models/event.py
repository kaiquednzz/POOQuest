class Event:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

events = [
    Event("Enemy Encounter", "A wild enemy appears!", "enemy"),
    Event("Food Discovery", "You find some food!", "food"),
    Event("Nothing Found", "You find nothing of interest.", "nothing")
]
    