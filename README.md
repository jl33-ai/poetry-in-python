# poetry-in-python

### Excerpt 0: 
```
We can be so beautiful 
The idea that a human can look at another human being 
Despite our spectrum of subtlety and scepticism
And simply { feel ∩ think } in 1's and 0's that: 
	I want that person, forever \inf 
	And sometimes: 
		Mean it... 
		
Breathtaking simplicity in our code. 
```

### Excerpt 1: 
```
class Heart:
    EMOTIONS = ['love', 'ambition', 'sadness']

    def __init__(self, love=False, ambition=False, sadness=False):
        self.states = {'love': love, 'ambition': ambition, 'sadness': sadness}

    def __str__(self):
        return ", ".join(f"{emotion.capitalize()}: {self.states[emotion]}" for emotion in self.EMOTIONS)

def choose_path(message, options):
    while True:
        print(message)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Choose a number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1

def update_heart(heart, choice_map, choice):
    for emotion, value in choice_map.items():
        heart.states[emotion] = value if choice == 0 else not value
    print(heart)

def pursue_dreams(heart):
    choice = choose_path("Do you fervently embrace love and ambition or reluctantly hold back?", ["Yes, with all my heart", "No, I fear to take the risk"])
    choice_map = {'love': True, 'ambition': True, 'sadness': False}
    update_heart(heart, choice_map, choice)

def face_loss(heart):
    choice = choose_path("Do you succumb to loss and despair or persevere with fortitude?", ["I face loss and feel broken", "I persevere and hold on"])
    choice_map = {'love': False, 'sadness': True}
    update_heart(heart, choice_map, choice)

def find_balance(heart):
    choice = choose_path("Do you seek equilibrium between love and ambition, or continue in turmoil?", ["Yes, I find balance and harmony", "No, I continue to struggle"])
    choice_map = {'love': True, 'ambition': True, 'sadness': False}
    update_heart(heart, choice_map, choice)

# ...

def poetic_journey():
    heart = Heart()
    print("A heart's journey through love, ambition, and life's many challenges begins:\n")

    for _ in range(3):
        pursue_dreams(heart)
        face_loss(heart)
        find_balance(heart)

    print("Embrace the journey, face the melancholy, find enduring love.")
    
    ending = ("In the end, the heart's quest leads to understanding and wisdom. "
              "The struggles faced and choices made carve the unique shape of the heart, "
              "leaving it enriched and enlightened.\n"
              "The heart, once naive and searching, now rests with a newfound serenity and purpose.\n"
              "The journey concludes, but the memories linger on... forever.")

    print(ending)
    blocker0 = input('Ready? 🫴')
    blocker1 = input("Okay, just always remember who you're doing it for. Good luck")
    while True:
        print('be free') 

if __name__ == "__main__":
    poetic_journey()


if __name__ == "__main__":
    poetic_journey()
```

### Excerpt 2
```
from heart import feelings, as_art
... from mind import ideas, unstart
... import world, life
... 
... class Soul:
...     def __init__(self, dreams, love):
...         self.dreams = dreams
...         self.love = love
... 
... def intertwine(heart, mind):
...     poetry = heart + mind
...     return poetry
... 
... def write(poetry):
...     for line in poetry:
...         print(line)
...     
... if __name__ == "__main__":
...     heart = feelings.as_art()
...     mind = ideas.unstart()
...     poetry = intertwine(heart, mind)
...     
...     write(poetry) # prints our unique life's code
...     world.interact() # engages us with the world
...     life.evolve() # ensures we keep growing
```
