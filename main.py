def on_button_pressed_a():
    籃子.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Go, 速度
    basic.clear_screen()
    game.set_score(0)
    game.resume()
    Go = True
    速度 = 500
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    籃子.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

雞蛋: game.LedSprite = None
速度 = 0
Go = False
籃子: game.LedSprite = None
籃子 = game.create_sprite(2, 4)
Go = False

def on_forever():
    global 雞蛋, Go, 速度
    if Go:
        雞蛋 = game.create_sprite(randint(0, 4), 0)
        雞蛋.set(LedSpriteProperty.BRIGHTNESS, 30)
        for index in range(6):
            if 雞蛋.is_deleted():
                break
            if index == 5:
                雞蛋.delete()
                Go = False
                game.pause()
                basic.show_number(game.score())
            雞蛋.set(LedSpriteProperty.Y, index)
            basic.pause(速度)
        雞蛋.delete()
        速度 += -20
basic.forever(on_forever)

def on_forever2():
    if Go:
        if 籃子.is_touching(雞蛋):
            game.add_score(1)
            雞蛋.delete()
basic.forever(on_forever2)
