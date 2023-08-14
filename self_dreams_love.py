from heart import feelings, as_art
from mind import ideas, unstart
import world, life

class Soul:
    def __init__(self, dreams, love):
        self.dreams = dreams
        self.love = love

def intertwine(heart, mind):
    poetry = heart + mind
    return poetry

def write(poetry):
    for line in poetry:
        print(line)
    
if __name__ == "__main__":
    heart = feelings.as_art()
    mind = ideas.unstart()
    poetry = intertwine(heart, mind)
    
    write(poetry) # prints our unique life's code
    world.interact() # engages us with the world
    life.evolve() # ensures we keep growing


    
