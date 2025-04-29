
from check_input import *
from account import Account
import csv, random

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

ACC_FILENAME = "users.csv"

class AccountManager:    
    def __init__(self, root, frame, app):
        """ Loads in accounts from file
        Args:
            root (tkinter.Tk): the Root instance to be passed on
            frame (tkinter.Frame): the Frame instance to be passed on
            app (App): the App instance to pass on
        """
        self._users = []
        self.root = root
        self.frame = frame
        self.app = app
        self._selected_user = None
        try:            
            with open(ACC_FILENAME, mode="r") as file:
                reader = csv.reader(file)            
                for row in reader:
                    username, user_id = row
                    self._users.append(Account(self.root, self.frame, app, username, user_id))
        except FileNotFoundError: # create new file if users.csv not found            
            open(ACC_FILENAME, mode="w").close()
    
    @property
    def user(self):
        return self._selected_user
  
    def open_new_acc_screen(self):
        """ Display the screen to create a new account
        """
        # Clear screen
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Change bg
        self.new_bg_image = Image.open("new_account_bg.png")  # New background image
        self.new_bg_photo = ImageTk.PhotoImage(self.new_bg_image)
        self.bg_label = tk.Label(self.frame, image=self.new_bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # RETURN button
        self.return_img = Image.open("return_button.png").resize((33,33))
        self.return_button_image = ImageTk.PhotoImage(self.return_img)     
        self.return_button = tk.Button(self.frame, image=self.return_button_image, background="#EE8B5F",
                                       activebackground="#EE8B5F", highlightbackground="#EE8B5F",
                                       command=(self.app).setup_main_screen, borderwidth=0)
        self.return_button.place(relx=0.05, rely=0.03)
        
        # Enter your username:
        self.label = tk.Label(self.frame, text="Enter your username:", font=("Courier", 17, "bold"), fg="#72615A", bg= "#C77E5D")
        self.label.place(relx=0.5, rely=0.35, anchor="center")

        # Add a text input (Entry widget)
        self.username_entry = tk.Entry(self.frame, font=("Courier", 14), width = 20)
        self.username_entry.place(relx=0.5, rely=0.40, anchor="center")

        # CONFIRM BUTTON
        self.confirm_button_image = Image.open("confirm_button.png")  # Replace with your image file path
        self.confirm_button_image = self.confirm_button_image.resize((310, 106))  # Resize to fit the button
        self.confirm_button_photo = ImageTk.PhotoImage(self.confirm_button_image)  # Corrected this line
        
        self.confirm_button = tk.Button(self.frame, image=self.confirm_button_photo, 
                                        command = self.process_new_acc, 
                                        bd=0, highlightthickness=0, activebackground="#EE8B5F")
        self.confirm_button.place(relx=0.5, rely=0.62, anchor="center")  # Position it in the center
        
    def process_new_acc(self):
        """ Handles the creation of a new account        
        """
        # choose and validate username
        new_username = self.username_entry.get()        
        
        # Check if the username is empty
        if not new_username:
            #removes previous error labels
            if hasattr(self, 'error_label'): 
                self.error_label.destroy()
            
            # Show an error message if the username is empty
            self.error_label = tk.Label(self.frame, text="Please enter a username", 
                                        font=("Courier", 13, "bold"), fg="white", bg="#BC0E00")
            self.error_label.place(relx=0.5, rely=0.31, anchor="center")
            return  # Stop further processing
        
        # Remove the error label if it exists
        if hasattr(self, 'error_label'):
                self.error_label.destroy()
        
        curr_usernames = [account.username for account in self._users]
        
        while new_username in curr_usernames:
            # Show error message that the username is taken
            self.error_label = tk.Label(self.frame, text="That username is taken", 
                                        font=("Courier", 13, "bold"), fg="white", bg="#BC0E00")
            self.error_label.place(relx=0.5, rely=0.31, anchor="center")

            # Clear the username entry box and ask for a new one
            self.username_entry.delete(0, tk.END)
            self.username_entry.focus()  # Focus back to the entry box

            return  # Exit the current method, forcing the user to try again

        # Generate a random 5-digit ID
        curr_ids = [account.user_id for account in self._users]
        while True:
            new_id = str(random.randint(10000, 99999))
            if new_id not in curr_ids:
                break
        new_acc = Account(self.root, self.frame,self.app, new_username, new_id)
        self._users.append(new_acc)
        self._selected_user = new_acc
        
        # saving new account to csv
        with open(ACC_FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_username, new_id])
        
        (self._selected_user).open_home_screen()
  
    def open_login_screen(self):
        """ Display screen to choose accounts
        """
        for widget in self.frame.winfo_children():
            widget.destroy()
                   
        self.new_bg_image = Image.open("choose_account_bg.png")  # New background image
        self.new_bg_photo = ImageTk.PhotoImage(self.new_bg_image)

        # Show background on pick screen
        self.bg_label = tk.Label(self.frame, image=self.new_bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # ACCOUNT LABEL
        account_label = tk.Label(self.frame, text="Accounts", font=("Courier", 22, "bold"), 
                                fg="#72615A", bg="#EE8B5F")
        account_label.place(relx=0.5, rely=0.18, anchor="center")     
        
        # RETURN button
        self.return_img = Image.open("return_button.png").resize((33,33))
        self.return_button_image = ImageTk.PhotoImage(self.return_img)     
        self.return_button = tk.Button(self.frame, image=self.return_button_image, background="#EE8B5F",
                                       activebackground="#EE8B5F", highlightbackground="#EE8B5F",
                                       command=(self.app).setup_main_screen, borderwidth=0)
        self.return_button.place(relx=0.05, rely=0.03)
        
        
        # SCROLLBAR; frame
        listbox_frame = tk.Frame(self.frame, bg="white")
        listbox_frame.place(relx=0.5, rely=0.38, anchor="center")

        # Create a listbox with options
        self.listbox = tk.Listbox(listbox_frame, font=("Courier", 23), height=5, width=15,
                                borderwidth=0, highlightthickness=0, selectmode=tk.SINGLE,
                                fg="#72615A", bg="white", selectbackground="#72615A", 
                                selectforeground="white", activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True, pady=10)  # Pack inside the listbox_frame

        # Add items to the listbox
        for account in self._users:
            self.listbox.insert(tk.END, " " + account.username)
        
        if not self._users:
            # Display "No accounts located" message above the listbox
            no_user_label = tk.Label(self.frame, text="No accounts located", font=("Courier", 16, "bold"),
                                     fg="#BC0E00", bg="white", pady=20)
            no_user_label.place(relx=0.5, rely=0.33, anchor="center")
        
        # Create a scrollbar for the listbox
        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        # Link the scrollbar to the Listbox
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # CONFIRM BUTTON
        button_bg_img = Image.open("confirm_button.png")  # Replace with your image
        button_bg_img = button_bg_img.resize((240, 80))  # Resize to fit your button size
        button_bg_photo = ImageTk.PhotoImage(button_bg_img)

        self.select_button = tk.Button(self.frame, image=button_bg_photo, 
                                    command = self.handle_login, bd=0, border=0,
                                    font=("Courier", 12), borderwidth=0, 
                                    highlightthickness=0, activebackground="#EE8B5F", relief="flat")
        self.select_button.place(relx=0.5, rely=0.65, anchor="center")

        # Keep a reference to the button background image to prevent garbage collection
        self.select_button.image = button_bg_photo  # Store a reference to the image
  
    def handle_login(self):
        """ Handles user selection and calls next screen
        """
        selected_index = self.listbox.curselection() # gives index selection
        
        if not selected_index:
            return
        selected_index = selected_index[0]  # get index from tuple of size 1

        selected_user = self._users[selected_index]  # get the Account object by index
        self._selected_user = selected_user        
        (self._selected_user).open_home_screen()
        
    def open_setting_screen(self): 
        """ Displays the starter setting screen
        """
        for widget in self.frame.winfo_children():
            widget.destroy()
                   
        self.new_bg_image = Image.open("choose_account_bg.png")  # New background image
        self.new_bg_photo = ImageTk.PhotoImage(self.new_bg_image)

        # Show background on pick screen
        self.bg_label = tk.Label(self.frame, image=self.new_bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # ACCOUNT LABEL
        account_label = tk.Label(self.frame, text="Accounts", font=("Courier", 22, "bold"), 
                                fg="#72615A", bg="#EE8B5F")
        account_label.place(relx=0.5, rely=0.18, anchor="center")     
        
        # SCROLLBAR; frame
        listbox_frame = tk.Frame(self.frame)
        listbox_frame.place(relx=0.5, rely=0.38, anchor="center")

        # Create a listbox with options
        self.listbox = tk.Listbox(listbox_frame, font=("Courier", 23), height=5, width=15,
                                borderwidth=0, highlightthickness=0, selectmode=tk.SINGLE,
                                fg="#72615A", bg="white", selectbackground="#72615A", 
                                selectforeground="white", activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)  # Pack inside the listbox_frame

        # Add items to the listbox
        for account in self._users:
            self.listbox.insert(tk.END, " " + account.username)

        # Create a scrollbar for the listbox
        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        # Link the scrollbar to the Listbox
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # CONFIRM BUTTON
        button_bg_img = Image.open("delete_button.png")  # Replace with your image
        button_bg_img = button_bg_img.resize((240, 90))  # Resize to fit your button size
        button_bg_photo = ImageTk.PhotoImage(button_bg_img)

        self.select_button = tk.Button(self.frame, image=button_bg_photo, 
                                    command = self.handle_removal, bd=0, border=0,
                                    font=("Courier", 12), borderwidth=0, 
                                    highlightthickness=0, activebackground="#EE8B5F", relief="flat")
        self.select_button.place(relx=0.5, rely=0.65, anchor="center")

        # Keep a reference to the button background image to prevent garbage collection
        self.select_button.image = button_bg_photo  # Store a reference to the image
  
    def handle_removal(self):
        """ Handles the removal of selected account        
        """
        selected_index = self.listbox.curselection() # gives index selection
        
        if not selected_index: # return if no selection is made
            return 
        selected_index = selected_index[0]  # get index from tuple of size 1

        selected_user = self._users[selected_index]  # get the Account object by index
            
        # Ask for confirmation
        confirmation = messagebox.askyesno(
            title="Confirm Deletion",
            message=f"Delete the account of {selected_user.username}?"
        )
        
        # Process removal with CSV
        if confirmation:            
            new_rows = []
            with open(ACC_FILENAME, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[1] != selected_user.user_id:
                        new_rows.append(row)

            # Rewrite CSV without the deleted account
            with open(ACC_FILENAME, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)

            self._users.remove(selected_user)  # Remove from the list of users

            # Call back to the main screen
            self.app.back_to_main()            

            
        