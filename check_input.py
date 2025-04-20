def get_int(prompt):
    """ Validate user input as an integer
    Args:
        prompt(str): display prompt before taking input
    Returns:
        user input of an integer
    """
    value = 0
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            valid = True
        except ValueError:
            print("Invalid - input needs to be an integer.")
    return value

def get_float(prompt):
    """ Validate user input as a Float type
    Args:
        prompt(str): display prompt before taking input
    Returns:
        value of float type
    """
    value = 0
    valid = False
    while not valid:
        try:
            value = float(input(prompt))
            valid = True
        except ValueError:
            print("Invalid - input needs to be a decimal value.")
    return value

def get_positive_int(prompt):
    """ Validate user input as a positive integer
    Args:
        prompt(str): display prompt before taking input
    Returns:
        user input of a positive integer
    """
    value = 0
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            if value >= 0:
                valid = True
            else:
                print("Invalid - input can't not be negative.")
        except ValueError:
            print("Invalid - input needs to be an integer.")
    return value  

def get_int_range(prompt, low, high):
    """ Validate user input as an integer between the specified range (inclusive)
    Args:
        prompt(str): display prompt before taking input
        low (int): lower range bound
        high (int): higher range bound
    Returns:
        an integer within the specified range
    """
    value = 0
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            if value >= low and value <= high:
                valid = True
            else:
                print("Invalid - input is not within range of " + str(low) + "-" + str(high) + ".")
        except ValueError:
            print("Invalid - input needs to be an integer.")
    return value

def get_yes_no(prompt):
    """ Validate user input for yes/no OR y/n
    Args:
        prompt(str): display prompt before taking input
    Returns:
        True for yes, False otherwise
    """
    valid = False
    while not valid:
        value = input(prompt).upper()
        if value == "YES" or value == "Y":
            return True
        elif value == "NO" or value == "N":
            return False
        else:
            print("Invalid - input is either 'Yes/Y' or 'No/N'")

def get_username(prompt, curr_usernames):
    """ Validate the current username
    Args:
        prompt(str): display prompt before taking input
        new_user (str): the chosen username
        curr_usernames (str[]): the list of existing usernames
    Returns:
        a unique username
    """
    username = input(prompt)    
    while username in curr_usernames:
        print("That name is taken :(")
        username = input("Please choose another name: ")
    return username
    
    
    