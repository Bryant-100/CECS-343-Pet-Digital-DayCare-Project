from check_input import *


class Task:
    """ Serves as a container called activities
        Attributes:
            root (Tk): root Tkinter window
            frame (tkFrame): GUI frame to display
            pet (Pet): associated pet object
            _pet_id (str): unique 5-digit id of Pet instance
            _task_id (str): unique 5-digit id of Task instance
            _desc (str): task's text description
            _status (str): the task's completion status; 1 for completed, 0 otherwise
    """
    def __init__(self, root, frame,pet, pet_id, task_id, description, status):
        """ Initializes a Task object
        Args:
            root (Tk): root Tkinter window
            frame (tk.Frame): frame where the task will be displayed or controlled
            pet (Pet): the pet this task is associated with
            pet_id (str): unique 5-digit ID of the pet
            task_id (str): unique 5-digit ID of the task
            description (str): the textual description of the task
            status (int): task status; 1 for completed, 0 for not completed
        """
        self.root = root
        self.frame = frame
        self.pet = pet
        
        self._pet_id = pet_id
        self._desc = description
        self._status = status
        self._task_id = task_id
    
    @property
    def task_id(self):
        return self._task_id
    
    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, new_desc):
        self._desc = new_desc
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):        
        self._status = new_status
