games = ['mario kart', 'candy crush', 'flappy bird']
for game in games:
    print("I like playing: " + game)

userGame = input('What game is your favorite: ')
games.append(userGame)
for game in games:
    print("The games we like play are: " + game)
