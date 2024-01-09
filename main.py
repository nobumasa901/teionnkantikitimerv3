def LED消灯(数値: number, 数値2: number):
    global x
    x = 数値
    for y in range(5):
        basic.pause(数値2)
        led.unplot(x, y)

def on_pin_pressed_p0():
    global x
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    x = 4
    for index in range(5):
        LED消灯(x, time)
        x += -1
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global x
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    x = 4
    for index2 in range(5):
        LED消灯(x, time)
        x += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global カウンター時間, time
    basic.clear_screen()
    カウンター時間 = 0
    for index3 in range(25):
        if input.button_is_pressed(Button.B):
            time = カウンター時間 * 400
            break
        else:
            led.plot(abs(カウンター時間 / 5), カウンター時間 % 5)
            カウンター時間 += 1
            basic.pause(1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

カウンター時間 = 0
time = 0
x = 0
basic.show_icon(IconNames.YES)
basic.pause(200)