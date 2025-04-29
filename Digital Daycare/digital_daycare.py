import tkinter as tk
from PIL import Image, ImageTk
from account_manager import AccountManager
import csv


class App:
    def __init__(self, root):
        # WINDOW CREATION
        self.root = root
        self.root.title("Digital Daycare")
        
        self.bg_image = Image.open("start.png")
        self.bg_width, self.bg_height = self.bg_image.size
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.root.geometry(f"{self.bg_width}x{self.bg_height}")# window size to bg
        self.root.resizable(False, False)
                
        # PERMANENT BANNER CREATION
        self.banner_frame = tk.Frame(self.root, bg="#72615A")
        self.banner_frame.pack(fill="x", side="top", anchor="n")  # Place banner at the top        

        self.banner_button = tk.Button(self.banner_frame, text="Log Out", command=self.back_to_main,
                                       font=("Courier", 12,"bold"), bd=0, fg = "#3E302A",
                                       bg="#7E6D66", activebackground="#7E6D66")
        self.banner_button.pack(side="right", padx=10, pady=10)
                
        self.frame = tk.Frame(self.root) # body frame
        self.frame.pack(fill="both", expand=True)
        
        # PREPROCESSES        
        self._manager = AccountManager(self.root, self.frame, self)        
        self.setup_main_screen()
        

    
    def setup_main_screen(self):        
        self.bg_label = tk.Label(self.frame, image=self.bg_photo) #reload bg label
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # SIGN IN button        
        self.start_img = Image.open("log_in.png").resize((280, 95))  #load img
        self.start_photo = ImageTk.PhotoImage(self.start_img)
        
        self.start_button = tk.Button(
            self.frame,
            image=self.start_photo,
            command=self._manager.open_login_screen,
            borderwidth=0,
            highlightthickness=0,
            highlightbackground="white",            
            activebackground="#EE8B5F",
            relief="flat"
        )        
        self.start_button.place(relx=0.5, rely=0.60, anchor="center")
        
        # NEW ACCOUNT button
        self.new_account_button_img = Image.open("new_account_button.png").resize((165, 38))
        self.new_acc_photo = ImageTk.PhotoImage(self.new_account_button_img)
        
        self.new_account_button = tk.Button(
            self.frame,
            image=self.new_acc_photo,
            command= self._manager.open_new_acc_screen,
            borderwidth=0,                   # No default border around the button
            highlightthickness=0,
            highlightbackground="white",     # Border color when clicked (not visible with highlightthickness=0)            
            activebackground="#EE8B5F",        # Button background color when clicked
            relief="flat"                    # Make it flat (removes button 3D effect)            
        )
        self.new_account_button.place(relx=0.5, rely=0.71, anchor="center")    
        
        # SETTING button
        self.setting_icon_img = Image.open("setting_icon.png").resize((45, 40))
        self.setting_icon_photo = ImageTk.PhotoImage(self.setting_icon_img)
        
        self.setting_button = tk.Button(
            self.frame,
            image=self.setting_icon_photo,
            command= self._manager.open_setting_screen,
            borderwidth=0,                   # No default border around the button
            highlightthickness=0,
            highlightbackground="white",     # Border color when clicked (not visible with highlightthickness=0)            
            activebackground="#EE8B5F",        # Button background color when clicked
            relief="flat"                    # Make it flat (removes button 3D effect)            
        )
        self.setting_button.place(relx=0.08, rely=0.05, anchor="center")


    def back_to_main(self):
        # clears current screen, remove all widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

        # reset background
        self.bg_label = tk.Label(self.frame, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Recreate initial widgets (the main screen setup)
        self.setup_main_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
