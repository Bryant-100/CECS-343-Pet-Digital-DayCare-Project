import random

class Event():
    """ Random one-time effect daily events with consequences on pet's status based on a fix chance
    """
    def park(self):
        """ Park prompt that gains 1 and lose w/ 0; 65%
        Returns:
            tuple of status gained/lost and a respective prompt
        """
        result = 1 if random.random() < 0.65 else 0
        if result == 1:
            prompt="The weather was great today. You both had a fantastic time at the park. It leaves you in a great mood."
        else:
            prompt="The ground is slippery form last night's rain. You lost your footing and fall in the mud. The day starts off gloomy..."
        
        return (result, prompt)

    def swim(self):
        """ Park prompt that gains 2 and lose w/ -1; 45% chance
        Returns:
            tuple of status gained/lost and a respective prompt
        """
        result = 2 if random.random() < 0.45 else -1
        if result == 2:
            prompt="Swimming at the lake feels great! Your choice to pack lunch AND dessert was genius.\nToday was unforgettable!!"
        else:
            prompt="You both went for a swim at a nearby lake, only to realize your change of clothes was left at home. You walk home in the freezing cold..."
        return (result, prompt)
    
    def bake(self):
        """ Park prompt that gains 2 and lose w/ 0; 20% chance
        Returns:
            tuple of status gained/lost and a respective prompt
        """
        result = 2 if random.random() < 0.20 else 0
        if result == 2:
            prompt="You made dessert for your house guests. It was a big hit! The plate was spotless. Elated, you're thinking about opening a bakery..."
        else:            
            prompt="You made dessert for your house guests. It wasn't very popular, now your fridge is filled with leftovers..."
        return (result, prompt)