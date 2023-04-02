import sqlite3
import sys
import os
import random, string
import pynput
from PyQt5.QtCore import Qt, QSettings

def add_run_home_db(save_name, mouse_type, click_type, repeat_or_range, click_repeat, select_or_fixed,
                    location_x, location_y, wait_interval_min, wait_interval_max, wait_type, area_width, area_height,
                    saved_date):
    conn = sqlite3.connect('autoclicker.db')
    cursor = conn.cursor()
    sql = f'''INSERT INTO home_run_settings
        (save_name, mouse_type, click_type, repeat_or_range, click_repeat, select_or_fixed, location_x,
        location_y, wait_interval_min, wait_interval_max, wait_type, area_width, area_height, saved_date)
        VALUES (
        '{save_name}', '{mouse_type}', '{click_type}', '{repeat_or_range}', '{click_repeat}', '{select_or_fixed}',
        '{location_x}', '{location_y}', '{wait_interval_min}', '{wait_interval_max}', '{wait_type}',
        '{area_width}', '{area_height}', '{saved_date}'
        )'''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def add_run_record_db(save_name, csv_text, saved_date, repeat_all, delay_time, delay_type):
    conn = sqlite3.connect('autoclicker.db')
    cursor = conn.cursor()
    sql = f'''INSERT INTO record_run_settings
        (save_name, csv_text, saved_date, repeat_all, delay_time, delay_type)
        VALUES (
        '{save_name}', '{csv_text}', '{saved_date}', '{repeat_all}', '{delay_time}', '{delay_type}'
        )'''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def key_converter(key):
    if key == 'alt':
        return pynput.keyboard.Key.alt
    elif key == 'alt_gr':
        return pynput.keyboard.Key.alt_gr
    elif key == 'alt_l':
        return pynput.keyboard.Key.alt_l
    elif key == 'alt_r':
        return pynput.keyboard.Key.alt_r
    elif key == 'backspace':
        return pynput.keyboard.Key.backspace
    elif key == 'caps_lock':
        return pynput.keyboard.Key.caps_lock
    elif key == 'cmd':
        return pynput.keyboard.Key.cmd
    elif key == 'cmd_l':
        return pynput.keyboard.Key.cmd_l
    elif key == 'cmd_r':
        return pynput.keyboard.Key.cmd_r
    elif key == 'ctrl':
        return pynput.keyboard.Key.ctrl
    elif key == 'ctrl_l':
        return pynput.keyboard.Key.ctrl_l
    elif key == 'ctrl_r':
        return pynput.keyboard.Key.ctrl_r
    elif key == 'delete':
        return pynput.keyboard.Key.delete
    elif key == 'down':
        return pynput.keyboard.Key.down
    elif key == 'end':
        return pynput.keyboard.Key.end
    elif key == 'enter':
        return pynput.keyboard.Key.enter
    elif key == 'esc':
        return pynput.keyboard.Key.esc
    elif key == 'f1':
        return pynput.keyboard.Key.f1
    elif key == 'f2':
        return pynput.keyboard.Key.f2
    elif key == 'f3':
        return pynput.keyboard.Key.f3
    elif key == 'f4':
        return pynput.keyboard.Key.f4
    elif key == 'f5':
        return pynput.keyboard.Key.f5
    elif key == 'f6':
        return pynput.keyboard.Key.f6
    elif key == 'f7':
        return pynput.keyboard.Key.f7
    elif key == 'f8':
        return pynput.keyboard.Key.f8
    elif key == 'f9':
        return pynput.keyboard.Key.f9
    elif key == 'f10':
        return pynput.keyboard.Key.f10
    elif key == 'f11':
        return pynput.keyboard.Key.f11
    elif key == 'f12':
        return pynput.keyboard.Key.f12
    elif key == 'f13':
        return pynput.keyboard.Key.f13
    elif key == 'f14':
        return pynput.keyboard.Key.f14
    elif key == 'f15':
        return pynput.keyboard.Key.f15
    elif key == 'f16':
        return pynput.keyboard.Key.f16
    elif key == 'f17':
        return pynput.keyboard.Key.f17
    elif key == 'f18':
        return pynput.keyboard.Key.f18
    elif key == 'f19':
        return pynput.keyboard.Key.f19
    elif key == 'f20':
        return pynput.keyboard.Key.f20
    elif key == 'home':
        return pynput.keyboard.Key.home
    elif key == 'insert':
        return pynput.keyboard.Key.insert
    elif key == 'left':
        return pynput.keyboard.Key.left
    elif key == 'media_next':
        return pynput.keyboard.Key.media_next
    elif key == 'media_play_pause':
        return pynput.keyboard.Key.media_play_pause
    elif key == 'media_previous':
        return pynput.keyboard.Key.media_previous
    elif key == 'media_volume_down':
        return pynput.keyboard.Key.media_volume_down
    elif key == 'media_volume_mute':
        return pynput.keyboard.Key.media_volume_mute
    elif key == 'media_volume_up':
        return pynput.keyboard.Key.media_volume_up
    elif key == 'menu':
        return pynput.keyboard.Key.menu
    elif key == 'num_lock':
        return pynput.keyboard.Key.num_lock
    elif key == 'page_down':
        return pynput.keyboard.Key.page_down
    elif key == 'page_up':
        return pynput.keyboard.Key.page_up
    elif key == 'pause':
        return pynput.keyboard.Key.pause
    elif key == 'print_screen':
        return pynput.keyboard.Key.print_screen
    elif key == 'right':
        return pynput.keyboard.Key.right
    elif key == 'scroll_lock':
        return pynput.keyboard.Key.scroll_lock
    elif key == 'shift':
        return pynput.keyboard.Key.shift
    elif key == 'shift_l':
        return pynput.keyboard.Key.shift_l
    elif key == 'shift_r':
        return pynput.keyboard.Key.shift_r
    elif key == 'space':
        return pynput.keyboard.Key.space
    elif key == 'tab':
        return pynput.keyboard.Key.tab
    elif key == 'up':
        return pynput.keyboard.Key.up
    else:
        return 'wrong'


def char_converter(key):
    if key == "\\x00":
        return "@"
    elif key == "\\x01":
        return "a"
    elif key == "\\x02":
        return "b"
    elif key == "\\x03":
        return "c"
    elif key == "\\x04":
        return "d"
    elif key == "\\x05":
        return "e"
    elif key == "\\x06":
        return "f"
    elif key == "\\x07":
        return "g"
    elif key == "\\x08":
        return "h"
    elif key == "\\x09":
        return "i"
    elif key == "\\x0a":
        return "j"
    elif key == "\\x0b":
        return "k"
    elif key == "\\x0c":
        return "l"
    elif key == "\\x0d":
        return "m"
    elif key == "\\x0e":
        return "n"
    elif key == "\\x0f":
        return "o"
    elif key == "\\x10":
        return "p"
    elif key == "\\x11":
        return "q"
    elif key == "\\x12":
        return "r"
    elif key == "\\x13":
        return "s"
    elif key == "\\x14":
        return "t"
    elif key == "\\x15":
        return "u"
    elif key == "\\x16":
        return "v"
    elif key == "\\x17":
        return "w"
    elif key == "\\x18":
        return "x"
    elif key == "\\x19":
        return "y"
    elif key == "\\x1a":
        return "z"
    elif key == "\\x1b":
        return "["
    elif key == "\\x1c":
        return "\\"
    elif key == "\\x1d":
        return "]"
    elif key == "\\x1e":
        return "^"
    elif key == "\\x1f":
        return "_"
    elif str(key)[1] == "\\":
        return "\\"
    else:
        return key


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))
