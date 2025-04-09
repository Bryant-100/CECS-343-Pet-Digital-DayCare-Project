#Pet – the object that the user interacts with.


class Pet:
     # Attributes: __name, _pet_id, __tasklist, _needs, and _wins.
    def __init__(self, name, pet_id, tasklist, needs, wins):
        self._name = name
        self._pet_id = pet_id
        self._tasklist = tasklist
        self._needs = needs
        self._wins = wins

    def get_pet_name(self):
        return self._name
    
    def get_pet_id(self):
        return self._pet_id
    
    def get_tasklist(self):
        return self._tasklist
    
    def get_needs(self):
        return self._needs
    
    def get_wins(self):
        return self._wins
    
    def set_pet_name(name):
        name = None

    def set_pet_id(pet_id):
        pet_id = None

    def set_tasklist(tasklist):
        tasklist = None

    def set_wins(wins):
        wins = None

    def display_meter(self):
        return None