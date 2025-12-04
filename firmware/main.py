# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Delay, Macros
from kmk.modules.encoder import EncoderHandler 
from kmk.extensions.RGB import RGB
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
encoderHandler = EncoderHandler()
rgb = RGB(pixel_pin = board.D2, num_pixels = 1)
keyboard.extensions.append(rgb, MediaKeys())
keyboard.modules.append(macros, encoderHandler)

rgb.animation_mode("rainbow")

# Define your pins here!
keyboard.col_pins = (board.D28, board.D29, board.D6)
keyboard.row_pins = (board.D7, board.D0, board.D1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoderHandler.pins = ((board.D26, board.D27, board.D4, board.D3))

#Macros
MACRO_1 = KC.MACRO(
Tap(KC.LCTL(KC.C))
)
MACRO_2 = KC.MACRO(
Tap(KC.LCTL(KC.V))
)
MACRO_3 = KC.MACRO(
Tap(KC.LCTL(KC.SHIFT(KC.ESCAPE)))
)


# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
     [[MACRO_1, MACRO_2, MACRO_3],
     [KC.SPACE, KC.UP,KC.ENTER], 
     [KC.DOWN, KC.LEFT,KC.RIGHT]],
]

encoderHandler.map = [[[KC.VOLU, KC.VOLD, KC.MUTE]]]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()