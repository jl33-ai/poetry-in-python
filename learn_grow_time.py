from life import learn, grow
from time import past, now
import future, change

class You:
    def __init__(self, curiosity, ambition):
        self.curiosity = curiosity
        self.ambition = ambition

def embrace_change(you, life):
    path = you.curiosity + life.learn()
    return path

def travel_through_time(path):
    for moment in path:
        print(moment)  # each moment is a lesson

if __name__ == "__main__":
    you = You(curiosity=True, ambition=True)
    path = embrace_change(you, life)

    travel_through_time(path)  # live, learn, grow
    future.prepare()  # prepare for what's next
    change.welcome()  # welcome change with open arms
