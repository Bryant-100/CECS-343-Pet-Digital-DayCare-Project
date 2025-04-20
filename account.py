from check_input import *
from pet import Pet
import csv, random

PETS_FILENAME = "pets.csv"

class Account:
    def __init__(self, username, user_id):
        self._username = username
        self._user_id = user_id        
        self._pets = []
           
        # reading in pets
        try:            
            with open(PETS_FILENAME, mode="r") as file:
                reader = csv.reader(file)            
                for row in reader:
                    read_user_id, pet_name, pet_id, status, species = row
                    if read_user_id == user_id: #checking for correct user_id
                        self._pets.append(Pet(pet_name, pet_id, status, species))
        except FileNotFoundError: # create new file if pets.csv not found
            print("Error: pets.csv file not found. Creating a new file.")
            open(PETS_FILENAME, mode="w").close()

    @property
    def username(self):
        return self._username
    
    @property
    def user_id(self):
        return self._user_id

    def main_menu(self):
        print("-" * 30)
        print("Main Menu".center(30))
        print("-" * 30)
        print("""What would you like to do today?
    1. Visit friends
    2. Make new friends
    3. Say goodbyes
    4. Settings
    5. Logout
> """,end="")
        return get_int_range("",1,5)

    def display_pets(self):
        # consider new user or no pet found
        print("\n------Friends------")
        if (len(self._pets) != 0):
            for i, pet in enumerate(self._pets, start = 1):
                print(str(i) + ". " + pet.name)
        else:
            print("There are no friends at your house yet!")
    
    def add_pet(self): # add task is separate, done after adding friend
        if len(self._pets) < 3:
            pet_name = get_username("What is the name of your friend? ",[pet.name for pet in self._pets])            
            # Generate a random 5-digit ID
            curr_pet_ids = [pet.pet_id for pet in self._pets]
            while True:
                new_pet_id = str(random.randint(10000, 99999))
                if new_pet_id not in curr_pet_ids:
                    break
                                                
            selected_species = get_int_range("Where are you meeting this friend?\n1. Local park\
                                            \n2. Pokemon World\n3. Age of Dinosaurs\n>> ",1,3)
            
            new_pet = Pet(pet_name, new_pet_id, 5, selected_species)
            self._pets.append(new_pet)
            
            # saving new pet to csv
            with open(PETS_FILENAME, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self._user_id, pet_name, new_pet_id, 5, selected_species])
            
            print(f"{new_pet.name} has arrived!")
        else:
            print(f"There is not enough room for another friend :(")
    
    def remove_pet(self):        
        pet_cnt = len(self._pets)
        if pet_cnt != 0:            
            self.display_pets()
            print(f"{pet_cnt+1}. Nevermind, send me back.")            
            choice = get_int_range("Who will you be saying goodbye to? ",1,pet_cnt+1)
            
            if choice != pet_cnt + 1:
                target_pet = self._pets[choice-1]

                if get_yes_no(f"{target_pet.name} will be leaving. Are you sure? "):
                    # re-read csv to filter
                    new_rows = []
                    with open(PETS_FILENAME, mode="r", newline="") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if row and row[2] != target_pet.pet_id:
                                new_rows.append(row)
                                                
                    # rewrite
                    with open(PETS_FILENAME, mode="w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(new_rows)
                        
                    self._pets.remove(target_pet)
                    print(f"{target_pet.name} has left...")
                else: print("Gotcha! Going back...") # final cancellation
            else: # deletion canceled
                print("Gotcha! Going back...")            
        else: # no pets
            print("There are currently no friends here!")
    
    def pet_handler(self): # handle visitation        
        self.display_pets()
        if (len(self._pets) != 0):
            pet_index = get_int_range("Who would you like to visit? ",1, len(self._pets))
            return self._pets[pet_index-1]
        return None
        
        
        
    
    