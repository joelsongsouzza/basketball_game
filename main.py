import pygame as game

game.init()
gameWindow = game.display.set_mode(size = (800, 800))
gameClock = game.time.Clock()

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()

    gameClock.tick(60)

