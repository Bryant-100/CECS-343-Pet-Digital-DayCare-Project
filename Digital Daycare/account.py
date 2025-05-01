from check_input import *
from pet import Pet
from datetime import datetime
import csv, random

import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox

PETS_FILENAME = "pets.csv"

class Account:
    """ Represent a user account, holds information on the account holder's pet
     Attributes:
        root (Tk): The root Tkinter window
        frame (Frame): The GUI frame where the pet is displayed
        acc (Account): The account associated with this pet
        app (App): the App instance to refer to        
        _username (str): unique 14 character username of the account holder
        _user_id (str): 5-digit unique identifier
        _pets (list): stores Pet owned by account holder
        button_dict (dict): A dictionary to store button widgets associated with pets.
        pet (Pet): The current pet associated with the account (if any).
    """
    def __init__(self, root, frame, app, username, user_id):
        """ Initialize the Account instance with basic user information and setup.
        Args:
            root (Tk): The root Tkinter window
            frame (Frame): The GUI frame where the pet is displayed
            app (App): the App instance to refer to        
            username (str): unique 14 character username of the account holder
            user_id (str): 5-digit unique identifier
        """
        self.root = root
        self.frame = frame
        self.app = app
        self._username = username
        self._user_id = user_id
        self._pets = []
        self.button_dict = {}                
        self.pet = None
    
    @property
    def username(self):
        return self._username

    @property
    def user_id(self):
        return self._user_id
        
    def open_home_screen(self):
        """ Displays the starter screen for home
        """
        # Clear the main screen
        for widget in self.frame.winfo_children():
            widget.destroy()
                
        # Change the background image for this screen
        self.new_bg_image = Image.open("interfaces/template.png")
        self.new_bg_photo = ImageTk.PhotoImage(self.new_bg_image)
        self.bg_label = tk.Label(self.frame, image=self.new_bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)    
            
        self.load_csv() # initialize user
        
        # RETURN BUTTON
        back_button_img = Image.open("interfaces/return_button.png")
        back_button_img = back_button_img.resize((36, 36))
        self.back_button_img_photo = ImageTk.PhotoImage(back_button_img)

        self.back_button = tk.Button(self.frame, image=self.back_button_img_photo, 
                                    command=(self.app).back_to_main, bd=0, border=0,
                                    font=("Courier", 12), borderwidth=0, background="#EE8B5F",
                                    highlightthickness=0, activebackground="#EE8B5F", relief="flat")
        self.back_button.place(relx=0.08, rely=.03)
        
        self.load_banner()
    
    def load_csv(self):
        """ Load in pet data from csv file
        """
        self._pets = []
        today = datetime.today().date()        
        try:            
            with open(PETS_FILENAME, mode="r") as file:
                reader = csv.reader(file)            
                for row in reader:
                    read_user_id, pet_name, pet_id, status, species, animal_id, event, last_date = row
                    if read_user_id == self.user_id: #checking for correct user_id                        
                        if last_date != str(today): #new day == reset mood, reset event attempt
                            status = 1
                            event = 0                            
                        self._pets.append(Pet(self.root, self.frame, self, pet_name, pet_id, int(status), int(species),int(animal_id), int(event)))
        except FileNotFoundError: # create new file if pets.csv not found            
            open(PETS_FILENAME, mode="w").close()
        
        # since creating Pet object will update pet data; we need to save
        self.save_pets()        
    
    def save_pets(self):
        """ Save current pet data to file
        """
        with open(PETS_FILENAME, mode = "r") as file:
            reader = csv.reader(file)

            new_rows = []
            for row in reader:
                read_user_id, pet_name, read_pet_id, status, species, animal_id, event, last_date = row                
                
                if read_user_id == self._user_id: # locate records of user's pet
                    for pet in self._pets: # locate Pet object
                        if pet.pet_id == read_pet_id:
                            new_rows.append([self._user_id, pet_name, read_pet_id, pet.status,\
                                species, animal_id, pet.event, str(datetime.today().date())])
                else: # keep original row if belong to other users
                    new_rows.append(row)
        
        with open(PETS_FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
            
    def load_banner(self):
        """ Load the initial banners for home screen
        """
        selection = {1: "interfaces/domes_banner.png", 
                     2: "interfaces/dino_banner.png"}
        if len(self._pets) > 0: # at least 1
            self.pet1 = self._pets[0]
            room1_banner_img = selection[self.pet1.species]
            image1 = tk.PhotoImage(file=room1_banner_img)
            
            # Store image reference so it's not garbage collected
            self.room1_image = image1            
            # Create main button with image background            
            self.room1_button = tk.Button(self.frame, text=self.pet1.name,image=image1, compound='center',
                                           command=lambda: self.room_selection_handler(self.pet1,1), 
                                           font=("Courier", 29, "bold"), fg='#FFBC9D', 
                                           bd=3, borderwidth=0, highlightthickness=2, activebackground="#C77E5D",
                                           background = "#EE8B5F")
            self.room1_button.place(x=34, rely=0.1)
            self.button_dict[1] = self.room1_button
            
            
            def process_enter_button():
                """ Process button for room selection and moves on to next screen
                """        
                if self.main_button_selected:
                    self.main_button_selected = False
                    for button in self.button_dict.values():
                        if button.winfo_exists():
                            button.config(relief="flat")
                        button.update()
                    
                    (self.pet).open_pet_room()

            # ENTER button            
            self.enter_button_img = tk.PhotoImage(file="interfaces/enter_button.png")            
            self.enter_button = tk.Button(self.frame, image=self.enter_button_img, 
                                          command=process_enter_button,
                                          bd=0, highlightthickness=0, borderwidth=0, background="#EE8B5F",
                                          activebackground="#EE8B5F")
            self.enter_button.place(relx=0.29, y=500)
            
            # SETTING button            
            resized_image = Image.open("interfaces/setting_icon.png").resize((45, 40))
            self.setting_img = ImageTk.PhotoImage(resized_image)
            self.setting_button = tk.Button(self.frame, image=self.setting_img, 
                                          command=self.open_pet_removal_screen,
                                          bd=0, highlightthickness=0, borderwidth=0, background="#EE8B5F",
                                          activebackground="#EE8B5F")
            self.setting_button.place(relx=0.82, rely=.02)

            # Internal state
            self.main_button_selected = False
            
            if len(self._pets) > 1: # at least 2
                self.pet2 = self._pets[1]
                                
                room2_banner_img = selection[self.pet2.species]
                image2 = tk.PhotoImage(file=room2_banner_img)

                self.room2_image = image2                
                self.room2_button = tk.Button(self.frame, text=self.pet2.name,image=image2, compound='center',
                                            command=lambda: self.room_selection_handler(self.pet2,2),
                                            font=("Courier", 29, "bold"), fg='#FFBC9D', 
                                            bd=3, borderwidth=0, highlightthickness=2, activebackground="#C77E5D",
                                            background = "#EE8B5F")
                self.room2_button.place(x=34, rely=0.30)
                self.button_dict[2] = self.room2_button

                if len(self._pets) > 2: # at least 3; limit reached
                    self.pet3 = self._pets[2]
                                        
                    room3_banner_img = selection[self.pet3.species]
                    image3 = tk.PhotoImage(file=room3_banner_img)

                    self.room3_image = image3
                    self.room3_button = tk.Button(self.frame, text=self.pet3.name,image=image3,compound='center',
                                                command=lambda: self.room_selection_handler(self.pet3,3),
                                                font=("Courier", 29, "bold"), fg='#FFBC9D', 
                                                bd=3, borderwidth=0, highlightthickness=2, activebackground="#C77E5D",
                                                background = "#EE8B5F")
                    self.room3_button.place(x=34, rely=0.5)
                    self.button_dict[3] = self.room3_button

                else: # creates 1 button for add pet
                    empty_img = tk.PhotoImage(file="interfaces/empty_banner.png")

                    self.empty_image = empty_img                
                    self.empty_button1 = tk.Button(self.frame,image=empty_img, command=self.open_create_pet_screen,
                                                bd=3, borderwidth=0, highlightthickness=2, activebackground="#C77E5D",
                                                background = "#EE8B5F")
                    self.empty_button1.place(x=34, rely=0.5)
            else: # create two button for add_pet                
                empty_img = tk.PhotoImage(file="interfaces/empty_banner.png")

                self.empty_image = empty_img                
                self.empty_button1 = tk.Button(self.frame,image=empty_img, command=self.open_create_pet_screen,
                                            bd=3, borderwidth=0, highlightthickness=2, activebackground="#C77E5D",
                                            background = "#EE8B5F")
                self.empty_button1.place(x=34, rely=0.30)
                
                self.empty_button2 = tk.Button(self.frame,image=empty_img, command=self.open_create_pet_screen,
                                            bd=3, borderwidth=0, highlightthickness=2, activebackground="#C77E5D",
                                            background = "#EE8B5F")
                self.empty_button2.place(x=34, rely=0.5)       
        else:
            self.open_create_pet_screen()
    
    def room_selection_handler(self, pet, index):
        """ Confirms the room selection for the pet home screen
        Args:
            pet (Pet): the Pet instance to refer to
            index (int): the index of the selected room
        """
        # Deselect the previously selected button (if any) and check if it exists
        if hasattr(self, 'selected_button') and self.selected_button and self.selected_button.winfo_exists():
            self.selected_button.config(relief="flat", background="#EE8B5F", activebackground="#EE8B5F")

        # Get the button from the dictionary using the index
        button = self.button_dict.get(index)

        # If a valid button is found, select it
        if button:
            button.config(relief="sunken", borderwidth=5, background="#C77E5D", activebackground="#AA5D4D")
            self.selected_button = button  # Track the currently selected button
            button.update()            
            self.main_button_selected = True
            self.pet = pet            

    def open_pet_removal_screen(self):
        """ Displays pet removal screen
        """
        for widget in self.frame.winfo_children():
            widget.destroy()
                   
        self.new_bg_image = Image.open("interfaces/choose_account_bg.png") 
        self.new_bg_photo = ImageTk.PhotoImage(self.new_bg_image)

        # Show background on pick screen
        self.bg_label = tk.Label(self.frame, image=self.new_bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                
        # FRIEND LABEL
        friend_label = tk.Label(self.frame, text="Friends", font=("Courier", 23, "bold"), 
                                fg="#72615A", bg="#EE8B5F")
        friend_label.place(relx=0.5, rely=0.18, anchor="center")
        
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
        for account in self._pets:
            self.listbox.insert(tk.END, " " + account.name)

        # Create a scrollbar for the listbox
        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        # Link the scrollbar to the Listbox
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # EXILE BUTTON
        button_bg_img = Image.open("interfaces/bye_button.png")
        button_bg_img = button_bg_img.resize((220, 90))
        button_bg_photo = ImageTk.PhotoImage(button_bg_img)

        def handle_removal():
            """ Handles the removal of selected account        
            """
            selected_index = self.listbox.curselection() # gives index selection
            
            if not selected_index: # return if no selection is made
                return 
            selected_index = selected_index[0]  # get index from tuple of size 1
            selected_pet = self._pets[selected_index]  # get the Account object by index
                
            # Ask for confirmation
            confirmation = messagebox.askyesno(
                title="Confirm Removal",
                message=f"Say goodbye to {selected_pet.name}?")
            
            # Process removal with CSV
            if confirmation:                
                new_rows = []
                with open(PETS_FILENAME, mode="r", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row and row[2] != selected_pet.pet_id:
                            new_rows.append(row)

                # Rewrite CSV without the deleted account
                with open(PETS_FILENAME, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(new_rows)
                self._pets.remove(selected_pet)
                
                # Call back to the main screen
                self.open_home_screen()

        self.select_button = tk.Button(self.frame, image=button_bg_photo, 
                                    command = handle_removal, bd=0, border=0,
                                    font=("Courier", 12), borderwidth=0, background="#EE8B5F",
                                    highlightthickness=0, activebackground="#EE8B5F", relief="flat")
        self.select_button.place(relx=0.5, rely=0.65, anchor="center")

        # Keep a reference to the button background image to prevent garbage collection
        self.select_button.image = button_bg_photo  # Store a reference to the image
        
        # BACK BUTTON
        back_button_img = Image.open("interfaces/return_button.png")  # Load the image
        back_button_img = back_button_img.resize((38, 38))  # Resize to fit your button size
        self.back_button_img_photo = ImageTk.PhotoImage(back_button_img)  # Keep reference with self.

        self.back_button = tk.Button(self.frame, image=self.back_button_img_photo, 
                                    command=self.open_home_screen, bd=0, border=0,
                                    font=("Courier", 12), borderwidth=0, background="#EE8B5F",
                                    highlightthickness=0, activebackground="#EE8B5F", relief="flat")
        self.back_button.place(relx=0.1, rely=.1, anchor="center")
    
    def open_create_pet_screen(self):
        """ Display and Process pet creation 
        """
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        self.selected_animal_id = None
        self.selected_button = None
        
        self.new_bg_image = Image.open("interfaces/template.png")  # New background image
        self.new_bg_photo = ImageTk.PhotoImage(self.new_bg_image)
        
        self.bg_label = tk.Label(self.frame, image=self.new_bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # dog, cat, ham, rex, bronto, trice
        image_paths = [
            "pets/dog.png", "pets/cat.png", "pets/ham.png",
            "pets/rex.png", "pets/bronto.png", "pets/trice.png"]
        self.selected_index = [None]  # Mutable to update inside inner functions
        
        # Inner frame (smaller)
        container = tk.Frame(self.frame, width=435, height=380, background="#C77E5D", bd=0, relief="flat")
        container.place(relx=0.5, rely=0.47, anchor="center")  # Center it at 40% height
        
        # BACK BUTTON; disabled for now
        # back_button_img = Image.open("return_button.png")
        # back_button_img = back_button_img.resize((36, 36))
        # self.back_button_img_photo = ImageTk.PhotoImage(back_button_img)

        # self.back_button = tk.Button(self.frame, image=self.back_button_img_photo, 
        #                             command=(self.app).back_to_main, bd=0, border=0,
        #                             font=("Courier", 12), borderwidth=0, background="#EE8B5F",
        #                             highlightthickness=0, activebackground="#EE8B5F", relief="flat")
        # self.back_button.place(relx=0.08, rely=.03)
        
        # Canvas and scrollbar                
        canvas = tk.Canvas(container, background="#C77E5D", width=359, height=275,
                        bd=0, highlightthickness=0)

        # Create style for ttk.Scrollbar
        style = ttk.Style()
        style.configure("Vertical.TScrollbar",
            background="#C77E5D", #bar
            troughcolor="white",            
            relief='raised'
        )
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview, style="Vertical.TScrollbar")

        scrollable_frame = tk.Frame(canvas, background="#C77E5D",padx=10, pady=23)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mouse wheel scrolling to canvas
        def on_mouse_wheel(event):
            """Handle mouse wheel scrolling."""
            if canvas.winfo_exists():  # Check if the canvas still exists
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        # Bind mouse wheel event directly to the canvas (not globally)
        canvas.bind("<MouseWheel>", on_mouse_wheel)  # For Windows
        canvas.bind("<Button-4>", on_mouse_wheel)  # For Linux (wheel up)
        canvas.bind("<Button-5>", on_mouse_wheel)  # For Linux (wheel down)

        # Store images and buttons as before
        images = []
        self.buttons = []

        def on_image_clicked(idx):
            """ Helper function to handle image click event """            
            self.selected_index[0] = idx
            if self.selected_index[0] is not None:
                self.selected_animal_id = self.selected_index[0]
            
            # Only highlight the clicked button — don't reset others yet
            if self.selected_button:
                self.selected_button.config(relief="flat", background="#C77E5D")

            selected_btn = self.buttons[idx - 1]  # idx was passed as idx+1
            selected_btn.config(relief="sunken", background="#72615A", bd=3)
            self.selected_button = selected_btn

        # Create buttons for each image
        for idx, path in enumerate(image_paths):
            img = Image.open(path)
            img = img.resize((90, 90))  # Resize image to fit button
            photo = ImageTk.PhotoImage(img)
            images.append(photo)

            btn = tk.Button(scrollable_frame, image=photo, 
                            command=lambda idx=idx: on_image_clicked(idx+1), highlightcolor="#C77E5D", 
                            bd=0, relief="flat", background="#C77E5D", activebackground="#C77E5D",
                            activeforeground="#C77E5D")
            row = idx // 3
            col = idx % 3
            btn.grid(row=row, column=col, padx=10, pady=10)
            self.buttons.append(btn)

        scrollable_frame.images = images        
        
        
        # PET NAME LABEL
        question_label = tk.Label(self.frame, text="Enter your new", font=("Courier", 24, "bold"), 
                                fg="#72615A", bg="#EE8B5F")
        question_label.place(relx=0.5, rely=0.12, anchor="center")   
        
        friend_label = tk.Label(self.frame, text="friend's name", font=("Courier", 24, "bold"), 
                                fg="white", bg="#EE8B5F")
        friend_label.place(relx=0.5, rely=0.17, anchor="center")   

        # TEXT ENTRY BOX
        self.pet_name_entry = tk.Entry(self.frame, font=("Courier", 24), width = 13)
        self.pet_name_entry.place(relx=0.5, rely=0.23, anchor="center")  # Place it between the images and confirm button

        # ERROR LABEL (initially invisible)
        self.error_label = tk.Label(self.frame, text="Please enter a name", 
                                        font=("Courier", 14, "bold"), fg="white", bg="#BC0E00")
        self.error_label.place(relx=0.5, rely=0.1, anchor="center")  # Just below the entry box
        self.error_label.place_forget()

        # CONFIRM button
        self.confirm_button_image = Image.open("interfaces/confirm_button.png")  # Replace with your image file path
        self.confirm_button_image = self.confirm_button_image.resize((226, 85))  # Resize to fit the button
        self.confirm_button_photo = ImageTk.PhotoImage(self.confirm_button_image)  # Corrected this line
        
        self.confirm_button = tk.Button(self.frame, image=self.confirm_button_photo, 
                                        command = self.pet_creation_handler, 
                                        bd=0, highlightthickness=0, activebackground="#EE8B5F")
        self.confirm_button.place(relx=0.5, rely=0.75, anchor="center")  # Position it in the center       

    def pet_creation_handler(self):
        """ Handles pet selection and username and moves to next screen
        """
        pet_name = self.pet_name_entry.get()
        if len(pet_name) > 14:
            self.error_label.config(text="Name is too long (max 14 characters)")
            self.error_label.place(relx=0.5, rely=0.15, anchor="center")
            return
                
        if not pet_name.strip():
            self.error_label.place(relx=0.5, rely=0.15, anchor="center")  # Show error
        else:
            self.error_label.place_forget()  # Hide error if input is fine
            if self.selected_animal_id is not None:
                species = 1 if self.selected_animal_id < 4 else 2            
                
                curr_ids = [pet.pet_id for pet in self._pets]
                while True:
                    new_id = str(random.randint(10000, 99999))
                    if new_id not in curr_ids:
                        break
                new_pet = Pet(self.root, self.frame,self, pet_name, new_id, 1, 
                            species, self.selected_animal_id, 0)
                self._pets.append(new_pet)
                self.pet = new_pet
                # save new pet to csv
                with open(PETS_FILENAME, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([self._user_id, pet_name, new_id, 1, species, self.selected_animal_id,0 , datetime.today().date()])
                
                # Reset button visual state
                if self.selected_button:
                    self.selected_button.config(relief="flat", background="#C77E5D")
                    self.selected_button = None

                (self.pet).open_pet_room()

