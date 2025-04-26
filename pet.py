from task import Task
from challenge import Challenge
from check_input import *
from datetime import datetime
import csv, random

TASK_FILENAME = "tasks.csv"

class Pet:
    def __init__(self, name, pet_id, status, species, challenge):
        self._name = name
        self._pet_id = pet_id
        self._status = int(status)
        self._species = species
        self._challenge = int(challenge)
        self._tasks = []
        
        try:
            with open(TASK_FILENAME, mode="r") as file:
                reader = csv.reader(file)            
                for row in reader:
                    read_pet_id, task_id, description, status = row
                    if read_pet_id == self._pet_id: #checking for correct pet_id                        
                        self._tasks.append(Task(self._pet_id, task_id, description, int(status)))
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
    
    @property
    def species(self):
        return self._species
    
    @property
    def challenge(self):
        return self._challenge


    def get_task_len(self):
        return len(self._tasks)
    
    def add_task(self):        
        if len(self._tasks) < 5:
            new_desc = input("What will you add to your routine together? ")
                        
            # Generate a random 5-digit ID
            curr_task_id = [task.task_id for task in self._tasks]
            while True:
                new_task_id = str(random.randint(10000, 99999))
                if new_task_id not in curr_task_id:
                    break
            
            # saving new task to csv
            with open(TASK_FILENAME, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self._pet_id,new_task_id, new_desc, 0])

            self._tasks.append(Task(self._pet_id, new_task_id, new_desc, 0))
            print("New activity added!!")
        else:
            print(f"Adding another activity will tire {self._name} out :(")
    
    def remove_task(self):        
        if len(self._tasks) > 0:            
            print("\nWhich activity do you want to remove?")
            self.display_all_tasks()
            quit_index = len(self._tasks)+1
            print(f"{quit_index}. Return...")
            choice = get_int_range("", 1, quit_index)
            
            if choice != quit_index:
                validation = get_yes_no("Are you sure? ")
                if validation:
                    target = self._tasks[choice-1]
                    self._tasks.remove(target)                                         
                    self.save_tasks()
                    print("Activity has been removed.")
                else:
                    print("Going back...")
            else:
                print("Going back...")                            
        else:
            print("There is currently no activity. Go add one!")
        
    def display_status(self):
        statuses = {1: "exhausted", 2:"tired", 3:"fine", 4:"happy", 5:"elated"}
        print()
        print("-"*30)
        print(f"{self._name}'s Room".center(30))        
        print(f"~{self._name} is feeling {statuses[self._status]}~".center(30))
        print("-"*30)            
    
    def display_all_tasks(self):
        if len(self._tasks) > 0:            
            for i, task in enumerate(self._tasks, start = 1):
                print(f"{i}. {task.desc}")
        else:
            print("There is currently no activity you can do together. Go add one!")
                
    def mark_list_complete(self):
        inactive_tasks = [task for task in self._tasks if task.status == 0]
        
        if len(inactive_tasks) > 0:
            print("\nWhich activity have you completed?")            
            for i, task in enumerate(inactive_tasks, start = 1):
                print(f"{i}. {task.desc}")
            
            choice = get_int_range(">> ",1, len(inactive_tasks))
            selected_task = inactive_tasks[choice-1]
            selected_task.status = 1
            self._status = min(5, self._status + 1)
            self.save_tasks()
        else:
            print("You've completed everything!")
    
    def mark_list_incomplete(self):
        active_tasks = [task for task in self._tasks if task.status == 1]
        if len(active_tasks) > 0:
            print("\nWhich activity to undo?")            
            for i, task in enumerate(active_tasks, start = 1):
                print(f"{i}. {task.desc}")
                
            
            choice = get_int_range(">> ",1, len(active_tasks))
            
            selected_task = active_tasks[choice-1]
            selected_task.status = 0                        
            self._status = max(1, self._status - 1)
            self.save_tasks()
        else:
            print("There is nothing completed yet.")
        
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
            options = "1. Mark completed\n2. Undo completion\n3. Challenges\n4. Add/Remove Activity\n5. Go back\n>> "
            return get_int_range("What do you want to do first?\n" + options,1,5)
        else: # go add task
            print("You currently have no activities to do together. Let's make one!")
            self.add_task() # returns nothing; case default will handle            
        
    def save_tasks(self):                    
        with open(TASK_FILENAME, mode = "r") as file:
            reader = csv.reader(file)
                                        
            new_rows = []
            for row in reader:
                read_pet_id, read_task_id, description, status = row  
                if read_pet_id == self.pet_id:
                    for task in self._tasks:  
                        if read_task_id == task.task_id:
                            new_rows.append([self.pet_id, task.task_id, description, task.status])
                else: # keep original row if belong to other users
                    new_rows.append(row)
        
        with open(TASK_FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
    
    def process_challenge(self):
        if self._challenge == 0: # if not attempted
            challenge_random = random.randint(1,3)
            chal = Challenge()
            available = { 1 : chal.park, 2 : chal.swim, 3 : chal.bake}
            result = available[challenge_random]()
            
            # process result
            self._status += result
            self._status = max(1, min(5, self._status)) # ensure range 1-5
                                    
            self._challenge = 1            
        else:
            print(f"You've already done a challenge with {self.name} today.")
    
    def task_handler(self):
        print('-'*15)
        choice = get_int_range("1. Add activity\n2. Remove activity\n3. Go back\n>> ",1,3)
        match choice:
            case 1:
                self.add_task()
            case 2:
                self.remove_task()
            case 3:
                pass
        

