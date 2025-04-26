import random

class Challenge():    
    def park(self): 
        result = 1 if random.random() < 0.75 else 0
        if result == 1:
            print("The weather is great today. You both had a fantastic time at the park. It leaves you in a great mood.")
        else:
            print("The ground is slippery form last night's rain. You lose your footing and fall.")
            print("You're now covered in mud. The day starts off gloomy...")
        
        return result

    def swim(self):
        result = 2 if random.random() < 0.50 else -1
        if result == 2:
            print("Swimming at the lake feels great! Your choice to pack lunch AND desert was genius.\nToday was unforgettable!!")
        else:
            print("You both went for a swim at a nearby lake, only to realize your towels and change of clothes were left at home. You walk home in the cold and feel sickness creeping in.")            
        return result
    
    def bake(self): 
        result = 2 if random.random() < 0.25 else 0
        if result == 2:
            print("You made desert for your house guests. It was a big hit! The plate was spotless. \nElated, you're thinking about opening a bakery...")
        else:
            # print("You baked something for desert, but the milk you used was expired.\nBoth you and your guest fell sick. The discomfort lasted throughout the night...") #negative instance
            print("You made desert for your house guests. It wasn't very popular, now your fridge is filled with leftovers...")
        return result