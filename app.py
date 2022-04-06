input = input(">")

while input != "quit":
    if input == "help":
        print('start - start the car')
        print('stop - stop the car')
        print('quit - stop the game')
    elif input == "start":
        print('Car started...Ready to go!')
    elif input == "stop":
        print('Car stopped')
    elif input == "quit":
        print('game over')
        break
    else:
        print("I don't understand that..")
