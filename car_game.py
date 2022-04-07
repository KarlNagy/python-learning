command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print('start - start the car')
        print('stop - stop the car')
        print('quit - stop the game')
    elif command == "start":
        if not started:
            print('Car started...Ready to go!')
            started = True
        else:
            print('the car is already moving')
    elif command == "stop":
        if started:
            print('Car stopped')
            started = False
        else:
            print('The Car already stopped')
    elif command == "quit":
        print('game over')
        break
    else:
        print("I don't understand that..")
