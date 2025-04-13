from account_manager import AccountManager
from check_input import *


def main():    
    login = True    
    while login:
        print("Welcome to the digital pet daycare!")
        manager = AccountManager()
        user = manager.handle_login()
        session = True
        while session:            
            choice = user.main_menu()
            match choice:
                case 1: #visit friend 
                    user.display_pets()
                    # user.action_handler()                 
                case 2: # add friends                                                            
                    user.add_pet()
                case 3: # remove friend
                    user.remove_pet()
                case 4: # settings (notifs + removal)
                    print("\n----Settings----\n1. Notifications\n2. Delete Account\n3. Go back")
                    setting_choice = get_int_range("What would you like to do? ",1,3)
                    print()
                    match setting_choice:
                        case 1: # notifs
                            pass
                        case 2: # delete current account
                            deletion = get_yes_no("This account will be permanently removed, are you sure? ")
                            if deletion:                   
                                manager.delete_account(user)
                                session = False
                                print("Going back to Login...")
                            else: 
                                print("Going back to main menu...")
                        case 3:
                            print("Going back..")                            
                case 5: # back to main menu
                    print()                
                    break
            print()
    print("See you again!")
    
                
if __name__ == "__main__":
    main()
