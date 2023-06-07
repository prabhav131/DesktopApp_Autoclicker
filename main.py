import csv
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QFrame, QWidget, QComboBox, QPushButton, QGroupBox,\
    QLineEdit, QRadioButton, QScrollArea, QHBoxLayout, QFormLayout, QFileDialog, QGridLayout, QListWidgetItem,\
    QCheckBox, QDialog, QListWidget, QToolButton
from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt, QSettings
import sys
import os
import threading
from time import sleep
import time
import mouse
import keyboard
import random
from functions_file import functions
import ctypes
from win10toast import ToastNotifier
import pynput
import datetime
import webbrowser

form = functions.resource_path("version2.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(form)


# starts the clicking actions set in home screen
def home_fixed_clicking(mouse_type, click_type, click_repeat, location_x, location_y, wait_interval):
    stop_home_event.clear()
    if wait_interval[0] == wait_interval[1]:
        if wait_interval[0] > 2:
            repeat = int(wait_interval[0] / 2)
            last = float(wait_interval[0] - (repeat * 2))
            delay = 2
        else:
            repeat = 1
            last = 0
            delay = wait_interval[0]
        if click_repeat > 0:
            if click_type == 'Single':
                for i in range(click_repeat):
                    mouse.move(location_x, location_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                for i in range(click_repeat):
                    mouse.move(location_x, location_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
        elif click_repeat == 0:
            pass
        else:
            if click_type == 'Single':
                while True:
                    mouse.move(location_x, location_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                while True:
                    mouse.move(location_x, location_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
    else:
        wait_time = round(random.uniform(wait_interval[0], wait_interval[1]), 1)
        if wait_time > 2:
            repeat = int(wait_time / 2)
            last = float(wait_time - (repeat * 2))
            delay = 2
        else:
            repeat = 1
            last = 0
            delay = wait_time
        if click_repeat > 0:
            if click_type == 'Single':
                for i in range(click_repeat):
                    mouse.move(location_x, location_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                for i in range(click_repeat):
                    mouse.move(location_x, location_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
        elif click_repeat == 0:
            pass
        else:
            if click_type == 'Single':
                while True:
                    mouse.move(location_x, location_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                while True:
                    mouse.move(location_x, location_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
    UIWindow.after_home_thread()


# starts the clicking actions in current location set in home screen
def home_current_clicking(mouse_type, click_type, click_repeat, waiting_interval):
    stop_home_event.clear()
    if waiting_interval[0] == waiting_interval[1]:
        if waiting_interval[0] > 2:
            repeat = int(waiting_interval[0] / 2)
            last = float(waiting_interval[0] - (repeat * 2))
            delay = 2
        else:
            repeat = 1
            last = 0
            delay = waiting_interval[0]
        if click_repeat > 0:
            if click_type == 'Single':
                for i in range(click_repeat):
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                for i in range(click_repeat):
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
        elif click_repeat == 0:
            pass
        else:
            if click_type == 'Single':
                while True:
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                while True:
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
    else:
        wait_time = round(random.uniform(waiting_interval[0], waiting_interval[1]), 1)
        if wait_time > 2:
            repeat = int(wait_time / 2)
            last = float(wait_time - (repeat * 2))
            delay = 2
        else:
            repeat = 1
            last = 0
            delay = wait_time
        if click_repeat > 0:
            if click_type == 'Single':
                for i in range(click_repeat):
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                for i in range(click_repeat):
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
        elif click_repeat == 0:
            pass
        else:
            if click_type == 'Single':
                while True:
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                while True:
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
    UIWindow.after_home_thread()

# starts the dragging actions set in home screen
def home_random_clicking(mouse_type, click_type, click_repeat, location_x, location_y, wait_interval, area_width, area_height):
    stop_home_event.clear()
    end_x = location_x + area_width
    end_y = location_y + area_height
    if wait_interval[0] == wait_interval[1]:
        if wait_interval[0] > 2:
            repeat = int(wait_interval[0] / 2)
            last = float(wait_interval[0] - (repeat * 2))
            delay = 2
        else:
            repeat = 1
            last = 0
            delay = wait_interval[0]
        if click_repeat > 0:
            if click_type == 'Single':
                for i in range(click_repeat):
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                for i in range(click_repeat):
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
        elif click_repeat == 0:
            pass
        else:
            if click_type == 'Single':
                while True:
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                while True:
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
    else:
        wait_time = round(random.uniform(wait_interval[0], wait_interval[1]), 1)
        if wait_time > 2:
            repeat = int(wait_time / 2)
            last = float(wait_time - (repeat * 2))
            delay = 2
        else:
            repeat = 1
            last = 0
            delay = wait_time
        if click_repeat > 0:
            if click_type == 'Single':
                for i in range(click_repeat):
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                for i in range(click_repeat):
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
        elif click_repeat == 0:
            pass
        else:
            if click_type == 'Single':
                while True:
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
            else:
                while True:
                    random_x = random.randint(location_x, end_x)
                    random_y = random.randint(location_y, end_y)
                    mouse.move(random_x, random_y)
                    mouse.double_click(button=mouse_type)
                    for j in range(repeat):
                        sleep(delay)
                        if stop_home_event.is_set():
                            break
                    sleep(last)
                    if stop_home_event.is_set():
                        stop_home_event.clear()
                        break
    UIWindow.after_home_thread()

# simulates clicking action for record screen
def click_for_record(location_x, location_y, mouse_type, action_type, wait_interval):
    delay = wait_interval / 1000
    current = mouse.get_position()
    if action_type == 'Press':
        sleep(delay)
        if not current == (location_x, location_y):
            mouse.move(location_x, location_y, duration=0.01)
        mouse.press(button=mouse_type)
    else:
        sleep(delay)
        if not current == (location_x, location_y):
            mouse.move(location_x, location_y, duration=0.10)
        mouse.release(button=mouse_type)

# simulates scrolling action for record screen
def scroll_for_record(location_x, location_y, scroll_type, click_repeat, waiting_interval):
    delay = int(waiting_interval / click_repeat) / 1000
    current = mouse.get_position()
    if scroll_type == 'Up':
        for i in range(click_repeat):
            sleep(delay)
            if not current == (location_x, location_y):
                mouse.move(location_x, location_y)
            mouse.wheel(1)
            if stop_record_event.is_set():
                return
    else:
        for i in range(click_repeat):
            sleep(delay)
            if not current == (location_x, location_y):
                mouse.move(location_x, location_y)
            mouse.wheel(-1)
            if stop_record_event.is_set():
                return

# simulates keyboard typing for record screen
def type_for_record(key, key_type, action_type, waiting_interval):
    controller = pynput.keyboard.Controller()
    if key_type == 'Key':
        if str(key)[0] == "<":
            try:
                pressed_key = pynput.keyboard.KeyCode(vk=int(str(key)[1:-1]))
            except ValueError:
                stop_record_event.set()
                return
            sleep(waiting_interval / 1000)
            if action_type == 'Press':
                controller.press(pressed_key)
            else:
                controller.release(pressed_key)
        else:
            pressed_key = functions.key_converter(key.replace('Key.', '').replace('_l', '').replace('_r', '').lower())
            if pressed_key == 'wrong':
                stop_record_event.set()
                wrong_key_event.set()
                return
            else:
                sleep(waiting_interval / 1000)
                if action_type == 'Press':
                    controller.press(pressed_key)
                else:
                    controller.release(pressed_key)
    else:
        type_no = len(key)
        delay = int(waiting_interval / type_no) / 1000
        for i in range(type_no):
            sleep(delay)
            if action_type == 'Press':
                controller.press(key[i])
            else:
                controller.release(key[i])
            if stop_record_event.is_set():
                return

# starts recording actions
def start_record_actions(actions_data, repeat_all, delay_time, i):
    last_line = 0
    if delay_time > 2:
        repeat = int(delay_time / 2)
        last = float(delay_time - (repeat * 2))
        delay = 2
    else:
        repeat = 1
        last = 0
        delay = delay_time
    for b in range(int(repeat_all)):
        for a in range(i - 1):
            last_line += 1
            if actions_data[a][0] == 'mouse':
                try:
                    click_for_record(int(actions_data[a][1]), int(actions_data[a][2]), actions_data[a][3].lower(),
                                     actions_data[a][4], int(actions_data[a][5]))
                except:
                    break
            elif actions_data[a][0] == 'keyboard':
                try:
                    type_for_record(actions_data[a][1], actions_data[a][2], actions_data[a][3], int(actions_data[a][4]))
                except:
                    break
            else:
                try:
                    scroll_for_record(int(actions_data[a][1]), int(actions_data[a][2]), actions_data[a][3],
                                      int(actions_data[a][4]), int(actions_data[a][5]))
                except:
                    break
            if stop_record_event.is_set():
                break
        if stop_record_event.is_set():
            stop_record_event.clear()
            break
        for j in range(repeat):
            sleep(delay)
            if stop_record_event.is_set():
                break
        sleep(last)
        if stop_record_event.is_set():
            stop_record_event.clear()
            break
    for c in range(i - 1):
        if actions_data[c][0] == 'keyboard':
            converted_key = actions_data[c][1].replace('Key.', '').replace('_l', '').replace('_r', '').lower()
            if keyboard.is_pressed(converted_key):
                type_for_record(converted_key, actions_data[c][2], 'Release', 0)
    UIWindow.after_record_thread(last_line)


class UI(QMainWindow):
    # defines all variables and UI elements for the app
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("version2.ui", self)
        self.settings = QSettings("GG", "autoclicker")

        self.MainWindow = self.findChild(QMainWindow, "MainWindow")
        self.setWindowIcon(QtGui.QIcon("images/app_logo.png"))
        self.setFixedWidth(662)
        self.setFixedHeight(533)
        self.central_widget = self.findChild(QWidget, "central_widget")
        self.central_widget_2 = self.findChild(QFrame, "central_widget_2")
        self.integer = QIntValidator()
        self.main_frame = self.findChild(QFrame, "main_frame")
        self.home_frame = self.findChild(QFrame, "home_frame")

        self.snipping_push_button = self.findChild(QPushButton, "snipping_push_button")
        self.snipping_push_button.clicked.connect(self.screenCapture)

        # Dim Splashscreen object, also responsible for tracking mouse and capturing screenshot.
        self.tmpDimScreen = CaptureScreen()
        self.snipping_radio_button = self.findChild(QRadioButton, "snipping_radio_button")
        self.fixed_location_radio_button = self.findChild(QRadioButton, "fixed_location_radio_button")
        self.current_location_radio_button = self.findChild(QRadioButton, "current_location_radio_button")
        self.fixed_location_x = self.findChild(QLineEdit, "fixed_location_x")
        self.fixed_location_y = self.findChild(QLineEdit, "fixed_location_y")
        self.height_label = self.findChild(QLabel, "height_label")
        self.select_area_height = self.findChild(QLineEdit, "select_area_height")
        self.select_area_radio_button = self.findChild(QRadioButton, "select_area_radio_button")
        self.select_area_width = self.findChild(QLineEdit, "select_area_width")
        self.select_area_x = self.findChild(QLineEdit, "select_area_x")
        self.select_area_y = self.findChild(QLineEdit, "select_area_y")
        self.short_cut_label = self.findChild(QLabel, "short_cut_label")
        self.width_label = self.findChild(QLabel, "width_label")
        self.x_left_label = self.findChild(QLabel, "x_left_label")
        self.x_right_label = self.findChild(QLabel, "x_right_label")
        self.y_left_label = self.findChild(QLabel, "y_left_label")
        self.y_right_label = self.findChild(QLabel, "y_right_label")

        self.click_options_groupbox = self.findChild(QGroupBox, "click_options_groupbox")
        self.click_type_combobox = self.findChild(QComboBox, "click_type_combobox")
        self.click_type_combobox.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                               'border: 1px solid;'
                                               'border-radius: 3px;'
                                               'border-color: rgb(218, 218, 218);}'
                                               'QComboBox QAbstractItemView {'
                                               'background-color: rgb(249, 249, 245);'
                                               'border: none;'
                                               'color: black;}'
                                               'QComboBox::drop-down {'
                                               'border: 1px;'
                                               'border-radius: 2px;'
                                               'border-color: rgb(249, 249, 245);}'
                                               'QComboBox::down-arrow {'
                                               'image: url(images/arrow1.png);'
                                               'width: 8px;'
                                               'height: 8px;}')
        self.click_type_label = self.findChild(QLabel, "click_type_label")
        self.mouse_button_combobox = self.findChild(QComboBox, "mouse_button_combobox")
        self.mouse_button_combobox.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                                 'border: 1px solid;'
                                                 'border-radius: 3px;'
                                                 'border-color: rgb(218, 218, 218);}'
                                                 'QComboBox QAbstractItemView {'
                                                   'background-color: rgb(249, 249, 245);'
                                                   'border: none;'
                                                 'color: black;}'
                                                 'QComboBox::drop-down {'
                                                 'border: 1px;'
                                                 'border-radius: 2px;'
                                                 'border-color: rgb(218, 218, 218);}'
                                                 'QComboBox::down-arrow {'
                                                 'image: url(images/arrow1.png);'
                                                 'width: 8px;'
                                                 'height: 8px;}')
        self.mouse_button_label = self.findChild(QLabel, "mouse_button_label")
        self.click_repeat_groupbox = self.findChild(QGroupBox, "click_repeat_groupbox")
        self.never_stop_combobox = self.findChild(QComboBox, "never_stop_combobox")
        self.never_stop_combobox.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                               'border: 1px solid;'
                                               'border-radius: 3px;'
                                               'border-color: rgb(218, 218, 218);}'
                                               'QComboBox QAbstractItemView {'
                                             'background-color: rgb(249, 249, 245);'
                                             'border: none;'
                                               'color: black;}'
                                               'QComboBox::drop-down {'
                                               'border: 1px;'
                                               'border-radius: 2px;'
                                               'border-color: rgb(218, 218, 218);}'
                                               'QComboBox::down-arrow {'
                                               'image: url(images/arrow1.png);'
                                               'width: 8px;'
                                               'height: 8px;}')
        self.never_stop_label = self.findChild(QLabel, "never_stop_label")
        self.repeat_for_label = self.findChild(QLabel, "repeat_for_label")
        self.repeat_for_number = self.findChild(QLineEdit, "repeat_for_number")
        self.delay_groupbox = self.findChild(QGroupBox, "delay_groupbox")
        self.delay_time_combobox = self.findChild(QComboBox, "delay_time_combobox")
        self.delay_time_combobox.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                               'border: 1px solid;'
                                               'border-radius: 3px;'
                                               'border-color: rgb(218, 218, 218);}'
                                               'QComboBox QAbstractItemView {'
                                             'background-color: rgb(249, 249, 245);'
                                             'border: none;'
                                               'color: black;}'
                                               'QComboBox::drop-down {'
                                               'border: 1px;'
                                               'border-radius: 2px;'
                                               'border-color: rgb(218, 218, 218);}'
                                               'QComboBox::down-arrow {'
                                               'image: url(images/arrow1.png);'
                                               'width: 8px;'
                                               'height: 8px;}')
        self.delay_time_combobox_2 = self.findChild(QComboBox, "delay_time_combobox_2")
        self.delay_time_combobox_2.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                                 'border: 1px solid;'
                                                 'border-radius: 3px;'
                                                 'border-color: rgb(218, 218, 218);}'
                                                 'QComboBox QAbstractItemView {'
                                             'background-color: rgb(249, 249, 245);'
                                             'border: none;'
                                                 'color: black;}'
                                                 'QComboBox::drop-down {'
                                                 'border: 1px;'
                                                 'border-radius: 2px;'
                                                 'border-color: rgb(218, 218, 218);}'
                                                 'QComboBox::down-arrow {'
                                                 'image: url(images/arrow1.png);'
                                                 'width: 8px;'
                                                 'height: 8px;}')
        self.delay_time_entrybox = self.findChild(QLineEdit, "delay_time_entrybox")
        self.line_label = self.findChild(QLabel, "line_label")
        self.range_max = self.findChild(QLineEdit, "range_max")
        self.range_min = self.findChild(QLineEdit, "range_min")
        self.range_radio_button = self.findChild(QRadioButton, "range_radio_button")
        self.repeat_radio_button = self.findChild(QRadioButton, "repeat_radio_button")
        self.play_button = self.findChild(QPushButton, "play_button")
        self.reset_settings_button = self.findChild(QPushButton, "reset_settings_button")
        self.save_settings_button = self.findChild(QPushButton, "save_settings_button")
        self.hotkey_settings_frame = self.findChild(QFrame, "hotkey_settings_frame")
        self.left_frame = self.findChild(QFrame, "left_frame")
        self.home_button = self.findChild(QToolButton, "home_button")
        self.home_button.setIcon(QtGui.QIcon("images/home"))
        self.record_button = self.findChild(QToolButton, "record_button")
        self.record_button.setIcon(QtGui.QIcon("images/Record"))
        self.theme_button = self.findChild(QToolButton, "theme_button")
        self.theme_button.setIcon(QtGui.QIcon("images/Mode"))
        self.view_settings_button = self.findChild(QToolButton, "view_settings_button")
        self.view_settings_button.setIcon(QtGui.QIcon("images/Settings"))
        self.navigation_frame = self.findChild(QFrame, "navigation_frame")
        self.record_frame = self.findChild(QFrame, "record_frame")
        self.view_settings_frame = self.findChild(QFrame, "view_settings_frame")
        self.hotkey_settings_button = self.findChild(QToolButton, "hotkey_settings_button")
        self.hotkey_settings_button.setIcon(QtGui.QIcon("images/HotkeyBlack"))
        self.hotkey_settings_frame = self.findChild(QFrame, "hotkey_settings_frame")
        self.top_frame = self.findChild(QFrame, "top_frame")
        self.top_frame_logged_out = self.findChild(QFrame, "top_frame_logged_out")
        self.app_icon = self.findChild(QLabel, "app_icon")
        self.complete_combobox = self.findChild(QComboBox, "complete_combobox")
        self.complete_combobox.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                             'border: 2px solid;'
                                             'border-radius: 7px;'
                                             'border-color: rgb(217, 217, 217);}'
                                             'QComboBox QAbstractItemView {'
                                             'background-color: rgb(249, 249, 245);'
                                             'border: none;'
                                             'color: black;}'
                                             'QComboBox::drop-down {'
                                             'border: 2px;'
                                             'border-radius: 5px;'
                                             'border-color: rgb(249, 249, 245);}'
                                             'QComboBox::down-arrow {'
                                             'image: url(images/arrow1);'
                                             'width: 8px;'
                                             'height: 8px;}')
        self.complete_combobox_3 = self.findChild(QComboBox, "complete_combobox_3")
        self.complete_combobox_3.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                             'border: 2px solid;'
                                             'border-radius: 7px;'
                                             'border-color: rgb(217, 217, 217);}'
                                             'QComboBox QAbstractItemView {'
                                             'background-color: rgb(249, 249, 245);'
                                             'border: none;'
                                             'color: black;}'
                                             'QComboBox::drop-down {'
                                             'border: 2px;'
                                             'border-radius: 5px;'
                                             'border-color: rgb(249, 249, 245);}'
                                             'QComboBox::down-arrow {'
                                             'image: url(images/arrow1);'
                                             'width: 8px;'
                                             'height: 8px;}')
        self.GG_icon = self.findChild(QPushButton, "GG_icon")
        self.GG_icon.setIcon(QtGui.QIcon('images/GGicon'))
        self.navigate_button = self.findChild(QPushButton, "navigate_button")
        self.navigate_button.setIcon(QtGui.QIcon("images/Hambuger"))
        self.navigate_button_3 = self.findChild(QPushButton, "navigate_button_3")
        self.navigate_button_3.setIcon(QtGui.QIcon("images/Hambuger"))
        self.profile_button = self.findChild(QPushButton, "profile_button")
        self.profile_button.setIcon(QtGui.QIcon("images/liliajohn"))
        self.profile_button_3 = self.findChild(QPushButton, "profile_button_3")
        self.profile_button_3.setIcon(QtGui.QIcon("images/liliajohn"))
        self.record_add_button = self.findChild(QPushButton, "record_add_button")
        self.record_add_button.setIcon(QtGui.QIcon("images/icons8-ui-64"))
        self.record_add_items = self.findChild(QComboBox, "record_add_items")
        self.record_load_button = self.findChild(QPushButton, "record_load_button")
        self.record_load_button.setIcon(QtGui.QIcon("images/icons8-upload-96"))
        self.record_play_button = self.findChild(QPushButton, "record_play_button")
        self.record_play_button.setIcon(QtGui.QIcon("images/Run"))
        self.record_record_button = self.findChild(QPushButton, "record_record_button")
        self.record_record_button.setIcon(QtGui.QIcon("images/red-circle"))
        self.repeat_for_label_2 = self.findChild(QLabel, "repeat_for_label_2")
        self.repeat_for_number_2 = self.findChild(QLineEdit, "repeat_for_number_2")
        self.repeat_for_number_2.setValidator(self.integer)
        self.repeat_for_label_2.hide()
        self.repeat_for_number_2.hide()
        self.repeat_for_number_2.setText("1")
        self.delay_label_2 = self.findChild(QLabel, "delay_label_2")
        self.delay_2 = self.findChild(QLineEdit, "delay_2")
        self.delay_time_combobox_record = self.findChild(QComboBox, "delay_time_combobox_record")
        self.delay_label_2.hide()
        self.delay_2.hide()
        self.delay_time_combobox_record.hide()
        self.delay_2.setText("100")
        self.delay_time_combobox_record.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                                      'border: 1px solid;'
                                                      'border-radius: 3px;'
                                                      'border-color: rgb(249, 249, 245);}'
                                                      'QComboBox QAbstractItemView {'
                                                     'background-color: rgb(249, 249, 245);'
                                                     'border: none;'
                                                      'color: black;}'
                                                      'QComboBox::drop-down {'
                                                      'border: 1px;'
                                                      'border-radius: 2px;'
                                                      'border-color: rgb(249, 249, 245);'
                                                      'background-color: rgb(249, 249, 245);}'
                                                      'QComboBox::down-arrow {'
                                                      'background-color: rgb(249, 249, 245);'
                                                      'image: url(images/arrow1.png);'
                                                      'width: 8px;'
                                                      'height: 8px;}')
        self.delay_time_combobox_record.addItem("ms")
        self.delay_time_combobox_record.addItem("s")
        self.delay_time_combobox_record.addItem("min")
        self.delay_time_combobox_record.addItem("hr")
        self.record_remove_all_button = self.findChild(QPushButton, "record_remove_all_button")
        self.record_save_button = self.findChild(QPushButton, "record_save_button")
        self.record_scroll_area = self.findChild(QScrollArea, "record_scroll_area")
        self.scroll_bar = self.record_scroll_area.findChildren(QWidget)[5]
        self.scrollAreaWidgetContents = self.findChild(QWidget, "scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setFixedWidth(518)
        self.scrollAreaWidgetContents.setStyleSheet("border: none;")
        self.form_layout = QFormLayout(self.scrollAreaWidgetContents)
        self.foot_note_label = self.findChild(QLabel, "foot_note_label")
        self.live_mouse_label = self.findChild(QLabel, "live_mouse_label")
        self.home_start_stop_hotkey_label = self.findChild(QLabel, "home_start_stop_hotkey")
        self.mouse_location_hotkey_label = self.findChild(QLabel, "mouse_location_hotkey")
        self.record_start_stop_hotkey_label = self.findChild(QLabel, "record_start_stop_hotkey")
        self.playback_start_stop_hotkey_label = self.findChild(QLabel, "playback_start_stop_hotkey")
        self.set_new_hotkey_button_1 = self.findChild(QPushButton, "set_new_hotkey_1")
        self.set_new_hotkey_button_2 = self.findChild(QPushButton, "set_new_hotkey_2")
        self.set_new_hotkey_button_3 = self.findChild(QPushButton, "set_new_hotkey_3")
        self.set_new_hotkey_button_4 = self.findChild(QPushButton, "set_new_hotkey_4")
        self.on_click_complete_label = self.findChild(QLabel, "on_click_label")
        self.on_click_complete_label_3 = self.findChild(QLabel, "on_click_label_3")
        self.username_box = self.findChild(QLabel, "name")
        self.label = self.findChild(QPushButton, "label")
        self.frame = self.findChild(QFrame, "frame")
        self.frame_2 = self.findChild(QFrame, "frame_2")
        self.frame_3 = self.findChild(QFrame, "frame_3")
        self.frame_4 = self.findChild(QFrame, "frame_4")
        self.frame_10 = self.findChild(QFrame, "frame_10")
        self.frame_11 = self.findChild(QFrame, "frame_11")
        self.frame_12 = self.findChild(QFrame, "frame_12")
        self.frame_13 = self.findChild(QFrame, "frame_13")
        self.frame_14 = self.findChild(QFrame, "frame_14")
        self.frame_6 = self.findChild(QFrame, "frame_6")
        self.frame_7 = self.findChild(QFrame, "frame_7")
        self.frame_8 = self.findChild(QFrame, "frame_8")
        self.frame_9 = self.findChild(QFrame, "frame_9")
        self.line_list = []
        self.i = 1
        self.j = 0
        self.dark_theme_activated = False
        # --------------
        app.aboutToQuit.connect(self.exit_app)
        # --------------
        self.mouse_button_combobox.addItem("Left")
        self.mouse_button_combobox.addItem("Middle")
        self.mouse_button_combobox.addItem("Right")
        self.click_type_combobox.addItem("Single")
        self.click_type_combobox.addItem("Double")
        self.never_stop_combobox.addItem("No")
        self.never_stop_combobox.addItem("Yes")
        self.delay_time_combobox.addItem("ms")
        self.delay_time_combobox.addItem("s")
        self.delay_time_combobox.addItem("min")
        self.delay_time_combobox.addItem("hr")
        self.complete_combobox.addItem(" Idle")
        self.complete_combobox.addItem(" Quit")
        self.complete_combobox.addItem(" Lock")
        self.complete_combobox.addItem(" Turn off")
        self.complete_combobox.addItem(" Log off")
        self.complete_combobox.addItem(" Standby")
        self.complete_combobox.addItem(" Hibernate")
        self.complete_combobox_3.addItem(" Idle")
        self.complete_combobox_3.addItem(" Quit")
        self.complete_combobox_3.addItem(" Lock")
        self.complete_combobox_3.addItem(" Turn off")
        self.complete_combobox_3.addItem(" Log off")
        self.complete_combobox_3.addItem(" Standby")
        self.complete_combobox_3.addItem(" Hibernate")
        self.delay_time_combobox_2.addItem("ms")
        self.delay_time_combobox_2.addItem("s")
        self.delay_time_combobox_2.addItem("min")
        self.delay_time_combobox_2.addItem("hr")
        self.record_add_items.addItem(" Mouse")
        self.record_add_items.addItem(" Keyboard")
        self.record_add_items.addItem(" Scroll")
        # --------------
        self.repeat_radio_button.setChecked(True)
        self.current_location_radio_button.setChecked(True)
        self.record_remove_all_button.setEnabled(False)
        self.repeat_for_number.setText("1")
        self.delay_time_entrybox.setText("100")
        for widget in self.home_frame.findChildren(QLineEdit):
            widget.setValidator(self.integer)
        # --------------
        self.record_button.clicked.connect(self.get_record_screen)
        self.home_button.clicked.connect(self.get_home_screen)
        self.view_settings_button.clicked.connect(self.get_view_screen)
        self.hotkey_settings_button.clicked.connect(self.get_hotkey_screen)
        self.navigate_button.clicked.connect(self.open_menu)
        self.navigate_button_3.clicked.connect(self.open_menu)
        self.play_button.clicked.connect(self.home_start_process)
        self.reset_settings_button.clicked.connect(self.home_reset_settings)
        self.record_add_button.clicked.connect(self.add_new_line)
        self.record_load_button.clicked.connect(self.window_load)
        self.record_save_button.clicked.connect(self.window_record_save)
        self.save_settings_button.clicked.connect(self.window_home_save)
        self.record_play_button.clicked.connect(self.record_start_process)
        self.theme_button.clicked.connect(self.get_dark_theme)
        self.record_remove_all_button.clicked.connect(self.remove_all_lines)
        self.never_stop_combobox.currentIndexChanged.connect(self.check_repeat_style)
        self.complete_combobox.activated.connect(lambda: self.on_click_complete_label.hide())
        self.complete_combobox_3.activated.connect(lambda: self.on_click_complete_label_3.hide())
        # --------------
        # below defines hotkey settings
        self.label_21 = self.findChild(QLabel, "label_21")
        self.label_22 = self.findChild(QLabel, "label_22")
        self.label_23 = self.findChild(QLabel, "label_23")
        self.label_24 = self.findChild(QLabel, "label_24")
        self.label_21.hide()
        self.label_22.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.set_new_hotkey_button_1.clicked.connect(self.start_thread_hotkey_1)
        self.set_new_hotkey_button_2.clicked.connect(self.start_thread_hotkey_4)
        self.set_new_hotkey_button_3.clicked.connect(self.start_thread_hotkey_3)
        self.set_new_hotkey_button_4.clicked.connect(self.start_thread_hotkey_2)
        self.record_record_button.clicked.connect(self.thread_for_live_record)
        # --------------
        # below defines app minimization on close
        self.minimized_icon = QtGui.QIcon("images/app_logo.png")
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(self.minimized_icon)
        self.tray.setVisible(True)
        self.minimized_menu = QtWidgets.QMenu()
        self.menu_option_1 = QtWidgets.QAction("Open")
        self.menu_option_1.triggered.connect(self.show)
        self.minimized_menu.addAction(self.menu_option_1)
        self.menu_option_2 = QtWidgets.QAction("Quit")
        self.menu_option_2.triggered.connect(app.exit)
        self.minimized_menu.addAction(self.menu_option_2)
        self.tray.setContextMenu(self.minimized_menu)
        # --------------
        # below defines the tool tips
        self.setStyleSheet('QToolTip {'
                           'background-color: #e0e0e0;'
                           'border: none;}'
                           'QRadioButton::indicator {'
                           'height: 15px;'
                           'width: 15px;}'
                           'QRadioButton::indicator::unchecked {'
                           'image: url(images/radio_unchecked.png);'
                           'margin-top: 2px;}'
                           'QRadioButton::indicator::checked {'
                           'image: url(images/radio_checked.png);'
                           'margin-top: 2px;}')
        self.central_widget_2.setStyleSheet("QToolTip {background-color: #e0e0e0;"
                                            "border: none;"
                                            "color: black;}"
                                            "QFrame {color: rgb(30, 30, 30);"
                                            "background-color: rgb(239, 229, 220); }")
        self.record_add_items.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                                            'border: 1px solid;'
                                            'border-radius: 3px;'
                                            'border-color: rgb(249, 249, 245);}'
                                            'QComboBox::drop-down {'
                                            'background-color: rgb(249, 249, 245);'
                                            'border: 0px;'
                                            'border-color: rgb(249, 249, 245);}'
                                            'QComboBox::down-arrow {'
                                            'background-color: rgb(249, 249, 245);'
                                            'image: url(images/arrow1.png);'
                                            'width: 8px;'
                                            'height: 8px;}'
                                            "QToolTip {background-color: #e0e0e0;"
                                            "border: none;"
                                            "color: black;}"
                                            "QFrame {color: rgb(30, 30, 30);"
                                            "background-color: rgb(239, 229, 220); }")
        self.complete_combobox.setItemData(0, "No changes to PC", QtCore.Qt.ToolTipRole)
        self.complete_combobox.setItemData(1, "Close the tool (PC keeps running)", QtCore.Qt.ToolTipRole)
        self.complete_combobox.setItemData(2, "Sign out of PC with apps still running", QtCore.Qt.ToolTipRole)
        self.complete_combobox.setItemData(3, "Shut down the PC", QtCore.Qt.ToolTipRole)
        self.complete_combobox.setItemData(4, "Sign out of the PC with all the apps closed", QtCore.Qt.ToolTipRole)
        self.complete_combobox.setItemData(5, "Put the PC to Standby mode", QtCore.Qt.ToolTipRole)
        self.complete_combobox.setItemData(6, "Put the  PC to Hibernate mode", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(0, "No changes to PC", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(1, "Close the tool (PC keeps running)", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(2, "Sign out of PC with apps still running", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(3, "Shut down the PC", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(4, "Sign out of the PC with all the apps closed", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(5, "Put the PC to Standby mode", QtCore.Qt.ToolTipRole)
        self.complete_combobox_3.setItemData(6, "Put the  PC to Hibernate mode", QtCore.Qt.ToolTipRole)
        # --------------
        # below are app settings initialized
        self.hide_to_tray_checkbox2 = self.findChild(QPushButton, "hide_to_tray_checkbox2")
        self.show_after_complete_checkbox2 = self.findChild(QPushButton, "hide_while_click_checkbox2")
        self.mouse_location_checkbox2 = self.findChild(QPushButton, "mouse_location_checkbox2")
        self.hide_to_tray_checkbox = self.findChild(QCheckBox, "hide_to_tray_checkbox")
        self.show_after_complete_checkbox = self.findChild(QCheckBox, "hide_while_click_checkbox")
        self.mouse_location_checkbox = self.findChild(QCheckBox, "mouse_location_checkbox")
        self.hide_to_tray_checkbox.hide()
        self.show_after_complete_checkbox.hide()
        self.mouse_location_checkbox.hide()
        self.hide_to_tray_checkbox2.clicked.connect(self.trigger_tray_checkbox)
        self.mouse_location_checkbox2.clicked.connect(self.trigger_live_mouse)
        self.show_after_complete_checkbox2.clicked.connect(self.trigger_show_tool)
        if self.dark_theme_activated:
            self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
            self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                        "background-color: #10131b;")
            self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
            self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                             "background-color: #10131b")
            self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
            self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                      "background-color: #10131b")
        else:
            self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
            self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                        "background-color: rgb(239, 229, 220);")
            self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
            self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                      "background-color: rgb(239, 229, 220)")
            self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
            self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                             "background-color: rgb(239, 229, 220)")

        self.check_live_mouse()
        if show_tool_after == 1:
            self.show_after_complete_checkbox2.click()
        if hide_system_tray == 1:
            self.hide_to_tray_checkbox2.click()
        if disable_cursor_location == 1:
            self.mouse_location_checkbox2.click()
        if dark_theme == 1:
            self.get_dark_theme()
        # self.username_box.setText(str(new_username))
        self.home_start_stop_hotkey = home_start_hotkey
        self.record_start_stop_hotkey = record_start_hotkey
        self.record_recording_hotkey = record_recording_hotkey
        self.mouse_location_hotkey = mouse_location_hotkey
        keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
        keyboard.add_hotkey(self.home_start_stop_hotkey, lambda: self.play_button.click())
        keyboard.add_hotkey(self.record_start_stop_hotkey, lambda: self.record_play_button.click())
        keyboard.add_hotkey(self.record_recording_hotkey, lambda: self.record_record_button.click())
        self.home_start_stop_hotkey_label.setText(str(home_start_hotkey))
        self.playback_start_stop_hotkey_label.setText(str(record_start_hotkey))
        self.record_start_stop_hotkey_label.setText(str(record_recording_hotkey))
        self.mouse_location_hotkey_label.setText(str(mouse_location_hotkey))
        # --------------------------
        self.label_10 = self.findChild(QLabel, "label_10")
        self.label_2 = self.findChild(QLabel, "label_2")
        self.label_3 = self.findChild(QLabel, "label_3")
        self.label_4 = self.findChild(QLabel, "label_4")
        self.label_6 = self.findChild(QLabel, "label_6")
        self.label_7 = self.findChild(QLabel, "label_7")
        self.font = QtGui.QFont()
        self.font.setPixelSize(13)
        for item in self.findChildren(QLabel):
            item.setFont(self.font)
        for item in self.findChildren(QComboBox):
            item.setFont(self.font)
        for item in self.findChildren(QRadioButton):
            item.setFont(self.font)
        for item in self.findChildren(QLineEdit):
            item.setFont(self.font)
        for item in self.home_frame.findChildren(QPushButton):
            item.setFont(self.font)
        for item in self.record_frame.findChildren(QPushButton):
            item.setFont(self.font)
        for item in self.findChildren(QToolButton):
            item.setFont(self.font)
        self.font.setPixelSize(11)
        self.on_click_complete_label.setFont(self.font)
        self.on_click_complete_label_3.setFont(self.font)
        self.font.setPixelSize(10)
        self.label_10.setFont(self.font)
        self.font.setPixelSize(11)
        self.font.setBold(False)
        self.username_box.setFont(self.font)
        self.font.setBold(True)
        self.label_2.setFont(self.font)
        self.label_3.setFont(self.font)
        self.label_4.setFont(self.font)
        self.label_6.setFont(self.font)
        self.label_7.setFont(self.font)
        self.label_9 = self.findChild(QLabel, "label_9")
        self.label_14 = self.findChild(QLabel, "label_14")
        self.label_15 = self.findChild(QLabel, "label_15")
        self.label_16 = self.findChild(QLabel, "label_16")
        self.label_17 = self.findChild(QLabel, "label_17")
        self.label_9.setFont(self.font)
        self.label_14.setFont(self.font)
        self.label_15.setFont(self.font)
        self.label_16.setFont(self.font)
        self.label_17.setFont(self.font)
        self.font.setBold(False)
        self.foot_note_label.setFont(self.font)
        self.live_mouse_label.setFont(self.font)
        self.font.setPixelSize(12)
        self.record_add_items.setFont(self.font)
        self.delay_time_combobox.setFont(self.font)
        self.delay_time_combobox_2.setFont(self.font)
        self.delay_time_combobox_record.setFont(self.font)
        # ------------------------
        # menu bar buttons below
        about_us = self.findChild(QPushButton, "pushButton")
        about_us.clicked.connect(lambda: webbrowser.open("https://autoclicker.gg/"))
        how_to_use = self.findChild(QPushButton, "pushButton_2")
        how_to_use.clicked.connect(lambda: webbrowser.open("https://autoclicker.gg/windows"))
        email_us = self.findChild(QPushButton, "pushButton_3")
        email_us.clicked.connect(lambda: webbrowser.open("https://autoclicker.gg/contact"))
        faqs = self.findChild(QPushButton, "pushButton_4")
        faqs.clicked.connect(lambda: webbrowser.open("https://autoclicker.gg/FAQs"))
        privacy_policy = self.findChild(QPushButton, "pushButton_5")
        privacy_policy.clicked.connect(lambda: webbrowser.open("https://autoclicker.gg/privacy-policy/"))

    def screenCapture(self):
        """Show the dim Splashscreen"""
        self.hide()

        self.tmpDimScreen.show()
        self.original_x = self.tmpDimScreen.getOriginal_x()
        self.original_y = self.tmpDimScreen.getOriginal_y()
        self.final_x = self.tmpDimScreen.getFinal_x()
        self.final_y = self.tmpDimScreen.getFinal_y()
        self.snipping_width = abs(self.final_x - self.original_x)
        self.snipping_height = abs(self.final_y - self.original_y)
        self.snip_x = min(self.final_x,self.original_x)
        self.snip_y = min(self.final_y,self.original_y)

    # triggers show tool checkbox
    def trigger_show_tool(self):
        if self.show_after_complete_checkbox.isChecked():
            self.show_after_complete_checkbox.setChecked(False)
            if self.dark_theme_activated:
                self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
                self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                                 "background-color: #10131b")
            else:
                self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
                self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                                 "background-color: rgb(239, 229, 220)")
        else:
            self.show_after_complete_checkbox.setChecked(True)
            if self.dark_theme_activated:
                self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/check_icon_dark"))
                self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                                 "background-color: #10131b")
            else:
                self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/check_icon"))
                self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                                 "background-color: rgb(239, 229, 220)")

    # exits app
    def exit_app(self):
        if self.show_after_complete_checkbox.isChecked():
            new_show_tool_after = 1
        else:
            new_show_tool_after = 0
        if self.hide_to_tray_checkbox.isChecked():
            new_hide_system_tray = 1
        else:
            new_hide_system_tray = 0
        if self.mouse_location_checkbox.isChecked():
            new_cursor_location = 1
        else:
            new_cursor_location = 0
        if self.dark_theme_activated:
            new_dark_theme = 1
        else:
            new_dark_theme = 0
        # user_name = self.username_box.text()
        new_home_start_hotkey = self.home_start_stop_hotkey
        new_record_start_hotkey = self.record_start_stop_hotkey
        new_record_recording_hotkey = self.record_recording_hotkey
        new_mouse_location_hotkey = self.mouse_location_hotkey
        conn = sqlite3.connect('autoclicker.db')
        cursor = conn.cursor()
        delete_row = '''DELETE FROM app_settings'''
        cursor.execute(delete_row)
        add_new_row = f'''INSERT INTO app_settings VALUES (
                '{new_show_tool_after}',
                '{new_hide_system_tray}',
                '{new_cursor_location}',
                '{new_dark_theme}',
                '{new_home_start_hotkey}',
                '{new_record_start_hotkey}',
                '{new_record_recording_hotkey}',
                '{new_mouse_location_hotkey}'
                )'''
        cursor.execute(add_new_row)
        conn.commit()
        conn.close()
        app.exit()

    # activates dark theme
    def get_dark_theme(self):
        self.setStyleSheet("QComboBox {color: black;"
                            "background-color: rgb(249, 249, 245);"
                            "border: none}"
                            'QComboBox::drop-down {'
                           'background-color: rgb(249, 249, 245);'
                           'border-color: rgb(249, 249, 245);}'
                           'QToolTip {'
                           'background-color: #e0e0e0;'
                           'border: none;}'
                           'QRadioButton::indicator {'
                           'height: 15px;'
                           'width: 15px;}'
                           'QRadioButton::indicator::unchecked {'
                           'image: url(images/dark_unchecked.png);'
                           'margin-top: 2px;}'
                           'QRadioButton::indicator::checked {'
                           'image: url(images/dark_checked.png);'
                           'margin-top: 2px;}'
                           )
        self.dark_theme_activated = True
        # self.central_widget_2.setStyleSheet("background-color: #10131b;")
        self.left_frame.setStyleSheet("background-color: #10131b;"
                                      "color: #bfcfb2;"
                                      "border: 2px solid #bfcfb2;"
                                      "border-radius: 10px;")
        self.GG_icon.setStyleSheet("border:none;")
        self.GG_icon.setIcon(QtGui.QIcon('images/GG_dark'))
        self.home_button.setStyleSheet("border:none;")
        self.home_button.setIcon(QtGui.QIcon('images/Home_dark'))
        self.record_button.setStyleSheet("border:none;")
        self.record_button.setIcon(QtGui.QIcon('images/Record_dark'))
        self.theme_button.setStyleSheet("border:none;")
        self.theme_button.setIcon(QtGui.QIcon('images/Mode_dark.png'))
        self.view_settings_button.setStyleSheet("border:none;")
        self.view_settings_button.setIcon(QtGui.QIcon('images/Setting_dark.png'))
        self.hotkey_settings_button.setStyleSheet("border:none;")
        self.hotkey_settings_button.setIcon(QtGui.QIcon('images/HotKey_dark.png'))
        self.central_widget_2.setStyleSheet("QFrame {background-color: #10131b;"
                                            "color: #bfcfb2;"
                                            "border: none;}"
                                            "QComboBox {color: black;"
                                            "background-color: rgb(249, 249, 245);"
                                            "border: none}"
                                            "QLineEdit {color: black;"
                                            "background-color: rgb(249, 249, 245);"
                                            "border: none}"
                                            "QRadioButton {color: #bfcfb2;}")
        self.main_frame.setStyleSheet("QFrame {background-color: #10131b;"
                                      "color: #bfcfb2;"
                                      "border: none;}"
                                      "QComboBox {color: black;"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: none}"
                                      "QLineEdit {color: black;"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: none}"
                                      "QRadioButton {color: #bfcfb2;}")
        self.top_frame.setStyleSheet("QFrame {background-color: #10131b;"
                                     "color: #bfcfb2;"
                                     "border: none;}"
                                     "QComboBox {color: black;"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: none}"
                                     "QLineEdit {color: black;"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: none}")
        self.top_frame_logged_out.setStyleSheet("QFrame {background-color: #10131b;"
                                     "color: #bfcfb2;"
                                     "border: none;}"
                                     "QComboBox {color: black;"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: none}"
                                     "QLineEdit {color: black;"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: none}")
        self.home_frame.setStyleSheet("QFrame {background-color: #10131b;"
                                      "color: #bfcfb2;"
                                      "border: none;}"
                                      "QComboBox {color: black;"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: none}"
                                      "QLineEdit {color: black;"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: none}"
                                      "QRadioButton {color: #bfcfb2;}")
        self.reset_settings_button.setStyleSheet("QPushButton {color: #ffa94d;"
                                                 "border: 2px solid #ffa94d;"
                                                 "border-radius: 5px;"
                                                 "color: #ffa94d;}"
                                                 "QPushButton::hover {color:white;"
                                                 "background-color: #ffa94d;}")
        self.play_button.setStyleSheet("QPushButton {color: #c98860;"
                                       "border: 2px solid #c98860;"
                                       "border-radius: 5px;"
                                       "color: #c98860;}"
                                       "QPushButton::hover {color:white;"
                                       "background-color: #c98860;}")
        self.play_button.setIcon(QtGui.QIcon("images/run_dark"))
        self.save_settings_button.setStyleSheet("QPushButton {color: #1ecd97;"
                                                "border: 2px solid #1ecd97;"
                                                "border-radius: 5px;"
                                                "color: #1ecd97;}"
                                                "QPushButton::hover {color:white;"
                                                "background-color: #1ecd97;}")
        self.foot_note_label.setStyleSheet("border:none;")
        self.navigate_button.setStyleSheet("border:none;")
        self.navigate_button.setIcon(QtGui.QIcon("images/Menu_dark.png"))
        self.navigation_frame.setStyleSheet("QPushButton {background-color: #10131b;"
                                            "border: 1px solid #bfcfb2;"
                                            "color: #bfcfb2;}")
        self.navigate_button_3.setStyleSheet("border:none;")
        self.navigate_button_3.setIcon(QtGui.QIcon("images/Menu_dark.png"))

        self.on_click_complete_label.setStyleSheet("QLabel {color: black;"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border: none;}"
                                                   'QToolTip {'
                                                   'background-color: #e0e0e0;'
                                                   'border: none;}')
        self.on_click_complete_label_3.setStyleSheet("QLabel {color: black;"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border: none;}"
                                                   'QToolTip {'
                                                   'background-color: #e0e0e0;'
                                                   'border: none;}')
        # self.set_new_hotkey_1.setStyleSheet
        self.profile_button.setStyleSheet("border: none;")
        self.profile_button.setIcon(QtGui.QIcon("images/Profile-Picture_dark"))
        self.profile_button_3.setStyleSheet("border: none;")
        self.profile_button_3.setIcon(QtGui.QIcon("images/Profile-Picture_dark"))
        self.username_box.setStyleSheet("QLineEdit {background-color: #10131b;"
                                        "color: #bfcfb2;}"
                                        "QToolTip {background-color: #e0e0e0;}")
        self.home_start_stop_hotkey_label.setStyleSheet("color: black;"
                                                        "border: 1px solid #bfcfb2;"
                                                        "border-radius: 5px;"
                                                        "background-color: rgb(249, 249, 245);")
        self.playback_start_stop_hotkey_label.setStyleSheet("color: black;"
                                                            "border: 1px solid #bfcfb2;"
                                                            "border-radius: 5px;"
                                                            "background-color: rgb(249, 249, 245);")
        self.record_start_stop_hotkey_label.setStyleSheet("color: black;"
                                                          "border: 1px solid #bfcfb2;"
                                                          "border-radius: 5px;"
                                                          "background-color: rgb(249, 249, 245);")
        self.mouse_location_hotkey_label.setStyleSheet("color: black;"
                                                       "border: 1px solid #bfcfb2;"
                                                       "border-radius: 5px;"
                                                       "background-color: rgb(249, 249, 245);")
        self.frame.setStyleSheet("QFrame {border: 1.5px solid #bfcfb2;"
                                 "border-radius: 10px;}"
                                 'QComboBox::drop-down {'
                                 'background-color: rgb(249, 249, 245);'
                                 'border-color: rgb(249, 249, 245);}'
                                 )
        self.frame_2.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.frame_3.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.frame_4.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.frame_10.setStyleSheet("border: 2px solid #bfcfb2;"
                                    "border-radius: 10px;")
        self.frame_11.setStyleSheet("border: 2px solid #bfcfb2;"
                                    "border-radius: 10px;")
        self.frame_12.setStyleSheet("border: 2px solid #bfcfb2;"
                                    "border-radius: 10px;")
        self.frame_13.setStyleSheet("border: 2px solid #bfcfb2;"
                                    "border-radius: 10px;")
        self.frame_14.setStyleSheet("border: 2px solid #bfcfb2;"
                                    "border-radius: 10px;")
        self.view_settings_frame.setStyleSheet("QFrame {background-color: #10131b;"
                                               "color: #bfcfb2;"
                                               "border: none;}")
        self.frame_6.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.frame_7.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.frame_8.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.frame_9.setStyleSheet("border: 1.5px solid #bfcfb2;"
                                   "border-radius: 10px;")
        self.record_scroll_area.setStyleSheet("QScrollArea {border: 1.5px solid #bfcfb2;"
                                              "background-color: #10131b;"
                                              "border-radius: 5px;}")
        self.scrollAreaWidgetContents.setStyleSheet("border: none;"
                                                    "background-color: #10131b")

        self.scroll_bar.setStyleSheet("""QScrollBar:vertical {
                                        border-color: #10131b;
                                        border-width: 1px;
                                        border-style: solid;
                                        border-radius: 10px;
                                        background-color: #10131b;
                                        width:18px;
                                        margin: 10px 4px 10px 0;}
                                    QScrollBar::handle:vertical {
                                        background-color: #bfcfb2;
                                        min-height: 25px;
                                        border: 1px solid #bfcfb2;
                                        border-radius: 5px;}
                                    QScrollBar::add-line:vertical {
                                        border: 1px solid #10131b;
                                        background-color: #10131b;
                                        height: 0px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;}
                                    QScrollBar::sub-line:vertical {
                                        border: 1px solid #10131b;
                                        background-color: #10131b;
                                        height: 0px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;}
                                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                        background: none;}
                                    QScrollBar::up-arrow:vertical {
                                      background-color: #10131b;}
                                    QScrollBar::down-arrow:vertical {
                                      background-color: #10131b;}""")
        for row in self.scrollAreaWidgetContents.children():
            for button in row.findChildren(QPushButton):
                button.setStyleSheet("background-color: #10131b")
        self.record_record_button.setStyleSheet("QPushButton {color: white;"
                                                "border: 2px solid white;"
                                                "border-radius: 5px;"
                                                "color: white;}"
                                                "QPushButton::hover {color:black;"
                                                "background-color: white;}")
        self.record_play_button.setStyleSheet("QPushButton {color: #c98860;"
                                              "border: 2px solid #c98860;"
                                              "border-radius: 5px;"
                                              "color: #c98860;}"
                                              "QPushButton::hover {color:white;"
                                              "background-color: #c98860;}")
        self.record_play_button.setIcon(QtGui.QIcon("images/run_dark"))
        self.record_save_button.setStyleSheet("QPushButton {color: #1ecd97;"
                                              "border: 2px solid #1ecd97;"
                                              "border-radius: 5px;"
                                              "color: #1ecd97;}"
                                              "QPushButton::hover {color:white;"
                                              "background-color: #1ecd97;}")
        self.record_remove_all_button.setStyleSheet("QPushButton {color: #ffa94d;"
                                                    "border: 2px solid #ffa94d;"
                                                    "border-radius: 5px;"
                                                    "color: #ffa94d;}"
                                                    "QPushButton::hover {color:white;"
                                                    "background-color: #ffa94d;}")
        self.record_load_button.setStyleSheet("QPushButton {color: black;"
                                              "background-color: #bfcfb2;"
                                              "border 1px solid #bfcfb2;"
                                              "border-radius: 3px;}"
                                              'QToolTip {'
                                              'background-color: #e0e0e0;'
                                              'border: none;}'
                                              )
        self.record_load_button.setIcon(QtGui.QIcon("images/uplode_dark.png"))
        self.record_add_button.setStyleSheet("QPushButton {border: 1px solid rgb(196, 177, 174);"
                                             "border-radius: 10;"
                                             "background-color: #bfcfb2;}"
                                             'QToolTip {'
                                             'background-color: #e0e0e0;'
                                             'border: none;}'
                                             )
        self.record_add_button.setIcon(QtGui.QIcon("images/icons8-ui-64.png"))
        self.label_21.setStyleSheet("color: black;"
                                    "background-color: #e0e0e0;")
        self.label_22.setStyleSheet("color: black;"
                                    "background-color: #e0e0e0;")
        self.label_23.setStyleSheet("color: black;"
                                    "background-color: #e0e0e0;")
        self.label_24.setStyleSheet("color: black;"
                                    "background-color: #e0e0e0;")
        self.theme_button.disconnect()
        self.theme_button.clicked.connect(self.get_normal_theme)
        if self.hide_to_tray_checkbox.isChecked():
            self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/check_icon_dark"))
        else:
            self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
        self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                  "background-color: #10131b;")
        if self.show_after_complete_checkbox.isChecked():
            self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/check_icon_dark"))
        else:
            self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
        self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                         "background-color: #10131b;")
        if self.mouse_location_checkbox.isChecked():
            self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/check_icon_dark"))
        else:
            self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
        self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                    "background-color: #10131b;")

    # activates normal theme
    def get_normal_theme(self):
        self.setStyleSheet('QComboBox::drop-down {'
                           'background-color: rgb(249, 249, 245);'
                           'border-color: rgb(249, 249, 245);}'
                           'QToolTip {'
                           'background-color: #e0e0e0;'
                           'border: none;}'
                           'QRadioButton::indicator {'
                           'height: 15px;'
                           'width: 15px;}'
                           'QRadioButton::indicator::unchecked {'
                           'image: url(images/radio_unchecked.png);'
                           'margin-top: 2px;}'
                           'QRadioButton::indicator::checked {'
                           'image: url(images/radio_checked.png);'
                           'margin-top: 2px;}'
                           )
        self.dark_theme_activated = False
        self.left_frame.setStyleSheet("background-color: rgb(196, 177, 174);"
                                      "color: black;"
                                      "border: 2px solid rgb(196, 177, 174);"
                                      "border-radius: 10px;")
        self.GG_icon.setStyleSheet("border:none;")
        self.GG_icon.setIcon(QtGui.QIcon('images/GGicon'))
        self.home_button.setStyleSheet("border:none;")
        self.home_button.setIcon(QtGui.QIcon('images/home'))
        self.record_button.setStyleSheet("border:none;")
        self.record_button.setIcon(QtGui.QIcon('images/Record'))
        self.theme_button.setStyleSheet("border:none;")
        self.theme_button.setIcon(QtGui.QIcon('images/Mode.png'))
        self.view_settings_button.setStyleSheet("border:none;")
        self.view_settings_button.setIcon(QtGui.QIcon('images/Settings.png'))
        self.hotkey_settings_button.setStyleSheet("border:none;")
        self.hotkey_settings_button.setIcon(QtGui.QIcon('images/HotkeyBlack.png'))
        self.central_widget_2.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
                                            "color: rgb(30, 30, 30);"
                                            "border: none;}"
                                            "QComboBox {color: rgb(30, 30, 30);"
                                            "background-color: rgb(249, 249, 245);"
                                            "border: 1px solid;"
                                            "border-radius: 3px;}"
                                            "QLineEdit {color: rgb(30, 30, 30);"
                                            "background-color: rgb(249, 249, 245);"
                                            "border: 1px solid;"
                                            "border-radius: 3px solid;}"
                                            "QRadioButton {color: rgb(30, 30, 30);"
                                            "border: none;}")
        self.main_frame.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
                                      "color: rgb(30, 30, 30);"
                                      "border: none;}"
                                      "QComboBox {color: rgb(30, 30, 30);"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: 1px solid;"
                                      "border-radius: 3px;}"
                                      "QLineEdit {color: rgb(30, 30, 30);"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: 1px solid;"
                                      "border-radius: 3px solid;}"
                                      "QRadioButton {color: rgb(30, 30, 30);"
                                      "border: none;}")
        self.top_frame.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
                                     "color: rgb(30, 30, 30);"
                                     "border: none;}"
                                     "QComboBox {color: rgb(30, 30, 30);"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: 1px solid;"
                                     "border-radius: 3px;}"
                                     "QLineEdit {color: rgb(30, 30, 30);"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: 1px solid;"
                                     "border-radius: 3px solid;}"
                                     "QRadioButton {color: rgb(30, 30, 30);"
                                     "border: none;}")
        self.top_frame_logged_out.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
                                     "color: rgb(30, 30, 30);"
                                     "border: none;}"
                                     "QComboBox {color: rgb(30, 30, 30);"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: 1px solid;"
                                     "border-radius: 3px;}"
                                     "QLineEdit {color: rgb(30, 30, 30);"
                                     "background-color: rgb(249, 249, 245);"
                                     "border: 1px solid;"
                                     "border-radius: 3px solid;}"
                                     "QRadioButton {color: rgb(30, 30, 30);"
                                     "border: none;}")
        self.home_frame.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
                                      "color: rgb(30, 30, 30);"
                                      "border: none;}"
                                      "QComboBox {color: rgb(30, 30, 30);"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: 1px solid;"
                                      "border-radius: 3px;}"
                                      "QLineEdit {color: rgb(30, 30, 30);"
                                      "background-color: rgb(249, 249, 245);"
                                      "border: 1px solid;"
                                      "border-radius: 3px solid;}"
                                      "QRadioButton {color: rgb(30, 30, 30);"
                                      "border: none;}")
        self.reset_settings_button.setStyleSheet("QPushButton {color: rgb(255, 162, 0);"
                                                 "border: 2px solid rgb(255, 162, 0);"
                                                 "border-radius: 5px;"
                                                 "color: #ffa94d;}"
                                                 "QPushButton::hover {color:white;"
                                                 "background-color: rgb(255, 162, 0);}")
        self.play_button.setStyleSheet("QPushButton {color: #3A5A40;"
                                       "border: 2px solid #3A5A40;"
                                       "border-radius: 5px;"
                                       "color: #3A5A40;}"
                                       "QPushButton::hover {color:white;"
                                       "background-color: #3A5A40;}")
        self.play_button.setIcon(QtGui.QIcon("images/run"))
        self.save_settings_button.setStyleSheet("QPushButton {color: rgb(3, 199, 26);"
                                                "border: 2px solid rgb(3, 199, 26);"
                                                "border-radius:5px; "
                                                "color: rgb(3, 199, 26);}"
                                                "QPushButton::hover {color:white;"
                                                "background-color: rgb(3, 199, 26);}")
        self.foot_note_label.setStyleSheet("border:none;")
        self.navigate_button.setStyleSheet("border:none;")
        self.navigate_button.setIcon(QtGui.QIcon("images/Hambuger"))
        self.navigate_button_3.setStyleSheet("border:none;")
        self.navigate_button_3.setIcon(QtGui.QIcon("images/Hambuger"))
        self.navigation_frame.setStyleSheet("QPushButton {background-color: rgb(242,242,242);"
                                            "border: 1px solid rgb(204, 204, 204);"
                                            "color: rgb(30, 30, 30);}")
        self.on_click_complete_label.setStyleSheet("QLabel {color: black;"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border: none;}"
                                                   'QToolTip {'
                                                   'background-color: #e0e0e0;'
                                                   'border: none;}')
        self.on_click_complete_label_3.setStyleSheet("QLabel {color: black;"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border: none;}"
                                                   'QToolTip {'
                                                   'background-color: #e0e0e0;'
                                                   'border: none;}')
        self.profile_button.setStyleSheet("border: none;")
        self.profile_button.setIcon(QtGui.QIcon("images/liliajohn.png"))
        self.profile_button_3.setStyleSheet("border: none;")
        self.profile_button_3.setIcon(QtGui.QIcon("images/liliajohn.png"))
        self.username_box.setStyleSheet("QLabel {background-color: rgb(239, 229, 220);"
                                        "color: rgb(30, 30, 30);"
                                        "border: none;}"
                                        "QToolTip {background-color: #e0e0e0;}")
        self.home_start_stop_hotkey_label.setStyleSheet("color: black;"
                                                        "border: 1px solid #bfcfb2;"
                                                        "border-radius: 5px;"
                                                        "background-color: rgb(249, 249, 245);")
        self.playback_start_stop_hotkey_label.setStyleSheet("color: black;"
                                                            "border: 1px solid #bfcfb2;"
                                                            "border-radius: 5px;"
                                                            "background-color: rgb(249, 249, 245);")
        self.record_start_stop_hotkey_label.setStyleSheet("color: black;"
                                                          "border: 1px solid #bfcfb2;"
                                                          "border-radius: 5px;"
                                                          "background-color: rgb(249, 249, 245);")
        self.mouse_location_hotkey_label.setStyleSheet("color: black;"
                                                       "border: 1px solid #bfcfb2;"
                                                       "border-radius: 5px;"
                                                       "background-color: rgb(249, 249, 245);")
        self.frame.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                 "border-radius: 10px;")
        self.frame_2.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.frame_3.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.frame_4.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.frame_10.setStyleSheet("border: 2px solid rgb(196, 177, 174);"
                                    "border-radius: 10px;")
        self.frame_11.setStyleSheet("border: 2px solid rgb(196, 177, 174);"
                                    "border-radius: 10px;")
        self.frame_12.setStyleSheet("border: 2px solid rgb(196, 177, 174);"
                                    "border-radius: 10px;")
        self.frame_13.setStyleSheet("border: 2px solid rgb(196, 177, 174);"
                                    "border-radius: 10px;")
        self.frame_14.setStyleSheet("border: 2px solid rgb(196, 177, 174);"
                                    "border-radius: 10px;")
        self.view_settings_frame.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
                                               "color: rgb(30, 30, 30);"
                                               "border: none;}")
        self.frame_6.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.frame_7.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.frame_8.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.frame_9.setStyleSheet("border: 1.5px solid rgb(196, 177, 174);"
                                   "border-radius: 10px;")
        self.record_scroll_area.setStyleSheet("QScrollArea {border: 1.5px solid #c8bab7;"
                                              "background-color: rgb(239, 229, 220);"
                                              "border-radius: 5px;}")
        self.scrollAreaWidgetContents.setStyleSheet("border: none;"
                                                    "background-color: rgb(239, 229, 220)")
        self.scroll_bar.setStyleSheet("""QScrollBar:vertical {
                                        border-color: rgb(239, 229, 220);
                                        border-width: 1px;
                                        border-style: solid;
                                        border-radius: 10px;
                                        background-color: rgb(239, 229, 220);
                                        width:18px;
                                        margin: 10px 4px 10px 0;}
                                    QScrollBar::handle:vertical {
                                        background-color: #c4b1ad;
                                        min-height: 25px;
                                        border: 1px solid #c4b1ad;
                                        border-radius: 5px;}
                                    QScrollBar::add-line:vertical {
                                        border: 1px solid rgb(239, 229, 220);
                                        background-color: rgb(239, 229, 220);
                                        height: 0px;
                                        subcontrol-position: bottom;
                                        subcontrol-origin: margin;}
                                    QScrollBar::sub-line:vertical {
                                        border: 1px solid rgb(239, 229, 220);
                                        background-color: rgb(241, 241, 241);
                                        height: 0px;
                                        subcontrol-position: top;
                                        subcontrol-origin: margin;}
                                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                        background: none;}
                                    QScrollBar::up-arrow:vertical {
                                      background-color: rgb(239, 229, 220);}
                                    QScrollBar::down-arrow:vertical {
                                      background-color: rgb(239, 229, 220);}""")
        for row in self.scrollAreaWidgetContents.children():
            for button in row.findChildren(QPushButton):
                button.setStyleSheet("background-color: rgb(239, 229, 220)")
        self.record_record_button.setStyleSheet("QPushButton {color: black;"
                                                "border: 2px solid black;"
                                                "border-radius: 5px;"
                                                "color: black;}"
                                                "QPushButton::hover {color: white;"
                                                "background-color: black;}")
        self.record_play_button.setStyleSheet("QPushButton {color: #3A5A40;"
                                              "border: 2px solid #3A5A40;"
                                              "border-radius: 5px;"
                                              "color: #3A5A40;}"
                                              "QPushButton::hover {color:white;"
                                              "background-color: #3A5A40;}")
        self.record_play_button.setIcon(QtGui.QIcon("images/run_dark"))
        self.record_save_button.setStyleSheet("QPushButton {color: rgb(3, 199, 26);"
                                              "border: 2px solid rgb(3, 199, 26);"
                                              "border-radius: 5px;"
                                              "color: rgb(3, 199, 26);}"
                                              "QPushButton::hover {color:white;"
                                              "background-color: rgb(3, 199, 26);}")
        self.record_remove_all_button.setStyleSheet("QPushButton {color: rgb(255, 162, 0);"
                                                    "border-radius: 5px;"
                                                    "border: 2px solid rgb(255, 162, 0);"
                                                    "color: rgb(255, 162, 0);}"
                                                    "QPushButton::hover {color:white;"
                                                    "background-color: rgb(255, 162, 0);}")
        self.record_load_button.setStyleSheet("QPushButton {color: white;"
                                              "background-color: #5579c7;"
                                              "border 1px solid #5579c7;"
                                              "border-radius: 3px;}"
                                              'QToolTip {'
                                              'background-color: #e0e0e0;'
                                              'border: none;}'
                                              )
        self.record_load_button.setIcon(QtGui.QIcon("images/icons8-upload-96.png"))
        self.record_add_button.setStyleSheet("QPushButton {border: 1px solid rgb(196, 177, 174);"
                                             "border-radius: 10;"
                                             "background-color:  #c1b3b0;}"
                                             'QToolTip {'
                                             'background-color: #e0e0e0;'
                                             'border: none;}'
                                             )
        self.record_add_button.setIcon(QtGui.QIcon("images/icons8-ui-64.png"))
        self.theme_button.clicked.disconnect()
        self.theme_button.clicked.connect(self.get_dark_theme)
        if self.hide_to_tray_checkbox.isChecked():
            self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/check_icon"))
        else:
            self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
        self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                  "background-color: rgb(239, 229, 220);")
        if self.show_after_complete_checkbox.isChecked():
            self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/check_icon"))
        else:
            self.show_after_complete_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
        self.show_after_complete_checkbox2.setStyleSheet("border: none;"
                                                         "background-color: rgb(239, 229, 220);")
        if self.mouse_location_checkbox.isChecked():
            self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/check_icon"))
        else:
            self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
        self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                    "background-color: rgb(239, 229, 220);")

    # gets home screen in front
    def get_home_screen(self):
        self.navigation_frame.lower()
        self.home_frame.show()

        self.record_frame.hide()
        self.view_settings_frame.hide()
        self.hotkey_settings_frame.hide()
        self.foot_note_label.setText('')

    def get_record_screen(self):

        self.navigation_frame.lower()
        self.view_settings_frame.hide()
        self.hotkey_settings_frame.hide()
        self.home_frame.hide()
        self.foot_note_label.setText('')
        self.record_frame.show()


    # gets view settings screen in front
    def get_view_screen(self):
        self.navigation_frame.lower()

        self.record_frame.hide()
        self.view_settings_frame.show()
        self.hotkey_settings_frame.hide()
        self.home_frame.hide()
        self.foot_note_label.setText('')

    # gets hotkey settings screen in front
    def get_hotkey_screen(self):
        self.navigation_frame.lower()

        self.record_frame.hide()
        self.view_settings_frame.hide()
        self.hotkey_settings_frame.show()
        self.home_frame.hide()

        self.foot_note_label.setText('')

    # changes hotkey of home -> start/stop button
    def change_home_start_hotkey(self):
        self.label_21.show()
        keyboard.remove_hotkey(self.home_start_stop_hotkey)
        self.home_start_stop_hotkey_label.setText('')
        self.set_new_hotkey_button_1.setEnabled(False)
        self.set_new_hotkey_button_2.setEnabled(False)
        self.set_new_hotkey_button_3.setEnabled(False)
        self.set_new_hotkey_button_4.setEnabled(False)
        new_hotkey = ''
        keyboard.start_recording()
        keyboard.wait('enter')
        pressed_keys = keyboard.stop_recording()
        for key in pressed_keys:
            if str(key)[-11: -6] == 'enter':
                continue
            if str(key)[-5:] == 'down)':
                if new_hotkey != '':
                    new_hotkey += ' + '
                new_hotkey += str(key)[14:-6]
        new_hotkey = new_hotkey.replace(' + enter ', '')
        if new_hotkey == '':
            keyboard.add_hotkey(self.home_start_stop_hotkey, lambda: self.play_button.click())
            self.home_start_stop_hotkey_label.setText(str(self.home_start_stop_hotkey))
        else:
            try:
                self.home_start_stop_hotkey = new_hotkey
                keyboard.add_hotkey(self.home_start_stop_hotkey, lambda: self.play_button.click())
                self.home_start_stop_hotkey_label.setText(new_hotkey)
            except ValueError:
                keyboard.add_hotkey(self.home_start_stop_hotkey, lambda: self.play_button.click())
                self.home_start_stop_hotkey_label.setText(str(self.home_start_stop_hotkey))
        self.set_new_hotkey_button_1.setEnabled(True)
        self.set_new_hotkey_button_2.setEnabled(True)
        self.set_new_hotkey_button_3.setEnabled(True)
        self.set_new_hotkey_button_4.setEnabled(True)
        self.label_21.hide()

    # changes hotkey of record -> start/stop button
    def change_record_start_hotkey(self):
        self.label_23.show()
        keyboard.remove_hotkey(self.record_start_stop_hotkey)
        self.playback_start_stop_hotkey_label.setText('')
        self.set_new_hotkey_button_1.setEnabled(False)
        self.set_new_hotkey_button_2.setEnabled(False)
        self.set_new_hotkey_button_3.setEnabled(False)
        self.set_new_hotkey_button_4.setEnabled(False)
        new_hotkey = ''
        keyboard.start_recording()
        keyboard.wait('enter')
        pressed_keys = keyboard.stop_recording()
        for key in pressed_keys:
            if str(key)[-11: -6] == 'enter':
                continue
            if str(key)[-5:] == 'down)':
                if new_hotkey != '':
                    new_hotkey += ' + '
                new_hotkey += str(key)[14:-6]
        new_hotkey = new_hotkey.replace(' + enter ', '')
        if new_hotkey == '':
            keyboard.add_hotkey(self.record_start_stop_hotkey, lambda: self.record_play_button.click())
            self.playback_start_stop_hotkey_label.setText(str(self.record_start_stop_hotkey))
        else:
            try:
                self.record_start_stop_hotkey = new_hotkey
                keyboard.add_hotkey(self.record_start_stop_hotkey, lambda: self.record_play_button.click())
                self.playback_start_stop_hotkey_label.setText(new_hotkey)
            except ValueError:
                keyboard.add_hotkey(self.record_start_stop_hotkey, lambda: self.record_play_button.click())
                self.playback_start_stop_hotkey_label.setText(str(self.record_start_stop_hotkey))
        self.set_new_hotkey_button_1.setEnabled(True)
        self.set_new_hotkey_button_2.setEnabled(True)
        self.set_new_hotkey_button_3.setEnabled(True)
        self.set_new_hotkey_button_4.setEnabled(True)
        self.label_23.hide()

    # changes hotkey of getting mouse location
    def change_mouse_location_hotkey(self):
        self.label_22.show()
        keyboard.remove_hotkey(self.mouse_location_hotkey)
        self.mouse_location_hotkey_label.setText('')
        self.set_new_hotkey_button_1.setEnabled(False)
        self.set_new_hotkey_button_2.setEnabled(False)
        self.set_new_hotkey_button_3.setEnabled(False)
        self.set_new_hotkey_button_4.setEnabled(False)
        new_hotkey = ''
        keyboard.start_recording()
        keyboard.wait('enter')
        pressed_keys = keyboard.stop_recording()
        for key in pressed_keys:
            if str(key)[-11: -6] == 'enter':
                continue
            if str(key)[-5:] == 'down)':
                if new_hotkey != '':
                    new_hotkey += ' + '
                new_hotkey += str(key)[14:-6]
        new_hotkey = new_hotkey.replace(' + enter ', '')
        if new_hotkey == '':
            keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
            self.mouse_location_hotkey_label.setText(str(self.mouse_location_hotkey))
        else:
            try:
                self.mouse_location_hotkey = new_hotkey
                keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
                self.mouse_location_hotkey_label.setText(new_hotkey)
            except ValueError:
                keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
                self.mouse_location_hotkey_label.setText(str(self.mouse_location_hotkey))
        self.set_new_hotkey_button_1.setEnabled(True)
        self.set_new_hotkey_button_2.setEnabled(True)
        self.set_new_hotkey_button_3.setEnabled(True)
        self.set_new_hotkey_button_4.setEnabled(True)
        self.label_22.hide()

    # changes hotkey of record -> recording button
    def change_recording_hotkey(self):
        self.label_24.show()
        keyboard.remove_hotkey(self.record_recording_hotkey)
        self.record_start_stop_hotkey_label.setText('')
        self.set_new_hotkey_button_1.setEnabled(False)
        self.set_new_hotkey_button_2.setEnabled(False)
        self.set_new_hotkey_button_3.setEnabled(False)
        self.set_new_hotkey_button_4.setEnabled(False)
        new_hotkey = ''
        keyboard.start_recording()
        keyboard.wait('enter')
        pressed_keys = keyboard.stop_recording()
        for key in pressed_keys:
            if str(key)[-11: -6] == 'enter':
                continue
            if str(key)[-5:] == 'down)':
                if new_hotkey != '':
                    new_hotkey += ' + '
                new_hotkey += str(key)[14:-6]
        new_hotkey = new_hotkey.replace(' + enter ', '')
        if new_hotkey == '':
            keyboard.add_hotkey(self.record_recording_hotkey, lambda: self.record_record_button.click())
            self.record_start_stop_hotkey_label.setText(str(self.record_recording_hotkey))
        else:
            try:
                self.record_recording_hotkey = new_hotkey
                keyboard.add_hotkey(self.record_recording_hotkey, lambda: self.record_record_button.click())
                self.record_start_stop_hotkey_label.setText(new_hotkey)
            except ValueError:
                keyboard.add_hotkey(self.record_recording_hotkey, lambda: self.record_record_button.click())
                self.record_start_stop_hotkey_label.setText(str(self.record_recording_hotkey))
        self.set_new_hotkey_button_1.setEnabled(True)
        self.set_new_hotkey_button_2.setEnabled(True)
        self.set_new_hotkey_button_3.setEnabled(True)
        self.set_new_hotkey_button_4.setEnabled(True)
        self.label_24.hide()

    # starts thread for hotkey change of home -> start_stop button
    def start_thread_hotkey_1(self):
        change_home_start_hotkey_thread = threading.Thread(target=self.change_home_start_hotkey)
        change_home_start_hotkey_thread.start()

    # starts thread for hotkey change of record -> start_stop button
    def start_thread_hotkey_2(self):
        change_record_start_hotkey_thread = threading.Thread(target=self.change_record_start_hotkey)
        change_record_start_hotkey_thread.start()

    # starts thread for hotkey change of getting mouse location
    def start_thread_hotkey_3(self):
        change_mouse_location_hotkey_thread = threading.Thread(target=self.change_mouse_location_hotkey)
        change_mouse_location_hotkey_thread.start()

    # starts thread for hotkey change of record -> record button
    def start_thread_hotkey_4(self):
        change_recording_hotkey_thread = threading.Thread(target=self.change_recording_hotkey)
        change_recording_hotkey_thread.start()

    # opens the menu bar
    def open_menu(self):
        self.navigation_frame.raise_()
        self.navigate_button.clicked.disconnect()
        self.navigate_button.clicked.connect(self.close_menu)
        self.navigate_button_3.clicked.disconnect()
        self.navigate_button_3.clicked.connect(self.close_menu)

    # closes the menu bar
    def close_menu(self):
        self.navigation_frame.lower()
        self.navigate_button.clicked.disconnect()
        self.navigate_button.clicked.connect(self.open_menu)
        self.navigate_button_3.clicked.disconnect()
        self.navigate_button_3.clicked.connect(self.open_menu)

    # triggered by record -> save button (pop-up window)
    def window_record_save(self):
        self.font.setBold(False)
        self.font.setPixelSize(11)
        self.record_save_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.record_save_window.setWindowTitle("Save")
        self.record_save_window.setWindowIcon(QtGui.QIcon('images/icons8-save-90'))
        self.record_save_window.setGeometry(827, 520, 300, 115)
        self.record_save_window.setFixedWidth(300)
        self.record_save_window.setFixedHeight(115)
        self.invisible_widget_1 = QWidget(self.record_save_window)
        self.record_save_layout = QGridLayout(self.invisible_widget_1)
        self.record_save_name_box = QLineEdit(self.invisible_widget_1)
        self.record_save_name_box.setAlignment(Qt.AlignRight)
        self.record_save_name_label = QLabel(self.invisible_widget_1)
        self.record_save_button_pc = QPushButton(self.invisible_widget_1)
        self.record_save_button_db = QPushButton(self.invisible_widget_1)
        self.record_save_footnote = QLabel(self.invisible_widget_1)
        self.invisible_widget_1.setGeometry(0, 0, 300, 115)
        if self.dark_theme_activated:
            self.invisible_widget_1.setStyleSheet("background-color: #10131b;")
        else:
            self.invisible_widget_1.setStyleSheet("background-color: rgb(239, 229, 220);")
        self.record_save_name_box.clear()
        self.record_save_frame1 = QFrame(self.invisible_widget_1)
        self.record_save_frame1.setGeometry(10, 8, 280, 91)
        if self.dark_theme_activated:
            self.record_save_frame1.setStyleSheet("border: 1px solid #bfcfb2;"
                                                  "border-radius: 5px;")
        else:
            self.record_save_frame1.setStyleSheet("border: 1px solid rgb(196, 174, 174);"
                                                  "border-radius: 5px;")
        self.record_save_frame1.lower()
        self.record_save_name_box.setGeometry(20, 22, 260, 30)
        if self.dark_theme_activated:
            self.record_save_name_box.setStyleSheet('background-color: #10131b;;'
                                                    'border: 1px solid #bfcfb2;'
                                                    'border-radius: none;'
                                                    'color: #bfcfb2')
        else:
            self.record_save_name_box.setStyleSheet('background-color: rgb(239, 229, 220);'
                                                    'border: 1px solid rgb(196, 177, 174);'
                                                    'border-radius: none;')
        self.record_save_name_box.setFont(self.font)
        self.record_save_name_label.setText('  Name your loop')
        if self.dark_theme_activated:
            self.record_save_name_label.setStyleSheet("color: #bfcfb2;"
                                                      "font-weight: bold")
        else:
            self.record_save_name_label.setStyleSheet("color: black;"
                                                      "font-weight: bold")
        self.record_save_name_label.setGeometry(26, 14, 98, 15)
        self.record_save_name_label.setFont(self.font)
        self.record_save_button_pc.setIcon(QtGui.QIcon("images/CPU"))
        self.record_save_button_pc.setGeometry(30, 60, 115, 30)
        self.record_save_button_pc.setText(" Save to PC")
        self.record_save_button_pc.clicked.connect(self.record_save_settings_pc)
        if self.dark_theme_activated:
            self.record_save_button_pc.setStyleSheet("QPushButton::hover {"
                                                     "border: 1px solid #bfcfb2;"
                                                     "background-color: rgb(196, 177, 174);"
                                                     "color: white;}"
                                                     "QPushButton {"
                                                     "background-color: rgb(249, 249, 245);"
                                                     "border-radius: 3px;"
                                                     "border: 1px solid #bfcfb2;}")
        else:
            self.record_save_button_pc.setStyleSheet("QPushButton::hover {"
                                                     "border: 1px solid rgb(158, 143, 141);"
                                                     "background-color: rgb(196, 177, 174);"
                                                     "color: white;}"
                                                     "QPushButton {"
                                                     "background-color: rgb(249, 249, 245);"
                                                     "border-radius: 3px;"
                                                     "border: 1px solid rgb(158, 143, 141)}")
        self.record_save_button_pc.setFont(self.font)
        self.record_save_button_db.setIcon(QtGui.QIcon("images/app_logo"))
        self.record_save_button_db.setGeometry(160, 60, 115, 30)
        self.record_save_button_db.setText(" Save in App")
        self.record_save_button_db.clicked.connect(self.record_save_settings)
        if self.dark_theme_activated:
            self.record_save_button_db.setStyleSheet("QPushButton::hover {"
                                                     "border: 1px solid #bfcfb2;"
                                                     "background-color: rgb(196, 177, 174);"
                                                     "color: white;}"
                                                     "QPushButton {"
                                                     "background-color: rgb(249, 249, 245);"
                                                     "border-radius: 3px;"
                                                     "border: 1px solid #bfcfb2;}")
        else:
            self.record_save_button_db.setStyleSheet("QPushButton::hover {"
                                                     "border: 1px solid rgb(158, 143, 141);"
                                                     "background-color: rgb(196, 177, 174);"
                                                     "color: white;}"
                                                     "QPushButton {"
                                                     "background-color: rgb(249, 249, 245);"
                                                     "border-radius: 3px;"
                                                     "border: 1px solid rgb(158, 143, 141)}")
        self.record_save_button_db.setFont(self.font)
        self.record_save_footnote.setGeometry(10, 99, 280, 13)
        self.record_save_footnote.setText("")
        self.record_save_footnote.setStyleSheet("color: red;")
        self.record_save_footnote.setFont(self.font)
        self.record_save_window.show()

    # saves the actions list from record screen into app
    def record_save_settings(self):
        if self.i == 1:
            self.foot_note_label.setText('error: no actions available')
            return
        actions_data = []
        save_name = self.record_save_name_box.text()
        if save_name == '':
            self.record_save_footnote.setText('error: name is needed')
            return
        for a in range(self.i - 1):
            csv_list = []
            row_elements = self.line_list[a][1].children()
            if self.line_list[a][0] == 'mouse':
                csv_list.append('mouse')
                for b in (3, 5):
                    if row_elements[b].text() == '':
                        self.foot_note_label.setText('error: x and y location are needed')
                        return
                    else:
                        csv_list.append(row_elements[b].text())
                for b in (7, 9):
                    csv_list.append(row_elements[b].currentText())
                if row_elements[11].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[11].text())
            elif self.line_list[a][0] == 'keyboard':
                csv_list.append('keyboard')
                csv_list.append(row_elements[3].text())
                csv_list.append(row_elements[5].currentText())
                csv_list.append(row_elements[7].currentText())
                if row_elements[9].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[9].text())
            elif self.line_list[a][0] == 'scroll':
                csv_list.append('scroll')
                for b in (3, 5):
                    if row_elements[b].text() == '':
                        self.foot_note_label.setText('error: x and y location are needed')
                        return
                    else:
                        csv_list.append(row_elements[b].text())
                csv_list.append(row_elements[7].currentText())
                csv_list.append(row_elements[9].text())
                if row_elements[11].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[11].text())
            csv_text = ', '.join(csv_list)
            actions_data.append(csv_text)
        full_csv_text = '---'.join(actions_data)
        saved_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
        if self.repeat_for_number_2.text() == '':
            repeat_all = '1'
        else:
            repeat_all = self.repeat_for_number_2.text()
        if self.delay_2.text() == '':
            delay_time = '100'
        else:
            delay_time = self.delay_2.text()
        delay_type = self.delay_time_combobox_record.currentText()
        try:
            functions.add_run_record_db(save_name, full_csv_text, saved_date, repeat_all, delay_time, delay_type)
            self.record_save_window.close()
        except sqlite3.IntegrityError:
            self.record_save_footnote.setText('error: this name exists')
            return

    # saves the actions list from record screen into pc
    def record_save_settings_pc(self):
        if self.i == 1:
            self.foot_note_label.setText('error: no actions available')
            return
        actions_data = []
        save_name = self.record_save_name_box.text()
        if save_name == '':
            self.record_save_footnote.setText('error: name is needed')
            return
        for a in range(self.i - 1):
            csv_list = []
            row_elements = self.line_list[a][1].children()
            if self.line_list[a][0] == 'mouse':
                csv_list.append('mouse')
                for b in (3, 5):
                    if row_elements[b].text() == '':
                        self.foot_note_label.setText('error: x and y location are needed')
                        return
                    else:
                        csv_list.append(row_elements[b].text())
                for b in (7, 9):
                    csv_list.append(row_elements[b].currentText())
                if row_elements[11].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[11].text())
            elif self.line_list[a][0] == 'keyboard':
                csv_list.append('keyboard')
                csv_list.append(row_elements[3].text())
                csv_list.append(row_elements[5].currentText())
                csv_list.append(row_elements[7].currentText())
                if row_elements[9].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[9].text())
            elif self.line_list[a][0] == 'scroll':
                csv_list.append('scroll')
                for b in (3, 5):
                    if row_elements[b].text() == '':
                        self.foot_note_label.setText('error: x and y location are needed')
                        return
                    else:
                        csv_list.append(row_elements[b].text())
                csv_list.append(row_elements[7].currentText())
                csv_list.append(row_elements[9].text())
                if row_elements[11].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[11].text())
            actions_data.append(csv_list)
        if self.repeat_for_number_2.text() == '':
            repeat_all = '1'
        else:
            repeat_all = self.repeat_for_number_2.text()
        if self.delay_2.text() == '':
            delay_time = '100'
        else:
            delay_time = self.delay_2.text()
        delay_type = self.delay_time_combobox_record.currentText()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", f"{save_name}", "CSV Files(*.csv)")
        if file_name:
            f = open(file_name, 'w', newline='')
            writer = csv.writer(f)
            for a in range(self.i - 1):
                writer.writerow(actions_data[a])
            writer.writerow(repeat_all)
            writer.writerow(delay_time)
            writer.writerow(delay_type)
            f.close()
            self.record_save_window.close()

        # triggered by record -> load button (pop-up window)

    def window_load(self):
        self.font.setBold(False)
        self.font.setPixelSize(11)
        self.load_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.load_window.setWindowTitle("Load")
        self.load_window.setWindowIcon(QtGui.QIcon("images/uplode_dark"))
        self.load_window.setGeometry(575, 250, 400, 400)
        self.load_window.setFixedWidth(400)
        self.load_window.setFixedHeight(400)
        self.invisible_widget_2 = QWidget(self.load_window)
        self.load_layout = QGridLayout(self.invisible_widget_2)
        self.load_list = QListWidget(self.invisible_widget_2)
        self.load_from_pc = QPushButton(self.invisible_widget_2)
        self.load_from_list = QPushButton(self.invisible_widget_2)
        self.delete_selected = QPushButton(self.invisible_widget_2)
        self.invisible_widget_2.setGeometry(0, 0, 400, 400)
        if self.dark_theme_activated:
            self.invisible_widget_2.setStyleSheet("background-color: #10131b;")
        else:
            self.invisible_widget_2.setStyleSheet("background-color: rgb(239, 229, 220)")
        self.load_list.setGeometry(10, 10, 380, 340)
        scroll_bar = self.load_list.findChildren(QWidget)[4]
        if self.dark_theme_activated:
            scroll_bar.setStyleSheet("""QScrollBar:vertical {
                                                       border-color: #10131b;
                                                       border-width: 1px;
                                                       border-style: solid;
                                                       border-radius: 10px;
                                                       background-color: #10131b;
                                                       width:18px;
                                                       margin: 10px 4px 10px 0;}
                                                   QScrollBar::handle:vertical {
                                                       background-color: #bfcfb2;
                                                       min-height: 25px;
                                                       border: 1px solid #bfcfb2;
                                                       border-radius: 5px;}
                                                   QScrollBar::add-line:vertical {
                                                       border: 1px solid #10131b;
                                                       background-color: #10131b;
                                                       height: 0px;
                                                       subcontrol-position: bottom;
                                                       subcontrol-origin: margin;}
                                                   QScrollBar::sub-line:vertical {
                                                       border: 1px solid #10131b;
                                                       background-color: #10131b;
                                                       height: 0px;
                                                       subcontrol-position: top;
                                                       subcontrol-origin: margin;}
                                                   QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                                       background: none;}
                                                   QScrollBar::up-arrow:vertical {
                                                     background-color: #10131b;}
                                                   QScrollBar::down-arrow:vertical {
                                                     background-color: #10131b;}""")
        else:
            scroll_bar.setStyleSheet("""QScrollBar:vertical {
                                               border-color: rgb(239, 229, 220);
                                               border-width: 1px;
                                               border-style: solid;
                                               border-radius: 10px;
                                               background: rgb(239, 229, 220);
                                               width:18px;
                                               margin: 10px 4px 10px 0;}
                                           QScrollBar::handle:vertical {
                                               background-color: #c4b1ad;
                                               min-height: 25px;
                                               border: 1px solid #c4b1ad;
                                               border-radius: 5px;}
                                           QScrollBar::add-line:vertical {
                                               border: 1px solid rgb(239, 229, 220);
                                               background-color: rgb(239, 229, 220);
                                               height: 0px;
                                               subcontrol-position: bottom;
                                               subcontrol-origin: margin;}
                                           QScrollBar::sub-line:vertical {
                                               border: 1px solid rgb(239, 229, 220);
                                               background-color: rgb(241, 241, 241);
                                               height: 0px;
                                               subcontrol-position: top;
                                               subcontrol-origin: margin;}
                                           QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                               background: none;}""")
        if self.dark_theme_activated:
            self.load_list.setStyleSheet("QListWidget {"
                                         "border: 1px solid #bfcfb2;"
                                         "border-radius: 5px;"
                                         "color: #bfcfb2;}")
        else:
            self.load_list.setStyleSheet("QListWidget {"
                                         "border: 1px solid rgb(196, 177, 174);"
                                         "border-radius: 5px;}"
                                         "color: black;")
        self.load_list.setFont(self.font)
        self.load_from_pc.setIcon(QtGui.QIcon("images/icons8-monitor-96"))
        self.load_from_pc.setGeometry(10, 360, 120, 30)
        self.load_from_pc.setText(" Load From PC")
        self.load_from_pc.clicked.connect(self.load_selected_from_pc)
        if self.dark_theme_activated:
            self.load_from_pc.setStyleSheet("QPushButton::hover {"
                                            "border: 1px solid #bfcfb2;"
                                            "background-color: rgb(196, 177, 174);"
                                            "color: white;}"
                                            "QPushButton {"
                                            "background-color: rgb(249, 249, 245);"
                                            "border-radius: 5px;"
                                            "border: 1px solid #bfcfb2;}")
        else:
            self.load_from_pc.setStyleSheet("QPushButton::hover {"
                                            "border: 1px solid rgb(196, 177, 174);"
                                            "background-color: rgb(196, 177, 174);"
                                            "color: white;}"
                                            "QPushButton {"
                                            "background-color: rgb(249, 249, 245);"
                                            "border-radius: 5px;"
                                            "border: 1px solid rgb(196, 177, 174);}")
        self.load_from_pc.setFont(self.font)
        self.load_from_list.setIcon(QtGui.QIcon("images/icons8-list-100"))
        self.load_from_list.setGeometry(270, 360, 120, 30)
        self.load_from_list.setText(" Load Selected")
        self.load_from_list.clicked.connect(self.load_selected_from_db)
        if self.dark_theme_activated:
            self.load_from_list.setStyleSheet("QPushButton::hover {"
                                              "border: 1px solid #bfcfb2;"
                                              "background-color: rgb(196, 177, 174);"
                                              "color: white;}"
                                              "QPushButton {"
                                              "background-color: rgb(249, 249, 245);"
                                              "border-radius: 5px;"
                                              "border: 1px solid rgb(196, 177, 174)}")
        else:
            self.load_from_list.setStyleSheet("QPushButton::hover {"
                                              "border: 1px solid rgb(196, 177, 174);"
                                              "background-color: rgb(196, 177, 174);"
                                              "color: white;}"
                                              "QPushButton {"
                                              "background-color: rgb(249, 249, 245);"
                                              "border-radius: 5px;"
                                              "border: 1px solid rgb(196, 177, 174);}")
        self.load_from_list.setFont(self.font)
        self.delete_selected.setIcon(QtGui.QIcon("images/icons8-delete-96"))
        self.delete_selected.setGeometry(140, 360, 120, 30)
        self.delete_selected.setText(" Delete Selected")
        self.delete_selected.clicked.connect(self.delete_from_db)
        if self.dark_theme_activated:
            self.delete_selected.setStyleSheet("QPushButton::hover {"
                                               "border: 1px solid #bfcfb2;"
                                               "background-color: rgb(196, 177, 174);"
                                               "color: white;}"
                                               "QPushButton {"
                                               "background-color: rgb(249, 249, 245);"
                                               "border-radius: 5px;"
                                               "border: 1px solid #bfcfb2;}")
        else:
            self.delete_selected.setStyleSheet("QPushButton::hover {"
                                               "border: 1px solid rgb(196, 177, 174);"
                                               "background-color: rgb(196, 177, 174);"
                                               "color: white;}"
                                               "QPushButton {"
                                               "background-color: rgb(249, 249, 245);"
                                               "border-radius: 5px;"
                                               "border: 1px solid rgb(196, 177, 174);}")
        self.delete_selected.setFont(self.font)
        self.load_list.clear()
        self.update_db_view()
        self.load_list.setCurrentRow(self.j - 1)
        self.load_window.show()

    # updates the database view on load window
    def update_db_view(self):
        self.j = 0
        self.items_list = []
        self.items_from_home = []
        self.items_from_record = []
        conn = sqlite3.connect('autoclicker.db')
        cursor = conn.cursor()
        sql = '''SELECT save_name, saved_date FROM home_run_settings'''
        cursor.execute(sql)
        for item in cursor.fetchall():
            self.items_list.append(str(item[0]) + f' ({str(item[1])})' + ' (saved from home)')
            self.items_from_home.append(item[0])
        sql_2 = '''SELECT save_name, saved_date FROM record_run_settings'''
        cursor.execute(sql_2)
        for item in cursor.fetchall():
            self.items_list.append(str(item[0]) + f' ({str(item[1])})' + ' (saved from record)')
            self.items_from_record.append(item[0])
        conn.close()
        for item in self.items_list:
            list_item = QListWidgetItem(item)
            list_item.setTextAlignment(Qt.AlignHCenter)
            self.load_list.addItem(list_item)
            self.j += 1

    # function to read a CSV without using pandas
    def read_csv(self, csv_file):
        data = []
        with open(csv_file, 'r') as f:

            # create a list of rows in the CSV file
            rows = f.readlines()

            # strip white-space and newlines
            rows = list(map(lambda x:x.strip(), rows))

            for row in rows:

                # further split each row into columns assuming delimiter is comma
                row = row.split(',')

                # append to data-frame our new row-object with columns
                data.append(row)

        return data

    # loads selected action from pc (csv files)
    def load_selected_from_pc(self):
        fetched_data_home = []
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "CSV Files(*.csv)")
        # print(type(file_name))
        if file_name:
            # f = pd.read_csv(file_name, header=None)
            f = self.read_csv(file_name)
            # print(f)

        else:
            return
        try:
            for i in range(12):
                # fetched_data_home.append(f[i][0])
                fetched_data_home.append(f[0][i]) # taking the first row of csv file
            # print(fetched_data_home)
            # print(",,,,,,,,,,,,,,,,,,")
            self.load_window.close()
            self.get_home_screen()
            delay_type = fetched_data_home[9]
            self.mouse_button_combobox.setCurrentText(fetched_data_home[0])
            self.click_type_combobox.setCurrentText(fetched_data_home[1])
            if fetched_data_home[2] == 'range':
                self.range_radio_button.setChecked(True)
                self.delay_time_combobox_2.setCurrentText(str(delay_type))
                range_min = fetched_data_home[7]
                range_max = fetched_data_home[8]
                self.range_min.setText(str(range_min))
                self.range_max.setText(str(range_max))
                self.delay_time_entrybox.setText('')
            else:
                self.repeat_radio_button.setChecked(True)
                self.delay_time_combobox.setCurrentText(str(delay_type))
                self.delay_time_entrybox.setText(str(fetched_data_home[7]))
                self.range_min.setText('')
                self.range_max.setText('')
            if fetched_data_home[3] == -1:
                self.never_stop_combobox.setCurrentText('Yes')
                self.repeat_for_number.setText('')
            else:
                self.never_stop_combobox.setCurrentText('No')
                self.repeat_for_number.setText(str(fetched_data_home[3]))
            if fetched_data_home[4] == 'fixed':
                self.fixed_location_radio_button.setChecked(True)
                self.fixed_location_x.setText(str(fetched_data_home[5]))
                self.fixed_location_y.setText(str(fetched_data_home[6]))
                self.select_area_x.setText('')
                self.select_area_y.setText('')
                self.select_area_width.setText('')
                self.select_area_height.setText('')
            elif fetched_data_home[4] == 'current':
                self.current_location_radio_button.setChecked(True)
                self.fixed_location_x.setText('')
                self.fixed_location_y.setText('')
                self.select_area_x.setText('')
                self.select_area_y.setText('')
                self.select_area_width.setText('')
                self.select_area_height.setText('')
            else:
                self.select_area_radio_button.setChecked(True)
                self.select_area_x.setText(str(fetched_data_home[5]))
                self.select_area_y.setText(str(fetched_data_home[6]))
                self.select_area_width.setText(str(fetched_data_home[10]))
                self.select_area_height.setText(str(fetched_data_home[11]))
                self.fixed_location_x.setText('')
                self.fixed_location_y.setText('')
        except KeyError:
            row_count = len(f)
            self.load_window.close()
            self.remove_all_lines()
            for a in range(row_count - 3):
                if f[a][0] == 'mouse':
                    self.add_mouse_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(str(int(f[a][1])))
                    row_elements[5].setText(str(int(f[a][2])))
                    row_elements[7].setCurrentText(f[a][3])
                    row_elements[9].setCurrentText(f[a][4])
                    row_elements[11].setText(str(int(f[a][5])))
                if f[a][0] == 'scroll':
                    self.add_scroll_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(str(int(f[a][1])))
                    row_elements[5].setText(str(int(f[a][2])))
                    row_elements[7].setCurrentText(f[a][3])
                    row_elements[9].setText(f[a][4])
                    row_elements[11].setText(str(int(f[a][5])))
                if f[a][0] == 'keyboard':
                    self.add_keyboard_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(str(f[a][1]))
                    row_elements[5].setCurrentText(str(f[a][2]))
                    row_elements[7].setCurrentText(f[a][3])
                    row_elements[9].setText(str(f[a][4]))
            self.repeat_for_number_2.setText(f[row_count - 3][0])
            self.delay_2.setText(f[row_count - 2][0])
            self.delay_time_combobox_record.setCurrentText(f[row_count - 1][0])

    # deletes selected action from database
    def delete_from_db(self):
        try:
            selected_item = self.load_list.currentItem().text()
        except AttributeError:
            return
        item_key = selected_item[-5:]
        conn = sqlite3.connect('autoclicker.db')
        cursor = conn.cursor()
        if item_key == 'home)':
            index = selected_item.find(" (saved from home)")
            selected_save_name = selected_item[:index][0:-19]
            sql = f"DELETE FROM home_run_settings WHERE save_name = '{selected_save_name}'"
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.load_list.clear()
            self.update_db_view()
        else:
            index = selected_item.find(" (saved from record)")
            selected_save_name = selected_item[:index][0:-19]
            sql = f"DELETE FROM record_run_settings WHERE save_name = '{selected_save_name}'"
            cursor.execute(sql)
            conn.commit()
            conn.close()
            self.load_list.clear()
            self.update_db_view()

    # loads selected action from database
    def load_selected_from_db(self):
        try:
            selected_item = self.load_list.currentItem().text()
        except AttributeError:
            return
        item_key = selected_item[-5:]
        conn = sqlite3.connect('autoclicker.db')
        cursor = conn.cursor()
        if item_key == 'home)':
            index = selected_item.find(" (saved from home)")
            selected_save_name = selected_item[:index][0:-19]
            sql = f"SELECT * FROM home_run_settings WHERE save_name = '{selected_save_name}'"
            cursor.execute(sql)
            fetched_data = cursor.fetchall()[0]
            conn.close()
            self.load_window.close()
            self.get_home_screen()
            delay_type = fetched_data[10]
            self.mouse_button_combobox.setCurrentText(fetched_data[1])
            self.click_type_combobox.setCurrentText(fetched_data[2])
            if fetched_data[3] == 'range':
                self.range_radio_button.setChecked(True)
                self.delay_time_combobox_2.setCurrentText(str(delay_type))
                range_min = fetched_data[8]
                range_max = fetched_data[9]
                self.range_min.setText(str(range_min))
                self.range_max.setText(str(range_max))
                self.delay_time_entrybox.setText('')
            else:
                self.repeat_radio_button.setChecked(True)
                self.delay_time_combobox.setCurrentText(str(delay_type))
                self.delay_time_entrybox.setText(str(fetched_data[8]))
                self.range_min.setText('')
                self.range_max.setText('')
            if fetched_data[4] == -1:
                self.never_stop_combobox.setCurrentText('Yes')
                self.repeat_for_number.setText('')
            else:
                self.never_stop_combobox.setCurrentText('No')
                self.repeat_for_number.setText(str(fetched_data[4]))
            if fetched_data[5] == 'fixed':
                self.fixed_location_radio_button.setChecked(True)
                self.fixed_location_x.setText(str(fetched_data[6]))
                self.fixed_location_y.setText(str(fetched_data[7]))
                self.select_area_x.setText('')
                self.select_area_y.setText('')
                self.select_area_width.setText('')
                self.select_area_height.setText('')
            elif fetched_data[5] == 'current':
                self.current_location_radio_button.setChecked(True)
                self.fixed_location_x.setText('')
                self.fixed_location_y.setText('')
                self.select_area_x.setText('')
                self.select_area_y.setText('')
                self.select_area_width.setText('')
                self.select_area_height.setText('')
            else:
                self.select_area_radio_button.setChecked(True)
                self.select_area_x.setText(str(fetched_data[6]))
                self.select_area_y.setText(str(fetched_data[7]))
                self.select_area_width.setText(str(fetched_data[11]))
                self.select_area_height.setText(str(fetched_data[12]))
                self.fixed_location_x.setText('')
                self.fixed_location_y.setText('')
        else:
            index = selected_item.find(" (saved from record)")
            selected_save_name = selected_item[:index][0:-19]
            sql = f"SELECT * FROM record_run_settings WHERE save_name = '{selected_save_name}'"
            cursor.execute(sql)
            fetched_text = cursor.fetchall()[0]
            fetched_data = fetched_text[1].split('---')
            repeat_all = fetched_text[3]
            delay_time = fetched_text[4]
            delay_type = fetched_text[5]
            conn.close()
            self.load_window.close()
            row_count = len(fetched_data)
            self.remove_all_lines()
            for a in range(row_count):
                row_list = fetched_data[a].split(', ')
                if row_list[0] == 'mouse':
                    self.add_mouse_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(row_list[1])
                    row_elements[5].setText(row_list[2])
                    row_elements[7].setCurrentText(row_list[3])
                    row_elements[9].setCurrentText(row_list[4])
                    row_elements[11].setText(row_list[5])
                elif row_list[0] == 'keyboard':
                    self.add_keyboard_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(row_list[1])
                    row_elements[5].setCurrentText(row_list[2])
                    row_elements[7].setCurrentText(row_list[3])
                    row_elements[9].setText(row_list[4])
                elif row_list[0] == 'scroll':
                    self.add_scroll_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(row_list[1])
                    row_elements[5].setText(row_list[2])
                    row_elements[7].setCurrentText(row_list[3])
                    row_elements[9].setText(row_list[4])
                    row_elements[11].setText(row_list[5])
            self.repeat_for_number_2.setText(str(repeat_all))
            self.delay_2.setText(str(delay_time))
            self.delay_time_combobox_record.setCurrentText(str(delay_type))

    # adds new line according to what's chosen
    def add_new_line(self):
        record_text = self.record_add_items.currentText()
        if record_text == " Mouse":
            self.add_mouse_line()
        elif record_text == " Keyboard":
            self.add_keyboard_line()
        elif record_text == " Scroll":
            self.add_scroll_line()

    # adds new mouse line to the record screen
    def add_mouse_line(self):
        record_line_frame = QFrame(self)
        line_layout = QHBoxLayout(record_line_frame)
        line_layout.setContentsMargins(5, 0, 0, 0)
        line_layout.setSpacing(5)
        record_line_frame.setFixedSize(500, 30)
        record_line_frame.setStyleSheet('QFrame {border-bottom: 1.5px solid;'
                                        'border-radius: none;'
                                        'border-color: #c8bab7}')
        column_1 = QLabel(record_line_frame)
        column_1.setStyleSheet('border: none;'
                               'color: #3a5b41;')
        column_1.setText(str(self.i))
        column_1.setFixedSize(20, 10)
        column_2 = QLabel(record_line_frame)
        column_2.setStyleSheet('border: none;')
        column_2.setText('X:')
        column_2.setFixedSize(10, 20)
        column_3 = QLineEdit(record_line_frame)
        column_3.setFixedSize(40, 20)
        column_3.setStyleSheet('background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218)')
        column_4 = QLabel(record_line_frame)
        column_4.setStyleSheet('border: none;')
        column_4.setText('Y:')
        column_4.setFixedSize(10, 20)
        column_5 = QLineEdit(record_line_frame)
        column_5.setFixedSize(40, 20)
        column_5.setStyleSheet('background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218)')
        column_6 = QLabel(record_line_frame)
        column_6.setStyleSheet('border: none;')
        column_6.setText(' Type:')
        column_6.setFixedSize(30, 20)
        column_7 = QComboBox(record_line_frame)
        column_7.addItem("Left")
        column_7.addItem("Middle")
        column_7.addItem("Right")
        column_7.setFixedSize(55, 20)
        column_7.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218);'
                               'padding-left: 2px;}'
                               'QComboBox::drop-down {'
                               'border: 1px;'
                               'border-radius: 2px;'
                               'border-color: rgb(218, 218, 218);}'
                               'QComboBox::down-arrow {'
                               'image: url(images/arrow1.png);'
                               'width: 8px;'
                               'height: 8px;}')
        column_8 = QLabel(record_line_frame)
        column_8.setStyleSheet('border: none;')
        column_8.setText(' Action: ')
        column_8.setFixedSize(40, 20)
        column_9 = QComboBox(record_line_frame)
        column_9.addItem("Press")
        column_9.addItem("Release")
        column_9.setFixedSize(65, 20)
        column_9.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218);'
                               'padding-left: 2px;}'
                               'QComboBox::drop-down {'
                               'background-color: rgb(249, 249, 245);'
                               'border: 1px;'
                               'border-radius: 2px;'
                               'border-color: rgb(218, 218, 218);}'
                               'QComboBox::down-arrow {'
                               'image: url(images/arrow1.png);'
                               'width: 8px;'
                               'height: 8px;}')
        column_10 = QLabel(record_line_frame)
        column_10.setStyleSheet('border: none;')
        column_10.setText(' Delay:')
        column_10.setFixedSize(40, 20)
        column_11 = QLineEdit(record_line_frame)
        column_11.setPlaceholderText("    ms")
        column_11.setFixedSize(45, 20)
        column_11.setStyleSheet('background-color: rgb(249, 249, 245);'
                                'border: 1px solid;'
                                'border-radius: 3px;'
                                'border-color: rgb(218, 218, 218)')
        column_12 = QPushButton(record_line_frame)
        column_12.setIcon(QtGui.QIcon("images/Red-Minus-PNG-File"))
        column_12.setFixedSize(25, 20)
        if self.dark_theme_activated:
            column_12.setStyleSheet("QPushButton {"
                                    "background-color: #10131b;"
                                    "border-radius: 3px;"
                                    "border: 1px solid;"
                                    "border-color: #10131b;}")
        else:
            column_12.setStyleSheet("QPushButton {"
                                    "background-color: rgb(239, 229, 220);"
                                    "border-radius: 3px;"
                                    "border: 1px solid;"
                                    "border-color: rgb(239, 229, 220);}")
        column_12.clicked.connect(self.remove_line)
        for widget in record_line_frame.findChildren(QLineEdit):
            widget.setValidator(self.integer)
        line_layout.addWidget(column_1)
        line_layout.addWidget(column_2)
        line_layout.addWidget(column_3)
        line_layout.addWidget(column_4)
        line_layout.addWidget(column_5)
        line_layout.addWidget(column_6)
        line_layout.addWidget(column_7)
        line_layout.addWidget(column_8)
        line_layout.addWidget(column_9)
        line_layout.addWidget(column_10)
        line_layout.addWidget(column_11)
        line_layout.addWidget(column_12)
        self.form_layout.addWidget(record_line_frame)
        self.line_list.append(['mouse', record_line_frame])
        self.i += 1
        self.repeat_for_label_2.show()
        self.repeat_for_number_2.show()
        self.delay_label_2.show()
        self.delay_2.show()
        self.delay_time_combobox_record.show()
        self.record_remove_all_button.setEnabled(True)
        self.font.setBold(False)
        self.font.setPixelSize(11)
        for item in record_line_frame.findChildren(QLabel):
            item.setFont(self.font)
        for item in record_line_frame.findChildren(QComboBox):
            item.setFont(self.font)
        for item in record_line_frame.findChildren(QLineEdit):
            item.setFont(self.font)

    # adds new keyboard line to the record screen
    def add_keyboard_line(self):
        record_line_frame = QFrame(self)
        record_line_frame.setStyleSheet('QFrame {border-bottom: 1.5px solid;'
                                        'border-radius: none;'
                                        'border-color: #c8bab7}')
        record_line_frame.setFixedSize(500, 30)
        line_layout = QHBoxLayout(record_line_frame)
        line_layout.setContentsMargins(5, 0, 0, 0)
        line_layout.setSpacing(5)
        column_1 = QLabel(record_line_frame)
        column_1.setStyleSheet('border: none;'
                               'color: #3a5b41;')
        column_1.setText(str(self.i))
        column_1.setFixedSize(20, 10)
        column_2 = QLabel(record_line_frame)
        column_2.setStyleSheet('border: none;')
        column_2.setText('Input:')
        column_2.setFixedSize(35, 20)
        column_3 = QLineEdit(record_line_frame)
        column_3.setFixedSize(77, 20)
        column_3.setStyleSheet('background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218)')
        column_4 = QLabel(record_line_frame)
        column_4.setStyleSheet('border: none;')
        column_4.setText(' Type:')
        column_4.setFixedSize(30, 20)
        column_5 = QComboBox(record_line_frame)
        column_5.addItem("Char")
        column_5.addItem("Key")
        column_5.setFixedSize(55, 20)
        column_5.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218);'
                               'padding-left: 2px;}'
                               'QComboBox::drop-down {'
                               'border: 1px;'
                               'border-radius: 2px;'
                               'border-color: rgb(218, 218, 218);}'
                               'QComboBox::down-arrow {'
                               'image: url(images/arrow1.png);'
                               'width: 8px;'
                               'height: 8px;}')
        column_6 = QLabel(record_line_frame)
        column_6.setStyleSheet('border: none;')
        column_6.setText(' Action: ')
        column_6.setFixedSize(40, 20)
        column_7 = QComboBox(record_line_frame)
        column_7.addItem("Press")
        column_7.addItem("Release")
        column_7.setFixedSize(65, 20)
        column_7.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218);'
                               'padding-left: 2px;}'
                               'QComboBox::drop-down {'
                               'border: 1px;'
                               'border-radius: 2px;'
                               'border-color: rgb(218, 218, 218);}'
                               'QComboBox::down-arrow {'
                               'image: url(images/arrow1.png);'
                               'width: 8px;'
                               'height: 8px;}')
        column_8 = QLabel(record_line_frame)
        column_8.setStyleSheet('border: none;')
        column_8.setText(' Delay:')
        column_8.setFixedSize(40, 20)
        column_9 = QLineEdit(record_line_frame)
        column_9.setPlaceholderText("    ms")
        column_9.setValidator(self.integer)
        column_9.setFixedSize(45, 20)
        column_9.setStyleSheet('background-color: rgb(249, 249, 245);'
                                'border: 1px solid;'
                                'border-radius: 3px;'
                                'border-color: rgb(218, 218, 218)')
        column_10 = QPushButton(record_line_frame)
        column_10.setIcon(QtGui.QIcon("images/Red-Minus-PNG-File"))
        column_10.setFixedSize(25, 20)
        if self.dark_theme_activated:
            column_10.setStyleSheet("QPushButton {"
                                    "background-color: #10131b;"
                                    "border-radius: 3px;"
                                    "border: 1px solid;"
                                    "border-color: #10131b;}")
        else:
            column_10.setStyleSheet("QPushButton {"
                                    "background-color: rgb(239, 229, 220);"
                                    "border-radius: 3px;"
                                    "border: 1px solid;"
                                    "border-color: rgb(239, 229, 220);}")
        column_10.clicked.connect(self.remove_line)
        line_layout.addWidget(column_1)
        line_layout.addWidget(column_2)
        line_layout.addWidget(column_3)
        line_layout.addWidget(column_4)
        line_layout.addWidget(column_5)
        line_layout.addWidget(column_6)
        line_layout.addWidget(column_7)
        line_layout.addWidget(column_8)
        line_layout.addWidget(column_9)
        line_layout.addWidget(column_10)
        self.form_layout.addWidget(record_line_frame)
        self.line_list.append(['keyboard', record_line_frame])
        self.i += 1
        self.repeat_for_label_2.show()
        self.repeat_for_number_2.show()
        self.delay_label_2.show()
        self.delay_2.show()
        self.delay_time_combobox_record.show()
        self.record_remove_all_button.setEnabled(True)
        self.font.setBold(False)
        self.font.setPixelSize(11)
        for item in record_line_frame.findChildren(QLabel):
            item.setFont(self.font)
        for item in record_line_frame.findChildren(QComboBox):
            item.setFont(self.font)
        for item in record_line_frame.findChildren(QLineEdit):
            item.setFont(self.font)

    # adds new scroll line to the record screen
    def add_scroll_line(self):
        record_line_frame = QFrame(self)
        record_line_frame.setStyleSheet('QFrame {border-bottom: 1.5px solid;'
                                        'border-radius: none;'
                                        'border-color: #c8bab7;}')
        record_line_frame.setFixedSize(500, 30)
        line_layout = QHBoxLayout(record_line_frame)
        line_layout.setContentsMargins(5, 0, 0, 0)
        line_layout.setSpacing(5)
        column_1 = QLabel(record_line_frame)
        column_1.setStyleSheet('border: none;'
                               'color: #3a5b41;')
        column_1.setText(str(self.i))
        column_1.setFixedSize(20, 10)
        column_2 = QLabel(record_line_frame)
        column_2.setStyleSheet('border: none;')
        column_2.setText('X:')
        column_2.setFixedSize(10, 20)
        column_3 = QLineEdit(record_line_frame)
        column_3.setFixedSize(40, 20)
        column_3.setStyleSheet('background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218)')
        column_4 = QLabel(record_line_frame)
        column_4.setStyleSheet('border: none;')
        column_4.setText('Y:')
        column_4.setFixedSize(10, 20)
        column_5 = QLineEdit(record_line_frame)
        column_5.setFixedSize(40, 20)
        column_5.setStyleSheet('background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218)')
        column_6 = QLabel(record_line_frame)
        column_6.setStyleSheet('border: none;')
        column_6.setText(' Type:')
        column_6.setFixedSize(30, 20)
        column_7 = QComboBox(record_line_frame)
        column_7.addItem("Up")
        column_7.addItem("Down")
        column_7.setFixedSize(55, 20)
        column_7.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218);'
                               'padding-left: 2px;}'
                               'QComboBox::drop-down {'
                               'border: 1px;'
                               'border-radius: 2px;'
                               'border-color: rgb(218, 218, 218);}'
                               'QComboBox::down-arrow {'
                               'image: url(images/arrow1.png);'
                               'width: 8px;'
                               'height: 8px;}')
        column_8 = QLabel(record_line_frame)
        column_8.setStyleSheet('border: none;')
        column_8.setText(' Repeat:')
        column_8.setFixedSize(40, 20)
        column_9 = QLineEdit(record_line_frame)
        column_9.setFixedSize(65, 20)
        column_9.setStyleSheet('background-color: rgb(249, 249, 245);'
                               'border: 1px solid;'
                               'border-radius: 3px;'
                               'border-color: rgb(218, 218, 218)')
        column_10 = QLabel(record_line_frame)
        column_10.setStyleSheet('border: none;')
        column_10.setText(' Delay:')
        column_10.setFixedSize(40, 20)
        column_11 = QLineEdit(record_line_frame)
        column_11.setPlaceholderText("    ms")
        column_11.setFixedSize(45, 20)
        column_11.setStyleSheet('background-color: rgb(249, 249, 245);'
                                'border: 1px solid;'
                                'border-radius: 3px;'
                                'border-color: rgb(218, 218, 218)')
        column_12 = QPushButton(record_line_frame)
        column_12.setIcon(QtGui.QIcon("images/Red-Minus-PNG-File"))
        column_12.setFixedSize(25, 20)
        if self.dark_theme_activated:
            column_12.setStyleSheet("QPushButton {"
                                    "background-color: #10131b;"
                                    "border-radius: 3px;"
                                    "border: 1px solid;"
                                    "border-color: #10131b;}")
        else:
            column_12.setStyleSheet("QPushButton {"
                                    "background-color: rgb(239, 229, 220);"
                                    "border-radius: 3px;"
                                    "border: 1px solid;"
                                    "border-color: rgb(239, 229, 220);}")
        column_12.clicked.connect(self.remove_line)
        for widget in record_line_frame.findChildren(QLineEdit):
            widget.setValidator(self.integer)
        line_layout.addWidget(column_1)
        line_layout.addWidget(column_2)
        line_layout.addWidget(column_3)
        line_layout.addWidget(column_4)
        line_layout.addWidget(column_5)
        line_layout.addWidget(column_6)
        line_layout.addWidget(column_7)
        line_layout.addWidget(column_8)
        line_layout.addWidget(column_9)
        line_layout.addWidget(column_10)
        line_layout.addWidget(column_11)
        line_layout.addWidget(column_12)
        self.form_layout.addWidget(record_line_frame)
        self.line_list.append(['scroll', record_line_frame])
        self.i += 1
        self.repeat_for_label_2.show()
        self.repeat_for_number_2.show()
        self.delay_label_2.show()
        self.delay_2.show()
        self.delay_time_combobox_record.show()
        self.record_remove_all_button.setEnabled(True)
        self.font.setBold(False)
        self.font.setPixelSize(11)
        for item in record_line_frame.findChildren(QLabel):
            item.setFont(self.font)
        for item in record_line_frame.findChildren(QComboBox):
            item.setFont(self.font)
        for item in record_line_frame.findChildren(QLineEdit):
            item.setFont(self.font)

    # removes new line from the record screen
    def remove_line(self):
        sender = self.sender()
        parent = sender.parentWidget()
        row = int(parent.findChild(QLabel).text())
        self.form_layout.removeRow(row - 1)
        del self.line_list[row - 1]
        self.i -= 1
        for i in range(row - 1, self.i - 1):
            column_1s = self.line_list[i][1].findChild(QLabel)
            column_1s.setText(str(i + 1))
        if self.i == 1:
            self.repeat_for_label_2.hide()
            self.repeat_for_number_2.hide()
            self.repeat_for_number_2.setText("1")
            self.delay_label_2.hide()
            self.delay_2.hide()
            self.delay_time_combobox_record.hide()
            self.delay_2.setText("100")
            self.record_remove_all_button.setEnabled(False)

    # removes all lines from the record screen
    def remove_all_lines(self):
        while self.i > 1:
            self.form_layout.removeRow(self.i - 2)
            del self.line_list[-1]
            self.i -= 1
        self.record_remove_all_button.setEnabled(False)
        self.repeat_for_label_2.hide()
        self.repeat_for_number_2.hide()
        self.repeat_for_number_2.setText("1")
        self.delay_label_2.hide()
        self.delay_2.hide()
        self.delay_time_combobox_record.hide()
        self.delay_2.setText("100")

    # checking if repeat value is "yes" or "no" whenever combobox is changed
    def check_repeat_style(self):
        if self.never_stop_combobox.currentText() == 'Yes':
            self.repeat_for_number.setDisabled(True)
            self.repeat_for_number.setStyleSheet('background-color: rgb(225, 225, 225);'
                                                 'border: 1px solid;'
                                                 'border-color: rgb(218, 218, 218);'
                                                 'border-radius: 3px;')
        else:
            self.repeat_for_number.setDisabled(False)
            self.repeat_for_number.setStyleSheet('background-color: rgb(249, 249, 245);'
                                                 'border: 1px solid;'
                                                 'border-color: rgb(218, 218, 218);'
                                                 'border-radius: 3px;')

    # triggers check tray checkbox
    def trigger_tray_checkbox(self):
        if self.hide_to_tray_checkbox.isChecked():
            self.hide_to_tray_checkbox.setChecked(False)
            if self.dark_theme_activated:
                self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
                self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                          "background-color: #10131b")
            else:
                self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
                self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                          "background-color: rgb(239, 229, 220)")
        else:
            self.hide_to_tray_checkbox.setChecked(True)
            if self.dark_theme_activated:
                self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/check_icon_dark"))
                self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                          "background-color: #10131b")
            else:
                self.hide_to_tray_checkbox2.setIcon(QtGui.QIcon("images/check_icon"))
                self.hide_to_tray_checkbox2.setStyleSheet("border: none;"
                                                          "background-color: rgb(239, 229, 220)")
        self.check_tray_checkbox()

    # checking whether hide to tray checkbox is checked whenever checkbox is clicked
    def check_tray_checkbox(self):
        if self.hide_to_tray_checkbox.isChecked():
            app.setQuitOnLastWindowClosed(False)
        else:
            app.setQuitOnLastWindowClosed(True)

    # gets the current mouse location and writes inside app (triggered by hotkey)
    def get_mouse_location(self):
        for item in self.home_frame.findChildren(QLineEdit):
            item.clearFocus()
        mouse_location = mouse.get_position()
        x = mouse_location[0]
        y = mouse_location[1]
        if not self.home_frame.isHidden():
            self.fixed_location_x.setText(str(x))
            self.fixed_location_y.setText(str(y))

    # triggers live mouse checkbox
    def trigger_live_mouse(self):
        if self.mouse_location_checkbox.isChecked():
            self.mouse_location_checkbox.setChecked(False)
            if self.dark_theme_activated:
                self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox_dark"))
                self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                            "background-color: #10131b;")
            else:
                self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/empty_checkbox"))
                self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                            "background-color: rgb(239, 229, 220);")
        else:
            self.mouse_location_checkbox.setChecked(True)
            if self.dark_theme_activated:
                self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/check_icon_dark"))
                self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                            "background-color: #10131b;")
            else:
                self.mouse_location_checkbox2.setIcon(QtGui.QIcon("images/check_icon"))
                self.mouse_location_checkbox2.setStyleSheet("border: none;"
                                                            "background-color: rgb(239, 229, 220);")
        self.check_live_mouse()

    # starts the thread for writing live cursor position
    def check_live_mouse(self):
        live_mouse_thread = threading.Thread(target=self.get_live_mouse)
        live_mouse_thread.setDaemon(True)
        live_mouse_thread.start()

    # constantly writes the live cursor position to the screen
    def get_live_mouse(self):
        while 1:
            if self.mouse_location_checkbox.isChecked():
                self.live_mouse_label.setText('')
                break
            mouse_location = mouse.get_position()
            self.live_mouse_label.setText(f"X: {mouse_location[0]}, Y: {mouse_location[1]}")
            sleep(0.05)

    # resets the actions in home screen
    def home_reset_settings(self):
        self.mouse_button_combobox.setCurrentText('Left')
        self.click_type_combobox.setCurrentText('Single')
        self.never_stop_combobox.setCurrentText('No')
        self.repeat_for_number.setText('1')
        self.delay_time_entrybox.setText('100')
        self.delay_time_combobox.setCurrentText('ms')
        self.repeat_radio_button.setChecked(True)
        self.current_location_radio_button.setChecked(True)
        self.range_min.setText('')
        self.range_max.setText('')
        self.select_area_x.setText('')
        self.select_area_y.setText('')
        self.select_area_width.setText('')
        self.select_area_height.setText('')
        self.fixed_location_x.setText('')
        self.fixed_location_y.setText('')

    # triggered by home -> save button (pop-up window)
    def window_home_save(self):
        self.font.setBold(False)
        self.font.setPixelSize(11)
        self.home_save_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.home_save_window.setWindowTitle("Save")
        self.home_save_window.setWindowIcon(QtGui.QIcon('images/icons8-save-90'))
        self.home_save_window.setGeometry(827, 520, 300, 115)
        self.home_save_window.setFixedWidth(300)
        self.home_save_window.setFixedHeight(115)
        self.invisible_widget_3 = QWidget(self.home_save_window)
        self.home_save_layout = QGridLayout(self.invisible_widget_3)
        self.save_name_box = QLineEdit(self.invisible_widget_3)
        self.save_name_box.setAlignment(Qt.AlignRight)
        self.save_name_label = QLabel(self.invisible_widget_3)
        self.home_save_button_pc = QPushButton(self.invisible_widget_3)
        self.home_save_button_db = QPushButton(self.invisible_widget_3)
        self.home_save_footnote = QLabel(self.invisible_widget_3)
        if self.dark_theme_activated:
            self.invisible_widget_3.setStyleSheet("background-color: #10131b")
        else:
            self.invisible_widget_3.setStyleSheet("background-color: rgb(239, 229, 220)")
        self.invisible_widget_3.setGeometry(0, 0, 300, 115)
        self.save_name_box.clear()
        self.home_save_frame1 = QFrame(self.invisible_widget_3)
        self.home_save_frame1.setGeometry(10, 8, 280, 91)
        if self.dark_theme_activated:
            self.home_save_frame1.setStyleSheet("border: 1px solid #bfcfb2;"
                                                "border-radius: 5px;")
        else:
            self.home_save_frame1.setStyleSheet("border: 1px solid rgb(196, 174, 174);"
                                                "border-radius: 5px;")
        self.home_save_frame1.lower()
        self.save_name_box.setGeometry(20, 22, 260, 30)
        if self.dark_theme_activated:
            self.save_name_box.setStyleSheet('background-color: #10131b;;'
                                             'border: 1px solid #bfcfb2;'
                                             'border-radius: none;'
                                             'color: #bfcfb2')
        else:
            self.save_name_box.setStyleSheet('background-color: rgb(239, 229, 220);'
                                             'border: 1px solid rgb(196, 177, 174);'
                                             'border-radius: none;')
        self.save_name_box.setFont(self.font)
        self.save_name_label.setText('  Name your loop')
        if self.dark_theme_activated:
            self.save_name_label.setStyleSheet("color: #bfcfb2;"
                                               "font-weight: bold")
        else:
            self.save_name_label.setStyleSheet("color: black;"
                                               "font-weight: bold")
        self.save_name_label.setGeometry(26, 14, 98, 15)
        self.save_name_label.setFont(self.font)
        self.home_save_button_pc.setIcon(QtGui.QIcon("images/CPU"))
        self.home_save_button_pc.setGeometry(30, 60, 115, 30)
        self.home_save_button_pc.setText(" Save to PC")
        self.home_save_button_pc.clicked.connect(self.home_save_settings_pc)
        if self.dark_theme_activated:
            self.home_save_button_pc.setStyleSheet("QPushButton::hover {"
                                                   "border: 1px solid #bfcfb2;"
                                                   "background-color: rgb(196, 177, 174);"
                                                   "color: white;}"
                                                   "QPushButton {"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border-radius: 3px;"
                                                   "border: 1px solid #bfcfb2;}")
        else:
            self.home_save_button_pc.setStyleSheet("QPushButton::hover {"
                                                   "border: 1px solid rgb(158, 143, 141);"
                                                   "background-color: rgb(196, 177, 174);"
                                                   "color: white;}"
                                                   "QPushButton {"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border-radius: 3px;"
                                                   "border: 1px solid rgb(158, 143, 141)}")
        self.home_save_button_pc.setFont(self.font)
        self.home_save_button_db.setIcon(QtGui.QIcon("images/app_logo"))
        self.home_save_button_db.setGeometry(160, 60, 115, 30)
        self.home_save_button_db.setText(" Save in App")
        self.home_save_button_db.clicked.connect(self.home_save_settings)
        if self.dark_theme_activated:
            self.home_save_button_db.setStyleSheet("QPushButton::hover {"
                                                   "border: 1px solid #bfcfb2;"
                                                   "background-color: rgb(196, 177, 174);"
                                                   "color: white;}"
                                                   "QPushButton {"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border-radius: 3px;"
                                                   "border: 1px solid #bfcfb2;}")
        else:
            self.home_save_button_db.setStyleSheet("QPushButton::hover {"
                                                   "border: 1px solid rgb(158, 143, 141);"
                                                   "background-color: rgb(196, 177, 174);"
                                                   "color: white;}"
                                                   "QPushButton {"
                                                   "background-color: rgb(249, 249, 245);"
                                                   "border-radius: 3px;"
                                                   "border: 1px solid rgb(158, 143, 141)}")
        self.home_save_button_db.setFont(self.font)
        self.home_save_footnote.setGeometry(10, 99, 280, 13)
        self.home_save_footnote.setText("")
        if self.dark_theme_activated:
            self.home_save_footnote.setStyleSheet("color: red;")
        else:
            self.home_save_footnote.setStyleSheet("color: red;")
        self.home_save_footnote.setFont(self.font)
        self.home_save_window.show()

    # saves the actions from home screen into app
    def home_save_settings(self):
        save_name = self.save_name_box.text()
        if save_name == '':
            self.home_save_footnote.setText('error: name is needed')
            return
        mouse_type = str(self.mouse_button_combobox.currentText())
        click_type = str(self.click_type_combobox.currentText())
        if self.repeat_radio_button.isChecked():
            repeat_or_range = 'repeat'
        else:
            repeat_or_range = 'range'
        if str(self.never_stop_combobox.currentText()) == 'Yes':
            click_repeat = -1
        else:
            try:
                click_repeat = int(self.repeat_for_number.text())
            except ValueError:
                self.home_save_footnote.setText('error: number of repeat is needed to save')
                return
        if self.select_area_radio_button.isChecked():
            select_or_fixed = 'select'
        elif self.current_location_radio_button.isChecked():
            select_or_fixed = 'current'
        else:
            select_or_fixed = 'fixed'
        try:
            if self.select_area_radio_button.isChecked():
                location_x = int(self.select_area_x.text())
                location_y = int(self.select_area_y.text())
                area_width = int(self.select_area_width.text())
                area_height = int(self.select_area_height.text())
            elif self.current_location_radio_button.isChecked():
                location_x = 0
                location_y = 0
                area_width = 0
                area_height = 0
            else:
                location_x = int(self.fixed_location_x.text())
                location_y = int(self.fixed_location_y.text())
                area_width = 0
                area_height = 0
        except ValueError:
            self.home_save_footnote.setText('error: mouse location (and area width/height) is needed')
            return
        try:
            if self.repeat_radio_button.isChecked():
                delay_type = str(self.delay_time_combobox.currentText())
                delay_time = int(self.delay_time_entrybox.text())
                wait_interval_min, wait_interval_max = delay_time, delay_time
            else:
                delay_type = str(self.delay_time_combobox_2.currentText())
                wait_interval_min = int(self.range_min.text())
                wait_interval_max = int(self.range_max.text())
        except ValueError:
            self.home_save_footnote.setText('error: set delay time for your choice')
            return
        saved_date = datetime.today().strftime('%Y-%m-%d %H:%M')
        try:
            functions.add_run_home_db(save_name, mouse_type, click_type, repeat_or_range, click_repeat, select_or_fixed,
                                      location_x, location_y, wait_interval_min, wait_interval_max, delay_type,
                                      area_width, area_height, saved_date)
            self.home_save_window.close()
        except sqlite3.IntegrityError:
            self.home_save_footnote.setText('error: this name exists')
            return

    # saves the actions from home screen into pc
    def home_save_settings_pc(self):
        save_name = self.save_name_box.text()
        if save_name == '':
            self.home_save_footnote.setText('error: name is needed')
            return
        mouse_type = str(self.mouse_button_combobox.currentText())
        click_type = str(self.click_type_combobox.currentText())
        if self.repeat_radio_button.isChecked():
            repeat_or_range = 'repeat'
        else:
            repeat_or_range = 'range'
        if str(self.never_stop_combobox.currentText()) == 'Yes':
            click_repeat = -1
        else:
            try:
                click_repeat = int(self.repeat_for_number.text())
            except ValueError:
                self.home_save_footnote.setText('error: number of repeat is needed to save')
                return
        if self.select_area_radio_button.isChecked():
            select_or_fixed = 'select'
        elif self.current_location_radio_button.isChecked():
            select_or_fixed = 'current'
        else:
            select_or_fixed = 'fixed'
        try:
            if self.select_area_radio_button.isChecked():
                location_x = int(self.select_area_x.text())
                location_y = int(self.select_area_y.text())
                area_width = int(self.select_area_width.text())
                area_height = int(self.select_area_height.text())
            elif self.current_location_radio_button.isChecked():
                location_x = 0
                location_y = 0
                area_width = 0
                area_height = 0
            else:
                location_x = int(self.fixed_location_x.text())
                location_y = int(self.fixed_location_y.text())
                area_width = 0
                area_height = 0
        except ValueError:
            self.home_save_footnote.setText('error: mouse location (and area width/height) is needed')
            return
        try:
            if self.repeat_radio_button.isChecked():
                delay_type = str(self.delay_time_combobox.currentText())
                delay_time = int(self.delay_time_entrybox.text())
                if delay_type == 'ms':
                    wait_interval = (delay_time, delay_time)
                else:
                    wait_interval = (delay_time, delay_time)
            else:
                delay_type = str(self.delay_time_combobox_2.currentText())
                delay_time_min = int(self.range_min.text())
                delay_time_max = int(self.range_max.text())
                wait_interval = (delay_time_min, delay_time_max)
        except ValueError:
            self.home_save_footnote.setText('error: set delay time for your choice')
            return
        pc_csv_list = [mouse_type, click_type, repeat_or_range, click_repeat, select_or_fixed,
                       location_x, location_y, wait_interval[0], wait_interval[1], delay_type, area_width, area_height]
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", f"{save_name}", "CSV Files(*.csv)")
        if file_name:
            try:
                f = open(file_name, 'w')
                writer = csv.writer(f)
                writer.writerow(pc_csv_list)
                f.close()
                self.home_save_window.close()
            except PermissionError:
                self.home_save_footnote.setText('error: cannot overwrite because it is being used')
                return

    # starts the process for home -> play button
    def home_start_process(self):
        self.get_home_screen()
        mouse_type = self.mouse_button_combobox.currentText().lower()
        click_type = self.click_type_combobox.currentText()
        never_stop_boolean = self.never_stop_combobox.currentText()
        if never_stop_boolean == 'Yes':
            click_repeat = -1
        else:
            try:
                click_repeat = int(self.repeat_for_number.text())
            except ValueError:
                self.foot_note_label.setText('error: repeat number is missing')
                return
        try:
            if self.repeat_radio_button.isChecked():
                delay_type = str(self.delay_time_combobox.currentText())
                delay_time = int(self.delay_time_entrybox.text())
                if delay_type == 'ms':
                    wait_interval = (delay_time / 1000, delay_time / 1000)
                elif delay_type == 's':
                    wait_interval = (delay_time, delay_time)
                elif delay_type == 'min':
                    wait_interval = (delay_time * 60, delay_time * 60)
                else:
                    wait_interval = (delay_time * 1440, delay_time * 1440)
            else:
                delay_type = str(self.delay_time_combobox_2.currentText())
                if delay_type == 'ms':
                    delay_time_min = int(self.range_min.text()) / 1000
                    delay_time_max = int(self.range_max.text()) / 1000
                    wait_interval = (delay_time_min, delay_time_max)
                elif delay_type == 's':
                    delay_time_min = int(self.range_min.text())
                    delay_time_max = int(self.range_max.text())
                    wait_interval = (delay_time_min, delay_time_max)
                elif delay_type == 'min':
                    delay_time_min = int(self.range_min.text()) * 60
                    delay_time_max = int(self.range_max.text()) * 60
                    wait_interval = (delay_time_min, delay_time_max)
                else:
                    delay_time_min = int(self.range_min.text()) * 1440
                    delay_time_max = int(self.range_max.text()) * 1440
                    wait_interval = (delay_time_min, delay_time_max)
        except ValueError:
            self.foot_note_label.setText('error: value is missing for your repeat or range choice')
            return
        if not self.current_location_radio_button.isChecked():
            try:
                if self.select_area_radio_button.isChecked():
                    location_x = int(self.select_area_x.text())
                    location_y = int(self.select_area_y.text())
                else:
                    location_x = int(self.fixed_location_x.text())
                    location_y = int(self.fixed_location_y.text())
            except ValueError:
                self.foot_note_label.setText('error: x and y location is missing')
                return
        else:
            location_x = 0
            location_y = 0
        if self.select_area_width.text() == '':
            area_width = 0
        else:
            area_width = int(self.select_area_width.text())
        if self.select_area_height.text() == '':
            area_height = 0
        else:
            area_height = int(self.select_area_height.text())
        self.foot_note_label.setText('')
        if self.fixed_location_radio_button.isChecked():
            radio_button = 1
        elif self.current_location_radio_button.isChecked():
            radio_button = 2
        else:
            radio_button = 3
        self.showMinimized()
        # ----------------------
        keyboard.remove_hotkey(self.home_start_stop_hotkey)
        keyboard.add_hotkey(self.home_start_stop_hotkey, self.home_stop_process)
        self.foot_note_label.setText('')
        self.play_button.setEnabled(False)
        toaster.show_toast(title="Clicking started", msg=f'Press {self.home_start_stop_hotkey.upper()} to stop',
                           icon_path=r'images/ico_logo.ico', threaded=True, duration=2)
        if radio_button == 1:
            thread = threading.Thread(target=lambda: home_fixed_clicking(
                mouse_type, click_type, click_repeat, int(location_x), int(location_y), wait_interval))
            thread.start()
        elif radio_button == 2:
            thread = threading.Thread(target=lambda: home_current_clicking(mouse_type, click_type,
                                                                           click_repeat, wait_interval))
            thread.start()
        else:
            thread = threading.Thread(target=lambda: home_random_clicking(mouse_type, click_type, click_repeat,
                                                                          location_x, location_y,
                                                                          wait_interval, area_width, area_height))
            thread.start()

    # starts after the process for home -> play button is finished
    def after_home_thread(self):
        self.play_button.setEnabled(True)
        keyboard.remove_hotkey(self.home_start_stop_hotkey)
        keyboard.add_hotkey(self.home_start_stop_hotkey, lambda: self.play_button.click())
        if self.show_after_complete_checkbox.isChecked():
            self.showNormal()
        toaster.show_toast("Clicking stopped", f'Press {self.home_start_stop_hotkey.upper()} to start again',
                           icon_path=r'images/ico_logo.ico', threaded=True, duration=2)

        if self.whether_logged_in() == 1:
            computer_type = self.complete_combobox.currentText()
        else:
            computer_type = self.complete_combobox_3.currentText()

        if computer_type == " Turn off":
            os.system("shutdown /s /t 1")
        elif computer_type == " Log off":
            os.system("shutdown -l")
        elif computer_type == " Hibernate":
            os.system("shutdown.exe /h")
        elif computer_type == " Lock":
            ctypes.windll.user32.LockWorkStation()
        elif computer_type == " Quit":
            app.exit()
        elif computer_type == "Standby":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # stops the actions set in home screen (intervenes the thread)
    def home_stop_process(self):
        stop_home_event.set()

    # stops the actions set in record screen (intervenes the thread)
    def record_stop_process(self):
        stop_record_event.set()

    # starts the process for record -> play button
    def record_start_process(self):
        self.get_record_screen()
        if self.i == 1:
            self.foot_note_label.setText('error: no actions available')
            return
        actions_data = []
        print("here bro")
        for a in range(self.i - 1):
            csv_list = []
            row_elements = self.line_list[a][1].children()
            if self.line_list[a][0] == 'mouse':
                csv_list.append('mouse')
                for b in (3, 5):
                    if row_elements[b].text() == '':
                        self.foot_note_label.setText('error: x and y location are needed')
                        return
                    else:
                        csv_list.append(row_elements[b].text())
                for b in (7, 9):
                    csv_list.append(row_elements[b].currentText())
                if row_elements[11].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[11].text())
                actions_data.append(csv_list)
            elif self.line_list[a][0] == 'keyboard':
                csv_list.append('keyboard')
                csv_list.append(row_elements[3].text())
                if row_elements[3].text() == '':
                    self.foot_note_label.setText('error: no input given')
                    return
                csv_list.append(row_elements[5].currentText())
                csv_list.append(row_elements[7].currentText())
                if row_elements[9].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[9].text())
                actions_data.append(csv_list)
            elif self.line_list[a][0] == 'scroll':
                csv_list.append('scroll')
                for b in (3, 5):
                    if row_elements[b].text() == '':
                        self.foot_note_label.setText('error: x and y location are needed')
                        return
                    else:
                        csv_list.append(row_elements[b].text())
                csv_list.append(row_elements[7].currentText())
                csv_list.append(row_elements[9].text())
                if row_elements[11].text() == '':
                    csv_list.append('100')
                else:
                    csv_list.append(row_elements[11].text())
                actions_data.append(csv_list)
        if actions_data[0][0] == 'keyboard':
            if actions_data[0][2] == 'Key':
                pressed_key = functions.key_converter(actions_data[0][1].replace('Key.', '').lower())
                if pressed_key == 'wrong':
                    self.foot_note_label.setText('error: wrong key input')
                    return
        if self.repeat_for_number_2.text() == '':
            repeat_all = '1'
        else:
            repeat_all = self.repeat_for_number_2.text()
        if self.delay_2.text() == '':
            delay_time = 0.1
        else:
            delay_type = self.delay_time_combobox_record.currentText()
            if delay_type == "ms":
                delay_time = int(self.delay_2.text()) / 1000
            elif delay_type == "s":
                delay_time = int(self.delay_2.text())
            elif delay_type == "min":
                delay_time = int(self.delay_2.text()) * 60
            else:
                delay_time = int(self.delay_2.text()) * 1440
        self.foot_note_label.setText('')
        self.showMinimized()
        # -------------------------
        keyboard.remove_hotkey(self.record_start_stop_hotkey)
        keyboard.add_hotkey(self.record_start_stop_hotkey, self.record_stop_process)
        self.record_play_button.setEnabled(False)
        toaster.show_toast(title="Playback started",
                           msg=f'Press {self.record_start_stop_hotkey.upper()} to stop playback',
                           icon_path=r'images/ico_logo.ico', threaded=True, duration=2)
        thread_2 = threading.Thread(target=lambda: start_record_actions(actions_data, repeat_all, delay_time, self.i))
        thread_2.start()

    # starts after the process for record -> play button is finished
    def after_record_thread(self, a):
        if wrong_key_event.is_set():
            self.foot_note_label.setText(f'error: wrong key input at line {a + 1}')
            wrong_key_event.clear()
        self.record_play_button.setEnabled(True)
        keyboard.remove_hotkey(self.record_start_stop_hotkey)
        keyboard.add_hotkey(self.record_start_stop_hotkey, lambda: self.record_play_button.click())
        if self.show_after_complete_checkbox.isChecked():
            self.showNormal()
        toaster.show_toast(title="Playback completed",
                           msg=f'Press {self.record_start_stop_hotkey.upper()} to start again',
                           icon_path=r'images/ico_logo.ico', threaded=True, duration=2)

        if self.whether_logged_in() == 1:
            computer_type = self.complete_combobox.currentText()
        else:
            computer_type = self.complete_combobox_3.currentText()

        if computer_type == " Turn off":
            os.system("shutdown /s /t 1")
        elif computer_type == " Log off":
            os.system("shutdown -l")
        elif computer_type == " Hibernate":
            os.system("shutdown.exe /h")
        elif computer_type == " Lock":
            ctypes.windll.user32.LockWorkStation()
        elif computer_type == " Quit":
            app.exit()
        elif computer_type == " Standby":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    # gets data from recording and inserts into list in record screen
    # takes list of recording actions as parameter; mouse, keyboard or scroll action
    def insert_recording_list(self, events):
        c = 0
        release_counter = 0
        while len(events[c]) == 6:
            if events[0][3] == 'release':
                del events[0]
                release_counter += 1
            else:
                break
        if release_counter == 0:
            del events[-1]
            del events[-1]
        else:
            del events[-1]
        self.remove_all_lines()
        total_row = len(events)
        a = 0
        b = 0
        while a < total_row:
            if len(events[a]) == 5:
                self.add_mouse_line()
                children = self.line_list[b][1].children()
                children[3].setText(str(events[a][0]))
                children[5].setText(str(events[a][1]))
                if str(events[a][2]) == 'Button.left':
                    children[7].setCurrentText('Left')
                elif str(events[a][2]) == 'Button.middle':
                    children[7].setCurrentText('Middle')
                else:
                    children[7].setCurrentText('Right')
                if events[a][3] is True:
                    children[9].setCurrentText('Press')
                else:
                    children[9].setCurrentText('Release')
                delay = int(events[a][4] * 1000)
                children[11].setText(str(delay))
            elif len(events[a]) == 4:
                self.add_scroll_line()
                children = self.line_list[b][1].children()
                children[3].setText(str(events[a][0]))
                children[5].setText(str(events[a][1]))
                scroll_count = 1
                delay = int(events[a][3] * 1000)
                if str(events[a][2]) == '-1':
                    children[7].setCurrentText('Down')
                    for scrolls in range(1, total_row - a):
                        if len(events[a+scrolls]) == 4:
                            if str(events[a+scrolls][2]) == '-1':
                                scroll_count += 1
                                delay += int(events[a+scrolls][3] * 1000)
                            else:
                                break
                        else:
                            break
                    children[9].setText(str(scroll_count))
                else:
                    children[7].setCurrentText('Up')
                    for scrolls in range(1, total_row - a):
                        if len(events[a+scrolls]) == 4:
                            if str(events[a+scrolls][2]) == '1':
                                scroll_count += 1
                                delay += int(events[a+scrolls][3] * 1000)
                            else:
                                break
                        else:
                            break
                    children[9].setText(str(scroll_count))
                if scroll_count > 1:
                    a += scroll_count - 1
                children[11].setText(str(delay))
            elif len(events[a]) == 6:
                self.add_keyboard_line()
                children = self.line_list[b][1].children()
                char_group = events[a][0]
                char_count = 1
                delay = int(events[a][2] * 1000)
                if events[a][1] == 'char':
                    children[5].setCurrentText('Char')
                    for char in range(1, total_row - a):
                        if len(events[a+char]) == 3:
                            if str(events[a+char][1]) == 'char':
                                char_group += events[a+char][0]
                                delay += int(events[a+char][2] * 1000)
                                char_count += 1
                            else:
                                break
                    children[3].setText(str(char_group))
                else:
                    children[5].setCurrentText('Key')
                    children[3].setText(str(char_group))
                if char_count > 1:
                    a += char_count - 1
                if events[a][3] == 'press':
                    children[7].setCurrentText('Press')
                else:
                    children[7].setCurrentText('Release')
                children[9].setText(str(delay))
            a += 1
            b += 1

    # starts a thread for live_record_process function
    def thread_for_live_record(self):
        self.remove_all_lines()
        new_thread = threading.Thread(target=self.live_record_process)
        new_thread.setDaemon(True)
        new_thread.start()

    # handles live recording process
    def live_record_process(self):
        def on_click(x, y, button, pressed):
            nonlocal time_counter
            old_time = time_counter
            time_counter = time.time()
            delay = round(time_counter - old_time, 2)
            new_list = [x, y, button, pressed, delay]
            self.record_events.append(new_list)

        def on_scroll(x, y, dx, dy):
            nonlocal time_counter
            old_time = time_counter
            time_counter = time.time()
            delay = round(time_counter - old_time, 2)
            new_list = [x, y, dy, delay]
            self.record_events.append(new_list)

        def on_press(key):
            nonlocal time_counter
            old_time = time_counter
            time_counter = time.time()
            delay = round(time_counter - old_time, 2)
            press_type = 'press'
            if hasattr(key, 'char'):
                if str(key)[0] == "<":
                    key_type = 'key'
                    new_list = [key, key_type, delay, press_type, 0, 0]
                elif str(key)[0] == "[":
                    key_type = 'char'
                    new_list = [str(key)[2:-2].lower(), key_type, delay, press_type, 0, 0]
                elif str(key)[1] == "\\":
                    key_type = 'char'
                    converted_key = functions.char_converter(str(key)[1:-1])
                    new_list = [converted_key.lower(), key_type, delay, press_type, 0, 0]
                else:
                    key_type = 'char'
                    new_list = [str(key)[1:-1].lower(), key_type, delay, press_type, 0, 0]
            else:
                key_type = 'key'
                new_list = [key, key_type, delay, press_type, 0, 0]
            self.record_events.append(new_list)

        def on_release(key):
            nonlocal time_counter
            old_time = time_counter
            time_counter = time.time()
            delay = round(time_counter - old_time, 2)
            press_type = 'release'
            if hasattr(key, 'char'):
                if str(key)[0] == "<":
                    key_type = 'key'
                    new_list = [key, key_type, delay, press_type, 0, 0]
                elif str(key)[0] == "[":
                    key_type = 'char'
                    new_list = [str(key)[2:-2].lower(), key_type, delay, press_type, 0, 0]
                elif str(key)[1] == "\\":
                    key_type = 'char'
                    converted_key = functions.char_converter(str(key)[1:-1])
                    new_list = [converted_key.lower(), key_type, delay, press_type, 0, 0]
                else:
                    key_type = 'char'
                    new_list = [str(key)[1:-1].lower(), key_type, delay, press_type, 0, 0]
            else:
                key_type = 'key'
                new_list = [key, key_type, delay, press_type, 0, 0]
            self.record_events.append(new_list)

        self.record_record_button.disconnect()
        self.record_record_button.clicked.connect(self.stop_live_record)
        self.record_record_button.setText("Stop")
        self.record_events = []
        self.mouse_listener = pynput.mouse.Listener(on_click=on_click, on_scroll=on_scroll)
        self.keyboard_listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
        self.showMinimized()
        # send notification to desktop
        toaster.show_toast(title="Recording Started",
                           msg=f'Press {self.record_recording_hotkey.upper()} to stop recording',
                           icon_path=r'images/ico_logo.ico', threaded=True, duration=2)
        self.record_play_button.setEnabled(False)
        self.mouse_listener.start()
        self.keyboard_listener.start()
        time_counter = time.time()
        self.mouse_listener.join()
        self.keyboard_listener.join()

    # stops live recording process
    def stop_live_record(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        toaster.show_toast(title="Recording completed",
                           msg=f'Press {self.record_start_stop_hotkey.upper()} to start playback',
                           icon_path=r'images/ico_logo.ico', threaded=True, duration=2)
        self.record_record_button.setIcon(QtGui.QIcon("images/red-circle"))
        self.record_record_button.disconnect()
        self.record_record_button.clicked.connect(self.thread_for_live_record)
        self.record_record_button.setText("Record")
        self.insert_recording_list(self.record_events)
        self.showNormal()
        self.record_play_button.setEnabled(True)


class CaptureScreen(QtWidgets.QSplashScreen):
    """QSplashScreen, that track mouse event for capturing screenshot."""
    def __init__(self):


        super(CaptureScreen, self).__init__()

        # Points on screen marking the origin and end of regtangle area.
        self.origin = QtCore.QPoint(0,0)
        self.end = QtCore.QPoint(0,0)
        self.signal = 0

        # A drawing widget for representing bounding area
        self.rubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)

        self.createDimScreenEffect()

    def createDimScreenEffect(self):
        """Fill splashScreen with black color and reduce the widget opacity to create dim screen effect"""

        # Get the screen geometry of the main desktop screen for size ref
        primScreenGeo = QtGui.QGuiApplication.primaryScreen().geometry()

        screenPixMap = QtGui.QPixmap(primScreenGeo.width(), primScreenGeo.height())
        screenPixMap.fill(QtGui.QColor(0,0,0))

        self.setPixmap(screenPixMap)

        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setWindowOpacity(0.4)

    def mousePressEvent(self, event):
        """Show rectangle at mouse position when left-clicked"""
        if event.button() == QtCore.Qt.LeftButton:
            self.origin = event.pos()
            print("origin_x: " + str(self.origin.x()))
            print("origin_y: " + str(self.origin.y()))
            self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.rubberBand.show()

    def getOriginal_x(self):
        return self.origin.x()
    def getOriginal_y(self):
        return self.origin.y()
    def getFinal_x(self):
        return self.end.x()
    def getFinal_y(self):
        return self.end.y()

    def mouseMoveEvent(self, event):
        """Resize rectangle as we move mouse, after left-clicked."""
        self.rubberBand.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())

    def indicator(self):
        return self.signal

    def mouseReleaseEvent(self, event):
        """Upon mouse released, ask the main desktop's QScreen to capture screen on defined area."""
        if event.button() == QtCore.Qt.LeftButton:
            self.end = event.pos()
            print("end_x: " + str(self.end.x()))
            print("end_y: " + str(self.end.y()))
            self.rubberBand.hide()
            self.hide()
            self.signal = 1
            primaryScreen = QtGui.QGuiApplication.primaryScreen()
            grabbedPixMap = primaryScreen.grabWindow(0, self.origin.x(), self.origin.y(), self.end.x()-self.origin.x(), self.end.y()-self.origin.y())
            # grabbedPixMap.save('screenshot_windowed.jpg', 'jpg')
            UIWindow = UI()

            self.original_x = self.getOriginal_x()
            self.original_y = self.getOriginal_y()
            self.final_x = self.getFinal_x()
            self.final_y = self.getFinal_y()
            self.snipping_width = abs(self.final_x - self.original_x)
            self.snipping_height = abs(self.final_y - self.original_y)
            self.snip_x = min(self.final_x,self.original_x)
            self.snip_y = min(self.final_y,self.original_y)
            UIWindow.select_area_x.setText(str(self.snip_x))
            UIWindow.select_area_y.setText(str(self.snip_y))
            UIWindow.select_area_width.setText(str(self.snipping_width))
            UIWindow.select_area_height.setText(str(self.snipping_height))
            UIWindow.select_area_radio_button.setChecked(True)
            UIWindow.show()


# below 7 lines gets the latest preferences of the user from the database
conn = sqlite3.connect('autoclicker.db')
cursor = conn.cursor()
sql = '''SELECT * FROM app_settings LIMIT 1'''
cursor.execute(sql)
app_settings = cursor.fetchone()
conn.close()
show_tool_after, hide_system_tray, disable_cursor_location, dark_theme, home_start_hotkey, record_start_hotkey, \
record_recording_hotkey, mouse_location_hotkey = app_settings
toaster = ToastNotifier()
# fetch the hardware UUID
# print(device_id.get_windows_uuid())
# ---------
stop_home_event = threading.Event()
stop_record_event = threading.Event()
wrong_key_event = threading.Event()
app = QApplication(sys.argv)
UIWindow = UI()
UIWindow.show()
app.exec_()
