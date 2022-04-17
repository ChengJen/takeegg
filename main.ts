input.onButtonPressed(Button.A, function () {
    籃子.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    game.setScore(0)
    game.resume()
    Go = true
    速度 = 500
})
input.onButtonPressed(Button.B, function () {
    籃子.change(LedSpriteProperty.X, 1)
})
let 雞蛋: game.LedSprite = null
let 速度 = 0
let Go = false
let 籃子: game.LedSprite = null
籃子 = game.createSprite(2, 4)
Go = false
basic.forever(function () {
    if (Go) {
        雞蛋 = game.createSprite(randint(0, 4), 0)
        雞蛋.set(LedSpriteProperty.Brightness, 30)
        for (let index = 0; index <= 5; index++) {
            if (雞蛋.isDeleted()) {
                break;
            }
            if (index == 5) {
                雞蛋.delete()
                Go = false
                game.pause()
                basic.showNumber(game.score())
            }
            雞蛋.set(LedSpriteProperty.Y, index)
            basic.pause(速度)
        }
        雞蛋.delete()
        速度 += -20
    }
})
basic.forever(function () {
    if (Go) {
        if (籃子.isTouching(雞蛋)) {
            game.addScore(1)
            雞蛋.delete()
        }
    }
})
