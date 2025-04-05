from account_manager import AccountManager

def display_menu():
    print("\nMain Menu:")
    print("1. View Pets")
    print("2. Notification Settings")
    print("3. Account Settings")
    print("7. Exit")

def main():

    while True:
        print("Welcome to the digital pet daycare!")
        manager = AccountManager()
        if manager.handle_login(): # exits otherwise
            # print pet here
            pass
        else: 
            pass
                
if __name__ == "__main__":
    main()
