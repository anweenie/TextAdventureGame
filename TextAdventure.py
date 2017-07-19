start = '''
You are on your morning A train, when all of a sudden, the conductor announces that there is a sick passenger on board.
The train is not moving because it is waiting for the ambulance.
You can either stay on the A train and chance being late for work, or leave the train station and use another mode of transportation.
'''

print(start)

print("Type 'stay' to stay. Type 'leave'to pick a new mode of transportation.")
user_input = input()
if user_input == "stay":
    print("You decide to stay and the train does not move for 30 minutes.") # finished the story by writing what happens

elif user_input == "leave":
    print("You decide to leave. Pick what mode of transportation you would like to take next: C train, uber, bus, bike, or walking") # finished the story writing what happens
    input_ = input()
    if input_ == "C train":
        print("There is a fire at your stop, which causes the train to go express. You miss your stop.")
        print("Pick another mode of transportation: uber, bus, bike, or walking.")
        imp == input()
        if imp == "uber":
            print("There is gridlock because the president is in town. You are an hour late.")
        if imp == "bus":
            print("It takes you 30 minutes to get to your destination.")
        if imp == "bike":
            print("It takes you 25 minutes to get to your destination.")
        if imp == "walking":
            print("Type 'walk with them' to join the protest. Type 'walk around them' to avoid the protest.")
            isp == input()
            if isp == "walk with them":
                print("The barricades go past your job, you must walk around. It takes you 45 minutes to get to work.")
            if isp == "walk around them":
                print("You must walk over three avenues to avoid the protestors. You are late by one hour.")
    if input_ == "uber":
        print("There is gridlock because the president is in town. You are an hour late.")
    if input_ =="bus": 
        print("There is gridlock because the president is in town. The bus never comes. You must choose a different mode of transportation.")

    if input_ == "bike":
        print("There are no citi bikes available. You must choose a different mode of transportation.")

    if input_ == "walking":
        print("There are protestors in the streets. They shut down the main avenue.")
        print("You can either 'walk with them' or 'walk around'.")
        print("Type 'walk with them' or 'walk around them'.")
        inp == input()
        if inp == "walk with them":
            print("The barricades go past your job, you must walk around.")
        if inp == "walk around them":
            print("You must walk over three avenues to avoid the protestors. You are late by one hour.")
else:
    print("Incorrect input! Try again.")
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
