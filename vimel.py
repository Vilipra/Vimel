# A game of camel
import random

done = False

print ("Welcome to Vimel!")
print ("You have stolen a Vimel to make your way across the desert.")
print ("The natives want their Vimel back and are chasing you down! \n Survive the desert treck and outrun the natives.")

distance_traveled = 0 # distance the player traveled in kilometers (standard: 0)
thirst = 0 # how thirsty the player is from 0 to 100. 100 = game over (standard: 0)
camel_tiredness = 0 # how tired the camel is from 0 to 100. 100 =  camel dies, game over (standard: 0)
natives = -20 # distance the natives have traveled in kilometers (standard: -20)
canteen = 3 # number of times player can drind from canteen (standard: 5)

while not done: # Main loop
    
    print ("A. Drink from your canteen.")
    print ("B. Ahead moderate speed.")
    print ("C. Ahead full speed.")
    print ("D. Stop for the night.")
    print ("E. Status check.")
    print ("Q. Quit.")
    
    choice = str(input("Your choice: "))
    
    #Keyboard checks
    if choice.lower() == "q" : # Q: Quit the game
        done = True 
        print ()
        print ("Thanks for playing!")
        
    elif choice.lower() == "a" : # A: Drink from canteen
        print ()
        if thirst <= 2 and canteen > 0: # When the player isn't really thirsty yet tell them what they did wrong
            print ("Even though you were not really thirsty you took a drink from your canteen.")
            canteen -= 1
            thirst = 0
        elif thirst <= 5 and canteen > 0: # Standard thirst message
            print ("You took a drink from your canteen.")
            canteen -= 1
            thirst = 0  
        elif canteen > 0: # When the player is really thirsty print custom message
            print ("You took a much needed drink from your canteen.")
            canteen -= 1
            thirst = 0            
        else:
            print ("You wanted to take a drink from your canteen, but found it empty. You better find a oasis to refill your canteen at.")
        print ()
        
    elif choice.lower() == "b" : # B: Ahead at moderate speed
        print ()
        
        traveled = random.randrange(5,13)
        distance_traveled += traveled
        thirst += 1
        camel_tiredness += 1
        natives += random.randrange(7,15)
        oasis = random.randrange(20)
        
        print ("You traveled",traveled,"kilometers")
        
        if oasis == 1:
            print ("You found an oasis!")
            print ("You drink, fill up your canteen and your Vimel rests.")
            thirst = 0
            camel_tiredness = 0
            canteen = 3
            print ()
            
        else:
            print ()
    
    elif choice.lower() == "c": # C: Ahead at full speed
        print ()
        
        traveled = random.randrange(10,21)
        distance_traveled += traveled
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives += random.randrange(7,15)
        oasis = random.randrange(20)
        
        print ("You traveled",traveled,"kilometers")
        
        if oasis == 1:
            print ("You found an oasis!")
            print ("You drink, fill up your canteen and your camel rests.")
            thirst = 0
            camel_tiredness = 0
            canteen = 3
            print ()
            
        else:
            print ()        
        
        
    elif choice.lower() == "d": # Stop for the night
        print ()
        
        camel_tiredness = 0
        natives += random.randrange(7,15)
        
        print ("Your camel had a good sleep and is happy.")
        
        print ()
        
    elif choice.lower() == "e": # Status check
        print ()
        
        print ("Kilometers traveled:", distance_traveled)
        print ("Drinks in canteen:", canteen)
        print ("The natives are", distance_traveled-natives, "kilometers behind you.")
        
        print ()
        
    elif len(choice) > 1: # If the input is longer than 1 tell the player what to do
        print ()
        print ("Sorry I don't understand what you want to do. To tell me what to do just type the letter of the action.")
        print ()
        
    elif len(choice) == 1: # if the input is one letter long, but not recognised tell the player what to do
        print ()
        print ("Sorry the key you pressed is not one of the actions availible to you.")
        print ()
        
    elif len(choice) == 0: # If the player didn't enter anything call them stupid (not really)
        print ()
        print ("Sorry you have to enter a letter to do something.")
        print ()
        
    
    # Game condition checks
    # Check for player thirst
    if thirst > 3 and  thirst < 6: # Standard thirst message
        print ("You are thirsty.")    
        print ()
        
    elif thirst == 6: # When the player is about to die warn them
        print ("You have to drink. If you don't you're going to die soon.")
        print ()
        
    elif thirst > 6: # Player dies of thirst
        print ("You died of thirst.")
        print ("GAME OVER")
        done = True
        
    # Check for camel tiredness    
    if camel_tiredness > 5 and camel_tiredness <= 8 and not done: # Standard camel tired message
        print ("Your camel is getting tired.")
        print ()
        
    elif camel_tiredness > 8 and not done: # Camel dies
        print ("Your camel is dead.")
        print ("GAME OVER")
        done = True
        
        
    # Check for natives distance to the player
    if natives == distance_traveled or natives > distance_traveled:
        print ("The natives caught up to you and killed you.")
        print ("GAME OVER")
        done = True
        
    if distance_traveled - natives < 15 and not done:
        print ("The natives are getting close.")
        print ()
        
    # Check for distance traveled if distance > 200 win the game
    if distance_traveled >= 200 and not done:
        print ("You made it across the desert! You won!")
        done = True
