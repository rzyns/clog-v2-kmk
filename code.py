print("STARTING")
import board

# from kmk.hid import HIDModes

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.D6,
    board.D5,
    board.D4,
    board.D3,
    board.D2,
)

keyboard.row_pins = (
    board.D10,
    board.D9,
    board.D8,
    board.D7,
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

modtap = ModTap()
modtap.tap_time = 250
keyboard.modules.append(modtap)

split = Split(split_type=SplitType.BLE, split_flip=True)
keyboard.modules.append(split)

layers = Layers()
keyboard.modules.append(layers)

ALPHA = 0
SYM = 1
NUM = 2
NAV = 3
RFN = 4
LFN = 5

keyboard.keymap = [
    [ # ALPHA
              KC.Q,                  KC.W,                   KC.E,                  KC.R,                  KC.T,                               KC.Y,                     KC.U,                   KC.I,                     KC.O,                     KC.P,
              KC.A,                  KC.S,                   KC.D,                  KC.F,                  KC.G,                               KC.H,                     KC.J,                   KC.K,                     KC.L,                     KC.SCOLON,                 
              KC.MT(KC.Z, KC.LCTRL), KC.MT(KC.X, KC.LSHIFT), KC.MT(KC.C, KC.LALT),  KC.MT(KC.V, KC.LCMD),  KC.B,                               KC.N,                     KC.MT(KC.M, KC.LCMD),   KC.MT(KC.COMMA, KC.LALT), KC.MT(KC.DOT, KC.LSHIFT), KC.MT(KC.SLASH, KC.LCTRL),
                                                             KC.NO,                 KC.LT(SYM, KC.SPC),    KC.LT(NUM, KC.ENTER),               KC.LT(SYM, KC.BACKSPACE), KC.LT(NUM, KC.SPACE),   KC.NO,
    ],

    [ # SYM
              KC.ESC,   KC.AT,    KC.HASH,   KC.DOLLAR,          KC.PERC,                          KC.CIRCUMFLEX,        KC.AMPR,                KC.ASTR, KC.UNDS, KC.BSPC,
              KC.TAB,   KC.MINUS, KC.EQUAL,  KC.EXLM,            KC.COLON,                         KC.BSLASH,            KC.GRAVE,               KC.LPRN, KC.RPRN, KC.ENTER,
              KC.COMMA, KC.DOT,   KC.BSLASH, KC.QUOTE,           KC.GRAVE,                         KC.PIPE,              KC.LBRC,                KC.RBRC, KC.LCBR, KC.RCBR,
                                  KC.NO,     KC.LT(NAV, KC.SPC), KC.LT(NAV, KC.SPC),               KC.LT(SYM, KC.SPC),   KC.LT(NAV, KC.SPC),     KC.NO,
    ],

    # NUM
    [
        KC.ESC,   KC.LPRN,  KC.LCBR, KC.LBRC,            KC.NO,                            KC.EQL,              KC.N7,              KC.N8,       KC.N9,    KC.BSPC,
        KC.TAB,   KC.UNDS,  KC.PLUS, KC.RPRN,            KC.COLON,                         KC.MINUS,            KC.N4,              KC.N5,       KC.N6,    KC.ENT,
        KC.LABK,  KC.RABK,  KC.BSLS, KC.DQUO,            KC.TILDE,                         KC.N0,               KC.N1,              KC.N2,       KC.N3,    KC.QUES,
                            KC.NO,   KC.LT(NAV, KC.SPC), KC.LT(NAV, KC.SPC),               KC.LT(NAV, KC.SPC),  KC.LT(NAV, KC.SPC), KC.NO,
    ],

    # NAV
    [
        KC.ESC,            KC.NO  ,  KC.NO  , KC.NO  , KC.BLE_REFRESH,             KC.HOME,    KC.NO,            KC.NO,       KC.NO,    KC.BSPC,
        KC.TAB,            KC.NO  ,  KC.NO  , KC.NO  , KC.NO  ,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.RIGHT, KC.ENTER,
        KC.MO(RFN),        KC.NO  ,  KC.NO  , KC.NO  , KC.NO,                      KC.NO,      KC.PGDN,          KC.PGUP,     KC.END,   KC.MO(LFN),
                                     KC.NO,   KC.NO  , KC.SPC,                     KC.BSPC,    KC.NO  ,          KC.NO,
    ],

    # RFN
    [
        KC.ESC,            KC.NO  ,  KC.NO  , KC.NO  , KC.BLE_REFRESH,             KC.HOME,    KC.NO,            KC.NO,       KC.NO,    KC.BSPC,
        KC.TAB,            KC.NO  ,  KC.NO  , KC.NO  , KC.NO  ,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.RIGHT, KC.ENTER,
        KC.MO(RFN),        KC.NO  ,  KC.NO  , KC.NO  , KC.NO,                      KC.NO,      KC.PGDN,          KC.PGUP,     KC.END,   KC.MO(LFN),
                                     KC.NO,   KC.NO  , KC.SPC,                     KC.BSPC,    KC.NO  ,          KC.NO,
    ],
    # [
    #     KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                             KC.F11,   KC.F7, KC.F8, KC.F9, KC.NO,
    #     KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                             KC.F10,   KC.F4, KC.F5, KC.F6, KC.NO,
    #     KC.NO,  KC.NO,  KC.NO, KC.NO, KC.NO,                             KC.NO,    KC.F1, KC.F2, KC.F3, KC.NO,
    #                     KC.NO, KC.NO, KC.SPC,                            KC.BSPC,  KC.NO, KC.NO,
    # ],

    # LFN
    [
        KC.ESC,            KC.NO  ,  KC.NO  , KC.NO  , KC.BLE_REFRESH,             KC.HOME,    KC.NO,            KC.NO,       KC.NO,    KC.BSPC,
        KC.TAB,            KC.NO  ,  KC.NO  , KC.NO  , KC.NO  ,                    KC.LEFT,    KC.DOWN,          KC.UP,       KC.RIGHT, KC.ENTER,
        KC.MO(RFN),        KC.NO  ,  KC.NO  , KC.NO  , KC.NO,                      KC.NO,      KC.PGDN,          KC.PGUP,     KC.END,   KC.MO(LFN),
                                     KC.NO,   KC.NO  , KC.SPC,                     KC.BSPC,    KC.NO  ,          KC.NO,
    ],
    # [
    #     KC.NO,  KC.F7,  KC.F8, KC.F9, KC.F11,                                      KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
    #     KC.NO,  KC.F4,  KC.F5, KC.F6, KC.F10,                                      KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
    #     KC.NO,  KC.F1,  KC.F2, KC.F3, KC.NO,                                       KC.NO,   KC.NO  , KC.NO  , KC.NO  , KC.NO,
    #                     KC.NO, KC.NO, KC.SPC,                                      KC.BSPC, KC.NO, KC.NO,
    # ],
]

# keyboard.debug_enabled = True

if __name__ == '__main__':
    # keyboard.go(hid_type=HIDModes.BLE, ble_name='CLOGv2-KMK')
    keyboard.go()
