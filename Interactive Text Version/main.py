from account_manager import AccountManager
from check_input import *


def main():    
    login = True    
    manager = AccountManager()
    while login:
        print("Welcome to the digital pet daycare!")        
        user = manager.handle_login()
        
        session = True if user is not None else False        
        while session:
            choice = user.main_menu()
            match choice:
                case 1: #visit friend
                    pet = user.pet_handler()
                    pet_room = True

                    while pet_room:                        
                        if pet: #if there is a pet
                            task_menu_opt = pet.pet_menu() # choose
                            
                            match task_menu_opt:
                                case 1: #mark complete
                                    pet.mark_list_complete()
                                    user.save_pets()
                                case 2: #mark incomplete
                                    pet.mark_list_incomplete()
                                    user.save_pets()
                                case 3: # Challenge
                                    pet.process_challenge()
                                    # saves pet's challenge and status
                                    user.save_pets()
                                case 4: # activity center
                                    pet.task_handler()
                                case 5: # Return
                                    pet_room = False
                                case default:
                                    continue
                        else:         
                            pet_room = False                                            
                case 2: # add friends                                                            
                    user.add_pet()
                case 3: # remove friend
                    user.remove_pet()
                case 4: # settings (notifs + removal)
                    print("\n----Settings----\n1. Delete Account\n2. Go back")
                    setting_choice = get_int_range("What would you like to do? ",1,2)
                    print()
                    match setting_choice:                        
                        case 1: # delete current account
                            deletion = get_yes_no("This account will be permanently removed, are you sure? ")
                            if deletion:                   
                                manager.delete_account(user)
                                session = False
                                print("Going back to Login...")
                            else: 
                                print("Going back to main menu...")
                        case 2:
                            print("Going back..")                            
                case 5: # back to main menu
                    print()
                    break
                              
            print()
    print("See you again!")
    
                
if __name__ == "__main__":
    main()
