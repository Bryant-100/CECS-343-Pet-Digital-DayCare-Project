import tkinter as tk
from PIL import Image, ImageTk
from account_manager import AccountManager


class App:
    """ The main application class for the program; initializes main GUI window
    """
    def __init__(self, root):
        """ Intialize the App with the main Tkinter window

        Args:
            root (Tk): the instance serving as the main application window
        """
        # WINDOW CREATION
        self.root = root
        self.root.title("Digital Daycare")
        
        self.bg_image = Image.open("interfaces/start.png")
        self.bg_width, self.bg_height = self.bg_image.size
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        self.root.geometry(f"{self.bg_width}x{self.bg_height}")
        self.root.resizable(False, False)
                
        # PERMANENT BANNER CREATION
        self.banner_frame = tk.Frame(self.root, bg="#72615A")
        self.banner_frame.pack(fill="x", side="top", anchor="n")

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
        """ Display the starter screen of the application
        """
        self.bg_label = tk.Label(self.frame, image=self.bg_photo) #reload bg label
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # SIGN IN button        
        self.start_img = Image.open("interfaces/log_in.png").resize((280, 95))  #load img
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
        self.new_account_button_img = Image.open("interfaces/new_account_button.png").resize((165, 38))
        self.new_acc_photo = ImageTk.PhotoImage(self.new_account_button_img)
        
        self.new_account_button = tk.Button(
            self.frame,
            image=self.new_acc_photo,
            command= self._manager.open_new_acc_screen,
            borderwidth=0,
            highlightthickness=0,
            highlightbackground="white",
            activebackground="#EE8B5F",
            relief="flat"
        )
        self.new_account_button.place(relx=0.5, rely=0.71, anchor="center")    
        
        # SETTING button
        self.setting_icon_img = Image.open("interfaces/setting_icon.png").resize((45, 40))
        self.setting_icon_photo = ImageTk.PhotoImage(self.setting_icon_img)
        
        self.setting_button = tk.Button(
            self.frame,
            image=self.setting_icon_photo,
            command= self._manager.open_setting_screen,
            borderwidth=0,
            highlightthickness=0,
            highlightbackground="white",
            activebackground="#EE8B5F",
            relief="flat"
        )
        self.setting_button.place(relx=0.08, rely=0.05, anchor="center")

    def back_to_main(self):
        """ Reload the starting screen for the app
        """
        # clears current screen, remove all widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

        # reset background
        self.bg_label = tk.Label(self.frame, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                
        self.setup_main_screen()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
