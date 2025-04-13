from task import Task
import csv 

TASK_FILENAME = "tasks.csv"

class Pet:
     
    def __init__(self, name, pet_id, needs, wins):        
        self._name = name
        self._pet_id = pet_id
        # add later; list of task objects created from their id
        self._tasklist = []
        # add later; []
        self._needs = needs
        self._wins = wins
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def pet_id(self):
        return self._pet_id
        
    def display_meter(self):
        pass
    
    def display_tasks(self):
        pass
    
    ##### Later        
    def get_wins(self):
        return self._wins
        
    def set_wins(self, wins):
        wins = None
        

