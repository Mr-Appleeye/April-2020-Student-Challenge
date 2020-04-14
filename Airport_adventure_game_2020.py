### 10.04.2020
### Aadit Sheth
### Adventure game submission for the April 2020 Student Challenge

import time
print("\n" * 3)
print("-------------------- Adventure Game --------------------")
print("\n")
time.sleep(2)
print("Welcome to Enceladus Airport named after one of the moons of Saturn! \nWe are delighted to see you today.")
time.sleep(5)
print("May I have the name your booking is under?")
user_name = input("> ").title()
time.sleep(1)
print("\n")
print("Nice to meet you, " + user_name + "." + "\nYou may proceed to the gateway where our staff will welcome you.")
time.sleep(3)
print("\n")
print("Narrator:")
time.sleep(3)
print("As " + user_name + " walks through the passage, he whispers to himself 'This looks more like a spaceship than a flight'")
time.sleep(5)
print(user_name + " has no idea what has yet to come...")
time.sleep(2)
print("..." "\n")
time.sleep(1)
print("..." "\n")
time.sleep(1)
print("..." "\n")
time.sleep(2)
print("During the long walk to the 'aircraft', " + user_name + "'s hands start to tremble. Stomach begins doing funny things. \nAnd ALL this uncertainty is explained when he sees the large TV screen that said")
time.sleep(8)
print("\n'WELCOME TO THE TIME MACHINE'")
time.sleep(4)

def start():
    print("----------- \nThe TV reads:")
    print("Which time period would you like to travel to? (type 'help' for assistance or 'quit' to exit the game.)")
    time.sleep(2)
    print("\n")
    print("1. The past")
    print("2. The future")

    cmdlist=["1", "2"]
    cmd=getcmd(cmdlist)
    if cmd == "1":
        past()
    elif cmd == "2":
        future()

# past option - 1 further option or quit
def past():
    print("\n" * 100)
    print("Weclome to 1920")
    time.sleep(3)
    print("Forward, you see a old hut")
    print("Back, you see a gateway back to the present")
    time.sleep(3)
    print("What direction do you travel in? (type 'help' for assistance or 'quit' to exit the game.)")
    time.sleep(2)
    print("\n")
    print("1. Forward")
    print("2. Back")
    cmdlist=["1", "2"]
    cmd=getcmd(cmdlist)
    if cmd == "1":
        past_forward()
    elif cmd == "2":
        back()

# future option - 1 further option or quit
def future():
    print("\n" * 100)
    print("Wecome to 2120")
    time.sleep(3)
    print("Forward, you see a flying car")
    print("Back, you see a gateway back to the present")
    time.sleep(3)
    print("What direction do you travel in? (type 'help' for assistance or 'quit' to exit the game.)")
    time.sleep(3)
    print("\n")
    print("1. Forward")
    print("2. Back")
    cmdlist=["1", "2"]
    cmd=getcmd(cmdlist)
    if cmd == "1":
        future_forward()
    elif cmd == "2":
        back()

def getcmd(cmdlist):
    cmd = input(user_name + ">")
    if cmd in cmdlist:
        return cmd
    elif cmd == "help":
        print("\nEnter your choice...")
        print("or enter 'quit' to leave the game")
        return getcmd(cmdlist)
    elif cmd == "quit":
        back()
    else:
        print("We did not understand your request, try again.")
        print("\nEnter your choice...")
        print("or enter 'quit' to leave the game")
        return getcmd(cmdlist)

def back():
    print("\n ----------")
    time.sleep(1)
    print("Thank you for flying with us. We hope to see you on board again...")
    time.sleep(5)
    exit()
    time.sleep(2)

def past_forward():
    print("The old hut catches on fire")
    print(user_name + " dies.")
    back()

def future_forward():
    print("You are greeted by a robot whom you must follow...")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("The robot crashes the flying car.")
    time.sleep(3)
    print(user_name + " dies.")
    back()

if __name__ == "__main__":
    start()
