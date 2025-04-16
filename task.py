class Task:
    def __init__(self):
        self.pet_id = pet_id
        self.task_id = task_id
        self.description = desc
        self.day_frequency = day_frequency
        self.frequency = frequency
        
    @property
    def task_id(self):
        return self._task_id
    
    @property
    def description(self):
        return self._description
    
    def day_frequency(self):
        pass
    
    def frequency(self):
        pass
   
    #Getters and Setters
    def get_pet_id(self):
        return self.pet_id

    def set_pet_id(self):
        pet_id = NONE  
    
    def get_task_id(self):
        return self.task_id
        
    def set_task_id(self):
        task_id = NONE  
        
    def get_description(self):
        return self.description

    def set_get_description(self):
        get_description = NONE

    def get_day_frequency(self):
        return self.day_frequency

    def set_day_frequency(self):
        day_frequency = NONE

    def get_frequency(self):
        return self.frequency
    
    def set_frequency(self):
        frequency = NONE
    
