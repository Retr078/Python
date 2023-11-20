command = ""
started = False
while command != "quit":
    command = input("Type a command: ").lower()
    if command == "help":
        print("start - start the car\nstop - stop the car\nquit - to exit the game")
    elif command == "start":
        if started:
            print("car has already started")
        else:  
            started = True  
            print("Car has started")
        
    elif command == "stop":
        if not started:
            print("car has already started")
        else:
            started = False
            print("Car has stoped")
        
    elif command == "quit":
        print("You have left the game")
        break
    
    else:
        print("we do not know this command, try another one")

# -------------------------------------------------------------------

temp = "5 degrees"
cel = 0
fahr = float(temp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

    
        
        
        
        

