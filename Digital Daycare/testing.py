from account_manager import AccountManager
import tkinter as tk
import unittest
from unittest.mock import MagicMock

from pet import Pet

class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a minimal Tk root window and frame for testing
        self.root = tk.Tk()        
        self.frame = tk.Frame(self.root)
        self.app = MagicMock()
        self.root.withdraw()  # Hide root window
                
        self.manager = AccountManager(self.root, self.frame, self.app)

        self.manager.listbox = MagicMock() # simulate account list
        
        # Simulate the selection of an item (index 0 in this case)
        self.manager.listbox.curselection.return_value = (0,)
        self.manager._users = [MagicMock(username="user1")] # Initialize test users
    
    def test_account_removal(self):
        # ensure we have 1 account
        self.assertEqual(len(self.manager._users), 1)
        self.manager.handle_removal() # Simulate account removal
        self.assertEqual(len(self.manager._users), 0)

    def test_account_addition(self):
        # simulate adding a new user
        new_user = MagicMock(username="user2")
        self.manager._users.append(new_user)
        
        self.assertEqual(len(self.manager._users), 2)
        self.assertEqual(self.manager._users[1].username, "user2")  # Verify new user is added

    def test_account_selection(self):
        # simulate selection of the first user
        self.manager.listbox.curselection.return_value = (0,)
        selected_user = self.manager._users[self.manager.listbox.curselection()[0]]
        # ensure selected user is the one at index 0
        self.assertEqual(selected_user.username, "user1")
    
    def test_handle_removal_empty_list(self):
        self.manager._users = []  # Ensure there are no users
        self.manager.listbox.curselection.return_value = ()  # simulate no selection
        
        self.manager.handle_removal()        
        self.assertEqual(len(self.manager._users), 0)

            
if __name__ == "__main__":
    unittest.main()
