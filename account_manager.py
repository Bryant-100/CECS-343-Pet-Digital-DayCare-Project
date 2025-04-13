from check_input import *
from account import Account
import csv, random

ACC_FILENAME = "users.csv"

class AccountManager:
    """ Handles actions involving accounts
    Attributes:
        _users(Account[]): stores a list of Account objects
    """
    def __init__(self):
        """ Loads in recorded accounts
        Args:
            self (AccountManager): the AccountManager instance to be initialized
        Returns:
            None
        """
        self._users = []
        try:            
            with open(ACC_FILENAME, mode="r") as file:
                reader = csv.reader(file)            
                for row in reader:
                    username, user_id, pet1_id, pet2_id, pet3_id = row
                    self._users.append(Account(username, user_id,[pet1_id, pet2_id, pet3_id]))
        except FileNotFoundError: # create new file if users.csv not found
            print("Error: users.csv file not found. Creating a new file.")
            open(ACC_FILENAME, mode="w").close()            
    
    def display_accounts(self):
        """ Display current accounts
        Args:
            self (AccountManager): the AccountManager instance to be accessed
        Returns:
            None
        """
        print("\nAccounts:")
        if len(self._users) != 0:
            for index,acc in enumerate(self._users, start=1):
                print(f"{index}. {acc.username}")
        else:
            print("No existing users.")
        
    def choose_account(self):        
        """ Display available username and process chosen account                        
        Args:
            self (AccountManager): the AccountManager instance to be accessed
        Returns:
            the Account object chosen by the user
        """
        # its length is additionally used as index for Exit option
        curr_users = len(self._users) 
        if curr_users==0: # if no users, create new account
            print("There are no existing accounts. Let's make a new one!\n")
            return self.create_account()
        else:    
            self.display_accounts()            
            print(f"{curr_users+ 1}. Return to Login")
            print("Which account is yours? ", end="")
            
            choice = get_int_range("",1, curr_users+1)
            if choice != curr_users+1:                                    
                return self._users[choice-1]
            else:
                return -1
    
    def create_account(self):
        """ Create a new account for the user
        Args:
            self (AccountManager): the AccountManager instance to be accessed
        Returns:
            the newly created Account object 
        """
        # choose and validate username
        username = get_username([account.username for account in self._users])

        # Generate a random 5-digit ID
        curr_ids = [account.user_id for account in self._users]
        while True:
            new_id = str(random.randint(10000, 99999))
            if new_id not in curr_ids:
                break
        
        # Create and store Account instance
        new_account = Account(username, new_id, [-1] * 3)
        self._users.append(new_account)
        
        # saving new account to csv
        with open(ACC_FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, new_id,-1,-1,-1])        
                
        print(f"Account created!")
        return new_account
    
    def delete_account(self, account): # takes Account object
        users_cnt = len(self._users)
                
        if users_cnt != 0:                                               
            # re-read csv to filter
            new_rows = []
            with open(ACC_FILENAME, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[1] != account.user_id:
                        new_rows.append(row)
            
            # rewrite
            with open(ACC_FILENAME, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)            
                                     
            self._users.remove(account)
            print(f"Removal completed.")
        else:
            print("There's no accounts to delete.")
    
    def handle_login(self):
        """ Manages login process
        Args:
            self (AccountManager): the AccountManager instance to be accessed
        Returns:
            True if successful, False otherwise
        """
        have_account = get_yes_no("1. Do you have an account already? ")
        if have_account:            
            user = self.choose_account()
            if user != -1:
                print()
                print("~" * 7 + f" Welcome {user.username}! " + "~" * 7)
                return user
        else:            
            return self.create_account()
    
    def handle_logout():
        pass
    
    
            
        