games = ['mario kart', 'candy crush', 'flappy bird']
for game in games:
    print("I like playing: " + game)
userGame = ''
while userGame != 'quit':
    userGame = input('What game is your favorite: ')
    if userGame != 'quit':
        games.append(userGame)

for game in games:
    print("The games we like play are: " + game)
