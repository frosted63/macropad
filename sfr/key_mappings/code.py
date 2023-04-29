# Write your code here :-)
"""
KEY BINDINGS FOR ADAFRUIT RP2040 MACRO PAD
0 = SPOTIFY (CTRL + ALT + S)
1 = UP ARROW
2 = DISCORD (CTRL + ALT + D)
3 = LEFT ARROW
4 = DOWN ARROW
5 = RIGHT ARROW
6 = PREVIOUS TRACK
7 = PAUSE/PLAY
8 = NEXT TRACK
9 = COPY
10 = PASTE
11 = UNDO
ENCODER = VOLUME/MUTE
"""
from adafruit_macropad import MacroPad
from adafruit_hid.consumer_control_code import ConsumerControlCode
from rainbowio import colorwheel
import os

macropad = MacroPad()

tone = 250
last_position = 0

""""macropad.display_image("mateo.bmp") """

while True:
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            macropad.pixels[key_event.key_number] = colorwheel(200)


        else:
            macropad.pixels.fill((0, 0, 0))


    if key_event:
        if key_event.pressed:
            if key_event.key_number == 0: #ESC
                #os.system('"C:/Users/Nico/Desktop/Spotify/Spotify.exe"')
                macropad.keyboard.press(macropad.Keycode.ESCAPE)
                macropad.keyboard.release_all()
            if key_event.key_number == 1: #PAUSE PLAY TRACK
               macropad.consumer_control.send(
                macropad.ConsumerControlCode.PLAY_PAUSE
                )
            #if key_event.key_number == 1: #UP ARROW
            #    macropad.keyboard.press(macropad.Keycode.UP_ARROW)
            #    macropad.keyboard.release_all()
                #macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.ALT, macropad.Keycode.D)
                #macropad.keyboard.release_all()
            if key_event.key_number == 2: #DEL
                macropad.keyboard.press(macropad.Keycode.DELETE)
                macropad.keyboard.release_all()
            if key_event.key_number == 3: #LEFT ARROW
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.C)
                macropad.keyboard.release_all()
            if key_event.key_number == 4: #UNDO
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.Z)
                macropad.keyboard.release_all()
            #if key_event.key_number == 4: #DOWN ARROW
            #    macropad.keyboard.press(macropad.Keycode.DOWN_ARROW)
            #    macropad.keyboard.release_all()
            if key_event.key_number == 5: #PASTE
                macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.V)
                macropad.keyboard.release_all()
            if key_event.key_number == 6: #LEFT ARROW
                macropad.keyboard.press(macropad.Keycode.LEFT_ARROW)
            #if key_event.key_number == 6: #PREVIOUS TRACK
            #    macropad.consumer_control.send(
            #    macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK
            #    )
                macropad.keyboard.release_all()
            if key_event.key_number == 7: #UP ARROW
                macropad.keyboard.press(macropad.Keycode.UP_ARROW)
            #if key_event.key_number == 7: #PAUSE PLAY TRACK
            #   macropad.consumer_control.send(
            #    macropad.ConsumerControlCode.PLAY_PAUSE
            #    )
                macropad.keyboard.release_all()
            if key_event.key_number == 8: #RIGHT ARROW
                macropad.keyboard.press(macropad.Keycode.RIGHT_ARROW)
            #if key_event.key_number == 8: #NEXT TRACK
            #    macropad.consumer_control.send(
            #    macropad.ConsumerControlCode.SCAN_NEXT_TRACK
            #    )
                macropad.keyboard.release_all()
            #if key_event.key_number == 9: #COPY
            #    macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.C)
            #    macropad.keyboard.release_all()
            if key_event.key_number == 9: #PAGE UP
                macropad.keyboard.press(macropad.Keycode.PAGE_UP)
                macropad.keyboard.release_all()
            #if key_event.key_number == 10: #PASTE
            #    macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.V)
            #    macropad.keyboard.release_all()
            if key_event.key_number == 10: #DOWN ARROW
                macropad.keyboard.press(macropad.Keycode.DOWN_ARROW)
                macropad.keyboard.release_all()
            #if key_event.key_number == 11: #UNDO
            #    macropad.keyboard.press(macropad.Keycode.CONTROL, macropad.Keycode.Z)
            #    macropad.keyboard.release_all()
            if key_event.key_number == 11: #PAGE DOWN
                macropad.keyboard.press(macropad.Keycode.PAGE_DOWN)
                macropad.keyboard.release_all()

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed: #MUTE
        macropad.consumer_control.send(
        macropad.ConsumerControlCode.MUTE
                )

    current_position = macropad.encoder

    if macropad.encoder > last_position: #VOLUME UP
        macropad.consumer_control.send(
        macropad.ConsumerControlCode.VOLUME_INCREMENT
                )

    if macropad.encoder < last_position: #VOLUME DOWN
        macropad.consumer_control.send(
        macropad.ConsumerControlCode.VOLUME_DECREMENT
                )

    last_position = current_position
