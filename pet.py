from task import Task
from check_input import *
import csv

TASK_FILENAME = "tasks.csv"

class Pet:
    def __init__(self, name, pet_id, status, species):        
        self._name = name
        self._pet_id = pet_id
        self._status = int(status)
        self._species = species
        self._tasks = []
        
        try:            
            with open(TASK_FILENAME, mode="r") as file:
                reader = csv.reader(file)            
                for row in reader:
                    read_pet_id, description, status = row
                    if read_pet_id == pet_id: #checking for correct pet_id                        
                        self._tasks.append(Task(self._pet_id, description, int(status)))
        except FileNotFoundError: # create new file if task.csv not found
            print("Error: tasks.csv file not found. Creating a new file.")
            open(TASK_FILENAME, mode="w").close()  
            
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def pet_id(self):
        return self._pet_id
    
    @property
    def status(self):
        return self._status

    def get_task_len(self):
        return len(self._tasks)
    
    def add_task(self):        
        if len(self._tasks) < 5:
            new_desc = input("What will you add to your routine together? ")
            
            self._tasks.append(Task(self._pet_id, new_desc, 0))
            # saving task to csv
            with open(TASK_FILENAME, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self._pet_id, new_desc, 0])
            
            print("New activity added!!")
        else:
            print(f"Adding another activity will tire {self._name} out :(")
    
    def remove_task(self):
        pass
        
    def display_status(self):
        statuses = {1: "exhausted", 2:"tired", 3:"fine", 4:"happy", 5:"elated"}
        print()
        print("-"*30)
        print(f"{self._name}'s Room".center(30))        
        print(f"~{self._name} is feeling {statuses[self._status]}~".center(30))
        print("-"*30)            
    
    def display_tasks(self):
        if len(self._tasks) > 0:            
            for i, task in enumerate(self._tasks, start = 1):
                print(f"{i}. {task.desc}")
        else:
            print("There is currently no activity you can do together. Go add one!")
    
    def pet_menu(self):
        if len(self._tasks) > 0: # task exists            
            self.display_status()
            
            # check for completed task
            if any(task.status == 0 for task in self._tasks): 
                print("Here are things you haven't done together today:")
                for i,task in enumerate(self._tasks, start = 1):
                    if (task.status == 0):
                        print(f"{i}. {task.desc}")                
            else: # all tasks completed
                print("You completed all tasks today!\n")
            print("_"*30)
            # input processing     
            options = "1. Mark completed\n2. Undo completion\n3. Setting\n4. Go back\n>> "
            return get_int_range("What do you want to do first?\n" + options,1,4)
        else: # go add task
            print("You currently have no activities to do together. Let's make one!")
            self.add_task() # returns nothing; case default will handle            
        
        
        
        
        

