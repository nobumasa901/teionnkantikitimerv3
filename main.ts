function LED消灯 (数値: number, 数値2: number) {
    x = 数値
    for (let y = 0; y <= 4; y++) {
        basic.pause(数値2)
        led.unplot(x, y)
    }
}
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    x = 4
    for (let index = 0; index < 5; index++) {
        LED消灯(x, time)
        x += -1
    }
    basic.showIcon(IconNames.Square)
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    カウンター時間 = 0
    for (let index = 0; index < 25; index++) {
        if (input.buttonIsPressed(Button.B)) {
            time = カウンター時間 * 400
            break;
        } else {
            led.plot(Math.abs(カウンター時間 / 5), カウンター時間 % 5)
            カウンター時間 += 1
            basic.pause(1000)
        }
    }
})
let カウンター時間 = 0
let time = 0
let x = 0
basic.showIcon(IconNames.Yes)
basic.pause(200)
