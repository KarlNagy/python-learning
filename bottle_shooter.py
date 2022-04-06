secret_word = "pow"
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('Take your shot pardner! ')
    guess_count += 1
    if guess == secret_word:
        print("Nice shootin'")
        break
    elif guess_count != guess_limit:
        print('you missed that one, try another!')
print("That's all, hoss!")
