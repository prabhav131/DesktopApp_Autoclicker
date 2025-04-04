import csv
import ctypes
import datetime
import hashlib
import json
import logging
import os
import random
import re
import sqlite3
import sys
import threading
import time
import webbrowser
from datetime import timedelta
import keyboard
import mouse
import pynput
import requests
from appdirs import *
from email_validator import EmailNotValidError, validate_email
from PyQt5 import QtCore, QtGui, QtWidgets, uic, QtTest
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
                             QFileDialog, QFormLayout, QFrame, QGridLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QListWidget, QListWidgetItem, QMainWindow,
                             QPushButton, QRadioButton, QScrollArea,
                             QToolButton, QWidget)
from win10toast import ToastNotifier

import resource_rc
from functions_file import functions


class WorkerThread1(threading.Thread):
    def __init__(
        self, main_window, mouse_type, click_type, click_repeat, waiting_interval
    ):
        super().__init__()
        self.main_window = main_window
        self.mouse_type = mouse_type
        self.click_type = click_type
        self.click_repeat = click_repeat
        self.waiting_interval = waiting_interval

    def run(self):
        try:
            logger.info("start execution of function: home_current_clicking()")
            stop_home_event.clear()
            if self.waiting_interval[0] == self.waiting_interval[1]:
                if self.waiting_interval[0] > 2:
                    repeat = int(self.waiting_interval[0] / 2)
                    last = float(self.waiting_interval[0] - (repeat * 2))
                    delay = 2
                else:
                    repeat = 1
                    last = 0
                    delay = self.waiting_interval[0]
                if self.click_repeat > 0:
                    if self.click_type == "Single":
                        for i in range(self.click_repeat):
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        for i in range(self.click_repeat):
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                elif self.click_repeat == 0:
                    pass
                else:
                    if self.click_type == "Single":
                        while True:
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        while True:
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
            else:
                wait_time = round(
                    random.uniform(self.waiting_interval[0], self.waiting_interval[1]),
                    1,
                )
                if wait_time > 2:
                    repeat = int(wait_time / 2)
                    last = float(wait_time - (repeat * 2))
                    delay = 2
                else:
                    repeat = 1
                    last = 0
                    delay = wait_time
                if self.click_repeat > 0:
                    if self.click_type == "Single":
                        for i in range(self.click_repeat):
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        for i in range(self.click_repeat):
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                elif self.click_repeat == 0:
                    pass
                else:
                    if self.click_type == "Single":
                        while True:
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        while True:
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
            logger.info("done current clicking")
            home_clicking_event.clear()
            self.main_window.maximize_signal.emit()
            UIWindow.after_home_thread()

            logger.info("ending execution of function: home_current_clicking()")
        except:
            logger.error("exception in home_current_clicking()", exc_info=True)


class WorkerThread2(threading.Thread):
    def __init__(
        self, main_window, mouse_type, click_type, click_repeat, location_x, location_y, wait_interval
    ):
        super().__init__()
        self.main_window = main_window
        self.mouse_type = mouse_type
        self.click_type = click_type
        self.click_repeat = click_repeat
        self.wait_interval = wait_interval
        self.location_x = location_x
        self.location_y = location_y

    def run(self):
        try:
            logger.info("start execution of function: home_fixed_clicking()")
            stop_home_event.clear()
            if self.wait_interval[0] == self.wait_interval[1]:
                if self.wait_interval[0] > 2:
                    repeat = int(self.wait_interval[0] / 2)
                    last = float(self.wait_interval[0] - (repeat * 2))
                    delay = 2
                else:
                    repeat = 1
                    last = 0
                    delay = self.wait_interval[0]
                if self.click_repeat > 0:
                    if self.click_type == "Single":
                        for i in range(self.click_repeat):
                            mouse.move(self.location_x, self.location_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        for i in range(self.click_repeat):
                            mouse.move(self.location_x, self.location_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                elif self.click_repeat == 0:
                    pass
                else:
                    if self.click_type == "Single":
                        while True:
                            mouse.move(self.location_x, self.location_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        while True:
                            mouse.move(self.location_x, self.location_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
            else:
                wait_time = round(random.uniform(self.wait_interval[0], self.wait_interval[1]), 1)

                if wait_time > 2:
                    repeat = int(wait_time / 2)
                    last = float(wait_time - (repeat * 2))
                    delay = 2
                else:
                    repeat = 1
                    last = 0
                    delay = wait_time

                if self.click_repeat > 0:
                    if self.click_type == "Single":
                        for i in range(self.click_repeat):
                            mouse.move(self.location_x, self.location_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break

                    else:
                        for i in range(self.click_repeat):
                            mouse.move(self.location_x, self.location_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                elif self.click_repeat == 0:
                    pass
                else:
                    if self.click_type == "Single":
                        while True:
                            mouse.move(self.location_x, self.location_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        while True:
                            mouse.move(self.location_x, self.location_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break

            logger.info("done fixed clicking")
            home_clicking_event.clear()
            self.main_window.maximize_signal.emit()
            UIWindow.after_home_thread()

            logger.info("ending execution of function: home_fixed_clicking()")
        except:
            logger.error("exception in home_fixed_clicking()", exc_info=True)


class WorkerThread3(threading.Thread):
    def __init__(
        self, main_window, mouse_type, click_type, click_repeat, location_x, location_y, wait_interval, area_width, area_height,
    ):
        super().__init__()
        self.main_window = main_window
        self.mouse_type = mouse_type
        self.click_type = click_type
        self.click_repeat = click_repeat
        self.wait_interval = wait_interval
        self.location_x = location_x
        self.location_y = location_y
        self.area_width = area_width
        self.area_height = area_height

    def run(self):
        try:
            logger.info("start execution of function: home_random_clicking()")
            stop_home_event.clear()
            end_x = self.location_x + self.area_width
            end_y = self.location_y + self.area_height
            if self.wait_interval[0] == self.wait_interval[1]:
                if self.wait_interval[0] > 2:
                    repeat = int(self.wait_interval[0] / 2)
                    last = float(self.wait_interval[0] - (repeat * 2))
                    delay = 2
                else:
                    repeat = 1
                    last = 0
                    delay = self.wait_interval[0]
                if self.click_repeat > 0:
                    if self.click_type == "Single":
                        for i in range(self.click_repeat):
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        for i in range(self.click_repeat):
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                elif self.click_repeat == 0:
                    pass
                else:
                    if self.click_type == "Single":
                        while True:
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        while True:
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
            else:
                wait_time = round(random.uniform(self.wait_interval[0], self.wait_interval[1]), 1)
                if wait_time > 2:
                    repeat = int(wait_time / 2)
                    last = float(wait_time - (repeat * 2))
                    delay = 2
                else:
                    repeat = 1
                    last = 0
                    delay = wait_time
                if self.click_repeat > 0:
                    if self.click_type == "Single":
                        for i in range(self.click_repeat):
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        for i in range(self.click_repeat):
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                elif self.click_repeat == 0:
                    pass
                else:
                    if self.click_type == "Single":
                        while True:
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
                    else:
                        while True:
                            random_x = random.randint(self.location_x, end_x)
                            random_y = random.randint(self.location_y, end_y)
                            mouse.move(random_x, random_y)
                            mouse.double_click(button=self.mouse_type)
                            for j in range(repeat):
                                QtTest.QTest.qWait(int(delay*1000))
                                if stop_home_event.is_set():
                                    break
                            QtTest.QTest.qWait(int(last*1000))
                            if stop_home_event.is_set():
                                stop_home_event.clear()
                                break
            logger.info("done random clicking")
            home_clicking_event.clear()
            self.main_window.maximize_signal.emit()
            UIWindow.after_home_thread()
            logger.info("ending execution of function: home_random_clicking()")
        except:
            logger.error("exception in home_random_clicking()", exc_info=True)


class WorkerThread_playback(threading.Thread):
    def __init__(
        self, main_window, actions_data, repeat_all, delay_time, i
    ):
        super().__init__()
        self.main_window = main_window
        self.actions_data = actions_data
        self.repeat_all = repeat_all
        self.delay_time = delay_time
        self.i = i


    def run(self):
        try:
            logger.info(
                "start execution of function: start_record_action(): playing back record actions from record screen"
            )
            last_line = 0
            if self.delay_time > 2:
                repeat = int(self.delay_time / 2)
                last = float(self.delay_time - (repeat * 2))
                delay = 2
            else:
                repeat = 1
                last = 0
                delay = self.delay_time
            logger.info(f"self.repeat_all- {self.repeat_all}")
            for b in range(int(self.repeat_all)):
                logger.info(f"inside the loop, value of i is: {self.i}")
                for a in range(self.i - 1):
                    last_line += 1
                    if self.actions_data[a][0] == "mouse":
                        try:
                            click_for_record(
                                int(self.actions_data[a][1]),
                                int(self.actions_data[a][2]),
                                self.actions_data[a][3].lower(),
                                self.actions_data[a][4],
                                int(self.actions_data[a][5]),
                            )
                        except:
                            logger.error("Exception occurred", exc_info=True)
                            break
                    elif self.actions_data[a][0] == "keyboard":
                        try:
                            type_for_record(
                                self.actions_data[a][1],
                                self.actions_data[a][2],
                                self.actions_data[a][3],
                                int(self.actions_data[a][4]),
                            )
                        except:
                            logger.error("Exception occurred", exc_info=True)
                            break
                    else:
                        try:
                            scroll_for_record(
                                int(self.actions_data[a][1]),
                                int(self.actions_data[a][2]),
                                self.actions_data[a][3],
                                int(self.actions_data[a][4]),
                                int(self.actions_data[a][5]),
                            )
                        except:
                            logger.error("Exception occurred", exc_info=True)
                            break
                    if stop_record_event.is_set():
                        logger.info("break here")
                        break
                if stop_record_event.is_set():
                    stop_record_event.clear()
                    break
                for j in range(repeat):
                    QtTest.QTest.qWait(int(delay*1000))
                    if stop_record_event.is_set():
                        break
                QtTest.QTest.qWait(int(last*1000))
                if stop_record_event.is_set():
                    stop_record_event.clear()
                    break
            for c in range(self.i - 1):
                if self.actions_data[c][0] == "keyboard":
                    converted_key = (
                        self.actions_data[c][1]
                            .replace("Key.", "")
                            .replace("_l", "")
                            .replace("_r", "")
                            .lower()
                    )
                    if keyboard.is_pressed(converted_key):
                        type_for_record(converted_key, self.actions_data[c][2], "Release", 0)
            record_playback_event.clear()
            logger.info("clearing record playback event")
            self.main_window.close_signal.emit()
            self.main_window.maximize_signal.emit()

            UIWindow.after_record_thread(last_line)

            logger.info(
                "ending execution of function: start_record_action(): playing back record actions from record screen"
            )
        except:
            logger.error("exception in start_record_action()", exc_info=True)


class WorkerThread_recording_actions(threading.Thread):
    def __init__(
        self, main_window
    ):
        super().__init__()
        self.main_window = main_window


    def run(self):
        try:
            logger.info("starting function to start recording user actions from screen")

            # try:
            #     keyboard.remove_hotkey(self.main_window.record_start_stop_hotkey)
            # except:
            #     logger.error(
            #         "error in removing record start stop hotkey", exc_info=True
            #     )

            def on_click(x, y, button, pressed):
                nonlocal time_counter
                old_time = time_counter
                time_counter = time.time()
                delay = round(time_counter - old_time, 2)
                new_list = [x, y, button, pressed, delay]
                self.main_window.record_events.append(new_list)

            def on_scroll(x, y, dx, dy):
                nonlocal time_counter
                old_time = time_counter
                time_counter = time.time()
                delay = round(time_counter - old_time, 2)
                new_list = [x, y, dy, delay]
                self.main_window.record_events.append(new_list)

            def on_press(key):
                nonlocal time_counter
                old_time = time_counter
                time_counter = time.time()
                delay = round(time_counter - old_time, 2)
                press_type = "press"
                if hasattr(key, "char"):
                    if str(key)[0] == "<":
                        key_type = "key"
                        new_list = [key, key_type, delay, press_type, 0, 0]
                    elif str(key)[0] == "[":
                        key_type = "char"
                        new_list = [
                            str(key)[2:-2].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    elif str(key)[1] == "\\":
                        key_type = "char"
                        converted_key = functions.char_converter(str(key)[1:-1])
                        new_list = [
                            converted_key.lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    else:
                        key_type = "char"
                        new_list = [
                            str(key)[1:-1].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                else:
                    key_type = "key"
                    new_list = [key, key_type, delay, press_type, 0, 0]
                self.main_window.record_events.append(new_list)

            def on_release(key):
                nonlocal time_counter
                old_time = time_counter
                time_counter = time.time()
                delay = round(time_counter - old_time, 2)
                press_type = "release"
                if hasattr(key, "char"):
                    if str(key)[0] == "<":
                        key_type = "key"
                        new_list = [key, key_type, delay, press_type, 0, 0]
                    elif str(key)[0] == "[":
                        key_type = "char"
                        new_list = [
                            str(key)[2:-2].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    elif str(key)[1] == "\\":
                        key_type = "char"
                        converted_key = functions.char_converter(str(key)[1:-1])
                        new_list = [
                            converted_key.lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    else:
                        key_type = "char"
                        new_list = [
                            str(key)[1:-1].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                else:
                    key_type = "key"
                    new_list = [key, key_type, delay, press_type, 0, 0]
                self.main_window.record_events.append(new_list)

            self.main_window.record_record_button.disconnect()
            self.main_window.record_record_button.clicked.connect(self.main_window.stop_live_record)
            self.main_window.record_record_button.setText("Stop")
            self.main_window.record_events = []
            self.main_window.mouse_listener = pynput.mouse.Listener(
                on_click=on_click, on_scroll=on_scroll
            )
            self.main_window.keyboard_listener = pynput.keyboard.Listener(
                on_press=on_press, on_release=on_release
            )
            # self.main_window.showMinimized()
            self.main_window.minimize_signal.emit()
            # main_window_visible.clear()
            # send notification to desktop
            toaster.show_toast(
                title="Recording Started",
                msg=f"Press {self.main_window.record_recording_hotkey.upper()} to stop recording",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )
            self.main_window.record_play_button.setEnabled(False)
            self.main_window.mouse_listener.start()
            self.main_window.keyboard_listener.start()
            time_counter = time.time()
            logger.info("ending function to start recording user actions from screen")
        except:
            logger.error("exception in live_record_process()", exc_info=True)


def combine(str1, str2):
    try:
        l1 = len(str1)
        l2 = len(str2)
        result = ""
        i = 0
        j = 0
        while i < l1 and j < l2:
            result += str1[i]
            result += str2[j]
            i += 1
            j += 1
        while i < l1:
            result += str1[i]
            i += 1
        while j < l2:
            result += str2[j]
            j += 1
        # print(result)
        return result
    except:
        logger.error("exception in combine()", exc_info=True)


def de_combine(str):
    try:
        l = len(str)
        s1 = ""
        s2 = ""
        if l % 2 == 0:
            i = 0
            while i < l:
                s1 += str[i]
                s2 += str[i + 1]
                i += 2
        else:
            i = 0
            while i < l - 1:
                s1 += str[i]
                s2 += str[i + 1]
                i += 2
            s2 += str[l - 1]
        return s1, s2
    except:
        logger.error("exception in de_combine()", exc_info=True)


def prompt_internet_issue():
    try:
        logger.info("starting function to raise user is offline popup")
        global dialog
        dialog = UI_connectivity()
        dialog.show()
        logger.info("ending function to raise user is offline popup")
    except:
        logger.error("exception in prompt_internet_issue()", exc_info=True)


def initialise_db():
    try:

        logger.info("inside init db")
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS app_settings")
        cursor.execute("DROP TABLE IF EXISTS home_run_settings")
        cursor.execute("DROP TABLE IF EXISTS local_table")
        cursor.execute("DROP TABLE IF EXISTS record_run_settings")
        cursor.execute("DROP TABLE IF EXISTS session_details")
        cursor.execute("DROP TABLE IF EXISTS user_info")
        logger.info("deleted tables")
        sql = """CREATE TABLE "app_settings" (
        "show_tool_after"	INTEGER NOT NULL,
        "hide_system_tray"	INTEGER NOT NULL,
        "disable_cursor_location"	INTEGER NOT NULL,
        "disable_small_window"	INTEGER NOT NULL DEFAULT 0,
        "dark_theme"	INTEGER NOT NULL,
        "home_start_hotkey"	TEXT NOT NULL,
        "record_add_line_hotkey"	TEXT,
        "record_start_hotkey"	TEXT NOT NULL,
        "record_recording_hotkey"	TEXT NOT NULL,
        "mouse_location_hotkey"	TEXT NOT NULL
        )"""
        cursor.execute(sql)
        logger.info("created table")
        add_new_row = f"""INSERT INTO app_settings VALUES (
                        '1',
                        '0',
                        '0',
                        '0',
                        '0',
                        'f8',
                        'f7',
                        'f10',
                        'f9',
                        'f6'
                        )"""
        cursor.execute(add_new_row)
        logger.info("created table")
        sql = """CREATE TABLE "home_run_settings" (
        "save_name"	TEXT NOT NULL,
        "mouse_type"	TEXT NOT NULL,
        "click_type"	TEXT NOT NULL,
        "repeat_or_range"	TEXT NOT NULL,
        "click_repeat"	INTEGER NOT NULL,
        "select_or_fixed"	TEXT NOT NULL,
        "location_x"	INTEGER NOT NULL,
        "location_y"	INTEGER NOT NULL,
        "wait_interval_min"	INTEGER NOT NULL,
        "wait_interval_max"	INTEGER NOT NULL,
        "wait_type"	TEXT NOT NULL,
        "area_width"	INTEGER NOT NULL,
        "area_height"	INTEGER NOT NULL,
        "saved_date"	TEXT NOT NULL
        )"""
        cursor.execute(sql)
        logger.info("created table")
        sql = """CREATE TABLE "local_table" (
        "email"	TEXT,
        "access_token"	TEXT,
        "funny_number"  TEXT,
        "funny_number_2"  TEXT,
        "timestamp" TEXT
        )"""
        cursor.execute(sql)
        logger.info("created table")

        sql = """CREATE TABLE record_run_settings (
                save_name TEXT NOT NULL UNIQUE,
                csv_text TEXT NOT NULL,
                saved_date TEXT NOT NULL,
                repeat_all INTEGER NOT NULL,
                delay_time INTEGER NOT NULL,
                delay_type TEXT NOT NULL
                )"""
        cursor.execute(sql)
        logger.info("created table")

        sql = """CREATE TABLE "session_details" (
        "username"	TEXT,
        "application_id"	TEXT,
        "application_key"	TEXT,
        "key_expiration_date"	TEXT,
        PRIMARY KEY("application_id")
        )"""
        cursor.execute(sql)
        logger.info("created table")

        sql = """CREATE TABLE "user_info" (
        "username"	TEXT,
        "password"	TEXT,
        "whether_subscribed"	INTEGER,
        "unique_device_id"	TEXT
        )"""
        cursor.execute(sql)
        logger.info("created table")

        conn.commit()
        conn.close()
    except:
        logger.error("exception in initialise_db()", exc_info=True)


def check(email):
    logger.info("starting function for checking if email entered is valid")
    try:
        # validate and get info
        # v = validate_email(email)
        # # replace with normalized form
        # email = v["email"]
        # logger.info(f"{email} is valid")
        # logger.info("ending function for checking if email entered is valid")
        # return "Yes"
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if re.fullmatch(regex, email):
            logger.info(f"{email} is valid")
            logger.info("ending function for checking if email entered is valid")
            return "Yes"
        else:
            logger.info(f"{email} is invalid")
            logger.info("ending function for checking if email entered is valid")
            return "Invalid Email"
    except EmailNotValidError as e:
        logger.error("Exception occurred in check()", exc_info=True)
        logger.info("ending function for checking if email entered is valid")
        # email is not valid, exception message is human-readable
        return str(e)


# starts the clicking actions set in home screen
def home_fixed_clicking(
    mouse_type, click_type, click_repeat, location_x, location_y, wait_interval
):
    try:
        logger.info("start execution of function: home_fixed_clicking()")
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
                if click_type == "Single":
                    for i in range(click_repeat):
                        mouse.move(location_x, location_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    for i in range(click_repeat):
                        mouse.move(location_x, location_y)
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
            elif click_repeat == 0:
                pass
            else:
                if click_type == "Single":
                    while True:
                        mouse.move(location_x, location_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    while True:
                        mouse.move(location_x, location_y)
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
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
                if click_type == "Single":
                    for i in range(click_repeat):
                        mouse.move(location_x, location_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break

                else:
                    for i in range(click_repeat):
                        mouse.move(location_x, location_y)
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
            elif click_repeat == 0:
                pass
            else:
                if click_type == "Single":
                    while True:
                        mouse.move(location_x, location_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    while True:
                        mouse.move(location_x, location_y)
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break

        logger.info("done fixed clicking")
        # clicking_event.clear()
        UIWindow.after_home_thread()
        # UIWindow.showNormal()
        # global is_clicking
        # is_clicking = False

        logger.info("ending execution of function: home_fixed_clicking()")
    except:
        logger.error("exception in home_fixed_clicking()", exc_info=True)


def database_action(query, query_params):
    try:
        # connecting to database + performing query execution
        logger.info("starting database_action function")
        con = sqlite3.connect(file_path)
        # con = sqlite3.connect(file_path)
        logger.info("connected to database")
        cursor = con.cursor()
        cursor.execute(query, query_params)

        con.commit()

        logger.info("updated database")
        con.close()
        logger.info("ending database_action function")
    except:
        logger.error("exception in database_action()", exc_info=True)


def post_register(email):
    logger.info("starting the post_register function")
    try:
        responses = []
        try:
            r = requests.post(
                "http://146.190.166.207/register",
                data={"email": email},
                headers={"Connection": "close"},
            )
            # r.raise_for_status()
            # r = requests.post('https://auth-provider.onrender.com/register', data={"email": email})
        except requests.exceptions.ConnectionError as conerr:
            logger.error("Exception occurred", exc_info=True)
            prompt_internet_issue()
            return
        responses.append(r)
        logger.info(f"got a post response - {responses}")
        logger.info("ending the post_register function")
        return

    except KeyboardInterrupt:
        logger.error("Exception occurred", exc_info=True)
        logger.info("ending the post_register function")
        return


# starts the clicking actions in current location set in home screen
def home_current_clicking(mouse_type, click_type, click_repeat, waiting_interval):
    try:
        logger.info("start execution of function: home_current_clicking()")
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
                if click_type == "Single":
                    for i in range(click_repeat):
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    for i in range(click_repeat):
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
            elif click_repeat == 0:
                pass
            else:
                if click_type == "Single":
                    while True:
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    while True:
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
        else:
            wait_time = round(
                random.uniform(waiting_interval[0], waiting_interval[1]), 1
            )
            if wait_time > 2:
                repeat = int(wait_time / 2)
                last = float(wait_time - (repeat * 2))
                delay = 2
            else:
                repeat = 1
                last = 0
                delay = wait_time
            if click_repeat > 0:
                if click_type == "Single":
                    for i in range(click_repeat):
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    for i in range(click_repeat):
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
            elif click_repeat == 0:
                pass
            else:
                if click_type == "Single":
                    while True:
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
                else:
                    while True:
                        mouse.double_click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
        logger.info("done current clicking")
        # clicking_event.clear()

        UIWindow.after_home_thread()

        logger.info("ending execution of function: home_current_clicking()")
    except:
        logger.error("exception in home_current_clicking()", exc_info=True)


# starts the dragging actions set in home screen
def home_random_clicking(
    mouse_type,
    click_type,
    click_repeat,
    location_x,
    location_y,
    wait_interval,
    area_width,
    area_height,
):
    try:
        logger.info("start execution of function: home_random_clicking()")
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
                if click_type == "Single":
                    for i in range(click_repeat):
                        random_x = random.randint(location_x, end_x)
                        random_y = random.randint(location_y, end_y)
                        mouse.move(random_x, random_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
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
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
            elif click_repeat == 0:
                pass
            else:
                if click_type == "Single":
                    while True:
                        random_x = random.randint(location_x, end_x)
                        random_y = random.randint(location_y, end_y)
                        mouse.move(random_x, random_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
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
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
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
                if click_type == "Single":
                    for i in range(click_repeat):
                        random_x = random.randint(location_x, end_x)
                        random_y = random.randint(location_y, end_y)
                        mouse.move(random_x, random_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
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
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
            elif click_repeat == 0:
                pass
            else:
                if click_type == "Single":
                    while True:
                        random_x = random.randint(location_x, end_x)
                        random_y = random.randint(location_y, end_y)
                        mouse.move(random_x, random_y)
                        mouse.click(button=mouse_type)
                        for j in range(repeat):
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
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
                            QtTest.QTest.qWait(int(delay*1000))
                            if stop_home_event.is_set():
                                break
                        QtTest.QTest.qWait(int(last*1000))
                        if stop_home_event.is_set():
                            stop_home_event.clear()
                            break
        logger.info("done random clicking")
        # clicking_event.clear()
        UIWindow.after_home_thread()
        # UIWindow.showNormal()
        # global is_clicking
        # is_clicking = False
        logger.info("ending execution of function: home_random_clicking()")
    except:
        logger.error("exception in home_random_clicking()", exc_info=True)


# simulates clicking action for record screen
def click_for_record(location_x, location_y, mouse_type, action_type, wait_interval):
    try:
        logger.info(
            "start execution of function: click for record: clicking action for record screen"
        )
        delay = wait_interval / 1000
        current = mouse.get_position()
        logger.info("a")
        if action_type == "Press":
            logger.info("b")
            QtTest.QTest.qWait(int(delay*1000))
            logger.info("c")
            if not current == (location_x, location_y):
                mouse.move(location_x, location_y, duration=0.01)
            mouse.press(button=mouse_type)
        else:
            logger.info("d")
            QtTest.QTest.qWait(int(delay*1000))
            logger.info("e")
            if not current == (location_x, location_y):
                mouse.move(location_x, location_y, duration=0.10)
            mouse.release(button=mouse_type)
        logger.info(
            "ending execution of function: click for record: clicking action for record screen"
        )
    except:
        logger.error("exception in click_for_record()", exc_info=True)


# simulates scrolling action for record screen
def scroll_for_record(
    location_x, location_y, scroll_type, click_repeat, waiting_interval
):
    try:
        logger.info(
            "start execution of function: scroll for record: scrolling action for record screen"
        )
        delay = int(waiting_interval / click_repeat) / 1000
        current = mouse.get_position()
        if scroll_type == "Up":
            for i in range(click_repeat):
                QtTest.QTest.qWait(int(delay*1000))
                if not current == (location_x, location_y):
                    mouse.move(location_x, location_y)
                mouse.wheel(1)
                if stop_record_event.is_set():
                    logger.info(
                        "ending execution of function: scroll for record: scrolling action for record screen"
                    )
                    return
        else:
            for i in range(click_repeat):
                QtTest.QTest.qWait(int(delay*1000))
                if not current == (location_x, location_y):
                    mouse.move(location_x, location_y)
                mouse.wheel(-1)
                if stop_record_event.is_set():
                    logger.info(
                        "ending execution of function: scroll for record: scrolling action for record screen"
                    )
                    return
    except:
        logger.error("exception in scroll_for_record()", exc_info=True)


# simulates keyboard typing for record screen
def type_for_record(key, key_type, action_type, waiting_interval):
    try:
        logger.info(
            "start execution of function: type for record: typing action for record screen"
        )
        controller = pynput.keyboard.Controller()
        if key_type == "Key":
            if str(key)[0] == "<":
                try:
                    pressed_key = pynput.keyboard.KeyCode(vk=int(str(key)[1:-1]))
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    stop_record_event.set()
                    return
                QtTest.QTest.qWait(waiting_interval)
                if action_type == "Press":
                    controller.press(pressed_key)
                else:
                    controller.release(pressed_key)
            else:
                pressed_key = functions.key_converter(
                    key.replace("Key.", "").replace("_l", "").replace("_r", "").lower()
                )
                if pressed_key == "wrong":
                    stop_record_event.set()
                    wrong_key_event.set()
                    logger.info(
                        "ending execution of function: type for record: typing action for record screen"
                    )
                    return
                else:
                    QtTest.QTest.qWait(waiting_interval)
                    if action_type == "Press":
                        controller.press(pressed_key)
                    else:
                        controller.release(pressed_key)
        else:
            type_no = len(key)
            delay = int(waiting_interval / type_no) / 1000
            for i in range(type_no):
                QtTest.QTest.qWait(int(delay*1000))
                if action_type == "Press":
                    controller.press(key[i])
                else:
                    controller.release(key[i])
                if stop_record_event.is_set():
                    logger.info(
                        "ending execution of function: type for record: typing action for record screen"
                    )
                    return
    except:
        logger.error("exception in type_for_record()", exc_info=True)


# starts recording actions
def start_record_actions(actions_data, repeat_all, delay_time, i):
    try:
        logger.info(
            "start execution of function: start_record_action(): playing back record actions from record screen"
        )
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
                if actions_data[a][0] == "mouse":
                    try:
                        click_for_record(
                            int(actions_data[a][1]),
                            int(actions_data[a][2]),
                            actions_data[a][3].lower(),
                            actions_data[a][4],
                            int(actions_data[a][5]),
                        )
                    except:
                        logger.error("Exception occurred", exc_info=True)
                        break
                elif actions_data[a][0] == "keyboard":
                    try:
                        type_for_record(
                            actions_data[a][1],
                            actions_data[a][2],
                            actions_data[a][3],
                            int(actions_data[a][4]),
                        )
                    except:
                        logger.error("Exception occurred", exc_info=True)
                        break
                else:
                    try:
                        scroll_for_record(
                            int(actions_data[a][1]),
                            int(actions_data[a][2]),
                            actions_data[a][3],
                            int(actions_data[a][4]),
                            int(actions_data[a][5]),
                        )
                    except:
                        logger.error("Exception occurred", exc_info=True)
                        break
                if stop_record_event.is_set():
                    break
            if stop_record_event.is_set():
                stop_record_event.clear()
                break
            for j in range(repeat):
                QtTest.QTest.qWait(int(delay*1000))
                if stop_record_event.is_set():
                    break
            QtTest.QTest.qWait(int(last*1000))
            if stop_record_event.is_set():
                stop_record_event.clear()
                break
        for c in range(i - 1):
            if actions_data[c][0] == "keyboard":
                converted_key = (
                    actions_data[c][1]
                    .replace("Key.", "")
                    .replace("_l", "")
                    .replace("_r", "")
                    .lower()
                )
                if keyboard.is_pressed(converted_key):
                    type_for_record(converted_key, actions_data[c][2], "Release", 0)
        UIWindow.after_record_thread(last_line)
        # clicking_event.clear()
        logger.info(
            "ending execution of function: start_record_action(): playing back record actions from record screen"
        )
    except:
        logger.error("exception in start_record_action()", exc_info=True)


class UI(QMainWindow):
    # defines all variables and UI elements for the app
    maximize_signal = pyqtSignal()
    minimize_signal = pyqtSignal()
    close_signal = pyqtSignal()

    def __init__(self):
        try:
            super(UI, self).__init__()
            logger.info("starting initialisation function of the main UI window")

            self.validity_24_hour = 0
            self.validity_infinity = 0
            conn = sqlite3.connect(file_path)

            cursor = conn.cursor()
            sql = """select funny_number, funny_number_2 from local_table"""
            cursor.execute(sql)
            val = cursor.fetchone()
            # print(val)f
            if val is not None:
                part1 = val[0]
                part2 = val[1]
                full = combine(part1, part2)

                funny = full
                a = str(1)
                hash_funny_enc = hashlib.sha256(a.encode())
                funny_enc = hash_funny_enc.hexdigest()

                b = str(2)
                hash_funny_2_enc = hashlib.sha256(b.encode())
                funny_2_enc = hash_funny_2_enc.hexdigest()
                logger.info("setting value of validity to avoid server call")
                # print(funny)
                if funny == funny_enc:
                    logger.info(
                        "token is valid under 24 hours, now no need to call server"
                    )
                    self.validity_24_hour = 1
                elif funny == funny_2_enc:
                    logger.info("token is valid forever, now no need to call server")
                    self.validity_infinity = 1

            self.flag = 0
            self.responses = []
            # logger.info("starting initialisation of main window")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
            self.small_window_opened = None
            self.small_window = None
            # main_window_visible.set()
            # self.window_status = True
            uic.loadUi(functions.resource_path("version2.ui"), self)
            self.threadLock = threading.Lock()
            self.MainWindow = self.findChild(QMainWindow, "MainWindow")
            self.setWindowIcon(
                QtGui.QIcon(functions.resource_path("images/app_logo.png"))
            )
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            self.screen_width = self.sizeObject.width()
            self.screen_height = self.sizeObject.height()
            # print(self.screen_width)
            # print(self.screen_height)
            self.setFixedWidth(662)
            self.setFixedHeight(533)
            self.central_widget = self.findChild(QWidget, "central_widget")
            self.central_widget_2 = self.findChild(QFrame, "central_widget_2")
            self.integer = QIntValidator()
            self.main_frame = self.findChild(QFrame, "main_frame")
            self.home_frame = self.findChild(QFrame, "home_frame")
            self.authentication_result = 0
            # self.activate_button = self.findChild(QPushButton, "activate_button")
            # # self.activate_button.clicked.connect(self.thread_for_authentication)
            # self.activate_button.clicked.connect(self.authentication_loop2)
            # self.activate_button.setVisible(False)

            self.snipping_push_button = self.findChild(
                QPushButton, "snipping_push_button"
            )
            self.snipping_push_button.clicked.connect(self.screenCapture)

            # Dim Splashscreen object, also responsible for tracking mouse and capturing screenshot.
            # self.tmpDimScreen = CaptureScreen(self)
            self.snipping_radio_button = self.findChild(
                QRadioButton, "snipping_radio_button"
            )
            self.fixed_location_radio_button = self.findChild(
                QRadioButton, "fixed_location_radio_button"
            )
            self.current_location_radio_button = self.findChild(
                QRadioButton, "current_location_radio_button"
            )
            self.fixed_location_x = self.findChild(QLineEdit, "fixed_location_x")
            self.fixed_location_y = self.findChild(QLineEdit, "fixed_location_y")
            self.height_label = self.findChild(QLabel, "height_label")
            self.select_area_height = self.findChild(QLineEdit, "select_area_height")
            self.select_area_radio_button = self.findChild(
                QRadioButton, "select_area_radio_button"
            )
            self.select_area_width = self.findChild(QLineEdit, "select_area_width")
            self.select_area_x = self.findChild(QLineEdit, "select_area_x")
            self.select_area_y = self.findChild(QLineEdit, "select_area_y")
            self.short_cut_label = self.findChild(QLabel, "short_cut_label")
            self.width_label = self.findChild(QLabel, "width_label")
            self.x_left_label = self.findChild(QLabel, "x_left_label")
            self.x_right_label = self.findChild(QLabel, "x_right_label")
            self.y_left_label = self.findChild(QLabel, "y_left_label")
            self.y_right_label = self.findChild(QLabel, "y_right_label")
            # self.arrow_url = functions.resource_path('images/arrow1.png').__str__()
            self.click_options_groupbox = self.findChild(
                QGroupBox, "click_options_groupbox"
            )
            self.click_type_combobox = self.findChild(QComboBox, "click_type_combobox")
            self.click_type_combobox.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(249, 249, 245);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.click_type_label = self.findChild(QLabel, "click_type_label")
            self.mouse_button_combobox = self.findChild(
                QComboBox, "mouse_button_combobox"
            )
            self.mouse_button_combobox.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.mouse_button_label = self.findChild(QLabel, "mouse_button_label")
            self.click_repeat_groupbox = self.findChild(
                QGroupBox, "click_repeat_groupbox"
            )
            self.never_stop_combobox = self.findChild(QComboBox, "never_stop_combobox")
            self.never_stop_combobox.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.never_stop_label = self.findChild(QLabel, "never_stop_label")
            self.repeat_for_label = self.findChild(QLabel, "repeat_for_label")
            self.repeat_for_number = self.findChild(QLineEdit, "repeat_for_number")
            self.repeat_for_number.setDisabled(True)
            self.repeat_for_number.setStyleSheet(
                "background-color: rgb(225, 225, 225);"
                "border: 1px solid;"
                "border-color: rgb(218, 218, 218);"
                "border-radius: 3px;"
            )
            self.delay_groupbox = self.findChild(QGroupBox, "delay_groupbox")
            self.delay_time_combobox = self.findChild(QComboBox, "delay_time_combobox")
            self.delay_time_combobox.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.delay_time_combobox_2 = self.findChild(
                QComboBox, "delay_time_combobox_2"
            )
            self.delay_time_combobox_2.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.delay_time_entrybox = self.findChild(QLineEdit, "delay_time_entrybox")
            self.line_label = self.findChild(QLabel, "line_label")
            self.range_max = self.findChild(QLineEdit, "range_max")
            self.range_min = self.findChild(QLineEdit, "range_min")
            self.range_radio_button = self.findChild(QRadioButton, "range_radio_button")
            self.repeat_radio_button = self.findChild(
                QRadioButton, "repeat_radio_button"
            )
            self.play_button = self.findChild(QPushButton, "play_button")
            self.reset_settings_button = self.findChild(
                QPushButton, "reset_settings_button"
            )
            self.save_settings_button = self.findChild(
                QPushButton, "save_settings_button"
            )
            self.hotkey_settings_frame = self.findChild(QFrame, "hotkey_settings_frame")
            self.left_frame = self.findChild(QFrame, "left_frame")
            self.home_button = self.findChild(QToolButton, "home_button")
            self.home_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/home"))
            )
            self.record_button = self.findChild(QToolButton, "record_button")
            self.record_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Record"))
            )
            self.theme_button = self.findChild(QToolButton, "theme_button")
            self.theme_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Mode"))
            )
            self.view_settings_button = self.findChild(
                QToolButton, "view_settings_button"
            )
            self.view_settings_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Settings"))
            )
            self.navigation_frame = self.findChild(QFrame, "navigation_frame")
            self.record_frame = self.findChild(QFrame, "record_frame")
            self.view_settings_frame = self.findChild(QFrame, "view_settings_frame")
            self.hotkey_settings_button = self.findChild(
                QToolButton, "hotkey_settings_button"
            )
            self.hotkey_settings_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/HotkeyBlack"))
            )
            self.hotkey_settings_frame = self.findChild(QFrame, "hotkey_settings_frame")
            # self.top_frame = self.findChild(QFrame, "top_frame")
            self.top_frame_logged_out = self.findChild(QFrame, "top_frame_logged_out")
            self.app_icon = self.findChild(QLabel, "app_icon")

            self.complete_combobox_3 = self.findChild(QComboBox, "complete_combobox_3")
            self.complete_combobox_3.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 2px solid;"
                "border-radius: 7px;"
                "border-color: rgb(217, 217, 217);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 2px;"
                "border-radius: 5px;"
                "border-color: rgb(249, 249, 245);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.GG_icon = self.findChild(QPushButton, "GG_icon")
            self.GG_icon.setIcon(QtGui.QIcon(functions.resource_path("images/GGicon")))

            self.navigate_button_3 = self.findChild(QPushButton, "navigate_button_3")
            self.navigate_button_3.setIcon(
                QtGui.QIcon(functions.resource_path("images/Hambuger"))
            )

            self.profile_button_3 = self.findChild(QPushButton, "profile_button_3")
            self.profile_button_3.setIcon(
                QtGui.QIcon(functions.resource_path("images/liliajohn"))
            )
            self.record_add_button = self.findChild(QPushButton, "record_add_button")
            self.record_add_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-ui-64"))
            )
            self.record_add_items = self.findChild(QComboBox, "record_add_items")
            self.record_load_button = self.findChild(QPushButton, "record_load_button")
            self.record_load_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-upload-96"))
            )
            self.record_play_button = self.findChild(QPushButton, "record_play_button")
            self.record_play_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Run"))
            )
            self.record_record_button = self.findChild(
                QPushButton, "record_record_button"
            )
            self.record_record_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/red-circle"))
            )
            self.repeat_for_label_2 = self.findChild(QLabel, "repeat_for_label_2")
            self.repeat_for_number_2 = self.findChild(QLineEdit, "repeat_for_number_2")
            self.repeat_for_number_2.setValidator(self.integer)
            self.repeat_for_label_2.hide()
            self.repeat_for_number_2.hide()
            self.repeat_for_number_2.setText("1")
            self.delay_label_2 = self.findChild(QLabel, "delay_label_2")
            self.delay_2 = self.findChild(QLineEdit, "delay_2")
            self.delay_time_combobox_record = self.findChild(
                QComboBox, "delay_time_combobox_record"
            )
            self.delay_label_2.hide()
            self.delay_2.hide()
            self.delay_time_combobox_record.hide()
            self.delay_2.setText("100")
            self.delay_time_combobox_record.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(249, 249, 245);}"
                "QComboBox QAbstractItemView {"
                "background-color: rgb(249, 249, 245);"
                "border: none;"
                "color: black;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(249, 249, 245);"
                "background-color: rgb(249, 249, 245);}"
                "QComboBox::down-arrow {"
                "background-color: rgb(249, 249, 245);"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            self.delay_time_combobox_record.addItem("ms")
            self.delay_time_combobox_record.addItem("s")
            self.delay_time_combobox_record.addItem("min")
            self.delay_time_combobox_record.addItem("hr")
            self.record_remove_all_button = self.findChild(
                QPushButton, "record_remove_all_button"
            )
            self.record_save_button = self.findChild(QPushButton, "record_save_button")
            self.record_scroll_area = self.findChild(QScrollArea, "record_scroll_area")
            self.scroll_bar = self.record_scroll_area.findChildren(QWidget)[5]
            self.scrollAreaWidgetContents = self.findChild(
                QWidget, "scrollAreaWidgetContents"
            )
            self.scrollAreaWidgetContents.setFixedWidth(518)
            self.scrollAreaWidgetContents.setStyleSheet("border: none;")
            self.form_layout = QFormLayout(self.scrollAreaWidgetContents)
            self.foot_note_label = self.findChild(QLabel, "foot_note_label")
            self.live_mouse_label = self.findChild(QLabel, "live_mouse_label")
            self.home_start_stop_hotkey_label = self.findChild(
                QLabel, "home_start_stop_hotkey"
            )
            self.add_record_line_hotkey_label = self.findChild(
                QLabel, "add_record_line_hotkey"
            )
            self.mouse_location_hotkey_label = self.findChild(
                QLabel, "mouse_location_hotkey"
            )
            self.record_start_stop_hotkey_label = self.findChild(
                QLabel, "record_start_stop_hotkey"
            )
            self.playback_start_stop_hotkey_label = self.findChild(
                QLabel, "playback_start_stop_hotkey"
            )
            self.set_new_hotkey_button_1 = self.findChild(
                QPushButton, "set_new_hotkey_1"
            )
            self.set_new_hotkey_button_6 = self.findChild(
                QPushButton, "set_new_hotkey_6"
            )
            self.set_new_hotkey_button_2 = self.findChild(
                QPushButton, "set_new_hotkey_2"
            )
            self.set_new_hotkey_button_3 = self.findChild(
                QPushButton, "set_new_hotkey_3"
            )
            self.set_new_hotkey_button_4 = self.findChild(
                QPushButton, "set_new_hotkey_4"
            )
            self.on_click_complete_label_3 = self.findChild(QLabel, "on_click_label_3")
            self.label = self.findChild(QPushButton, "label")
            self.frame = self.findChild(QFrame, "frame")
            self.frame_2 = self.findChild(QFrame, "frame_2")
            self.frame_3 = self.findChild(QFrame, "frame_3")
            self.frame_4 = self.findChild(QFrame, "frame_4")
            self.frame_10 = self.findChild(QFrame, "frame_10")
            self.frame_11 = self.findChild(QFrame, "frame_11")
            self.frame_16 = self.findChild(QFrame, "frame_16")
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
            self.never_stop_combobox.addItem("Yes")
            self.never_stop_combobox.addItem("No")
            self.delay_time_combobox.addItem("ms")
            self.delay_time_combobox.addItem("s")
            self.delay_time_combobox.addItem("min")
            self.delay_time_combobox.addItem("hr")
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
            self.delay_time_entrybox.setText("1")
            for widget in self.home_frame.findChildren(QLineEdit):
                widget.setValidator(self.integer)
            # --------------
            self.record_button.clicked.connect(self.get_record_screen)
            self.home_button.clicked.connect(self.get_home_screen)
            self.view_settings_button.clicked.connect(self.get_view_screen)
            self.hotkey_settings_button.clicked.connect(self.get_hotkey_screen)
            self.navigate_button_3.clicked.connect(self.open_menu)
            # self.play_button.clicked.connect(self.thread_for_home_start_process)
            self.play_button.clicked.connect(self.home_start_process)
            self.play_button.setStyleSheet(
                "QPushButton {color: #3A5A40;"
                "border: 2px solid #3A5A40;"
                "border-radius: 5px;"
                "color: #3A5A40;}"
                "QPushButton::hover {color:white;"
                "background-color: #3A5A40;}"
            )
            self.play_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/run.png"))
            )
            self.reset_settings_button.clicked.connect(self.home_reset_settings)
            self.record_add_button.clicked.connect(self.add_new_line)
            self.record_load_button.clicked.connect(self.window_load)
            self.record_save_button.clicked.connect(self.window_record_save)
            self.save_settings_button.clicked.connect(self.save_home_settings)
            # self.save_settings_button.clicked.connect(self.window_home_save)
            self.record_play_button.clicked.connect(self.record_start_process)
            # self.record_play_button.clicked.connect(self.sample)
            self.theme_button.clicked.connect(self.get_dark_theme)
            self.record_remove_all_button.clicked.connect(self.remove_all_lines)
            self.never_stop_combobox.currentIndexChanged.connect(
                self.check_repeat_style
            )
            self.complete_combobox_3.activated.connect(
                lambda: self.on_click_complete_label_3.hide()
            )
            # --------------
            # below defines hotkey settings
            self.label_21 = self.findChild(QLabel, "label_21")
            self.label_25 = self.findChild(QLabel, "label_25")
            self.label_22 = self.findChild(QLabel, "label_22")
            self.label_23 = self.findChild(QLabel, "label_23")
            self.label_24 = self.findChild(QLabel, "label_24")
            self.label_21.hide()
            self.label_25.hide()
            self.label_22.hide()
            self.label_23.hide()
            self.label_24.hide()

            self.set_new_hotkey_button_1.clicked.connect(self.start_thread_hotkey_1)
            self.set_new_hotkey_button_6.clicked.connect(self.start_thread_hotkey_6)
            self.set_new_hotkey_button_2.clicked.connect(self.start_thread_hotkey_4)
            self.set_new_hotkey_button_3.clicked.connect(self.start_thread_hotkey_3)
            self.set_new_hotkey_button_4.clicked.connect(self.start_thread_hotkey_2)
            self.record_record_button.clicked.connect(self.thread_for_live_record)
            # --------------
            # below defines app minimization on close
            self.minimized_icon = QtGui.QIcon(
                functions.resource_path("images/app_logo.png")
            )
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
            self.setStyleSheet(
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
                "QRadioButton::indicator {"
                "height: 15px;"
                "width: 15px;}"
                "QRadioButton::indicator::unchecked {"
                "image: url(:/images/radio_unchecked.png);"
                "margin-top: 2px;}"
                "QRadioButton::indicator::checked {"
                "image: url(:/images/radio_checked.png);"
                "margin-top: 2px;}"
            )
            self.central_widget_2.setStyleSheet(
                "QToolTip {background-color: #e0e0e0;"
                "border: none;"
                "color: black;}"
                "QFrame {color: rgb(30, 30, 30);"
                "background-color: rgb(239, 229, 220); }"
            )
            self.record_add_items.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(249, 249, 245);}"
                "QComboBox::drop-down {"
                "background-color: rgb(249, 249, 245);"
                "border: 0px;"
                "border-color: rgb(249, 249, 245);}"
                "QComboBox::down-arrow {"
                "background-color: rgb(249, 249, 245);"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
                "QToolTip {background-color: #e0e0e0;"
                "border: none;"
                "color: black;}"
                "QFrame {color: rgb(30, 30, 30);"
                "background-color: rgb(239, 229, 220); }"
            )
            self.complete_combobox_3.setItemData(
                0, "No changes to PC", QtCore.Qt.ToolTipRole
            )
            self.complete_combobox_3.setItemData(
                1, "Close the tool (PC keeps running)", QtCore.Qt.ToolTipRole
            )
            self.complete_combobox_3.setItemData(
                2, "Sign out of PC with apps still running", QtCore.Qt.ToolTipRole
            )
            self.complete_combobox_3.setItemData(
                3, "Shut down the PC", QtCore.Qt.ToolTipRole
            )
            self.complete_combobox_3.setItemData(
                4, "Sign out of the PC with all the apps closed", QtCore.Qt.ToolTipRole
            )
            self.complete_combobox_3.setItemData(
                5, "Put the PC to Standby mode", QtCore.Qt.ToolTipRole
            )
            self.complete_combobox_3.setItemData(
                6, "Put the  PC to Hibernate mode", QtCore.Qt.ToolTipRole
            )
            # --------------
            # below are app settings initialized
            self.hide_to_tray_checkbox2 = self.findChild(
                QPushButton, "hide_to_tray_checkbox2"
            )
            self.show_after_complete_checkbox2 = self.findChild(
                QPushButton, "hide_while_click_checkbox2"
            )
            self.mouse_location_checkbox2 = self.findChild(
                QPushButton, "mouse_location_checkbox2"
            )
            self.small_window_checkbox2 = self.findChild(
                QPushButton, "small_window_checkbox2"
            )
            self.hide_to_tray_checkbox = self.findChild(
                QCheckBox, "hide_to_tray_checkbox"
            )
            self.show_after_complete_checkbox = self.findChild(
                QCheckBox, "hide_while_click_checkbox"
            )
            self.mouse_location_checkbox = self.findChild(
                QCheckBox, "mouse_location_checkbox"
            )
            self.small_window_checkbox = self.findChild(
                QCheckBox, "small_window_checkbox"
            )
            self.hide_to_tray_checkbox.hide()
            self.show_after_complete_checkbox.hide()
            self.mouse_location_checkbox.hide()
            self.small_window_checkbox.hide()
            self.hide_to_tray_checkbox2.clicked.connect(self.trigger_tray_checkbox)
            self.mouse_location_checkbox2.clicked.connect(self.trigger_live_mouse)
            self.small_window_checkbox2.clicked.connect(
                self.trigger_small_window_checkbox
            )

            self.show_after_complete_checkbox2.clicked.connect(self.trigger_show_tool)
            if self.dark_theme_activated:
                self.mouse_location_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
                self.mouse_location_checkbox2.setStyleSheet(
                    "border: none;" "background-color: #10131b;"
                )
                self.small_window_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
                self.small_window_checkbox2.setStyleSheet(
                    "border: none;" "background-color: #10131b;"
                )
                self.show_after_complete_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
                self.show_after_complete_checkbox2.setStyleSheet(
                    "border: none;" "background-color: #10131b"
                )
                self.hide_to_tray_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
                self.hide_to_tray_checkbox2.setStyleSheet(
                    "border: none;" "background-color: #10131b"
                )
            else:
                self.mouse_location_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
                self.mouse_location_checkbox2.setStyleSheet(
                    "border: none;" "background-color: rgb(239, 229, 220);"
                )
                self.small_window_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
                self.small_window_checkbox2.setStyleSheet(
                    "border: none;" "background-color: rgb(239, 229, 220);"
                )
                self.hide_to_tray_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
                self.hide_to_tray_checkbox2.setStyleSheet(
                    "border: none;" "background-color: rgb(239, 229, 220)"
                )
                self.show_after_complete_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
                self.show_after_complete_checkbox2.setStyleSheet(
                    "border: none;" "background-color: rgb(239, 229, 220)"
                )

            self.check_live_mouse()
            if show_tool_after == 1:
                self.show_after_complete_checkbox2.click()
            if hide_system_tray == 1:
                self.hide_to_tray_checkbox2.click()
            if disable_cursor_location == 1:
                self.mouse_location_checkbox2.click()
            if disable_small_window == 1:
                self.small_window_checkbox2.click()
            if dark_theme == 1:
                self.get_dark_theme()
            self.home_start_stop_hotkey = home_start_hotkey
            self.add_record_line_hotkey = add_record_line_hotkey
            self.record_start_stop_hotkey = record_start_hotkey
            self.record_recording_hotkey = record_recording_hotkey
            self.mouse_location_hotkey = mouse_location_hotkey
            keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
            keyboard.add_hotkey(
                self.home_start_stop_hotkey, lambda: self.play_button.click()
            )
            # keyboard.add_hotkey(self.add_record_line_hotkey, lambda: self.record_add_button.click())
            # keyboard.add_hotkey(
            #     self.record_start_stop_hotkey, lambda: self.record_play_button.click()
            # )
            # keyboard.add_hotkey(
            #     self.record_recording_hotkey, lambda: self.record_record_button.click()
            # )
            # keyboard.add_hotkey(self.home_start_stop_hotkey, lambda: self.multiple_hotkey_actions_home())

            self.home_start_stop_hotkey_label.setText(str(home_start_hotkey))
            self.add_record_line_hotkey_label.setText(str(add_record_line_hotkey))
            self.playback_start_stop_hotkey_label.setText(str(record_start_hotkey))
            self.record_start_stop_hotkey_label.setText(str(record_recording_hotkey))
            self.mouse_location_hotkey_label.setText(str(mouse_location_hotkey))
            # --------------------------
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

            self.on_click_complete_label_3.setFont(self.font)
            self.font.setPixelSize(10)
            self.font.setPixelSize(11)
            self.font.setBold(False)
            self.font.setBold(True)
            self.label_2.setFont(self.font)
            self.label_3.setFont(self.font)
            self.label_4.setFont(self.font)
            self.label_6.setFont(self.font)
            self.label_7.setFont(self.font)
            self.label_9 = self.findChild(QLabel, "label_9")
            self.label_14 = self.findChild(QLabel, "label_14")
            self.label_19 = self.findChild(QLabel, "label_19")
            self.label_15 = self.findChild(QLabel, "label_15")
            self.label_16 = self.findChild(QLabel, "label_16")
            self.label_17 = self.findChild(QLabel, "label_17")
            self.label_9.setFont(self.font)
            self.label_14.setFont(self.font)
            self.label_19.setFont(self.font)
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
            # self.open_small_window(run_mode="home")
            # ------------------------
            # menu bar buttons below
            about_us = self.findChild(QPushButton, "pushButton")
            try:
                about_us.clicked.connect(
                    lambda: webbrowser.open("https://autoclicker.gg/")
                )
            except requests.exceptions.ConnectionError as conerr:
                logger.error("Exception occurred", exc_info=True)
                prompt_internet_issue()
            how_to_use = self.findChild(QPushButton, "pushButton_2")
            try:
                how_to_use.clicked.connect(
                    lambda: webbrowser.open("https://autoclicker.gg/windows")
                )
            except requests.exceptions.ConnectionError as conerr:
                logger.error("Exception occurred", exc_info=True)
                prompt_internet_issue()
            email_us = self.findChild(QPushButton, "pushButton_3")
            try:
                email_us.clicked.connect(
                    lambda: webbrowser.open("https://autoclicker.gg/contact")
                )
            except requests.exceptions.ConnectionError as conerr:
                logger.error("Exception occurred", exc_info=True)
                prompt_internet_issue()
            faqs = self.findChild(QPushButton, "pushButton_4")
            try:
                faqs.clicked.connect(
                    lambda: webbrowser.open("https://autoclicker.gg/FAQs")
                )
            except requests.exceptions.ConnectionError as conerr:
                logger.error("Exception occurred", exc_info=True)
                prompt_internet_issue()
            privacy_policy = self.findChild(QPushButton, "pushButton_5")
            try:
                privacy_policy.clicked.connect(
                    lambda: webbrowser.open("https://autoclicker.gg/privacy-policy/")
                )
            except requests.exceptions.ConnectionError as conerr:
                logger.error("Exception occurred", exc_info=True)
                prompt_internet_issue()
            self.save_home_params = 0
            self.load_home_settings()
            self.maximize_signal.connect(self.maximise)
            self.minimize_signal.connect(self.minimise)
            self.close_signal.connect(self.close_small)
            logger.info("ending initialisation of main window")
        except:
            logger.error("exception in init()", exc_info=True)

    def maximise(self):
        logger.info("inside function to maximise window")
        if self.show_after_complete_checkbox.isChecked():
            self.showNormal()
        logger.info("after calling shownormal")

    def minimise(self):
        logger.info("inside function to minimise window")
        self.showMinimized()
        logger.info("after calling showminimized")

    def close_small(self):
        logger.info("inside function to close small window")

        if not self.small_window_checkbox.isChecked():
            logger.info(f"small window status - {self.small_window_opened}")
            if self.small_window_opened is not None:
                logger.info("small window is opened")
                self.small_window_opened.close()
                self.small_window_opened.deleteLater()
                self.small_window_opened = None
                logger.info(f"small window status - {self.small_window_opened}")
        logger.info("after closing small window")

    def open_email_dialog(self):
        try:
            logger.info("starting open email dialog function")

            self.email_dialog = UI_Dialog()

            self.email_dialog.show()
            logger.info("ending open email dialog function")
        except:
            logger.error("exception in open_email_dialog()", exc_info=True)

    def open_email_sent_dialog(self, email):
        try:
            logger.info("starting open email sent dialog function")
            # self.dialog = QtWidgets.QDialog()
            # self.ui = UI_email_sent_Dialog()
            self.email_sent_dialog = UI_email_sent_Dialog(email)
            # self.ui.setupUi(self.dialog, email)
            self.email_sent_dialog.show()
            logger.info("ending open email sent dialog function")
        except:
            logger.error("exception in open_email_sent_dialog()", exc_info=True)

    def open_small_window(self, run_mode):
        try:
            logger.info("started function call to open small window")
            if self.small_window_checkbox.isChecked():
                return
            stop_hotkey_text = ""
            indicator = 0
            if run_mode == "home":
                stop_hotkey_text = self.home_start_stop_hotkey_label.text()
            elif run_mode == "record playback":
                stop_hotkey_text = self.playback_start_stop_hotkey_label.text()
            elif run_mode == "recording":
                indicator = 1
                logger.info("small window while recording")
                stop_hotkey_text = self.record_start_stop_hotkey_label.text()
            logger.info(f"status of small window is : {self.small_window_opened}")
            self.small_window_opened = UI_SmallWindow(
                stop_hotkey_text, UIWindow, indicator
            )
            # self.dialogs.append(weakref.ref(self.small_window_opened, self.dialogs.remove))
            logger.info("starting to show small window")
            self.small_window_opened.show()
            logger.info("small window should be visible")
            # self.small_window_opened = self.small_window  # holds the current object of small window
            logger.info("completed function call to open small window")
        except:
            logger.error("exception in open_small_window()", exc_info=True)

    def screenCapture(self):
        try:
            """Show the dim Splashscreen"""
            logger.info("started function call to capture screen")
            self.hide()
            self.tmpDimScreen = CaptureScreen(self)
            self.tmpDimScreen.show()
            self.original_x = self.tmpDimScreen.getOriginal_x()
            self.original_y = self.tmpDimScreen.getOriginal_y()
            self.final_x = self.tmpDimScreen.getFinal_x()
            self.final_y = self.tmpDimScreen.getFinal_y()
            self.snipping_width = abs(self.final_x - self.original_x)
            self.snipping_height = abs(self.final_y - self.original_y)
            self.snip_x = min(self.final_x, self.original_x)
            self.snip_y = min(self.final_y, self.original_y)
            logger.info("completed function call to capture screen")
        except:
            logger.error("exception in screencapture()", exc_info=True)

    # triggers show tool checkbox
    def trigger_show_tool(self):
        try:
            logger.info("starting function to toggle show_tool_after_clicking checkbox")
            if self.show_after_complete_checkbox.isChecked():
                self.show_after_complete_checkbox.setChecked(False)
                if self.dark_theme_activated:
                    self.show_after_complete_checkbox2.setIcon(
                        QtGui.QIcon(
                            functions.resource_path("images/empty_checkbox_dark")
                        )
                    )
                    self.show_after_complete_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b"
                    )
                else:
                    self.show_after_complete_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                    )
                    self.show_after_complete_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220)"
                    )
            else:
                self.show_after_complete_checkbox.setChecked(True)
                if self.dark_theme_activated:
                    self.show_after_complete_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                    )
                    self.show_after_complete_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b"
                    )
                else:
                    self.show_after_complete_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon"))
                    )
                    self.show_after_complete_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220)"
                    )
            logger.info("ending function to toggle show_tool_after_clicking checkbox")
        except:
            logger.error("exception in trigger_show_tool()", exc_info=True)

    def sample(self):
        logger.info("YO")
        if home_clicking_event.is_set():
            logger.info("wont start record playback bcos home clicking is taking place.")
            return
        elif record_recording_event.is_set():
            logger.info("wont start record playback bcos screen recording is taking place.")
            return
        logger.info("setting record playback event")
        record_playback_event.set()
        self.get_record_screen()
        logger.info("YO finish")

    # exits app
    def exit_app(self):
        try:
            logger.info("starting function to exit app")
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
            if self.small_window_checkbox.isChecked():
                new_small_window = 1
            else:
                new_small_window = 0
            if self.dark_theme_activated:
                new_dark_theme = 1
            else:
                new_dark_theme = 0
            new_home_start_hotkey = self.home_start_stop_hotkey
            new_add_record_line_hotkey = self.add_record_line_hotkey
            new_record_start_hotkey = self.record_start_stop_hotkey
            new_record_recording_hotkey = self.record_recording_hotkey
            new_mouse_location_hotkey = self.mouse_location_hotkey
            # self.query_thread.join()
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
            delete_row = """DELETE FROM app_settings"""
            cursor.execute(delete_row)
            add_new_row = f"""INSERT INTO app_settings VALUES (
                    '{new_show_tool_after}',
                    '{new_hide_system_tray}',
                    '{new_cursor_location}',
                    '{new_small_window}',
                    '{new_dark_theme}',
                    '{new_home_start_hotkey}',
                    '{new_add_record_line_hotkey}',
                    '{new_record_start_hotkey}',
                    '{new_record_recording_hotkey}',
                    '{new_mouse_location_hotkey}'
                    )"""
            cursor.execute(add_new_row)
            conn.commit()

            if self.save_home_params == 0:
                delete_home_row = """DELETE FROM home_run_settings"""
                cursor.execute(delete_home_row)

                logger.info("deleting any stored home settings")
                conn.commit()

            conn.close()

            logger.info("exiting app")
            app.exit()
        except:
            logger.error("exception in exit_app()", exc_info=True)

    # activates dark theme
    def get_dark_theme(self):
        try:
            logger.info("starting function to activate dark theme")
            self.setStyleSheet(
                "QComboBox {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QComboBox::drop-down {"
                "background-color: rgb(249, 249, 245);"
                "border-color: rgb(249, 249, 245);}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
                "QRadioButton::indicator {"
                "height: 15px;"
                "width: 15px;}"
                "QRadioButton::indicator::unchecked {"
                "image: url(:/images/dark_unchecked.png);"
                "margin-top: 2px;}"
                "QRadioButton::indicator::checked {"
                "image: url(:/images/dark_checked.png);"
                "margin-top: 2px;}"
            )
            self.dark_theme_activated = True
            # self.central_widget_2.setStyleSheet("background-color: #10131b;")
            self.left_frame.setStyleSheet(
                "background-color: #10131b;"
                "color: #bfcfb2;"
                "border: 2px solid #bfcfb2;"
                "border-radius: 10px;"
            )
            self.GG_icon.setStyleSheet("border:none;")
            self.GG_icon.setIcon(QtGui.QIcon(functions.resource_path("images/GG_dark")))
            self.home_button.setStyleSheet("border:none;")
            self.home_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Home_dark"))
            )
            self.record_button.setStyleSheet("border:none;")
            self.record_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Record_dark"))
            )
            self.theme_button.setStyleSheet("border:none;")
            self.theme_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Mode_dark.png"))
            )
            self.view_settings_button.setStyleSheet("border:none;")
            self.view_settings_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Setting_dark.png"))
            )
            self.hotkey_settings_button.setStyleSheet("border:none;")
            self.hotkey_settings_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/HotKey_dark.png"))
            )
            self.central_widget_2.setStyleSheet(
                "QFrame {background-color: #10131b;"
                "color: #bfcfb2;"
                "border: none;}"
                "QComboBox {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QLineEdit {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QRadioButton {color: #bfcfb2;}"
            )
            self.main_frame.setStyleSheet(
                "QFrame {background-color: #10131b;"
                "color: #bfcfb2;"
                "border: none;}"
                "QComboBox {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QLineEdit {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QRadioButton {color: #bfcfb2;}"
            )
            # self.top_frame.setStyleSheet("QFrame {background-color: #10131b;"
            #                              "color: #bfcfb2;"
            #                              "border: none;}"
            #                              "QComboBox {color: black;"
            #                              "background-color: rgb(249, 249, 245);"
            #                              "border: none}"
            #                              "QLineEdit {color: black;"
            #                              "background-color: rgb(249, 249, 245);"
            #                              "border: none}")
            self.top_frame_logged_out.setStyleSheet(
                "QFrame {background-color: #10131b;"
                "color: #bfcfb2;"
                "border: none;}"
                "QComboBox {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QLineEdit {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
            )
            self.home_frame.setStyleSheet(
                "QFrame {background-color: #10131b;"
                "color: #bfcfb2;"
                "border: none;}"
                "QComboBox {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QLineEdit {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none}"
                "QRadioButton {color: #bfcfb2;}"
            )
            self.reset_settings_button.setStyleSheet(
                "QPushButton {color: #ffa94d;"
                "border: 2px solid #ffa94d;"
                "border-radius: 5px;"
                "color: #ffa94d;}"
                "QPushButton::hover {color:white;"
                "background-color: #ffa94d;}"
            )
            self.play_button.setStyleSheet(
                "QPushButton {color: #c98860;"
                "border: 2px solid #c98860;"
                "border-radius: 5px;"
                "color: #c98860;}"
                "QPushButton::hover {color:white;"
                "background-color: #c98860;}"
            )
            self.play_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/run_dark.png"))
            )
            self.save_settings_button.setStyleSheet(
                "QPushButton {color: #1ecd97;"
                "border: 2px solid #1ecd97;"
                "border-radius: 5px;"
                "color: #1ecd97;}"
                "QPushButton::hover {color:white;"
                "background-color: #1ecd97;}"
            )
            self.foot_note_label.setStyleSheet("border:none;")
            self.navigation_frame.setStyleSheet(
                "QPushButton {background-color: #10131b;"
                "border: 1px solid #bfcfb2;"
                "color: #bfcfb2;}"
            )
            self.navigate_button_3.setStyleSheet("border:none;")
            self.navigate_button_3.setIcon(
                QtGui.QIcon(functions.resource_path("images/Menu_dark.png"))
            )

            self.on_click_complete_label_3.setStyleSheet(
                "QLabel {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none;}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
            )
            # self.set_new_hotkey_1.setStyleSheet
            self.profile_button_3.setStyleSheet("border: none;")
            self.profile_button_3.setIcon(
                QtGui.QIcon(functions.resource_path("images/Profile-Picture_dark"))
            )
            self.home_start_stop_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.add_record_line_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.playback_start_stop_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.record_start_stop_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.mouse_location_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.frame.setStyleSheet(
                "QFrame {border: 1.5px solid #bfcfb2;"
                "border-radius: 10px;}"
                "QComboBox::drop-down {"
                "background-color: rgb(249, 249, 245);"
                "border-color: rgb(249, 249, 245);}"
            )
            self.frame_2.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_3.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_4.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_10.setStyleSheet(
                "border: 2px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_11.setStyleSheet(
                "border: 2px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_16.setStyleSheet(
                "border: 2px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_12.setStyleSheet(
                "border: 2px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_13.setStyleSheet(
                "border: 2px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_14.setStyleSheet(
                "border: 2px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.view_settings_frame.setStyleSheet(
                "QFrame {background-color: #10131b;" "color: #bfcfb2;" "border: none;}"
            )
            self.frame_6.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_7.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_8.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.frame_9.setStyleSheet(
                "border: 1.5px solid #bfcfb2;" "border-radius: 10px;"
            )
            self.record_scroll_area.setStyleSheet(
                "QScrollArea {border: 1.5px solid #bfcfb2;"
                "background-color: #10131b;"
                "border-radius: 5px;}"
            )
            self.scrollAreaWidgetContents.setStyleSheet(
                "border: none;" "background-color: #10131b"
            )

            self.scroll_bar.setStyleSheet(
                """QScrollBar:vertical {
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
                                          background-color: #10131b;}"""
            )
            for row in self.scrollAreaWidgetContents.children():
                for button in row.findChildren(QPushButton):
                    button.setStyleSheet("background-color: #10131b")
            self.record_record_button.setStyleSheet(
                "QPushButton {color: white;"
                "border: 2px solid white;"
                "border-radius: 5px;"
                "color: white;}"
                "QPushButton::hover {color:black;"
                "background-color: white;}"
            )
            self.record_play_button.setStyleSheet(
                "QPushButton {color: #c98860;"
                "border: 2px solid #c98860;"
                "border-radius: 5px;"
                "color: #c98860;}"
                "QPushButton::hover {color:white;"
                "background-color: #c98860;}"
            )
            self.record_play_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/run_dark"))
            )
            self.record_save_button.setStyleSheet(
                "QPushButton {color: #1ecd97;"
                "border: 2px solid #1ecd97;"
                "border-radius: 5px;"
                "color: #1ecd97;}"
                "QPushButton::hover {color:white;"
                "background-color: #1ecd97;}"
            )
            self.record_remove_all_button.setStyleSheet(
                "QPushButton {color: #ffa94d;"
                "border: 2px solid #ffa94d;"
                "border-radius: 5px;"
                "color: #ffa94d;}"
                "QPushButton::hover {color:white;"
                "background-color: #ffa94d;}"
            )
            self.record_load_button.setStyleSheet(
                "QPushButton {color: black;"
                "background-color: #bfcfb2;"
                "border 1px solid #bfcfb2;"
                "border-radius: 3px;}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
            )
            self.record_load_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/uplode_dark.png"))
            )
            self.record_add_button.setStyleSheet(
                "QPushButton {border: 1px solid rgb(196, 177, 174);"
                "border-radius: 10;"
                "background-color: #bfcfb2;}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
            )
            self.record_add_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-ui-64.png"))
            )
            self.label_21.setStyleSheet("color: black;" "background-color: #e0e0e0;")
            self.label_25.setStyleSheet("color: black;" "background-color: #e0e0e0;")
            self.label_22.setStyleSheet("color: black;" "background-color: #e0e0e0;")
            self.label_23.setStyleSheet("color: black;" "background-color: #e0e0e0;")
            self.label_24.setStyleSheet("color: black;" "background-color: #e0e0e0;")
            self.theme_button.disconnect()
            self.theme_button.clicked.connect(self.get_normal_theme)
            if self.hide_to_tray_checkbox.isChecked():
                self.hide_to_tray_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                )
            else:
                self.hide_to_tray_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
            self.hide_to_tray_checkbox2.setStyleSheet(
                "border: none;" "background-color: #10131b;"
            )
            if self.show_after_complete_checkbox.isChecked():
                self.show_after_complete_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                )
            else:
                self.show_after_complete_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
            self.show_after_complete_checkbox2.setStyleSheet(
                "border: none;" "background-color: #10131b;"
            )
            if self.mouse_location_checkbox.isChecked():
                self.mouse_location_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                )
            else:
                self.mouse_location_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
            self.mouse_location_checkbox2.setStyleSheet(
                "border: none;" "background-color: #10131b;"
            )
            if self.small_window_checkbox.isChecked():
                self.small_window_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                )
            else:
                self.small_window_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox_dark"))
                )
            self.small_window_checkbox2.setStyleSheet(
                "border: none;" "background-color: #10131b;"
            )
            logger.info("ending function to activate dark theme")
        except:
            logger.error("exception in activate dark theme()", exc_info=True)

    # activates normal theme
    def get_normal_theme(self):
        try:
            logger.info("starting function to activate normal theme")
            self.setStyleSheet(
                "QComboBox::drop-down {"
                "background-color: rgb(249, 249, 245);"
                "border-color: rgb(249, 249, 245);}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
                "QRadioButton::indicator {"
                "height: 15px;"
                "width: 15px;}"
                "QRadioButton::indicator::unchecked {"
                "image: url(:/images/radio_unchecked.png);"
                "margin-top: 2px;}"
                "QRadioButton::indicator::checked {"
                "image: url(:/images/radio_checked.png);"
                "margin-top: 2px;}"
            )
            self.dark_theme_activated = False
            self.left_frame.setStyleSheet(
                "background-color: rgb(196, 177, 174);"
                "color: black;"
                "border: 2px solid rgb(196, 177, 174);"
                "border-radius: 10px;"
            )
            self.GG_icon.setStyleSheet("border:none;")
            self.GG_icon.setIcon(QtGui.QIcon(functions.resource_path("images/GGicon")))
            self.home_button.setStyleSheet("border:none;")
            self.home_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/home"))
            )
            self.record_button.setStyleSheet("border:none;")
            self.record_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Record"))
            )
            self.theme_button.setStyleSheet("border:none;")
            self.theme_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Mode.png"))
            )
            self.view_settings_button.setStyleSheet("border:none;")
            self.view_settings_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/Settings.png"))
            )
            self.hotkey_settings_button.setStyleSheet("border:none;")
            self.hotkey_settings_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/HotkeyBlack.png"))
            )
            self.central_widget_2.setStyleSheet(
                "QFrame {background-color: rgb(239, 229, 220);"
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
                "border: none;}"
            )
            self.main_frame.setStyleSheet(
                "QFrame {background-color: rgb(239, 229, 220);"
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
                "border: none;}"
            )
            # self.top_frame.setStyleSheet("QFrame {background-color: rgb(239, 229, 220);"
            #                              "color: rgb(30, 30, 30);"
            #                              "border: none;}"
            #                              "QComboBox {color: rgb(30, 30, 30);"
            #                              "background-color: rgb(249, 249, 245);"
            #                              "border: 1px solid;"
            #                              "border-radius: 3px;}"
            #                              "QLineEdit {color: rgb(30, 30, 30);"
            #                              "background-color: rgb(249, 249, 245);"
            #                              "border: 1px solid;"
            #                              "border-radius: 3px solid;}"
            #                              "QRadioButton {color: rgb(30, 30, 30);"
            #                              "border: none;}")
            self.top_frame_logged_out.setStyleSheet(
                "QFrame {background-color: rgb(239, 229, 220);"
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
                "border: none;}"
            )
            self.home_frame.setStyleSheet(
                "QFrame {background-color: rgb(239, 229, 220);"
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
                "border: none;}"
            )
            self.reset_settings_button.setStyleSheet(
                "QPushButton {color: rgb(255, 162, 0);"
                "border: 2px solid rgb(255, 162, 0);"
                "border-radius: 5px;"
                "color: #ffa94d;}"
                "QPushButton::hover {color:white;"
                "background-color: rgb(255, 162, 0);}"
            )
            self.play_button.setStyleSheet(
                "QPushButton {color: #3A5A40;"
                "border: 2px solid #3A5A40;"
                "border-radius: 5px;"
                "color: #3A5A40;}"
                "QPushButton::hover {color:white;"
                "background-color: #3A5A40;}"
            )
            self.play_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/run.png"))
            )
            self.save_settings_button.setStyleSheet(
                "QPushButton {color: rgb(3, 199, 26);"
                "border: 2px solid rgb(3, 199, 26);"
                "border-radius:5px; "
                "color: rgb(3, 199, 26);}"
                "QPushButton::hover {color:white;"
                "background-color: rgb(3, 199, 26);}"
            )
            self.foot_note_label.setStyleSheet("border:none;")

            self.navigate_button_3.setStyleSheet("border:none;")
            self.navigate_button_3.setIcon(
                QtGui.QIcon(functions.resource_path("images/Hambuger"))
            )
            self.navigation_frame.setStyleSheet(
                "QPushButton {background-color: rgb(242,242,242);"
                "border: 1px solid rgb(204, 204, 204);"
                "color: rgb(30, 30, 30);}"
            )
            self.on_click_complete_label_3.setStyleSheet(
                "QLabel {color: black;"
                "background-color: rgb(249, 249, 245);"
                "border: none;}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
            )
            self.profile_button_3.setStyleSheet("border: none;")
            self.profile_button_3.setIcon(
                QtGui.QIcon(functions.resource_path("images/liliajohn.png"))
            )
            self.home_start_stop_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.add_record_line_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.playback_start_stop_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.record_start_stop_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.mouse_location_hotkey_label.setStyleSheet(
                "color: black;"
                "border: 1px solid #bfcfb2;"
                "border-radius: 5px;"
                "background-color: rgb(249, 249, 245);"
            )
            self.frame.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_2.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_3.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_4.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_10.setStyleSheet(
                "border: 2px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_11.setStyleSheet(
                "border: 2px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_16.setStyleSheet(
                "border: 2px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_12.setStyleSheet(
                "border: 2px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_13.setStyleSheet(
                "border: 2px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_14.setStyleSheet(
                "border: 2px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.view_settings_frame.setStyleSheet(
                "QFrame {background-color: rgb(239, 229, 220);"
                "color: rgb(30, 30, 30);"
                "border: none;}"
            )
            self.frame_6.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_7.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_8.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.frame_9.setStyleSheet(
                "border: 1.5px solid rgb(196, 177, 174);" "border-radius: 10px;"
            )
            self.record_scroll_area.setStyleSheet(
                "QScrollArea {border: 1.5px solid #c8bab7;"
                "background-color: rgb(239, 229, 220);"
                "border-radius: 5px;}"
            )
            self.scrollAreaWidgetContents.setStyleSheet(
                "border: none;" "background-color: rgb(239, 229, 220)"
            )
            self.scroll_bar.setStyleSheet(
                """QScrollBar:vertical {
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
                                          background-color: rgb(239, 229, 220);}"""
            )
            for row in self.scrollAreaWidgetContents.children():
                for button in row.findChildren(QPushButton):
                    button.setStyleSheet("background-color: rgb(239, 229, 220)")
            self.record_record_button.setStyleSheet(
                "QPushButton {color: black;"
                "border: 2px solid black;"
                "border-radius: 5px;"
                "color: black;}"
                "QPushButton::hover {color: white;"
                "background-color: black;}"
            )
            self.record_play_button.setStyleSheet(
                "QPushButton {color: #3A5A40;"
                "border: 2px solid #3A5A40;"
                "border-radius: 5px;"
                "color: #3A5A40;}"
                "QPushButton::hover {color:white;"
                "background-color: #3A5A40;}"
            )
            self.record_play_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/run_dark"))
            )
            self.record_save_button.setStyleSheet(
                "QPushButton {color: rgb(3, 199, 26);"
                "border: 2px solid rgb(3, 199, 26);"
                "border-radius: 5px;"
                "color: rgb(3, 199, 26);}"
                "QPushButton::hover {color:white;"
                "background-color: rgb(3, 199, 26);}"
            )
            self.record_remove_all_button.setStyleSheet(
                "QPushButton {color: rgb(255, 162, 0);"
                "border-radius: 5px;"
                "border: 2px solid rgb(255, 162, 0);"
                "color: rgb(255, 162, 0);}"
                "QPushButton::hover {color:white;"
                "background-color: rgb(255, 162, 0);}"
            )
            self.record_load_button.setStyleSheet(
                "QPushButton {color: white;"
                "background-color: #5579c7;"
                "border 1px solid #5579c7;"
                "border-radius: 3px;}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
            )
            self.record_load_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-upload-96.png"))
            )
            self.record_add_button.setStyleSheet(
                "QPushButton {border: 1px solid rgb(196, 177, 174);"
                "border-radius: 10;"
                "background-color:  #c1b3b0;}"
                "QToolTip {"
                "background-color: #e0e0e0;"
                "border: none;}"
            )
            self.record_add_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-ui-64.png"))
            )
            self.theme_button.clicked.disconnect()
            self.theme_button.clicked.connect(self.get_dark_theme)
            if self.hide_to_tray_checkbox.isChecked():
                self.hide_to_tray_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon"))
                )
            else:
                self.hide_to_tray_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
            self.hide_to_tray_checkbox2.setStyleSheet(
                "border: none;" "background-color: rgb(239, 229, 220);"
            )
            if self.show_after_complete_checkbox.isChecked():
                self.show_after_complete_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon"))
                )
            else:
                self.show_after_complete_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
            self.show_after_complete_checkbox2.setStyleSheet(
                "border: none;" "background-color: rgb(239, 229, 220);"
            )
            if self.mouse_location_checkbox.isChecked():
                self.mouse_location_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon"))
                )
            else:
                self.mouse_location_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
            self.mouse_location_checkbox2.setStyleSheet(
                "border: none;" "background-color: rgb(239, 229, 220);"
            )
            if self.small_window_checkbox.isChecked():
                self.small_window_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/check_icon"))
                )
            else:
                self.small_window_checkbox2.setIcon(
                    QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                )
            self.small_window_checkbox2.setStyleSheet(
                "border: none;" "background-color: rgb(239, 229, 220);"
            )
            logger.info("ending function to activate dark theme")
        except:
            logger.error("exception in get_normal_theme()", exc_info=True)

    # gets home screen in front
    def get_home_screen(self):
        try:
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            # try:
            #     keyboard.remove_hotkey(self.record_start_stop_hotkey)
            # except:
            #     logger.info("record_start_stop_hotkey was not active")
            # try:
            #     keyboard.remove_hotkey(self.record_recording_hotkey)
            # except:
            #     logger.info("record_recording_hotkey was not active")
            # try:
            #     keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
            # except:
            #     logger.error("error in adding mouse location hotkey", exc_info=True)

            # try:
            #     keyboard.add_hotkey(
            #         self.home_start_stop_hotkey, lambda: self.play_button.click()
            #     )
            # except:
            #     logger.error("error in adding home start stop hotkey", exc_info=True)

            self.navigation_frame.lower()
            self.home_frame.show()

            self.record_frame.hide()
            self.view_settings_frame.hide()
            self.hotkey_settings_frame.hide()
            self.foot_note_label.setText("")
        except:
            logger.error("exception in get_home_screen()", exc_info=True)

    def get_record_screen(self):
        logger.info("getting record screen to front")
        try:

            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.error(
                    "error in removing record line hotkey", exc_info=True
                )
            keyboard.add_hotkey(
                self.add_record_line_hotkey, lambda: self.record_add_button.click()
            )
            try:
                keyboard.remove_hotkey(self.record_start_stop_hotkey)
            except:
                logger.error(
                    "error in removing record start stop hotkey", exc_info=True
                )
            keyboard.add_hotkey(
                self.record_start_stop_hotkey, lambda: self.record_play_button.click()
            )
            try:
                keyboard.remove_hotkey(self.record_recording_hotkey)
            except:
                logger.error(
                    "error in removing record recording hotkey", exc_info=True
                )
            keyboard.add_hotkey(
                self.record_recording_hotkey, lambda: self.record_record_button.click()
            )
            self.navigation_frame.lower()
            self.view_settings_frame.hide()
            self.hotkey_settings_frame.hide()
            self.home_frame.hide()
            self.foot_note_label.setText("")
            self.record_frame.show()
        except:
            logger.error("exception in get_record_screen()", exc_info=True)

    # gets view settings screen in front
    def get_view_screen(self):
        try:
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            # try:
            #     keyboard.remove_hotkey(self.record_start_stop_hotkey)
            # except:
            #     logger.info("record_start_stop_hotkey was not active")
            # try:
            #     keyboard.remove_hotkey(self.record_recording_hotkey)
            # except:
            #     logger.info("record_recording_hotkey was not active")
            self.navigation_frame.lower()

            self.record_frame.hide()
            self.view_settings_frame.show()
            self.hotkey_settings_frame.hide()
            self.home_frame.hide()
            self.foot_note_label.setText("")
        except:
            logger.error("exception in get_view_screen()", exc_info=True)

    # gets hotkey settings screen in front
    def get_hotkey_screen(self):
        try:
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            # try:
            #     keyboard.remove_hotkey(self.record_start_stop_hotkey)
            # except:
            #     logger.info("record_start_stop_hotkey was not active")
            # try:
            #     keyboard.remove_hotkey(self.record_recording_hotkey)
            # except:
            #     logger.info("record_recording_hotkey was not active")
            # try:
            #     keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
            # except:
            #     logger.error("error in adding mouse location hotkey", exc_info=True)

            self.navigation_frame.lower()

            self.record_frame.hide()
            self.view_settings_frame.hide()
            self.hotkey_settings_frame.show()
            self.home_frame.hide()

            self.foot_note_label.setText("")
        except:
            logger.error("exception in get_hotkey_screen()", exc_info=True)

    # changes hotkey of home -> start/stop button
    def change_home_start_hotkey(self):
        try:
            logger.info("starting function to change_home_start/stop_hotkey")
            self.label_21.show()
            try:
                keyboard.remove_hotkey(self.home_start_stop_hotkey)
            except:
                logger.error("error in removing home start stop hotkey", exc_info=True)
            self.home_start_stop_hotkey_label.setText("")
            self.set_new_hotkey_button_1.setEnabled(False)
            self.set_new_hotkey_button_6.setEnabled(False)
            self.set_new_hotkey_button_2.setEnabled(False)
            self.set_new_hotkey_button_3.setEnabled(False)
            self.set_new_hotkey_button_4.setEnabled(False)
            new_hotkey = ""
            keyboard.start_recording()
            keyboard.wait("enter")
            pressed_keys = keyboard.stop_recording()
            for key in pressed_keys:
                if str(key)[-11:-6] == "enter":
                    continue
                if str(key)[-5:] == "down)":
                    if new_hotkey != "":
                        new_hotkey += " + "
                    new_hotkey += str(key)[14:-6]
            new_hotkey = new_hotkey.replace(" + enter ", "")
            if new_hotkey == "":
                keyboard.add_hotkey(
                    self.home_start_stop_hotkey, lambda: self.play_button.click()
                )
                self.home_start_stop_hotkey_label.setText(
                    str(self.home_start_stop_hotkey)
                )
            else:
                try:
                    self.home_start_stop_hotkey = new_hotkey
                    keyboard.add_hotkey(
                        self.home_start_stop_hotkey, lambda: self.play_button.click()
                    )
                    self.home_start_stop_hotkey_label.setText(new_hotkey)
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    keyboard.add_hotkey(
                        self.home_start_stop_hotkey, lambda: self.play_button.click()
                    )
                    self.home_start_stop_hotkey_label.setText(
                        str(self.home_start_stop_hotkey)
                    )
            self.set_new_hotkey_button_1.setEnabled(True)
            self.set_new_hotkey_button_6.setEnabled(True)
            self.set_new_hotkey_button_2.setEnabled(True)
            self.set_new_hotkey_button_3.setEnabled(True)
            self.set_new_hotkey_button_4.setEnabled(True)
            self.label_21.hide()
            logger.info("ending function to change_home_start/stop_hotkey")
        except:
            logger.error("exception in change_home_start_hotkey()", exc_info=True)

    # changes hotkey of record add line button
    def change_add_record_line_hotkey(self):
        try:
            logger.info("starting function to change_add_record_line_hotkey")
            self.label_25.show()
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            self.add_record_line_hotkey_label.setText("")
            self.set_new_hotkey_button_1.setEnabled(False)
            self.set_new_hotkey_button_6.setEnabled(False)
            self.set_new_hotkey_button_2.setEnabled(False)
            self.set_new_hotkey_button_3.setEnabled(False)
            self.set_new_hotkey_button_4.setEnabled(False)
            new_hotkey = ""
            keyboard.start_recording()
            keyboard.wait("enter")
            pressed_keys = keyboard.stop_recording()
            for key in pressed_keys:
                if str(key)[-11:-6] == "enter":
                    continue
                if str(key)[-5:] == "down)":
                    if new_hotkey != "":
                        new_hotkey += " + "
                    new_hotkey += str(key)[14:-6]
            new_hotkey = new_hotkey.replace(" + enter ", "")
            if new_hotkey == "":
                keyboard.add_hotkey(self.add_record_line_hotkey, lambda: self.record_add_button.click())
                self.add_record_line_hotkey_label.setText(
                    str(self.add_record_line_hotkey)
                )
            else:
                try:
                    self.add_record_line_hotkey = new_hotkey
                    keyboard.add_hotkey(self.add_record_line_hotkey, lambda: self.record_add_button.click())
                    self.add_record_line_hotkey_label.setText(new_hotkey)
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    keyboard.add_hotkey(
                        self.add_record_line_hotkey,
                        lambda: self.record_add_button.click(),
                    )
                    self.add_record_line_hotkey_label.setText(
                        str(self.add_record_line_hotkey)
                    )
            self.set_new_hotkey_button_1.setEnabled(True)
            self.set_new_hotkey_button_6.setEnabled(True)
            self.set_new_hotkey_button_2.setEnabled(True)
            self.set_new_hotkey_button_3.setEnabled(True)
            self.set_new_hotkey_button_4.setEnabled(True)
            self.label_25.hide()
            logger.info("ending function to change_add_record_line_hotkey")
        except:
            logger.error("exception in change_add_record_line_hotkey()", exc_info=True)

    # changes hotkey of record -> start/stop button
    def change_record_start_hotkey(self):
        try:
            logger.info("starting function to change_record_start/stop_hotkey")
            self.label_23.show()
            try:
                keyboard.remove_hotkey(self.record_start_stop_hotkey)
            except:
                logger.error(
                    "error in removing playback start stop hotkey", exc_info=True
                )
            self.playback_start_stop_hotkey_label.setText("")
            self.set_new_hotkey_button_1.setEnabled(False)
            self.set_new_hotkey_button_6.setEnabled(False)
            self.set_new_hotkey_button_2.setEnabled(False)
            self.set_new_hotkey_button_3.setEnabled(False)
            self.set_new_hotkey_button_4.setEnabled(False)
            new_hotkey = ""
            keyboard.start_recording()
            keyboard.wait("enter")
            pressed_keys = keyboard.stop_recording()
            for key in pressed_keys:
                if str(key)[-11:-6] == "enter":
                    continue
                if str(key)[-5:] == "down)":
                    if new_hotkey != "":
                        new_hotkey += " + "
                    new_hotkey += str(key)[14:-6]
            new_hotkey = new_hotkey.replace(" + enter ", "")
            if new_hotkey == "":
                keyboard.add_hotkey(
                    self.record_start_stop_hotkey,
                    lambda: self.record_play_button.click(),
                )
                self.playback_start_stop_hotkey_label.setText(
                    str(self.record_start_stop_hotkey)
                )
            else:
                try:
                    self.record_start_stop_hotkey = new_hotkey
                    keyboard.add_hotkey(
                        self.record_start_stop_hotkey,
                        lambda: self.record_play_button.click(),
                    )
                    self.playback_start_stop_hotkey_label.setText(new_hotkey)
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    keyboard.add_hotkey(
                        self.record_start_stop_hotkey,
                        lambda: self.record_play_button.click(),
                    )
                    self.playback_start_stop_hotkey_label.setText(
                        str(self.record_start_stop_hotkey)
                    )
            self.set_new_hotkey_button_1.setEnabled(True)
            self.set_new_hotkey_button_6.setEnabled(True)
            self.set_new_hotkey_button_2.setEnabled(True)
            self.set_new_hotkey_button_3.setEnabled(True)
            self.set_new_hotkey_button_4.setEnabled(True)
            self.label_23.hide()
            logger.info("ending function to change_record_start/stop_hotkey")
        except:
            logger.error("exception in change_add_record_start_hotkey()", exc_info=True)

    # changes hotkey of getting mouse location
    def change_mouse_location_hotkey(self):
        try:
            logger.info("starting function to change_mouse_location_hotkey")
            self.label_22.show()
            try:
                keyboard.remove_hotkey(self.mouse_location_hotkey)
            except:
                logger.error("error in removing mouse location hotkey", exc_info=True)
            self.mouse_location_hotkey_label.setText("")
            self.set_new_hotkey_button_1.setEnabled(False)
            self.set_new_hotkey_button_6.setEnabled(False)
            self.set_new_hotkey_button_2.setEnabled(False)
            self.set_new_hotkey_button_3.setEnabled(False)
            self.set_new_hotkey_button_4.setEnabled(False)
            new_hotkey = ""
            keyboard.start_recording()
            keyboard.wait("enter")
            pressed_keys = keyboard.stop_recording()
            for key in pressed_keys:
                if str(key)[-11:-6] == "enter":
                    continue
                if str(key)[-5:] == "down)":
                    if new_hotkey != "":
                        new_hotkey += " + "
                    new_hotkey += str(key)[14:-6]
            new_hotkey = new_hotkey.replace(" + enter ", "")
            if new_hotkey == "":
                keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
                self.mouse_location_hotkey_label.setText(
                    str(self.mouse_location_hotkey)
                )
            else:
                try:
                    self.mouse_location_hotkey = new_hotkey
                    keyboard.add_hotkey(
                        self.mouse_location_hotkey, self.get_mouse_location
                    )
                    self.mouse_location_hotkey_label.setText(new_hotkey)
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    keyboard.add_hotkey(
                        self.mouse_location_hotkey, self.get_mouse_location
                    )
                    self.mouse_location_hotkey_label.setText(
                        str(self.mouse_location_hotkey)
                    )
            self.set_new_hotkey_button_1.setEnabled(True)
            self.set_new_hotkey_button_6.setEnabled(True)
            self.set_new_hotkey_button_2.setEnabled(True)
            self.set_new_hotkey_button_3.setEnabled(True)
            self.set_new_hotkey_button_4.setEnabled(True)
            self.label_22.hide()
            logger.info("ending function to change_mouse_location_hotkey")
        except:
            logger.error("exception in change_mouse_location_hotkey()", exc_info=True)

    # changes hotkey of record -> recording button
    def change_recording_hotkey(self):
        try:
            logger.info("starting function to change_recording_button_hotkey")
            self.label_24.show()
            try:
                keyboard.remove_hotkey(self.record_recording_hotkey)
            except:
                logger.error("error in removing screen recording hotkey", exc_info=True)
            self.record_start_stop_hotkey_label.setText("")
            self.set_new_hotkey_button_1.setEnabled(False)
            self.set_new_hotkey_button_6.setEnabled(False)
            self.set_new_hotkey_button_2.setEnabled(False)
            self.set_new_hotkey_button_3.setEnabled(False)
            self.set_new_hotkey_button_4.setEnabled(False)
            new_hotkey = ""
            keyboard.start_recording()
            keyboard.wait("enter")
            pressed_keys = keyboard.stop_recording()
            for key in pressed_keys:
                if str(key)[-11:-6] == "enter":
                    continue
                if str(key)[-5:] == "down)":
                    if new_hotkey != "":
                        new_hotkey += " + "
                    new_hotkey += str(key)[14:-6]
            new_hotkey = new_hotkey.replace(" + enter ", "")
            if new_hotkey == "":
                keyboard.add_hotkey(
                    self.record_recording_hotkey,
                    lambda: self.record_record_button.click(),
                )
                self.record_start_stop_hotkey_label.setText(
                    str(self.record_recording_hotkey)
                )
            else:
                try:
                    self.record_recording_hotkey = new_hotkey
                    keyboard.add_hotkey(
                        self.record_recording_hotkey,
                        lambda: self.record_record_button.click(),
                    )
                    self.record_start_stop_hotkey_label.setText(new_hotkey)
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    keyboard.add_hotkey(
                        self.record_recording_hotkey,
                        lambda: self.record_record_button.click(),
                    )
                    self.record_start_stop_hotkey_label.setText(
                        str(self.record_recording_hotkey)
                    )
            self.set_new_hotkey_button_1.setEnabled(True)
            self.set_new_hotkey_button_6.setEnabled(True)
            self.set_new_hotkey_button_2.setEnabled(True)
            self.set_new_hotkey_button_3.setEnabled(True)
            self.set_new_hotkey_button_4.setEnabled(True)
            self.label_24.hide()
            logger.info("ending function to change_recording_button_hotkey")
        except:
            logger.error("exception in change_recording_button_hotkey()", exc_info=True)

    # starts thread for hotkey change of home -> start_stop button
    def start_thread_hotkey_1(self):
        try:
            change_home_start_hotkey_thread = threading.Thread(
                target=self.change_home_start_hotkey
            )
            # change_home_start_hotkey_thread.setDaemon(True)
            change_home_start_hotkey_thread.start()
            logger.info("starting thread for hotkey change of home start stop")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
        except:
            logger.error("exception in start_thread_hotkey_1()", exc_info=True)

    # starts thread for hotkey change of add record line button
    def start_thread_hotkey_6(self):
        try:
            change_add_record_line_hotkey_thread = threading.Thread(
                target=self.change_add_record_line_hotkey
            )
            # change_add_record_line_hotkey_thread.setDaemon(True)
            change_add_record_line_hotkey_thread.start()
            logger.info("starting thread for hotkey change of add record line")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
        except:
            logger.error("exception in start_thread_hotkey_6()", exc_info=True)

    # starts thread for hotkey change of record -> start_stop button
    def start_thread_hotkey_2(self):
        try:
            change_record_start_hotkey_thread = threading.Thread(
                target=self.change_record_start_hotkey
            )
            # change_record_start_hotkey_thread.setDaemon(True)
            change_record_start_hotkey_thread.start()
            logger.info("starting thread for record change of home start stop")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
        except:
            logger.error("exception in start_thread_hotkey_2()", exc_info=True)

    # starts thread for hotkey change of getting mouse location
    def start_thread_hotkey_3(self):
        try:
            change_mouse_location_hotkey_thread = threading.Thread(
                target=self.change_mouse_location_hotkey
            )
            # change_mouse_location_hotkey_thread.setDaemon(True)
            change_mouse_location_hotkey_thread.start()
            logger.info("starting thread for getting mouse location")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
        except:
            logger.error("exception in start_thread_hotkey_3()", exc_info=True)

    # starts thread for hotkey change of record -> record button
    def start_thread_hotkey_4(self):
        try:
            change_recording_hotkey_thread = threading.Thread(
                target=self.change_recording_hotkey
            )
            # change_recording_hotkey_thread.setDaemon(True)
            change_recording_hotkey_thread.start()
            logger.info("starting thread for hotkey change of record button")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
        except:
            logger.error("exception in start_thread_hotkey_4()", exc_info=True)

    # opens the menu bar
    def open_menu(self):
        try:
            self.navigation_frame.raise_()

            self.navigate_button_3.clicked.disconnect()
            self.navigate_button_3.clicked.connect(self.close_menu)
        except:
            logger.error("exception in open_menu()", exc_info=True)

    # closes the menu bar
    def close_menu(self):
        try:
            self.navigation_frame.lower()

            self.navigate_button_3.clicked.disconnect()
            self.navigate_button_3.clicked.connect(self.open_menu)
        except:
            logger.error("exception in close_menu()", exc_info=True)

    # triggered by record -> save button (pop-up window)
    def window_record_save(self):
        try:
            logger.info(
                "starting function to open pop up window to save record screen actions"
            )
            if self.i == 1:
                self.popup = UI_no_actions(self)
                self.popup.show()
                logger.error("No actions available to save. Nothing to save!")
                logger.info(
                    "ending function to open pop up window to save record screen actions"
                )
                return
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            self.font.setBold(False)
            self.font.setPixelSize(11)
            # self.record_save_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
            self.record_save_window = new_dialog(self)

            self.record_save_window.setWindowTitle("Save")
            self.record_save_window.setWindowIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-save-90"))
            )
            # sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            # self.record_save_window.setGeometry(int(self.screen_width/2.3), int(self.screen_height/2.3), int(self.screen_width/6.4), int(self.screen_height/10.4))
            self.record_save_window.setGeometry(827, 520, 300, 115)
            self.record_save_window.setFixedWidth(300)
            # self.record_save_window.setFixedWidth(int(self.screen_width/6.4))
            # self.record_save_window.setFixedHeight(int(self.screen_height/10.4))
            self.record_save_window.setFixedHeight(115)
            self.invisible_widget_1 = QWidget(self.record_save_window)
            self.record_save_layout = QGridLayout(self.invisible_widget_1)
            self.record_save_name_box = QLineEdit(self.invisible_widget_1)
            self.record_save_name_box.setAlignment(Qt.AlignRight)
            self.record_save_name_label = QLabel(self.invisible_widget_1)
            self.record_save_button_pc = QPushButton(self.invisible_widget_1)
            self.record_save_button_db = QPushButton(self.invisible_widget_1)
            self.record_save_footnote = QLabel(self.invisible_widget_1)
            # self.invisible_widget_1.setGeometry(0, 0, int(self.sizeObject.width()/6.4), int(self.sizeObject.height()/10.4))
            self.invisible_widget_1.setGeometry(0, 0, 300, 115)
            if self.dark_theme_activated:
                self.invisible_widget_1.setStyleSheet("background-color: #10131b;")
            else:
                self.invisible_widget_1.setStyleSheet(
                    "background-color: rgb(239, 229, 220);"
                )
            self.record_save_name_box.clear()
            self.record_save_frame1 = QFrame(self.invisible_widget_1)
            self.record_save_frame1.setGeometry(10, 8, 280, 91)
            if self.dark_theme_activated:
                self.record_save_frame1.setStyleSheet(
                    "border: 1px solid #bfcfb2;" "border-radius: 5px;"
                )
            else:
                self.record_save_frame1.setStyleSheet(
                    "border: 1px solid rgb(196, 174, 174);" "border-radius: 5px;"
                )
            self.record_save_frame1.lower()
            self.record_save_name_box.setGeometry(20, 22, 260, 30)
            if self.dark_theme_activated:
                self.record_save_name_box.setStyleSheet(
                    "background-color: #10131b;;"
                    "border: 1px solid #bfcfb2;"
                    "border-radius: none;"
                    "color: #bfcfb2"
                )
            else:
                self.record_save_name_box.setStyleSheet(
                    "background-color: rgb(239, 229, 220);"
                    "border: 1px solid rgb(196, 177, 174);"
                    "border-radius: none;"
                )
            self.record_save_name_box.setFont(self.font)
            self.record_save_name_label.setText("  Name your loop")
            if self.dark_theme_activated:
                self.record_save_name_label.setStyleSheet(
                    "color: #bfcfb2;" "font-weight: bold"
                )
            else:
                self.record_save_name_label.setStyleSheet(
                    "color: black;" "font-weight: bold"
                )
            self.record_save_name_label.setGeometry(26, 14, 98, 15)
            self.record_save_name_label.setFont(self.font)
            self.record_save_button_pc.setIcon(
                QtGui.QIcon(functions.resource_path("images/CPU"))
            )
            self.record_save_button_pc.setGeometry(30, 60, 115, 30)
            self.record_save_button_pc.setText(" Save to PC")
            self.record_save_button_pc.clicked.connect(self.record_save_settings_pc)
            if self.dark_theme_activated:
                self.record_save_button_pc.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid #bfcfb2;}"
                )
            else:
                self.record_save_button_pc.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(158, 143, 141);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid rgb(158, 143, 141)}"
                )
            self.record_save_button_pc.setFont(self.font)
            self.record_save_button_db.setIcon(
                QtGui.QIcon(functions.resource_path("images/app_logo"))
            )
            self.record_save_button_db.setGeometry(160, 60, 115, 30)
            self.record_save_button_db.setText(" Save in App")
            self.record_save_button_db.clicked.connect(self.record_save_settings)
            if self.dark_theme_activated:
                self.record_save_button_db.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid #bfcfb2;}"
                )
            else:
                self.record_save_button_db.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(158, 143, 141);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid rgb(158, 143, 141)}"
                )
            self.record_save_button_db.setFont(self.font)
            self.record_save_footnote.setGeometry(10, 99, 280, 13)
            self.record_save_footnote.setText("")
            self.record_save_footnote.setStyleSheet("color: red;")
            self.record_save_footnote.setFont(self.font)
            self.record_save_window.show()
            logger.info(
                "ending function to open pop up window to save record screen actions"
            )
        except:
            logger.error("exception in window_record_save()", exc_info=True)

    # saves the actions list from record screen into app
    def record_save_settings(self):
        try:
            logger.info("starting function to save record screen actions into app")
            if self.i == 1:
                self.foot_note_label.setText("error: no actions available")
                logger.info("ending function to save record screen actions into app")
                return
            actions_data = []
            save_name = self.record_save_name_box.text()
            if save_name == "":
                self.record_save_footnote.setText("error: name is needed")
                logger.info("ending function to save record screen actions into app")
                return
            for a in range(self.i - 1):
                csv_list = []
                row_elements = self.line_list[a][1].children()
                if self.line_list[a][0] == "mouse":
                    csv_list.append("mouse")
                    for b in (3, 5):
                        if row_elements[b].text() == "":
                            self.foot_note_label.setText(
                                "error: x and y location are needed"
                            )
                            logger.info(
                                "ending function to save record screen actions into app"
                            )
                            return
                        else:
                            csv_list.append(row_elements[b].text())
                    for b in (7, 9):
                        csv_list.append(row_elements[b].currentText())
                    if row_elements[11].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[11].text())
                elif self.line_list[a][0] == "keyboard":
                    csv_list.append("keyboard")
                    csv_list.append(row_elements[3].text())
                    csv_list.append(row_elements[5].currentText())
                    csv_list.append(row_elements[7].currentText())
                    if row_elements[9].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[9].text())
                elif self.line_list[a][0] == "scroll":
                    csv_list.append("scroll")
                    for b in (3, 5):
                        if row_elements[b].text() == "":
                            self.foot_note_label.setText(
                                "error: x and y location are needed"
                            )
                            logger.info(
                                "ending function to save record screen actions into app"
                            )
                            return
                        else:
                            csv_list.append(row_elements[b].text())
                    csv_list.append(row_elements[7].currentText())
                    csv_list.append(row_elements[9].text())
                    if row_elements[11].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[11].text())
                csv_text = ", ".join(csv_list)
                actions_data.append(csv_text)
            full_csv_text = "---".join(actions_data)
            saved_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
            if self.repeat_for_number_2.text() == "":
                repeat_all = "1"
            else:
                repeat_all = self.repeat_for_number_2.text()
            if self.delay_2.text() == "":
                delay_time = "100"
            else:
                delay_time = self.delay_2.text()
            delay_type = self.delay_time_combobox_record.currentText()
            try:
                functions.add_run_record_db(
                    save_name,
                    full_csv_text,
                    saved_date,
                    repeat_all,
                    delay_time,
                    delay_type,
                )
                self.record_save_window.close()
            except sqlite3.IntegrityError:
                logger.error("Exception occurred", exc_info=True)
                self.record_save_footnote.setText("error: this name exists")
                logger.info("ending function to save record screen actions into app")
                return
            logger.info("ending function to save record screen actions into app")
        except:
            logger.error("exception in record_save_settings()", exc_info=True)

    # saves the actions list from record screen into pc
    def record_save_settings_pc(self):
        try:
            logger.info("starting function to save record screen actions into pc")
            if self.i == 1:
                self.foot_note_label.setText("error: no actions available")
                logger.info("ending function to save record screen actions into pc")
                return
            actions_data = []
            save_name = self.record_save_name_box.text()
            if save_name == "":
                self.record_save_footnote.setText("error: name is needed")
                logger.info("ending function to save record screen actions into pc")
                return
            for a in range(self.i - 1):
                csv_list = []
                row_elements = self.line_list[a][1].children()
                # print("************")
                # print(row_elements)
                # print("************")
                # print(self.line_list[a][1])
                # print("************")
                if self.line_list[a][0] == "mouse":
                    csv_list.append("mouse")
                    for b in (3, 5):
                        if row_elements[b].text() == "":
                            self.foot_note_label.setText(
                                "error: x and y location are needed"
                            )
                            logger.info(
                                "ending function to save record screen actions into pc"
                            )
                            return
                        else:
                            csv_list.append(row_elements[b].text())
                    for b in (7, 9):
                        csv_list.append(row_elements[b].currentText())
                    if row_elements[11].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[11].text())

                elif self.line_list[a][0] == "keyboard":
                    csv_list.append("keyboard")
                    csv_list.append(row_elements[3].text())
                    csv_list.append(row_elements[5].currentText())
                    csv_list.append(row_elements[7].currentText())
                    if row_elements[9].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[9].text())
                elif self.line_list[a][0] == "scroll":
                    csv_list.append("scroll")
                    for b in (3, 5):
                        if row_elements[b].text() == "":
                            self.foot_note_label.setText(
                                "error: x and y location are needed"
                            )
                            logger.info(
                                "ending function to save record screen actions into pc"
                            )
                            return
                        else:
                            csv_list.append(row_elements[b].text())
                    csv_list.append(row_elements[7].currentText())
                    csv_list.append(row_elements[9].text())
                    if row_elements[11].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[11].text())
                actions_data.append(csv_list)
            if self.repeat_for_number_2.text() == "":
                repeat_all = "1"
            else:
                repeat_all = self.repeat_for_number_2.text()
            if self.delay_2.text() == "":
                delay_time = "100"
            else:
                delay_time = self.delay_2.text()
            delay_type = self.delay_time_combobox_record.currentText()
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Save File", f"{save_name}", "CSV Files(*.csv)"
            )
            if file_name:
                f = open(file_name, "w", newline="")
                writer = csv.writer(f)
                # print(actions_data)
                for a in range(self.i - 1):
                    writer.writerow(actions_data[a])
                writer.writerow([repeat_all])
                writer.writerow([delay_time])
                writer.writerow([delay_type])
                f.close()
                self.record_save_window.close()
            logger.info("ending function to save record screen actions into pc")
            # triggered by record -> load button (pop-up window)
        except:
            logger.error("exception in record_save_settings_pc()", exc_info=True)

    def window_load(self):
        try:
            logger.info(
                "started function to load pop up window for uploading record settings"
            )
            self.font.setBold(False)
            self.font.setPixelSize(11)
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            # self.load_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
            self.load_window = new_dialog(self)
            self.load_window.setWindowTitle("Load")
            self.load_window.setWindowIcon(
                QtGui.QIcon(functions.resource_path("images/uplode_dark"))
            )
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
                self.invisible_widget_2.setStyleSheet(
                    "background-color: rgb(239, 229, 220)"
                )
            self.load_list.setGeometry(10, 10, 380, 340)
            scroll_bar = self.load_list.findChildren(QWidget)[4]
            if self.dark_theme_activated:
                scroll_bar.setStyleSheet(
                    """QScrollBar:vertical {
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
                                                         background-color: #10131b;}"""
                )
            else:
                scroll_bar.setStyleSheet(
                    """QScrollBar:vertical {
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
                                                   background: none;}"""
                )
            if self.dark_theme_activated:
                self.load_list.setStyleSheet(
                    "QListWidget {"
                    "border: 1px solid #bfcfb2;"
                    "border-radius: 5px;"
                    "color: #bfcfb2;}"
                )
            else:
                self.load_list.setStyleSheet(
                    "QListWidget {"
                    "border: 1px solid rgb(196, 177, 174);"
                    "border-radius: 5px;}"
                    "color: black;"
                )
            self.load_list.setFont(self.font)
            self.load_from_pc.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-monitor-96"))
            )
            self.load_from_pc.setGeometry(10, 360, 120, 30)
            self.load_from_pc.setText(" Load From PC")
            self.load_from_pc.clicked.connect(self.load_selected_from_pc)
            if self.dark_theme_activated:
                self.load_from_pc.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 5px;"
                    "border: 1px solid #bfcfb2;}"
                )
            else:
                self.load_from_pc.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(196, 177, 174);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 5px;"
                    "border: 1px solid rgb(196, 177, 174);}"
                )
            self.load_from_pc.setFont(self.font)
            self.load_from_list.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-list-100"))
            )
            self.load_from_list.setGeometry(270, 360, 120, 30)
            self.load_from_list.setText(" Load Selected")
            self.load_from_list.clicked.connect(self.load_selected_from_db)
            if self.dark_theme_activated:
                self.load_from_list.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 5px;"
                    "border: 1px solid rgb(196, 177, 174)}"
                )
            else:
                self.load_from_list.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(196, 177, 174);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 5px;"
                    "border: 1px solid rgb(196, 177, 174);}"
                )
            self.load_from_list.setFont(self.font)
            self.delete_selected.setIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-delete-96"))
            )
            self.delete_selected.setGeometry(140, 360, 120, 30)
            self.delete_selected.setText(" Delete Selected")
            self.delete_selected.clicked.connect(self.delete_from_db)
            if self.dark_theme_activated:
                self.delete_selected.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 5px;"
                    "border: 1px solid #bfcfb2;}"
                )
            else:
                self.delete_selected.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(196, 177, 174);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 5px;"
                    "border: 1px solid rgb(196, 177, 174);}"
                )
            self.delete_selected.setFont(self.font)
            self.load_list.clear()
            self.update_db_view()
            self.load_list.setCurrentRow(self.j - 1)
            self.load_window.show()
            logger.info(
                "ending function to load pop up window for uploading record settings"
            )
        except:
            logger.error("exception in window_load()", exc_info=True)

    # updates the database view on load window
    def update_db_view(self):
        try:
            logger.info(
                "started function to view info from database in the pop up window"
            )
            self.j = 0
            self.items_list = []
            self.items_from_home = []
            self.items_from_record = []
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            sql = """SELECT save_name, saved_date FROM home_run_settings"""
            cursor.execute(sql)
            for item in cursor.fetchall():
                self.items_list.append(
                    str(item[0]) + f" ({str(item[1])})" + " (saved from home)"
                )
                self.items_from_home.append(item[0])
            sql_2 = """SELECT save_name, saved_date FROM record_run_settings"""
            cursor.execute(sql_2)
            for item in cursor.fetchall():
                self.items_list.append(
                    str(item[0]) + f" ({str(item[1])})" + " (saved from record)"
                )
                self.items_from_record.append(item[0])
            conn.close()
            for item in self.items_list:
                list_item = QListWidgetItem(item)
                list_item.setTextAlignment(Qt.AlignHCenter)
                self.load_list.addItem(list_item)
                self.j += 1
            logger.info(
                "ending function to view info from database in the pop up window"
            )
        except:
            logger.error("exception in update_db_view()", exc_info=True)

    # function to read a CSV without using pandas
    def read_csv(self, csv_file):
        try:
            logger.info("started function to read a csv file")
            data = []
            with open(csv_file, "r") as f:
                # create a list of rows in the CSV file
                rows = f.readlines()

                # strip white-space and newlines
                rows = list(map(lambda x: x.strip(), rows))

                for row in rows:
                    # further split each row into columns assuming delimiter is comma
                    row = row.split(",")

                    # append to data-frame our new row-object with columns
                    data.append(row)
            logger.info("completed function to read a csv file")
            return data
        except:
            logger.error("exception in read_csv()", exc_info=True)

    # loads selected action from pc (csv files)
    def load_selected_from_pc(self):
        try:
            logger.info("started function to load selected action from pc (csv files)")
            fetched_data_home = []
            file_name, _ = QFileDialog.getOpenFileName(
                self, "Choose File", "", "CSV Files(*.csv)"
            )
            if file_name:
                # f = pd.read_csv(file_name, header=None)
                f = self.read_csv(file_name)

            else:
                logger.error("error in reading the csv file")
                logger.info(
                    "ending function to load selected action from pc (csv files)"
                )
                return
            row_count = len(f)
            self.load_window.close()
            self.remove_all_lines()
            for a in range(row_count - 3):
                if f[a][0] == "mouse":
                    self.add_mouse_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(str(int(f[a][1])))
                    row_elements[5].setText(str(int(f[a][2])))
                    row_elements[7].setCurrentText(f[a][3])
                    row_elements[9].setCurrentText(f[a][4])
                    row_elements[11].setText(str(int(f[a][5])))
                if f[a][0] == "scroll":
                    self.add_scroll_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(str(int(f[a][1])))
                    row_elements[5].setText(str(int(f[a][2])))
                    row_elements[7].setCurrentText(f[a][3])
                    row_elements[9].setText(f[a][4])
                    row_elements[11].setText(str(int(f[a][5])))
                if f[a][0] == "keyboard":
                    self.add_keyboard_line()
                    row_elements = self.line_list[a][1].children()
                    row_elements[3].setText(str(f[a][1]))
                    row_elements[5].setCurrentText(str(f[a][2]))
                    row_elements[7].setCurrentText(f[a][3])
                    row_elements[9].setText(str(f[a][4]))
            self.repeat_for_number_2.setText(f[row_count - 3][0])
            self.delay_2.setText(f[row_count - 2][0])
            self.delay_time_combobox_record.setCurrentText(f[row_count - 1][0])
            logger.info("ending function to load selected action from pc (csv files)")
        except:
            logger.error("exception in load_selected_from_pc()", exc_info=True)

    # deletes selected action from database
    def delete_from_db(self):
        try:
            logger.info("started function to deleted selected action from database")
            try:
                selected_item = self.load_list.currentItem().text()
            except AttributeError:
                logger.error("Exception occurred", exc_info=True)
                return
            item_key = selected_item[-5:]
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            if item_key == "home)":
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
            logger.info("ending function to deleted selected action from database")
        except:
            logger.error("exception in delete_from_db()", exc_info=True)

    def load_home_settings(self):
        try:
            logger.info(
                "started function to load saved home settings on the home screen"
            )
            sql = "SELECT * FROM home_run_settings"
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            if len(data) == 0:
                logger.info("no data saved in home run settings")
                conn.close()
                logger.info(
                    "ending function to load saved home settings on the home screen"
                )
                return
            fetched_data = data[0]
            logger.info(f"fetched data from database is- {fetched_data}")
            conn.close()
            self.get_home_screen()
            delay_type = fetched_data[10]
            self.mouse_button_combobox.setCurrentText(fetched_data[1])
            self.click_type_combobox.setCurrentText(fetched_data[2])
            if fetched_data[3] == "range":
                self.range_radio_button.setChecked(True)
                self.delay_time_combobox_2.setCurrentText(str(delay_type))
                range_min = fetched_data[8]
                range_max = fetched_data[9]
                self.range_min.setText(str(range_min))
                self.range_max.setText(str(range_max))
                self.delay_time_entrybox.setText("")
            else:
                self.repeat_radio_button.setChecked(True)
                self.delay_time_combobox.setCurrentText(str(delay_type))
                self.delay_time_entrybox.setText(str(fetched_data[8]))
                self.range_min.setText("")
                self.range_max.setText("")
            if fetched_data[4] == -1:
                self.never_stop_combobox.setCurrentText("Yes")
                self.repeat_for_number.setText("")
            else:
                self.never_stop_combobox.setCurrentText("No")
                self.repeat_for_number.setText(str(fetched_data[4]))
            if fetched_data[5] == "fixed":
                self.fixed_location_radio_button.setChecked(True)
                self.fixed_location_x.setText(str(fetched_data[6]))
                self.fixed_location_y.setText(str(fetched_data[7]))
                self.select_area_x.setText("")
                self.select_area_y.setText("")
                self.select_area_width.setText("")
                self.select_area_height.setText("")
            elif fetched_data[5] == "current":
                self.current_location_radio_button.setChecked(True)
                self.fixed_location_x.setText("")
                self.fixed_location_y.setText("")
                self.select_area_x.setText("")
                self.select_area_y.setText("")
                self.select_area_width.setText("")
                self.select_area_height.setText("")
            else:
                self.select_area_radio_button.setChecked(True)
                self.select_area_x.setText(str(fetched_data[6]))
                self.select_area_y.setText(str(fetched_data[7]))
                self.select_area_width.setText(str(fetched_data[11]))
                self.select_area_height.setText(str(fetched_data[12]))
                self.fixed_location_x.setText("")
                self.fixed_location_y.setText("")
            logger.info(
                "ending function to load saved home settings on the home screen"
            )
        except:
            logger.error("exception in load_home_Settings()", exc_info=True)

    # loads selected action from database
    def load_selected_from_db(self):
        try:
            logger.info("started function to load selected action from database")
            try:
                selected_item = self.load_list.currentItem().text()
            except AttributeError:
                logger.error("Exception occurred", exc_info=True)
                logger.info("ending function to load selected action from database")
                return
            item_key = selected_item[-5:]
            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()
            if item_key == "home)":
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
                if fetched_data[3] == "range":
                    self.range_radio_button.setChecked(True)
                    self.delay_time_combobox_2.setCurrentText(str(delay_type))
                    range_min = fetched_data[8]
                    range_max = fetched_data[9]
                    self.range_min.setText(str(range_min))
                    self.range_max.setText(str(range_max))
                    self.delay_time_entrybox.setText("")
                else:
                    self.repeat_radio_button.setChecked(True)
                    self.delay_time_combobox.setCurrentText(str(delay_type))
                    self.delay_time_entrybox.setText(str(fetched_data[8]))
                    self.range_min.setText("")
                    self.range_max.setText("")
                if fetched_data[4] == -1:
                    self.never_stop_combobox.setCurrentText("Yes")
                    self.repeat_for_number.setText("")
                else:
                    self.never_stop_combobox.setCurrentText("No")
                    self.repeat_for_number.setText(str(fetched_data[4]))
                if fetched_data[5] == "fixed":
                    self.fixed_location_radio_button.setChecked(True)
                    self.fixed_location_x.setText(str(fetched_data[6]))
                    self.fixed_location_y.setText(str(fetched_data[7]))
                    self.select_area_x.setText("")
                    self.select_area_y.setText("")
                    self.select_area_width.setText("")
                    self.select_area_height.setText("")
                elif fetched_data[5] == "current":
                    self.current_location_radio_button.setChecked(True)
                    self.fixed_location_x.setText("")
                    self.fixed_location_y.setText("")
                    self.select_area_x.setText("")
                    self.select_area_y.setText("")
                    self.select_area_width.setText("")
                    self.select_area_height.setText("")
                else:
                    self.select_area_radio_button.setChecked(True)
                    self.select_area_x.setText(str(fetched_data[6]))
                    self.select_area_y.setText(str(fetched_data[7]))
                    self.select_area_width.setText(str(fetched_data[11]))
                    self.select_area_height.setText(str(fetched_data[12]))
                    self.fixed_location_x.setText("")
                    self.fixed_location_y.setText("")
            else:
                index = selected_item.find(" (saved from record)")
                selected_save_name = selected_item[:index][0:-19]
                sql = f"SELECT * FROM record_run_settings WHERE save_name = '{selected_save_name}'"
                cursor.execute(sql)
                fetched_text = cursor.fetchall()[0]
                fetched_data = fetched_text[1].split("---")
                repeat_all = fetched_text[3]
                delay_time = fetched_text[4]
                delay_type = fetched_text[5]
                conn.close()
                self.load_window.close()
                row_count = len(fetched_data)
                self.remove_all_lines()
                for a in range(row_count):
                    row_list = fetched_data[a].split(", ")
                    if row_list[0] == "mouse":
                        self.add_mouse_line()
                        row_elements = self.line_list[a][1].children()
                        row_elements[3].setText(row_list[1])
                        row_elements[5].setText(row_list[2])
                        row_elements[7].setCurrentText(row_list[3])
                        row_elements[9].setCurrentText(row_list[4])
                        row_elements[11].setText(row_list[5])
                    elif row_list[0] == "keyboard":
                        self.add_keyboard_line()
                        row_elements = self.line_list[a][1].children()
                        row_elements[3].setText(row_list[1])
                        row_elements[5].setCurrentText(row_list[2])
                        row_elements[7].setCurrentText(row_list[3])
                        row_elements[9].setText(row_list[4])
                    elif row_list[0] == "scroll":
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
            logger.info("ending function to load selected action from database")
        except:
            logger.error("exception in load_selected_from_pc()", exc_info=True)

    # adds new line according to what's chosen
    def add_new_line(self):
        try:
            logger.info("started function to add new line in record actions")
            record_text = self.record_add_items.currentText()
            if record_text == " Mouse":
                self.add_mouse_line()
            elif record_text == " Keyboard":
                self.add_keyboard_line()
            elif record_text == " Scroll":
                self.add_scroll_line()
            logger.info("ending function to add new line in record actions")
        except:
            logger.error("exception in add_new_line()", exc_info=True)

    # adds new mouse line to the record screen
    def add_mouse_line(self):
        try:
            logger.info("started function to add new mouse line in record actions")
            record_line_frame = QFrame(self)
            line_layout = QHBoxLayout(record_line_frame)
            line_layout.setContentsMargins(5, 0, 0, 0)
            line_layout.setSpacing(5)
            record_line_frame.setFixedSize(500, 30)
            record_line_frame.setStyleSheet(
                "QFrame {border-bottom: 1.5px solid;"
                "border-radius: none;"
                "border-color: #c8bab7}"
            )
            column_1 = QLabel(record_line_frame)
            column_1.setStyleSheet("border: none;" "color: #3a5b41;")
            column_1.setText(str(self.i))
            column_1.setFixedSize(20, 10)
            column_2 = QLabel(record_line_frame)
            column_2.setStyleSheet("border: none;")
            column_2.setText("X:")
            column_2.setFixedSize(10, 20)
            column_3 = QLineEdit(record_line_frame)
            column_3.setFixedSize(40, 20)
            column_3.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_4 = QLabel(record_line_frame)
            column_4.setStyleSheet("border: none;")
            column_4.setText("Y:")
            column_4.setFixedSize(10, 20)
            column_5 = QLineEdit(record_line_frame)
            column_5.setFixedSize(40, 20)
            column_5.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_6 = QLabel(record_line_frame)
            column_6.setStyleSheet("border: none;")
            column_6.setText(" Type:")
            column_6.setFixedSize(30, 20)
            column_7 = QComboBox(record_line_frame)
            column_7.addItem("Left")
            column_7.addItem("Middle")
            column_7.addItem("Right")
            column_7.setFixedSize(55, 20)
            column_7.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);"
                "padding-left: 2px;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            column_8 = QLabel(record_line_frame)
            column_8.setStyleSheet("border: none;")
            column_8.setText(" Action: ")
            column_8.setFixedSize(40, 20)
            column_9 = QComboBox(record_line_frame)
            column_9.addItem("Press")
            column_9.addItem("Release")
            column_9.setFixedSize(65, 20)
            column_9.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);"
                "padding-left: 2px;}"
                "QComboBox::drop-down {"
                "background-color: rgb(249, 249, 245);"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            column_10 = QLabel(record_line_frame)
            column_10.setStyleSheet("border: none;")
            column_10.setText(" Delay:")
            column_10.setFixedSize(40, 20)
            column_11 = QLineEdit(record_line_frame)
            column_11.setPlaceholderText("    ms")
            column_11.setFixedSize(45, 20)
            column_11.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_12 = QPushButton(record_line_frame)
            column_12.setIcon(
                QtGui.QIcon(functions.resource_path("images/Red-Minus-PNG-File"))
            )
            column_12.setFixedSize(25, 20)
            if self.dark_theme_activated:
                column_12.setStyleSheet(
                    "QPushButton {"
                    "background-color: #10131b;"
                    "border-radius: 3px;"
                    "border: 1px solid;"
                    "border-color: #10131b;}"
                )
            else:
                column_12.setStyleSheet(
                    "QPushButton {"
                    "background-color: rgb(239, 229, 220);"
                    "border-radius: 3px;"
                    "border: 1px solid;"
                    "border-color: rgb(239, 229, 220);}"
                )
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
            self.line_list.append(["mouse", record_line_frame])
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
            logger.info("ending function to add new mouse line in record actions")
        except:
            logger.error("exception in add_mouse_line()", exc_info=True)

    # adds new keyboard line to the record screen
    def add_keyboard_line(self):
        try:
            logger.info("started function to add new keyboard line in record actions")
            record_line_frame = QFrame(self)
            record_line_frame.setStyleSheet(
                "QFrame {border-bottom: 1.5px solid;"
                "border-radius: none;"
                "border-color: #c8bab7}"
            )
            record_line_frame.setFixedSize(500, 30)
            line_layout = QHBoxLayout(record_line_frame)
            line_layout.setContentsMargins(5, 0, 0, 0)
            line_layout.setSpacing(5)
            column_1 = QLabel(record_line_frame)
            column_1.setStyleSheet("border: none;" "color: #3a5b41;")
            column_1.setText(str(self.i))
            column_1.setFixedSize(20, 10)
            column_2 = QLabel(record_line_frame)
            column_2.setStyleSheet("border: none;")
            column_2.setText("Input:")
            column_2.setFixedSize(35, 20)
            column_3 = QLineEdit(record_line_frame)
            column_3.setFixedSize(77, 20)
            column_3.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_4 = QLabel(record_line_frame)
            column_4.setStyleSheet("border: none;")
            column_4.setText(" Type:")
            column_4.setFixedSize(30, 20)
            column_5 = QComboBox(record_line_frame)
            column_5.addItem("Char")
            column_5.addItem("Key")
            column_5.setFixedSize(55, 20)
            column_5.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);"
                "padding-left: 2px;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            column_6 = QLabel(record_line_frame)
            column_6.setStyleSheet("border: none;")
            column_6.setText(" Action: ")
            column_6.setFixedSize(40, 20)
            column_7 = QComboBox(record_line_frame)
            column_7.addItem("Press")
            column_7.addItem("Release")
            column_7.setFixedSize(65, 20)
            column_7.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);"
                "padding-left: 2px;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            column_8 = QLabel(record_line_frame)
            column_8.setStyleSheet("border: none;")
            column_8.setText(" Delay:")
            column_8.setFixedSize(40, 20)
            column_9 = QLineEdit(record_line_frame)
            column_9.setPlaceholderText("    ms")
            column_9.setValidator(self.integer)
            column_9.setFixedSize(45, 20)
            column_9.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_10 = QPushButton(record_line_frame)
            column_10.setIcon(
                QtGui.QIcon(functions.resource_path("images/Red-Minus-PNG-File"))
            )
            column_10.setFixedSize(25, 20)
            if self.dark_theme_activated:
                column_10.setStyleSheet(
                    "QPushButton {"
                    "background-color: #10131b;"
                    "border-radius: 3px;"
                    "border: 1px solid;"
                    "border-color: #10131b;}"
                )
            else:
                column_10.setStyleSheet(
                    "QPushButton {"
                    "background-color: rgb(239, 229, 220);"
                    "border-radius: 3px;"
                    "border: 1px solid;"
                    "border-color: rgb(239, 229, 220);}"
                )
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
            self.line_list.append(["keyboard", record_line_frame])
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
            logger.info("ending function to add new keyboard line in record actions")
        except:
            logger.error("exception in add_keyboard_line()", exc_info=True)

    # adds new scroll line to the record screen
    def add_scroll_line(self):
        try:
            logger.info("started function to add new scroll line in record actions")
            record_line_frame = QFrame(self)
            record_line_frame.setStyleSheet(
                "QFrame {border-bottom: 1.5px solid;"
                "border-radius: none;"
                "border-color: #c8bab7;}"
            )
            record_line_frame.setFixedSize(500, 30)
            line_layout = QHBoxLayout(record_line_frame)
            line_layout.setContentsMargins(5, 0, 0, 0)
            line_layout.setSpacing(5)
            column_1 = QLabel(record_line_frame)
            column_1.setStyleSheet("border: none;" "color: #3a5b41;")
            column_1.setText(str(self.i))
            column_1.setFixedSize(20, 10)
            column_2 = QLabel(record_line_frame)
            column_2.setStyleSheet("border: none;")
            column_2.setText("X:")
            column_2.setFixedSize(10, 20)
            column_3 = QLineEdit(record_line_frame)
            column_3.setFixedSize(40, 20)
            column_3.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_4 = QLabel(record_line_frame)
            column_4.setStyleSheet("border: none;")
            column_4.setText("Y:")
            column_4.setFixedSize(10, 20)
            column_5 = QLineEdit(record_line_frame)
            column_5.setFixedSize(40, 20)
            column_5.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_6 = QLabel(record_line_frame)
            column_6.setStyleSheet("border: none;")
            column_6.setText(" Type:")
            column_6.setFixedSize(30, 20)
            column_7 = QComboBox(record_line_frame)
            column_7.addItem("Up")
            column_7.addItem("Down")
            column_7.setFixedSize(55, 20)
            column_7.setStyleSheet(
                "QComboBox {background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218);"
                "padding-left: 2px;}"
                "QComboBox::drop-down {"
                "border: 1px;"
                "border-radius: 2px;"
                "border-color: rgb(218, 218, 218);}"
                "QComboBox::down-arrow {"
                "image: url(:/images/arrow1.png);"
                "width: 8px;"
                "height: 8px;}"
            )
            column_8 = QLabel(record_line_frame)
            column_8.setStyleSheet("border: none;")
            column_8.setText(" Repeat:")
            column_8.setFixedSize(40, 20)
            column_9 = QLineEdit(record_line_frame)
            column_9.setFixedSize(65, 20)
            column_9.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_10 = QLabel(record_line_frame)
            column_10.setStyleSheet("border: none;")
            column_10.setText(" Delay:")
            column_10.setFixedSize(40, 20)
            column_11 = QLineEdit(record_line_frame)
            column_11.setPlaceholderText("    ms")
            column_11.setFixedSize(45, 20)
            column_11.setStyleSheet(
                "background-color: rgb(249, 249, 245);"
                "border: 1px solid;"
                "border-radius: 3px;"
                "border-color: rgb(218, 218, 218)"
            )
            column_12 = QPushButton(record_line_frame)
            column_12.setIcon(
                QtGui.QIcon(functions.resource_path("images/Red-Minus-PNG-File"))
            )
            column_12.setFixedSize(25, 20)
            if self.dark_theme_activated:
                column_12.setStyleSheet(
                    "QPushButton {"
                    "background-color: #10131b;"
                    "border-radius: 3px;"
                    "border: 1px solid;"
                    "border-color: #10131b;}"
                )
            else:
                column_12.setStyleSheet(
                    "QPushButton {"
                    "background-color: rgb(239, 229, 220);"
                    "border-radius: 3px;"
                    "border: 1px solid;"
                    "border-color: rgb(239, 229, 220);}"
                )
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
            self.line_list.append(["scroll", record_line_frame])
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
            logger.info("ending function to add new scroll line in record actions")
        except:
            logger.error("exception in add_scroll_line()", exc_info=True)

    # removes new line from the record screen
    def remove_line(self):
        try:
            logger.info("started function to add remove line from record actions")
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
            logger.info("ending function to add remove line from record actions")
        except:
            logger.error("exception in remove_line()", exc_info=True)

    # removes all lines from the record screen
    def remove_all_lines(self):
        try:
            logger.info("started function to remove All lines from record actions")
            self.foot_note_label.setText("")
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
            logger.info("ending function to remove All lines from record actions")
        except:
            logger.error("exception in remove_all_lines()", exc_info=True)

    # checking if repeat value is "yes" or "no" whenever combobox is changed
    def check_repeat_style(self):
        try:
            if self.never_stop_combobox.currentText() == "Yes":
                self.repeat_for_number.setDisabled(True)
                self.repeat_for_number.setStyleSheet(
                    "background-color: rgb(225, 225, 225);"
                    "border: 1px solid;"
                    "border-color: rgb(218, 218, 218);"
                    "border-radius: 3px;"
                )
            else:
                self.repeat_for_number.setDisabled(False)
                self.repeat_for_number.setStyleSheet(
                    "background-color: rgb(249, 249, 245);"
                    "border: 1px solid;"
                    "border-color: rgb(218, 218, 218);"
                    "border-radius: 3px;"
                )
        except:
            logger.error("exception in check_repeat_style()", exc_info=True)

    # triggers check tray checkbox
    def trigger_tray_checkbox(self):
        try:
            logger.info("starting function to toggle hide_to_tray checkbox")
            if self.hide_to_tray_checkbox.isChecked():
                self.hide_to_tray_checkbox.setChecked(False)
                if self.dark_theme_activated:
                    self.hide_to_tray_checkbox2.setIcon(
                        QtGui.QIcon(
                            functions.resource_path("images/empty_checkbox_dark")
                        )
                    )
                    self.hide_to_tray_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b"
                    )
                else:
                    self.hide_to_tray_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                    )
                    self.hide_to_tray_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220)"
                    )
            else:
                self.hide_to_tray_checkbox.setChecked(True)
                if self.dark_theme_activated:
                    self.hide_to_tray_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                    )
                    self.hide_to_tray_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b"
                    )
                else:
                    self.hide_to_tray_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon"))
                    )
                    self.hide_to_tray_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220)"
                    )
            self.check_tray_checkbox()
            logger.info("ending function to toggle hide_to_tray checkbox")
        except:
            logger.error("exception in trigger_tray_checkbox()", exc_info=True)

    # checking whether hide to tray checkbox is checked whenever checkbox is clicked
    def check_tray_checkbox(self):
        try:
            if self.hide_to_tray_checkbox.isChecked():
                app.setQuitOnLastWindowClosed(False)
            else:
                app.setQuitOnLastWindowClosed(True)
        except:
            logger.error("exception in check_tray_checkbox()", exc_info=True)

    # gets the current mouse location and writes inside app (triggered by hotkey)
    def get_mouse_location(self):
        try:
            logger.info(
                "starting function to get current mouse location and write to fixed location section of app"
            )
            for item in self.home_frame.findChildren(QLineEdit):
                item.clearFocus()
            mouse_location = mouse.get_position()
            x = mouse_location[0]
            y = mouse_location[1]
            if not self.home_frame.isHidden():
                self.fixed_location_x.setText(str(x))
                self.fixed_location_y.setText(str(y))
            logger.info(
                "ending function to get current mouse location and write to fixed location section of app"
            )
        except:
            logger.error("exception in get_mouse_location()", exc_info=True)

    # function to run when small_window_checkbox2 is clicked
    def trigger_small_window_checkbox(self):
        try:
            logger.info("starting function to toggle disable_small_window checkbox")
            # toggles the state of the small_window_checkbox
            if self.small_window_checkbox.isChecked():
                self.small_window_checkbox.setChecked(False)
                if self.dark_theme_activated:
                    self.small_window_checkbox2.setIcon(
                        QtGui.QIcon(
                            functions.resource_path("images/empty_checkbox_dark")
                        )
                    )
                    self.small_window_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b;"
                    )
                else:
                    self.small_window_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                    )
                    self.small_window_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220);"
                    )
            else:
                self.small_window_checkbox.setChecked(True)
                if self.dark_theme_activated:
                    self.small_window_checkbox2.setIcon(QtGui.QIcon(functions.resource_path("images/check_icon_dark")))
                    self.small_window_checkbox2.setStyleSheet("border: none;" "background-color: #10131b;")
                else:
                    self.small_window_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon"))
                    )
                    self.small_window_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220);"
                    )
            logger.info("ending function to toggle disable_small_window checkbox")
        except:
            logger.error("exception in trigger_small_window_checkbox()", exc_info=True)

# triggers live mouse checkbox
    def trigger_live_mouse(self):
        try:
            logger.info("starting function to toggle live_mouse checkbox")
            if self.mouse_location_checkbox.isChecked():
                self.mouse_location_checkbox.setChecked(False)
                if self.dark_theme_activated:
                    self.mouse_location_checkbox2.setIcon(
                        QtGui.QIcon(
                            functions.resource_path("images/empty_checkbox_dark")
                        )
                    )
                    self.mouse_location_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b;"
                    )
                else:
                    self.mouse_location_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/empty_checkbox"))
                    )
                    self.mouse_location_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220);"
                    )
            else:
                self.mouse_location_checkbox.setChecked(True)
                if self.dark_theme_activated:
                    self.mouse_location_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon_dark"))
                    )
                    self.mouse_location_checkbox2.setStyleSheet(
                        "border: none;" "background-color: #10131b;"
                    )
                else:
                    self.mouse_location_checkbox2.setIcon(
                        QtGui.QIcon(functions.resource_path("images/check_icon"))
                    )
                    self.mouse_location_checkbox2.setStyleSheet(
                        "border: none;" "background-color: rgb(239, 229, 220);"
                    )
            self.check_live_mouse()
            logger.info("ending function to toggle live_mouse checkbox")
        except:
            logger.error("exception in trigger_live_mouse()", exc_info=True)

    # starts the thread for writing live cursor position
    def check_live_mouse(self):
        try:
            logger.info(
                "starting function call to start thread to write live mouse position to screen"
            )
            live_mouse_thread = threading.Thread(target=self.get_live_mouse)
            live_mouse_thread.setDaemon(True)
            logger.info("created new thread for get live mouse function")
            live_mouse_thread.start()
            logger.info("started the new thread for get live mouse function")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
            logger.info(
                "ending function call to start thread to write live mouse position to screen"
            )
        except:
            logger.error("exception in check_live_mouse()", exc_info=True)

    # constantly writes the live cursor position to the screen
    def get_live_mouse(self):
        try:
            logger.info(
                "starting function to constantly write the live cursor position to the screen"
            )
            # logger.info("starting function call to write live mouse position to screen")
            while 1:
                if self.mouse_location_checkbox.isChecked():
                    self.live_mouse_label.setText("")
                    break
                mouse_location = mouse.get_position()
                self.live_mouse_label.setText(
                    f"X: {mouse_location[0]}, Y: {mouse_location[1]}"
                )
                QtTest.QTest.qWait(50)
            logger.info(
                "ending function to constantly write the live cursor position to the screen"
            )
        except:
            logger.error("exception in get_live_mouse()", exc_info=True)

    # resets the actions in home screen
    def home_reset_settings(self):
        try:
            logger.info("starting function to reset home settings")
            self.mouse_button_combobox.setCurrentText("Left")
            self.click_type_combobox.setCurrentText("Single")
            self.never_stop_combobox.setCurrentText("Yes")
            self.repeat_for_number.setText("1")
            self.delay_time_entrybox.setText("1")
            self.delay_time_combobox.setCurrentText("ms")
            self.repeat_radio_button.setChecked(True)
            self.current_location_radio_button.setChecked(True)
            self.range_min.setText("")
            self.range_max.setText("")
            self.select_area_x.setText("")
            self.select_area_y.setText("")
            self.select_area_width.setText("")
            self.select_area_height.setText("")
            self.fixed_location_x.setText("")
            self.fixed_location_y.setText("")
            logger.info("ending function to reset home settings")
        except:
            logger.error("exception in home_reset_Settings()", exc_info=True)

    def save_home_settings(self):
        try:
            logger.info("starting function to save home settings")
            self.save_home_params = 1
            self.home_save_settings_new()
            logger.info("ending function to save home settings")
        except:
            logger.error("exception in save_home_settings()", exc_info=True)

    # triggered by home -> save button (pop-up window)
    def window_home_save(self):
        try:
            logger.info(
                "starting function to open pop up window from home screen to save home settings"
            )
            self.font.setBold(False)
            self.font.setPixelSize(11)
            # self.home_save_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
            self.home_save_window = new_dialog(self)
            self.home_save_window.setWindowTitle("Save")
            self.home_save_window.setWindowIcon(
                QtGui.QIcon(functions.resource_path("images/icons8-save-90"))
            )
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
                self.invisible_widget_3.setStyleSheet(
                    "background-color: rgb(239, 229, 220)"
                )
            self.invisible_widget_3.setGeometry(0, 0, 300, 115)
            self.save_name_box.clear()
            self.home_save_frame1 = QFrame(self.invisible_widget_3)
            self.home_save_frame1.setGeometry(10, 8, 280, 91)
            if self.dark_theme_activated:
                self.home_save_frame1.setStyleSheet(
                    "border: 1px solid #bfcfb2;" "border-radius: 5px;"
                )
            else:
                self.home_save_frame1.setStyleSheet(
                    "border: 1px solid rgb(196, 174, 174);" "border-radius: 5px;"
                )
            self.home_save_frame1.lower()
            self.save_name_box.setGeometry(20, 22, 260, 30)
            if self.dark_theme_activated:
                self.save_name_box.setStyleSheet(
                    "background-color: #10131b;;"
                    "border: 1px solid #bfcfb2;"
                    "border-radius: none;"
                    "color: #bfcfb2"
                )
            else:
                self.save_name_box.setStyleSheet(
                    "background-color: rgb(239, 229, 220);"
                    "border: 1px solid rgb(196, 177, 174);"
                    "border-radius: none;"
                )
            self.save_name_box.setFont(self.font)
            self.save_name_label.setText("  Name your loop")
            if self.dark_theme_activated:
                self.save_name_label.setStyleSheet(
                    "color: #bfcfb2;" "font-weight: bold"
                )
            else:
                self.save_name_label.setStyleSheet("color: black;" "font-weight: bold")
            self.save_name_label.setGeometry(26, 14, 98, 15)
            self.save_name_label.setFont(self.font)
            self.home_save_button_pc.setIcon(
                QtGui.QIcon(functions.resource_path("images/CPU"))
            )
            self.home_save_button_pc.setGeometry(30, 60, 115, 30)
            self.home_save_button_pc.setText(" Save to PC")
            self.home_save_button_pc.clicked.connect(self.home_save_settings_pc)
            if self.dark_theme_activated:
                self.home_save_button_pc.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid #bfcfb2;}"
                )
            else:
                self.home_save_button_pc.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(158, 143, 141);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid rgb(158, 143, 141)}"
                )
            self.home_save_button_pc.setFont(self.font)
            self.home_save_button_db.setIcon(
                QtGui.QIcon(functions.resource_path("images/app_logo"))
            )
            self.home_save_button_db.setGeometry(160, 60, 115, 30)
            self.home_save_button_db.setText(" Save in App")
            self.home_save_button_db.clicked.connect(self.home_save_settings)
            if self.dark_theme_activated:
                self.home_save_button_db.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid #bfcfb2;"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid #bfcfb2;}"
                )
            else:
                self.home_save_button_db.setStyleSheet(
                    "QPushButton::hover {"
                    "border: 1px solid rgb(158, 143, 141);"
                    "background-color: rgb(196, 177, 174);"
                    "color: white;}"
                    "QPushButton {"
                    "background-color: rgb(249, 249, 245);"
                    "border-radius: 3px;"
                    "border: 1px solid rgb(158, 143, 141)}"
                )
            self.home_save_button_db.setFont(self.font)
            self.home_save_footnote.setGeometry(10, 99, 280, 13)
            self.home_save_footnote.setText("")
            if self.dark_theme_activated:
                self.home_save_footnote.setStyleSheet("color: red;")
            else:
                self.home_save_footnote.setStyleSheet("color: red;")
            self.home_save_footnote.setFont(self.font)
            self.home_save_window.show()
            logger.info(
                "ending function to open pop up window from home screen to save home settings"
            )
        except:
            logger.error("exception in window_home_save()", exc_info=True)

    # saves the actions from home screen into app, only 1 row
    def home_save_settings_new(self):
        try:
            logger.info("starting function to save home settings in the database")
            save_name = "GG"
            self.location_x = 0
            self.location_y = 0
            self.area_width = 0
            self.area_height = 0
            self.delay_time = 1
            self.delay_type = "ms"
            self.click_repeat = 1
            # if save_name == '':
            #     self.home_save_footnote.setText('error: name is needed')
            #     return
            mouse_type = str(self.mouse_button_combobox.currentText())
            click_type = str(self.click_type_combobox.currentText())
            if self.repeat_radio_button.isChecked():
                repeat_or_range = "repeat"
            else:
                repeat_or_range = "range"
            if str(self.never_stop_combobox.currentText()) == "Yes":
                self.click_repeat = -1
            else:
                try:
                    self.click_repeat = int(self.repeat_for_number.text())
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    # self.home_save_footnote.setText('error: number of repeat is needed to save')
                    # click_repeat = 1
                    # logger.info("saving default settings since user didnt enter")
                    logger.info("ending function to save home settings in the database")
                    return
            if self.select_area_radio_button.isChecked():
                select_or_fixed = "select"
            elif self.current_location_radio_button.isChecked():
                select_or_fixed = "current"
            else:
                select_or_fixed = "fixed"
            try:
                if self.select_area_radio_button.isChecked():
                    self.location_x = int(self.select_area_x.text())
                    self.location_y = int(self.select_area_y.text())
                    self.area_width = int(self.select_area_width.text())
                    self.area_height = int(self.select_area_height.text())
                elif self.current_location_radio_button.isChecked():
                    self.location_x = 0
                    self.location_y = 0
                    self.area_width = 0
                    self.area_height = 0
                else:
                    self.location_x = int(self.fixed_location_x.text())
                    self.location_y = int(self.fixed_location_y.text())
                    self.area_width = 0
                    self.area_height = 0
            except ValueError:
                logger.error("Exception occurred", exc_info=True)
                # self.home_save_footnote.setText('error: mouse location (and area width/height) is needed')
                # logger.info("saving default settings since user didnt enter")
                logger.info("ending function to save home settings in the database")
                return
            try:
                if self.repeat_radio_button.isChecked():
                    self.delay_type = str(self.delay_time_combobox.currentText())
                    self.delay_time = int(self.delay_time_entrybox.text())
                    wait_interval_min, wait_interval_max = (
                        self.delay_time,
                        self.delay_time,
                    )
                else:
                    self.delay_type = str(self.delay_time_combobox_2.currentText())
                    wait_interval_min = int(self.range_min.text())
                    wait_interval_max = int(self.range_max.text())
            except ValueError:
                logger.error("Exception occurred", exc_info=True)
                # self.home_save_footnote.setText('error: set delay time for your choice')
                # logger.info("saving default settings since user didnt enter")
                logger.info("ending function to save home settings in the database")
                return
            saved_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
            # try:

            # delete existing rows from database, it should store only 1 value

            conn = sqlite3.connect(file_path)
            cursor = conn.cursor()

            delete_home_row = """DELETE FROM home_run_settings"""
            cursor.execute(delete_home_row)

            logger.info("deleting any already stored home settings")

            sql = f"""INSERT INTO home_run_settings
                        (save_name, mouse_type, click_type, repeat_or_range, click_repeat, select_or_fixed, location_x,
                        location_y, wait_interval_min, wait_interval_max, wait_type, area_width, area_height, saved_date)
                        VALUES (
                        '{save_name}', '{mouse_type}', '{click_type}', '{repeat_or_range}', '{self.click_repeat}', '{select_or_fixed}',
                        '{self.location_x}', '{self.location_y}', '{wait_interval_min}', '{wait_interval_max}', '{self.delay_type}',
                        '{self.area_width}', '{self.area_height}', '{saved_date}'
                        )"""
            cursor.execute(sql)
            conn.commit()
            self.foot_note_label.setText("")
            self.foot_note_label.setText("Home settings saved!")
            logger.info("saved home settings in database")
            conn.close()
            logger.info("ending function to save home settings in the database")
        except:
            logger.error("exception in home_save_Settings_new()", exc_info=True)

    # saves the actions from home screen into app
    def home_save_settings(self):
        try:
            logger.info(
                "starting the old function to save home settings in the database"
            )
            save_name = self.save_name_box.text()
            if save_name == "":
                self.home_save_footnote.setText("error: name is needed")
                logger.info(
                    "ending the old function to save home settings in the database"
                )
                return
            mouse_type = str(self.mouse_button_combobox.currentText())
            click_type = str(self.click_type_combobox.currentText())
            if self.repeat_radio_button.isChecked():
                repeat_or_range = "repeat"
            else:
                repeat_or_range = "range"
            if str(self.never_stop_combobox.currentText()) == "Yes":
                click_repeat = -1
            else:
                try:
                    click_repeat = int(self.repeat_for_number.text())
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    self.home_save_footnote.setText(
                        "error: number of repeat is needed to save"
                    )
                    logger.info(
                        "ending the old function to save home settings in the database"
                    )
                    return
            if self.select_area_radio_button.isChecked():
                select_or_fixed = "select"
            elif self.current_location_radio_button.isChecked():
                select_or_fixed = "current"
            else:
                select_or_fixed = "fixed"
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
                logger.error("Exception occurred", exc_info=True)
                self.home_save_footnote.setText(
                    "error: mouse location (and area width/height) is needed"
                )
                logger.info(
                    "ending the old function to save home settings in the database"
                )
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
                logger.error("Exception occurred", exc_info=True)
                self.home_save_footnote.setText("error: set delay time for your choice")
                logger.info(
                    "ending the old function to save home settings in the database"
                )
                return
            saved_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
            try:
                functions.add_run_home_db(
                    save_name,
                    mouse_type,
                    click_type,
                    repeat_or_range,
                    click_repeat,
                    select_or_fixed,
                    location_x,
                    location_y,
                    wait_interval_min,
                    wait_interval_max,
                    delay_type,
                    area_width,
                    area_height,
                    saved_date,
                )
                self.home_save_window.close()
            except sqlite3.IntegrityError:
                logger.error("Exception occurred", exc_info=True)
                self.home_save_footnote.setText("error: this name exists")
                logger.info(
                    "ending the old function to save home settings in the database"
                )
                return
            logger.info("ending the old function to save home settings in the database")
        except:
            logger.error("exception in home_save_settings()", exc_info=True)

    # saves the actions from home screen into pc
    def home_save_settings_pc(self):
        try:
            logger.info("starting the function to save home settings in the pc")
            save_name = self.save_name_box.text()
            if save_name == "":
                self.home_save_footnote.setText("error: name is needed")
                logger.info("ending the function to save home settings in the pc")
                return
            mouse_type = str(self.mouse_button_combobox.currentText())
            click_type = str(self.click_type_combobox.currentText())
            if self.repeat_radio_button.isChecked():
                repeat_or_range = "repeat"
            else:
                repeat_or_range = "range"
            if str(self.never_stop_combobox.currentText()) == "Yes":
                click_repeat = -1
            else:
                try:
                    click_repeat = int(self.repeat_for_number.text())
                except ValueError:
                    logger.error("Exception occurred", exc_info=True)
                    self.home_save_footnote.setText(
                        "error: number of repeat is needed to save"
                    )
                    logger.info("ending the function to save home settings in the pc")
                    return
            if self.select_area_radio_button.isChecked():
                select_or_fixed = "select"
            elif self.current_location_radio_button.isChecked():
                select_or_fixed = "current"
            else:
                select_or_fixed = "fixed"
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
                logger.error("Exception occurred", exc_info=True)
                self.home_save_footnote.setText(
                    "error: mouse location (and area width/height) is needed"
                )
                logger.info("ending the function to save home settings in the pc")
                return
            try:
                if self.repeat_radio_button.isChecked():
                    delay_type = str(self.delay_time_combobox.currentText())
                    delay_time = int(self.delay_time_entrybox.text())
                    if delay_type == "ms":
                        wait_interval = (delay_time, delay_time)
                    else:
                        wait_interval = (delay_time, delay_time)
                else:
                    delay_type = str(self.delay_time_combobox_2.currentText())
                    delay_time_min = int(self.range_min.text())
                    delay_time_max = int(self.range_max.text())
                    wait_interval = (delay_time_min, delay_time_max)
            except ValueError:
                logger.error("Exception occurred", exc_info=True)
                self.home_save_footnote.setText("error: set delay time for your choice")
                logger.info("ending the function to save home settings in the pc")
                return
            pc_csv_list = [
                mouse_type,
                click_type,
                repeat_or_range,
                click_repeat,
                select_or_fixed,
                location_x,
                location_y,
                wait_interval[0],
                wait_interval[1],
                delay_type,
                area_width,
                area_height,
            ]
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Save File", f"{save_name}", "CSV Files(*.csv)"
            )
            if file_name:
                try:
                    f = open(file_name, "w")
                    writer = csv.writer(f)
                    writer.writerow(pc_csv_list)
                    f.close()
                    self.home_save_window.close()
                except PermissionError:
                    logger.error("Exception occurred", exc_info=True)
                    self.home_save_footnote.setText(
                        "error: cannot overwrite because it is being used"
                    )
                    logger.info("ending the function to save home settings in the pc")
                    return
            logger.info("ending the function to save home settings in the pc")
        except:
            logger.error("exception in home_save_settings_pc()", exc_info=True)

    def get_generate(self):
        try:
            logger.info("starting the get_generate function")
            try:
                self.responses = []
                try:
                    r = requests.get(
                        "http://146.190.166.207/generate-token",
                        headers={"Connection": "close"},
                    )
                    # r.raise_for_status()
                # r = requests.get('https://auth-provider.onrender.com/generate-token')
                except requests.exceptions.ConnectionError as conerr:
                    logger.error("Exception occurred", exc_info=True)
                    prompt_internet_issue()
                    return
                self.responses.append(r)
                logger.info("ending the get_generate function")
                return
            except KeyboardInterrupt:
                logger.error("Exception occurred", exc_info=True)
                logger.info("ending the get_generate function")
                return
        except:
            logger.error("exception in get_generate()", exc_info=True)

    def post_authenticate(self, token):
        logger.info("starting the post_authenticate function")
        try:
            self.responses = []
            # r = requests.post('https://auth-provider.onrender.com/authenticate', data={"token": token})
            try:
                r = requests.post(
                    "http://146.190.166.207/authenticate",
                    data={"token": token},
                    headers={"Connection": "close"},
                )
                # r.raise_for_status()
            except requests.exceptions.ConnectionError as conerr:
                logger.error("Exception occurred", exc_info=True)
                prompt_internet_issue()
                return
            self.responses.append(r)
            logger.info(f"got a post response - {self.responses}")
            logger.info("ending the post_authenticate function")
            return
        except KeyboardInterrupt:
            logger.error("Exception occurred", exc_info=True)
            logger.info("ending the post_authenticate function")
            return

    def database_query_execution(self, connection, cursor, query, query_params):
        try:
            # performing query execution
            logger.info("starting database_query_execution function")
            cursor.execute(query, query_params)

            connection.commit()

            logger.info("updated database")
            connection.close()

            logger.info("ending database_query_execution function")
        except:
            logger.error("exception in database_query_execution()", exc_info=True)

    def authentication_loop2(self):
        try:
            logger.info("started execution of function: authentication_loop2()")
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
            logger.info("connecting to database")
            con = sqlite3.connect(file_path)
            logger.info("connected to database")
            cursor = con.cursor()
            sql = "SELECT * FROM local_table"
            logger.info("executing sql query")
            cursor.execute(sql)
            fetched_data = cursor.fetchall()
            logger.info("completed sql query")
            if len(fetched_data) == 0:
                # Making a GET request
                logger.info("no token found in local database")
                logger.info("started get call")
                try:
                    response = requests.get(
                        "http://146.190.166.207/generate-token",
                        headers={"Connection": "close"},
                    )
                    # response.raise_for_status()
                except requests.exceptions.ConnectionError as conerr:
                    logger.error("Exception occurred", exc_info=True)
                    prompt_internet_issue()
                    self.authentication_result = -1
                    return
                logger.info("completed get call")
                # response = self.responses[0]
                info = response.text
                json_info = json.loads(info)
                token = json_info["accessToken"]
                email = ""
                logger.info(f"token is - {token}")

                logger.info("ending execution of function: authentication_loop2()")
                # return True
                self.authentication_result = 1
                self.validity_24_hour = 1
                time_1 = datetime.datetime.now()
                expiration_datetime = time_1 + timedelta(days=1)
                time_1_str = str(expiration_datetime)
                a = str(1)
                hash_funny_enc = hashlib.sha256(a.encode())
                funny_enc = hash_funny_enc.hexdigest()

                res_first, res_second = de_combine(funny_enc)
                funny_encrypt = res_first
                funny_pt2_encrypt = res_second
                cursor.execute(
                    "INSERT INTO local_table (email, access_token, funny_number, funny_number_2, timestamp) VALUES(?,?,?,?,?)",
                    (email, token, funny_encrypt, funny_pt2_encrypt, time_1_str),
                )
                cursor.close()
                con.commit()
                logger.info("done")
                con.close()
            else:
                email = fetched_data[0][0]
                token = fetched_data[0][1]
                logger.info("token found in local database")
                logger.info("authenticating")
                # Making a POST request
                logger.info("started post call")
                try:
                    response2 = requests.post(
                        "http://146.190.166.207/authenticate",
                        data={"token": token},
                        headers={"Connection": "close"},
                    )
                    # response2.raise_for_status()
                    logger.info(f"token sent for authentication is- {token}")
                    logger.info("done post call")
                # except requests.exceptions.ConnectionError as conerr:
                except requests.exceptions.ConnectionError as conerr:
                    logger.error("Exception occurred", exc_info=True)
                    prompt_internet_issue()
                    self.authentication_result = -1
                    logger.info("ending execution of function: authentication_loop2()")
                    return
                logger.info(response2)
                logger.info(response2.text)
                logger.info(
                    f"response received from authenticate post call - {response2.text}"
                )
                json_message = json.loads(response2.text)
                # print(type(response2.text))
                # logger.info("huhu")

                content = json_message["message"]
                if content != "success":
                    # the token has expired and user doesnt have a token with infinite validity
                    # either the user has not registered with mail or they have registered but not verified
                    logger.info("authentication failed")
                    if email != "":
                        logger.info(
                            "user has submitted email before, trying to check validity of email"
                        )
                        # email has been registered and may or may not been verified
                        # call api to send login email and check if email has been verified or not
                        # Making a POST request
                        logger.info("started post call")
                        # response2 = requests.post('https://auth-provider.onrender.com/login', data={"email": email})
                        response2 = requests.post(
                            "http://146.190.166.207/login",
                            data={"email": email},
                            headers={"Connection": "close"},
                        )
                        logger.info("done post call")
                        logger.info(f"received response- {response2.text}")
                        json_message = json.loads(response2.text)
                        # print(type(response2.text))
                        # logger.info("hihi")
                        try:
                            content = json_message["message"]
                            if content == "Email not found":
                                # register email
                                # Making a POST request
                                logger.info(
                                    "asking user to register their email as it is not found in our database"
                                )
                                logger.info("started post call")
                                # response2 = requests.post('https://auth-provider.onrender.com/register', data={"email": email})
                                response2 = requests.post(
                                    "http://146.190.166.207/register",
                                    data={"email": email},
                                    headers={"Connection": "close"},
                                )
                                logger.info("done post call")
                                logger.info(f"received response- {response2.text}")
                                json_message = json.loads(response2.text)
                                # print(type(response2.text))
                                # logger.info("hehe")
                            elif content == "Email not verified":
                                # email is not verified, prompt the user to verify the email or if that has expired start
                                # from scratch and register
                                logger.info(
                                    "asking user to verify their email or resend verification link"
                                )
                                logger.info(
                                    "calling function to open email sent dialog"
                                )
                                # self.open_email_sent_dialog(email)
                                # email_sent_dialog_thread = threading.Thread(target=self.open_email_sent_dialog, args=(email,))
                                # logger.info("starting email sent dialog thread")
                                # email_sent_dialog_thread.setDaemon(True)
                                self.open_email_sent_dialog(email)
                                # email_sent_dialog_thread.start()
                                # logger.info("function call complete")
                            # result[0] = False
                            logger.info(
                                "ending execution of function: authentication_loop2()"
                            )
                            # return False
                            self.authentication_result = -1
                        except:
                            content = json_message["token"]
                            logger.info("user has now been granted access for lifetime")

                            # email has been verified and an infinite token is returned
                            # update the database with this token now
                            logger.info("connecting to db")
                            logger.info(
                                "ending execution of function: authentication_loop2()"
                            )
                            # return True
                            self.authentication_result = 1
                            self.validity_infinity = 1
                            b = str(2)
                            hash_funny_2_enc = hashlib.sha256(b.encode())
                            funny_2_enc = hash_funny_2_enc.hexdigest()
                            # print(funny_2_enc)
                            res_first, res_second = de_combine(funny_2_enc)
                            # res_first, res_second = funny_2_enc[:len(funny_2_enc) // 2], funny_2_enc[len(funny_2_enc) // 2:]
                            funny_2_encrypt = res_first
                            funny_2_pt2_encrypt = res_second
                            query = "UPDATE local_table SET access_token = ?, funny_number = ?, funny_number_2 = ? WHERE email = ?"
                            self.query_thread = threading.Thread(
                                target=database_action,
                                args=(
                                    query,
                                    (
                                        content,
                                        funny_2_encrypt,
                                        funny_2_pt2_encrypt,
                                        email,
                                    ),
                                ),
                            )

                            logger.info("starting query_thread")
                            self.query_thread.setDaemon(True)
                            self.query_thread.start()

                    else:
                        # email has not been registered
                        logger.info(
                            "email has not been registered, user has to submit an email"
                        )
                        logger.info("calling function to open email dialog")

                        self.open_email_dialog()
                        # logger.info("function call complete")
                        # result[0] = False
                        logger.info(
                            "ending execution of function: authentication_loop2()"
                        )
                        # return False
                        self.authentication_result = -1
                else:
                    logger.info("authentication success")
                    # result[0] = True
                    logger.info("ending execution of function: authentication_loop2()")
                    # return True
                    self.authentication_result = 1
        except:
            logger.error("exception in auth_loop2()", exc_info=True)

    def home_start_process(self):
        try:
            logger.info("start execution of function: home_start_process()")
            if record_playback_event.is_set():
                logger.info("wont start home clicking bcos playback recording is taking place.")
                return
            elif record_recording_event.is_set():
                logger.info("wont start home clicking bcos screen recording is taking place.")
                return
            logger.info("setting home clicking event")
            home_clicking_event.set() # home clicking has started
            self.get_home_screen()
            if self.validity_infinity == 0 and self.validity_24_hour == 0:
                logger.info("user has to connect to internet for authentication")
                self.authentication_loop2()
                if self.authentication_result == -1 or self.authentication_result == 0:
                    self.foot_note_label.setText("")
                    self.foot_note_label.setText("you cant access run functionality")
                    logger.info(
                        "ending execution of function: home_start_process() as access is blocked"
                    )
                    return

            elif self.validity_infinity == 0 and self.validity_24_hour == 1:
                logger.info("token may be valid under 24 hours")
                time_2 = datetime.datetime.now()
                con = sqlite3.connect(file_path)
                cursor = con.cursor()
                cursor.execute("SELECT timestamp from local_table")
                value = cursor.fetchone()
                # print(value[0])
                cursor.close()
                con.close()
                expiration_datetime_object = datetime.datetime.strptime(
                    value[0], "%Y-%m-%d %H:%M:%S.%f"
                )
                # print(expiration_datetime_object < time_2)
                if expiration_datetime_object < time_2:
                    logger.info("token has expired")
                    self.authentication_loop2()
                    if (
                        self.authentication_result == -1
                        or self.authentication_result == 0
                    ):
                        self.foot_note_label.setText("")
                        self.foot_note_label.setText(
                            "you cant access run functionality"
                        )
                        logger.info(
                            "ending execution of function: home_start_process() as access is blocked"
                        )
                        return
                logger.info("user doesnt have to connect to internet")

            else:
                logger.info("token is valid for infinity")


            mouse_type = self.mouse_button_combobox.currentText().lower()
            click_type = self.click_type_combobox.currentText()
            never_stop_boolean = self.never_stop_combobox.currentText()
            if never_stop_boolean == "Yes":
                click_repeat = -1
            else:
                try:
                    click_repeat = int(self.repeat_for_number.text())
                except ValueError:
                    logger.error(
                        "Exception occurred- repeat number is missing", exc_info=True
                    )
                    self.foot_note_label.setText("error: repeat number is missing")
                    logger.info("ending execution of function: home_start_process()")
                    return
            try:
                if self.repeat_radio_button.isChecked():
                    delay_type = str(self.delay_time_combobox.currentText())
                    delay_time = int(self.delay_time_entrybox.text())
                    if delay_type == "ms":
                        wait_interval = (delay_time / 1000, delay_time / 1000)
                    elif delay_type == "s":
                        wait_interval = (delay_time, delay_time)
                    elif delay_type == "min":
                        wait_interval = (delay_time * 60, delay_time * 60)
                    else:
                        wait_interval = (delay_time * 1440, delay_time * 1440)
                else:
                    delay_type = str(self.delay_time_combobox_2.currentText())
                    if delay_type == "ms":
                        delay_time_min = int(self.range_min.text()) / 1000
                        delay_time_max = int(self.range_max.text()) / 1000
                        wait_interval = (delay_time_min, delay_time_max)
                    elif delay_type == "s":
                        delay_time_min = int(self.range_min.text())
                        delay_time_max = int(self.range_max.text())
                        wait_interval = (delay_time_min, delay_time_max)
                    elif delay_type == "min":
                        delay_time_min = int(self.range_min.text()) * 60
                        delay_time_max = int(self.range_max.text()) * 60
                        wait_interval = (delay_time_min, delay_time_max)
                    else:
                        delay_time_min = int(self.range_min.text()) * 1440
                        delay_time_max = int(self.range_max.text()) * 1440
                        wait_interval = (delay_time_min, delay_time_max)
            except ValueError:
                logger.error(
                    "Exception occurred- value is missing for repeat or range choice",
                    exc_info=True,
                )
                self.foot_note_label.setText(
                    "error: value is missing for your repeat or range choice"
                )
                logger.info("ending execution of function: home_start_process()")
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
                    logger.error(
                        "Exception occurred- x and y location is missing", exc_info=True
                    )
                    self.foot_note_label.setText("error: x and y location is missing")
                    logger.info("ending execution of function: home_start_process()")
                    return
            else:
                location_x = 0
                location_y = 0
            if self.select_area_width.text() == "":
                area_width = 0
            else:
                area_width = int(self.select_area_width.text())
            if self.select_area_height.text() == "":
                area_height = 0
            else:
                area_height = int(self.select_area_height.text())
            self.foot_note_label.setText("")
            if self.fixed_location_radio_button.isChecked():
                radio_button = 1
            elif self.current_location_radio_button.isChecked():
                radio_button = 2
            else:
                radio_button = 3
            self.showMinimized()
            # main_window_visible.clear()
            # self.window_status = False
            self.open_small_window(run_mode="home")
            # ----------------------

            try:
                keyboard.remove_hotkey(self.home_start_stop_hotkey)
            except:
                logger.error(
                    "error in removing home start stop hotkey", exc_info=True
                )  # keyboard.add_hotkey(self.home_start_stop_hotkey, self.home_stop_process)
            keyboard.add_hotkey(
                self.home_start_stop_hotkey, self.multiple_hotkey_actions_home
            )
            self.foot_note_label.setText("")
            self.play_button.setEnabled(False)
            # global is_clicking
            # is_clicking = True
            # clicking_event.set()
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.error("error in removing add record line hotkey", exc_info=True)
            # try:
            #     keyboard.remove_hotkey(self.record_recording_hotkey)
            # except:
            #     logger.error("error in removing screen recording hotkey", exc_info=True)
            #
            # try:
            #     keyboard.remove_hotkey(self.record_start_stop_hotkey)
            # except:
            #     logger.error(
            #         "error in removing playback start stop hotkey", exc_info=True
            #     )

            try:
                keyboard.remove_hotkey(self.mouse_location_hotkey)
            except:
                logger.error("error in removing mouse location hotkey", exc_info=True)

            toaster.show_toast(
                title="Clicking started",
                msg=f"Press {self.home_start_stop_hotkey.upper()} to stop",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )
            if radio_button == 1:
                logger.info("starting new thread for fixed clicking")

                worker = WorkerThread2(
                    self, mouse_type,
                        click_type,
                        click_repeat,
                        int(location_x),
                        int(location_y),
                        wait_interval
                )
                worker.start()

            elif radio_button == 2:
                logger.info("starting new thread for current clicking")
                worker = WorkerThread1(
                    self, mouse_type, click_type, click_repeat, wait_interval
                )
                worker.start()

            else:
                logger.info("starting new thread for random clicking")

                worker = WorkerThread3(
                    self, mouse_type,
                        click_type,
                        click_repeat,
                        location_x,
                        location_y,
                        wait_interval,
                        area_width,
                        area_height
                )
                worker.start()

            logger.info("ending execution of function: home_start_process()")
        except:
            logger.error("exception in home_start_process()", exc_info=True)

    # function to encompass multiple actions after home start stop hotkey is pressed
    def multiple_hotkey_actions_home(self):
        try:
            logger.info("started execution of function: multiple_hotkey_actions_home()")
            if not self.small_window_checkbox.isChecked():
                if self.small_window_opened is not None:
                    logger.info("small window is opened")
                    self.small_window_opened.close()
                    self.small_window_opened = None
                    logger.info("here")
            self.home_stop_process()
            self.record_stop_process()

            logger.info("ending execution of function: multiple_hotkey_actions_home()")
        except:
            logger.error("exception in multiple_hotkey_actions_home()", exc_info=True)

    # starts after the process for home -> play button is finished
    def after_home_thread(self):
        try:
            logger.info("started execution of function: after_home_thread()")
            self.play_button.setEnabled(True)
            try:
                keyboard.remove_hotkey(self.home_start_stop_hotkey)
            except:
                logger.error("error in removing home start stop hotkey", exc_info=True)
            keyboard.add_hotkey(
                self.home_start_stop_hotkey, lambda: self.play_button.click()
            )

            toaster.show_toast(
                "Clicking stopped",
                f"Press {self.home_start_stop_hotkey.upper()} to start again",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )

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

            logger.info("ending execution of function: after_home_thread()")
        except:
            logger.error("exception in after_home_thread()", exc_info=True)

    # stops the actions set in home screen (intervenes the thread)
    def home_stop_process(self):
        try:
            # clicking_event.clear()
            stop_home_event.set()

        except:
            logger.error("exception in home_stop_process()", exc_info=True)

    # stops the actions set in record screen (intervenes the thread)
    def record_stop_process(self):
        try:
            # clicking_event.clear()
            stop_record_event.set()

        except:
            logger.error("exception in record_stop_process()", exc_info=True)

    # starts the process for record -> play button
    def record_start_process(self):
        try:

            logger.info("started function record_start_process()")
            if home_clicking_event.is_set():
                logger.info("wont start record playback bcos home clicking is taking place.")
                return
            elif record_recording_event.is_set():
                logger.info("wont start record playback bcos screen recording is taking place.")
                return
            logger.info("setting record playback event")
            record_playback_event.set()
            self.get_record_screen()

            if self.validity_infinity == 0 and self.validity_24_hour == 0:
                logger.info("user has to connect to internet for authentication")
                self.authentication_loop2()
                if self.authentication_result == -1 or self.authentication_result == 0:
                    self.foot_note_label.setText("")
                    self.foot_note_label.setText("you cant access run functionality")
                    logger.info(
                        "ending execution of function: home_start_process() as access is blocked"
                    )
                    return
            elif self.validity_infinity == 0 and self.validity_24_hour == 1:
                time_2 = datetime.datetime.now()
                con = sqlite3.connect(file_path)
                cursor = con.cursor()
                cursor.execute("SELECT timestamp from local_table")
                value = cursor.fetchone()
                cursor.close()
                con.close()
                expiration_datetime_object = datetime.datetime.strptime(
                    value[0], "%Y-%m-%d %H:%M:%S.%f"
                )
                if expiration_datetime_object < time_2:
                    self.authentication_loop2()
                    if (
                        self.authentication_result == -1
                        or self.authentication_result == 0
                    ):
                        self.foot_note_label.setText("")
                        self.foot_note_label.setText(
                            "you cant access run functionality"
                        )
                        logger.info(
                            "ending execution of function: record_start_process() as access is blocked"
                        )
                        return
                logger.info("user doesnt have to connect to internet")

            if self.i == 1:
                logger.error("Exception occurred- no actions available", exc_info=True)
                logger.info("ending execution of function: record_start_process()")
                self.foot_note_label.setText("error: no actions available")
                record_playback_event.clear()
                logger.info("clearing record playback event")
                return

            logger.info("green signal given to perform recorded autoclicking!!")
            actions_data = []
            for a in range(self.i - 1):
                csv_list = []
                row_elements = self.line_list[a][1].children()
                if self.line_list[a][0] == "mouse":
                    csv_list.append("mouse")
                    for b in (3, 5):
                        if row_elements[b].text() == "":
                            logger.error(
                                "Exception occurred- x and y location are needed",
                                exc_info=True,
                            )
                            logger.info(
                                "ending execution of function: record_start_process()"
                            )
                            self.foot_note_label.setText(
                                "error: x and y location are needed"
                            )
                            return
                        else:
                            csv_list.append(row_elements[b].text())
                    for b in (7, 9):
                        csv_list.append(row_elements[b].currentText())
                    if row_elements[11].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[11].text())
                    actions_data.append(csv_list)
                elif self.line_list[a][0] == "keyboard":
                    csv_list.append("keyboard")
                    csv_list.append(row_elements[3].text())
                    if row_elements[3].text() == "":
                        logger.error(
                            "Exception occurred- no input given", exc_info=True
                        )
                        logger.info(
                            "ending execution of function: record_start_process()"
                        )
                        self.foot_note_label.setText("error: no input given")
                        return
                    csv_list.append(row_elements[5].currentText())
                    csv_list.append(row_elements[7].currentText())
                    if row_elements[9].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[9].text())
                    actions_data.append(csv_list)
                elif self.line_list[a][0] == "scroll":
                    csv_list.append("scroll")
                    for b in (3, 5):
                        if row_elements[b].text() == "":
                            logger.error(
                                "Exception occurred- x and y location are needed",
                                exc_info=True,
                            )
                            logger.info(
                                "ending execution of function: record_start_process()"
                            )
                            self.foot_note_label.setText(
                                "error: x and y location are needed"
                            )
                            return
                        else:
                            csv_list.append(row_elements[b].text())
                    csv_list.append(row_elements[7].currentText())
                    csv_list.append(row_elements[9].text())
                    if row_elements[11].text() == "":
                        csv_list.append("100")
                    else:
                        csv_list.append(row_elements[11].text())
                    actions_data.append(csv_list)
            if actions_data[0][0] == "keyboard":
                if actions_data[0][2] == "Key":
                    pressed_key = functions.key_converter(
                        actions_data[0][1].replace("Key.", "").lower()
                    )
                    if pressed_key == "wrong":
                        logger.error(
                            "Exception occurred- wrong key input", exc_info=True
                        )
                        logger.info(
                            "ending execution of function: record_start_process()"
                        )
                        self.foot_note_label.setText("error: wrong key input")
                        return
            if self.repeat_for_number_2.text() == "":
                repeat_all = "1"
            else:
                repeat_all = self.repeat_for_number_2.text()
            if self.delay_2.text() == "":
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
            self.foot_note_label.setText("")
            self.showMinimized()
            # main_window_visible.clear()
            self.open_small_window(run_mode="record playback")
            # -------------------------
            try:
                keyboard.remove_hotkey(self.record_start_stop_hotkey)
            except:
                logger.error(
                    "error in removing record start stop hotkey", exc_info=True
                )
            keyboard.add_hotkey(
                self.record_start_stop_hotkey, self.multiple_hotkey_actions_home
            )
            self.record_play_button.setEnabled(False)
            try:
                keyboard.remove_hotkey(self.add_record_line_hotkey)
            except:
                logger.error("error in removing add record line hotkey", exc_info=True)

            # try:
            #     keyboard.remove_hotkey(self.record_recording_hotkey)
            # except:
            #     logger.error("error in removing screen recording hotkey", exc_info=True)

            # try:
            #     keyboard.remove_hotkey(self.home_start_stop_hotkey)
            # except:
            #     logger.error("error in removing home start stop hotkey", exc_info=True)

            try:
                keyboard.remove_hotkey(self.mouse_location_hotkey)
            except:
                logger.error("error in removing mouse location hotkey", exc_info=True)

            toaster.show_toast(
                title="Playback started",
                msg=f"Press {self.record_start_stop_hotkey.upper()} to stop playback",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )
            logger.info("starting thread for playing back recorded actions")
            # try:
            #     keyboard.remove_hotkey(self.record_recording_hotkey)
            # except:
            #     logger.error("error in removing screen recording hotkey", exc_info=True)
            #

            worker_playback = WorkerThread_playback(
                self, actions_data, repeat_all, delay_time, self.i
            )
            worker_playback.start()

            logger.info("ending execution of function: record_start_process()")
        except:
            logger.error("exception in record_start_process()", exc_info=True)

    # starts after the process for record -> play button is finished
    def after_record_thread(self, a):
        try:
            logger.info("starting execution of function: after_record_thread()")
            if wrong_key_event.is_set():
                self.foot_note_label.setText(f"error: wrong key input at line {a + 1}")
                wrong_key_event.clear()
            self.record_play_button.setEnabled(True)
            try:
                keyboard.remove_hotkey(self.record_start_stop_hotkey)
            except:
                logger.error(
                    "error in removing record start stop hotkey", exc_info=True
                )
            keyboard.add_hotkey(
                self.record_start_stop_hotkey, lambda: self.record_play_button.click()
            )
            logger.info("record_start_stop_hotkey is now detached from multiple_hotkey_actions")
            toaster.show_toast(
                title="Playback completed",
                msg=f"Press {self.record_start_stop_hotkey.upper()} to start again",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )
            computer_type = self.complete_combobox_3.currentText()

            # try:
            #     keyboard.add_hotkey(
            #         self.record_recording_hotkey,
            #         lambda: self.record_record_button.click(),
            #     )
            # except:
            #     logger.error("error in adding screen recording hotkey", exc_info=True)

            # try:
            #     keyboard.add_hotkey(
            #         self.home_start_stop_hotkey, lambda: self.play_button.click()
            #     )
            # except:
            #     logger.error("error in adding home start stop hotkey", exc_info=True)
            #
            # try:
            #     keyboard.add_hotkey(self.mouse_location_hotkey, self.get_mouse_location)
            # except:
            #     logger.error("error in adding mouse location hotkey", exc_info=True)

            if computer_type == " Turn off":
                os.system("shutdown /s /t 1")
                app.exit()
            elif computer_type == " Log off":
                os.system("shutdown -l")
                app.exit()
            elif computer_type == " Hibernate":
                os.system("shutdown.exe /h")
                app.exit()
            elif computer_type == " Lock":
                ctypes.windll.user32.LockWorkStation()
                app.exit()
            elif computer_type == " Quit":
                app.exit()
            elif computer_type == " Standby":
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                app.exit()
            logger.info("ending execution of function: after_record_thread()")
        except:
            logger.error("exception in after_record_thread()", exc_info=True)

    # gets data from recording and inserts into list in record screen
    # takes list of recording actions as parameter; mouse, keyboard or scroll action
    def insert_recording_list(self, events):
        try:
            logger.info(
                "starting function: insert_recording_list()- gets data from recording and inserts into list in record screen"
            )
            c = 0
            release_counter = 0
            logger.info(f"the events recorded are- {events}")
            while len(events[c]) == 6:
                # logger.info("kokoko")
                if events[0][3] == "release":
                    del events[0]
                    release_counter += 1
                    if len(events) == 0:
                        break
                else:
                    break
            if release_counter == 0:
                # logger.info(events)
                # logger.info(events[-1])
                del events[-1]
                # logger.info(events)
                if len(events) == 0:
                    events.append("1")

                # logger.info(events[-1])
                del events[-1]
                # logger.info(events)
                # logger.info(events[-1])
            else:
                # logger.info("herere")
                # logger.info(events)
                if len(events) > 0:
                    # logger.info(events[-1])
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
                    if str(events[a][2]) == "Button.left":
                        children[7].setCurrentText("Left")
                    elif str(events[a][2]) == "Button.middle":
                        children[7].setCurrentText("Middle")
                    else:
                        children[7].setCurrentText("Right")
                    if events[a][3] is True:
                        children[9].setCurrentText("Press")
                    else:
                        children[9].setCurrentText("Release")
                    delay = int(events[a][4] * 1000)
                    children[11].setText(str(delay))

                elif len(events[a]) == 4:
                    self.add_scroll_line()
                    children = self.line_list[b][1].children()
                    children[3].setText(str(events[a][0]))
                    children[5].setText(str(events[a][1]))
                    scroll_count = 1
                    delay = int(events[a][3] * 1000)
                    if str(events[a][2]) == "-1":
                        children[7].setCurrentText("Down")
                        for scrolls in range(1, total_row - a):
                            if len(events[a + scrolls]) == 4:
                                if str(events[a + scrolls][2]) == "-1":
                                    scroll_count += 1
                                    delay += int(events[a + scrolls][3] * 1000)
                                else:
                                    break
                            else:
                                break
                        children[9].setText(str(scroll_count))
                    else:
                        children[7].setCurrentText("Up")
                        for scrolls in range(1, total_row - a):
                            if len(events[a + scrolls]) == 4:
                                if str(events[a + scrolls][2]) == "1":
                                    scroll_count += 1
                                    delay += int(events[a + scrolls][3] * 1000)
                                else:
                                    break
                            else:
                                break
                        children[9].setText(str(scroll_count))
                    if scroll_count > 1:
                        a += scroll_count - 1
                    children[11].setText(str(delay))
                elif len(events[a]) == 6:
                    # if stop_current_action.is_set():
                    #     logger.info("force stopping this-4")
                    #     return
                    self.add_keyboard_line()
                    children = self.line_list[b][1].children()
                    char_group = events[a][0]
                    char_count = 1
                    delay = int(events[a][2] * 1000)
                    if events[a][1] == "char":
                        children[5].setCurrentText("Char")
                        for char in range(1, total_row - a):
                            if len(events[a + char]) == 3:
                                if str(events[a + char][1]) == "char":
                                    char_group += events[a + char][0]
                                    delay += int(events[a + char][2] * 1000)
                                    char_count += 1
                                else:
                                    break
                        children[3].setText(str(char_group))
                    else:
                        children[5].setCurrentText("Key")
                        children[3].setText(str(char_group))
                    if char_count > 1:
                        a += char_count - 1
                    if events[a][3] == "press":
                        children[7].setCurrentText("Press")
                    else:
                        children[7].setCurrentText("Release")
                    children[9].setText(str(delay))
                a += 1
                b += 1
            logger.info(
                "ending function: insert_recording_list()- gets data from recording and inserts into list in record screen"
            )
        except:
            logger.error("exception in insert_recording_list()", exc_info=True)

    # starts a thread for live_record_process function
    def thread_for_live_record(self):
        try:
            logger.info(
                "starting function to start thread to start recording user actions from screen"
            )

            if home_clicking_event.is_set():
                logger.info("wont start screen recording bcos home clicking is taking place.")
                return
            elif record_playback_event.is_set():
                logger.info("wont start screen recording bcos record playback is taking place.")
                return
            logger.info("setting record recording event")
            record_recording_event.set()
            self.remove_all_lines()
            self.open_small_window(run_mode="recording")
            # new_thread = threading.Thread(target=self.live_record_process)
            # new_thread.setDaemon(True)
            # new_thread.start()
            worker_recording = WorkerThread_recording_actions(self)
            worker_recording.start()


            logger.info(
                "created and started new thread for live record process function"
            )
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")
            logger.info(
                "ending function to start thread to start recording user actions from screen"
            )
        except:
            logger.error("exception in thread_for_live_record()", exc_info=True)

    # handles live recording process
    def live_record_process(self):
        try:
            logger.info("starting function to start recording user actions from screen")

            # try:
            #     keyboard.remove_hotkey(self.record_start_stop_hotkey)
            # except:
            #     logger.error(
            #         "error in removing record start stop hotkey", exc_info=True
            #     )

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
                press_type = "press"
                if hasattr(key, "char"):
                    if str(key)[0] == "<":
                        key_type = "key"
                        new_list = [key, key_type, delay, press_type, 0, 0]
                    elif str(key)[0] == "[":
                        key_type = "char"
                        new_list = [
                            str(key)[2:-2].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    elif str(key)[1] == "\\":
                        key_type = "char"
                        converted_key = functions.char_converter(str(key)[1:-1])
                        new_list = [
                            converted_key.lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    else:
                        key_type = "char"
                        new_list = [
                            str(key)[1:-1].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                else:
                    key_type = "key"
                    new_list = [key, key_type, delay, press_type, 0, 0]
                self.record_events.append(new_list)

            def on_release(key):
                nonlocal time_counter
                old_time = time_counter
                time_counter = time.time()
                delay = round(time_counter - old_time, 2)
                press_type = "release"
                if hasattr(key, "char"):
                    if str(key)[0] == "<":
                        key_type = "key"
                        new_list = [key, key_type, delay, press_type, 0, 0]
                    elif str(key)[0] == "[":
                        key_type = "char"
                        new_list = [
                            str(key)[2:-2].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    elif str(key)[1] == "\\":
                        key_type = "char"
                        converted_key = functions.char_converter(str(key)[1:-1])
                        new_list = [
                            converted_key.lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                    else:
                        key_type = "char"
                        new_list = [
                            str(key)[1:-1].lower(),
                            key_type,
                            delay,
                            press_type,
                            0,
                            0,
                        ]
                else:
                    key_type = "key"
                    new_list = [key, key_type, delay, press_type, 0, 0]
                self.record_events.append(new_list)

            self.record_record_button.disconnect()
            self.record_record_button.clicked.connect(self.stop_live_record)
            self.record_record_button.setText("Stop")
            self.record_events = []
            self.mouse_listener = pynput.mouse.Listener(
                on_click=on_click, on_scroll=on_scroll
            )
            self.keyboard_listener = pynput.keyboard.Listener(
                on_press=on_press, on_release=on_release
            )
            self.showMinimized()

            # self.window_status = False
            # main_window_visible.clear()
            # send notification to desktop
            toaster.show_toast(
                title="Recording Started",
                msg=f"Press {self.record_recording_hotkey.upper()} to stop recording",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )
            self.record_play_button.setEnabled(False)
            self.mouse_listener.start()
            self.keyboard_listener.start()
            time_counter = time.time()
            # self.mouse_listener.join()
            # self.keyboard_listener.join()
            logger.info("ending function to start recording user actions from screen")
        except:
            logger.error("exception in live_record_process()", exc_info=True)

    # stops live recording process
    def stop_live_record(self):
        try:
            logger.info("starting function to stop recording user actions from screen")
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            toaster.show_toast(
                title="Recording completed",
                msg=f"Press {self.record_start_stop_hotkey.upper()} to start playback",
                icon_path=functions.resource_path(r"images/ico_logo.ico"),
                threaded=True,
                duration=2,
            )
            logger.info("clearing record recording event")
            record_recording_event.clear()
            self.record_record_button.setIcon(
                QtGui.QIcon(functions.resource_path("images/red-circle"))
            )
            self.record_record_button.disconnect()
            self.record_record_button.clicked.connect(self.thread_for_live_record)
            self.record_record_button.setText("Record")
            try:
                keyboard.remove_hotkey(self.record_start_stop_hotkey)
            except:
                logger.error(
                    "error in removing record start stop hotkey", exc_info=True
                )
            keyboard.add_hotkey(
                self.record_start_stop_hotkey, lambda: self.record_play_button.click()
            )
            if self.small_window_opened is not None:
                logger.info("small window is opened")
                self.small_window_opened.close()
            # if (
            #     clicking_event.is_set() == False
            #     and main_window_visible.is_set() == False
            # ):
            logger.info("inserting record actions")
            self.insert_recording_list(self.record_events)
            logger.info("showing mainwindow")
            self.showNormal()
            # main_window_visible.set()

            self.record_play_button.setEnabled(True)
            logger.info("ending function to stop recording user actions from screen")
        except:
            logger.error("exception in stop_live_record()", exc_info=True)


class UI_SmallWindow(QMainWindow):
    # defines all variables and UI elements for the app
    def __init__(self, stop_hotkey, MainWindow, indicator):
        try:
            logger.info("started initialisation of small window UI")
            super(UI_SmallWindow, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            uic.loadUi(functions.resource_path("small_window.ui"), self)
            self.MainWindow = self.findChild(QMainWindow, "MainWindow")
            self.setObjectName("SmallWindow")
            # self.resize(140, 41)
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            logger.info(
                " Screen size : "
                + str(self.sizeObject.height())
                + "x"
                + str(self.sizeObject.width())
            )
            self.setGeometry(self.sizeObject.width() - 141, 1, 140, 41)
            # self.setWindowFlag(Qt.FramelessWindowHint)
            flags = QtCore.Qt.WindowFlags(
                QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint
            )
            self.setWindowFlags(flags)
            # self.centralwidget = QtWidgets.QWidget(MainWindow)
            # self.centralwidget.setObjectName("centralwidget")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            # self.pushButton = QtWidgets.QPushButton(self)
            self.pushButton.setGeometry(QtCore.QRect(88, 0, 52, 41))
            self.pushButton.setText("")
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setStyleSheet("border :1px solid black")
            self.pushButton.setIcon(QIcon(functions.resource_path("images/red-circle")))
            self.pushButton.clicked.connect(
                lambda: self.button_action(MainWindow, indicator)
            )
            size = QSize(25, 25)
            self.pushButton.setIconSize(size)
            # self.label = QtWidgets.QLabel(self)
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 89, 41))
            self.label.setFrameShape(QtWidgets.QFrame.Box)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.label.setText("")
            self.label.setText(stop_hotkey)
            self.setCentralWidget(self.centralwidget)
            logger.info("ending initialisation of small window UI")
            # self.retranslateUi(stop_hotkey)
            # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        except:
            logger.error("exception in small_window_init()", exc_info=True)

    def button_action(self, MainWindow, indicator):
        try:
            # master_window = UI()
            # call stop function from this object
            logger.info("starting function of button press of small window")
            if indicator == 1:
                logger.info("calling function stop_live_record()")
                MainWindow.stop_live_record()

            else:
                self.close()
                MainWindow.showNormal()
                # main_window_visible.set()
                logger.info("calling function home_stop_process()")
                MainWindow.home_stop_process()
                logger.info("calling function record_stop_process()")
                MainWindow.record_stop_process()
            logger.info("ending function of button press of small window")
        except:
            logger.error("exception in button_action()", exc_info=True)


class UI_connectivity(QDialog):
    def __init__(self):
        try:
            logger.info("started initialisation of connectivity ui")
            super(UI_connectivity, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            uic.loadUi(functions.resource_path("connectivity_issue.ui"), self)
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            self.setWindowTitle("User seems offline")
            self.setObjectName("User seems offline")
            self.resize(327, 205)
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(70, 20, 211, 151))
            self.label.setWordWrap(True)
            self.label.setObjectName("label")
            logger.info("ending initialisation of connectivity ui")
        except:
            logger.error("exception in ui_connect_init()", exc_info=True)


class new_dialog(QDialog):
    def __init__(self, mainwindow):
        try:
            super(new_dialog, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            # flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowTitleHint)
            # self.setWindowFlags(flags)
            self.parent = mainwindow
        except:
            logger.error("exception in new_dialog_init()", exc_info=True)

    def closeEvent(self, event):
        try:
            try:
                keyboard.remove_hotkey(self.parent.add_record_line_hotkey)
            except:
                logger.error(
                    "error in parent.add_record_line_hotkey", exc_info=True
                )

            keyboard.add_hotkey(
                self.parent.add_record_line_hotkey,
                lambda: self.parent.record_add_button.click(),
            )
        except:
            logger.error("exception in new_dialogclose_event()", exc_info=True)


class UI_no_actions(QDialog):
    def __init__(self, mainwindow):
        try:
            logger.info("started initialisation of no actions ui")
            super(UI_no_actions, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            uic.loadUi(functions.resource_path("no_actions.ui"), self)
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            self.setWindowTitle("No actions available")
            self.setObjectName("No actions available")
            self.resize(327, 205)
            self.parent = mainwindow
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(70, 20, 211, 151))
            self.label.setWordWrap(True)
            self.label.setObjectName("label")
            try:
                keyboard.remove_hotkey(mainwindow.add_record_line_hotkey)
            except:
                logger.info("add_record_line_hotkey was not active")
            logger.info("ending initialisation of no actions ui")
        except:
            logger.error("exception in ui_no_actions_init()", exc_info=True)

    def closeEvent(self, event):
        try:
            try:
                keyboard.remove_hotkey(self.parent.add_record_line_hotkey)
            except:
                logger.error(
                    "error in parent.add_record_line_hotkey", exc_info=True
                )

            keyboard.add_hotkey(
                self.parent.add_record_line_hotkey,
                lambda: self.parent.record_add_button.click(),
            )
        except:
            logger.error("exception in ui_no_actions_close_event()", exc_info=True)


class UI_Dialog(QDialog):
    def __init__(self):
        try:
            logger.info("started initialisation of email dialog UI")
            super(UI_Dialog, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            # uic.loadUi(functions.resource_path("email_dialog.ui"), self)
            uic.loadUi(functions.resource_path("email_dialog.ui"), self)
            self.setObjectName("Email Registration")
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            self.resize(442, 159)
            # self.Dialog = Dialog
            self.submit_key = QtWidgets.QPushButton(self)
            self.submit_key.setGeometry(QtCore.QRect(340, 80, 75, 24))
            self.submit_key.setObjectName("submit_key")
            self.submit_key.setText("Submit")
            self.label_4 = QtWidgets.QLabel(self)
            self.label_4.setGeometry(QtCore.QRect(30, 10, 311, 61))
            self.label_4.setOpenExternalLinks(True)
            self.error_label = QtWidgets.QLabel(self)
            self.error_label.setGeometry(QtCore.QRect(40, 119, 331, 31))
            self.error_label.setObjectName("error_label")
            self.error_label.setStyleSheet("color: rgb(141, 34, 8);")
            self.error_label.setWordWrap(True)
            self.label_4.setObjectName("label_4")
            self.label_3 = QtWidgets.QLabel(self)
            self.label_3.setGeometry(QtCore.QRect(30, 85, 47, 13))
            self.label_3.setObjectName("label_3")
            self.name = QtWidgets.QLineEdit(self)
            self.name.setGeometry(QtCore.QRect(80, 82, 221, 20))
            self.name.setObjectName("name")
            self.submit_key.clicked.connect(self.open_email_sent_dialog)

            # self.retranslateUi(Dialog)
            # QtCore.QMetaObject.connectSlotsByName(Dialog)
            logger.info("ending initialisation of email dialog UI")
        except:
            logger.error("exception in ui_dialog_init()", exc_info=True)

    def open_email_sent_dialog(self):
        try:
            logger.info(
                "starting function to open email sent dialog box after user enters email"
            )
            email = self.name.text()
            # add email to database
            # con = sqlite3.connect(file_path)
            # cursor = con.cursor()
            # email_data = (email,)
            # cursor.execute("UPDATE local_table SET email = ?", email_data)
            # con.commit()
            # logger.info("adding email to local database")
            # con.close()
            is_valid = check(email)
            if is_valid != "Yes":
                self.error_label.setText(is_valid)
                logger.error("Email entered is not valid")
                logger.info(
                    "ending function to open email sent dialog box after user enters email"
                )
                return

            logger.info("connecting to database in open email sent")
            query = "UPDATE local_table SET email = ?"
            self.query_thread = threading.Thread(
                target=database_action, args=(query, (email,))
            )
            self.query_thread.setDaemon(True)
            self.query_thread.start()
            # con = sqlite3.connect(file_path)
            # cursor = con.cursor()
            # email_data = (email,)
            # cursor.execute("UPDATE local_table SET email = ?", email_data)
            # con.commit()
            # con.close()
            logger.info("adding email to local database")

            # call api to send verification email
            # Making a POST request
            logger.info("create new thread for sending verification mail)")
            email_thread = threading.Thread(target=post_register, args=(email,))
            email_thread.setDaemon(True)
            email_thread.start()
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")

            # response2 = responses[0]

            # response2 = requests.post('https://auth-provider.onrender.com/register', data={"email": email})
            # print(response2.text)
            # print(type(response2.text))
            # json_message = json.loads(response2.text)
            logger.info("Sending verification mail")
            # if json_message["message"] == "Email sent":
            # logger.info("here")
            self.hide()
            # self.dialog = QtWidgets.QDialog()
            self.email_sent_dialog = UI_email_sent_Dialog(email)
            # self.ui.setupUi(self.dialog, email)
            self.email_sent_dialog.show()
            logger.info(
                "ending function to open email sent dialog box after user enters email"
            )
        except:
            logger.error(
                "exception in ui_dialog_open_email_Sent_dialog()", exc_info=True
            )


class UI_email_sent_Dialog(QDialog):
    def __init__(self, email):
        try:
            logger.info("started initialisation of email sent dialog UI")
            super(UI_email_sent_Dialog, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            uic.loadUi(functions.resource_path("email_sent_dialog.ui"), self)
            self.setObjectName("Email Verification")
            self.sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            # logger.info("----")
            # print(email)
            self.em = email
            self.uii = UI_Dialog()
            logger.info("-----")
            self.resize(442, 159)
            # self.enter_key = QtWidgets.QPushButton(self)
            # self.enter_key.setGeometry(QtCore.QRect(180, 107, 75, 23))
            self.enter_key = QtWidgets.QPushButton(self)
            self.enter_key.setGeometry(QtCore.QRect(140, 120, 75, 23))
            self.enter_key.setObjectName("enter_key")
            self.enter_key.setText("Resend")

            self.enter_key.clicked.connect(lambda: self.resend_verification_link(email))
            self.re_enter_email = QtWidgets.QPushButton(self)
            self.re_enter_email.setGeometry(QtCore.QRect(220, 120, 101, 23))
            self.re_enter_email.setObjectName("re_enter_email")
            self.re_enter_email.setText("Re_enter_email")

            self.re_enter_email.clicked.connect(lambda: self.enter_email())
            # self.enter_key.setObjectName("enter_key")
            # self.enter_key.setText("Resend")
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(30, 10, 151, 31))
            self.label.setOpenExternalLinks(True)
            self.label.setObjectName("label")
            self.label_4 = QtWidgets.QLabel(self)
            self.label_4.setWordWrap(True)
            self.label_4.setText(email)
            self.label_4.setOpenExternalLinks(True)
            self.label_4.setObjectName("label_4")
            self.label_4.setGeometry(QtCore.QRect(180, 10, 231, 31))
            self.label_2 = QtWidgets.QLabel(self)
            self.label_2.setGeometry(QtCore.QRect(30, 50, 371, 31))
            self.label_2.setOpenExternalLinks(True)
            self.label_2.setObjectName("label_2")
            logger.info("ending initialisation of email sent dialog UI")
        except:
            logger.error("exception in ui_email_Sent_dialog_init()", exc_info=True)

    def enter_email(self):
        try:
            logger.info("starting function to ask user to re-enter email")
            self.uii.show()
            self.close()
            logger.info("ending function to ask user to re-enter email")
        except:
            logger.error(
                "exception in ui_email_Sent_dialog_enter_email()", exc_info=True
            )

    def resend_verification_link(self, email):
        try:
            # call api to send verification email
            # Making a POST request
            logger.info("starting function to resend verification mail")
            logger.info("create new thread for resending verification mail)")
            resend_email_thread = threading.Thread(target=post_register, args=(email,))
            resend_email_thread.setDaemon(True)
            resend_email_thread.start()
            logger.info("showing the current active threads:")
            for thread in threading.enumerate():
                logger.info(thread)
            logger.info("list complete")

            # response2 = responses[0]

            # response2 = requests.post('https://auth-provider.onrender.com/register', data={"email": email})
            # print(response2.text)
            # json_message = json.loads(response2.text)
            # print(type(response2.text))
            logger.info("ending function to resend verification mail")
        except:
            logger.error(
                "exception in ui_email_Sent_dialog_resend_verif()", exc_info=True
            )


class CaptureScreen(QtWidgets.QSplashScreen):
    """QSplashScreen, that track mouse event for capturing screenshot."""

    def __init__(self, MainWindow):
        try:
            logger.info("started initialisation of Capture Screen class")
            super(CaptureScreen, self).__init__()
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.master = MainWindow
            # Points on screen marking the origin and end of regtangle area.
            self.origin = QtCore.QPoint(0, 0)
            self.end = QtCore.QPoint(0, 0)
            self.signal = 0

            # A drawing widget for representing bounding area
            self.rubberBand = QtWidgets.QRubberBand(
                QtWidgets.QRubberBand.Rectangle, self
            )

            self.createDimScreenEffect()
            logger.info("ending initialisation of Capture Screen class")
        except:
            logger.error("exception in capture_screen_init()", exc_info=True)

    def createDimScreenEffect(self):
        try:
            """Fill splashScreen with black color and reduce the widget opacity to create dim screen effect"""
            logger.info(
                "started function createDimScreenEffect()- to create dim screen effect"
            )
            # Get the screen geometry of the main desktop screen for size ref
            primScreenGeo = QtGui.QGuiApplication.primaryScreen().geometry()

            screenPixMap = QtGui.QPixmap(primScreenGeo.width(), primScreenGeo.height())
            screenPixMap.fill(QtGui.QColor(0, 0, 0))

            self.setPixmap(screenPixMap)

            self.setWindowState(QtCore.Qt.WindowFullScreen)
            self.setWindowOpacity(0.4)
            logger.info("ending function createdimscreeneffect()")
        except:
            logger.error("exception in capture_screen_creatdimeffect()", exc_info=True)

    def mousePressEvent(self, event):
        try:
            """Show rectangle at mouse position when left-clicked"""
            if event.button() == QtCore.Qt.LeftButton:
                self.origin = event.pos()
                logger.info("origin_x: " + str(self.origin.x()))
                logger.info("origin_y: " + str(self.origin.y()))
                self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
                self.rubberBand.show()
        except:
            logger.error("exception in capture_screen_mousepressevent()", exc_info=True)

    def getOriginal_x(self):
        try:
            return self.origin.x()
        except:
            logger.error("exception in capture_screen_get_origX()", exc_info=True)

    def getOriginal_y(self):
        try:
            return self.origin.y()
        except:
            logger.error("exception in capture_screen_get_origY()", exc_info=True)

    def getFinal_x(self):
        try:
            return self.end.x()
        except:
            logger.error("exception in capture_screen_get_finalX()", exc_info=True)

    def getFinal_y(self):
        try:
            return self.end.y()
        except:
            logger.error("exception in capture_screen_get_finalY()", exc_info=True)

    def mouseMoveEvent(self, event):
        try:
            """Resize rectangle as we move mouse, after left-clicked."""
            self.rubberBand.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized()
            )
        except:
            logger.error("exception in capture_screen_mousemove_event()", exc_info=True)

    def indicator(self):
        try:
            return self.signal
        except:
            logger.error("exception in capture_screen_indicator()", exc_info=True)

    def mouseReleaseEvent(self, event):
        try:
            """Upon mouse released, ask the main desktop's QScreen to capture screen on defined area."""
            logger.info(
                "starting function to capture screen on defined area once mouse press is released"
            )
            if event.button() == QtCore.Qt.LeftButton:
                self.end = event.pos()
                logger.info("end_x: " + str(self.end.x()))
                logger.info("end_y: " + str(self.end.y()))
                self.rubberBand.hide()
                self.hide()
                self.signal = 1
                primaryScreen = QtGui.QGuiApplication.primaryScreen()
                grabbedPixMap = primaryScreen.grabWindow(
                    0,
                    self.origin.x(),
                    self.origin.y(),
                    self.end.x() - self.origin.x(),
                    self.end.y() - self.origin.y(),
                )
                # grabbedPixMap.save('screenshot_windowed.jpg', 'jpg')
                # UIWindow = UI()

                self.original_x = self.getOriginal_x()
                self.original_y = self.getOriginal_y()
                self.final_x = self.getFinal_x()
                self.final_y = self.getFinal_y()
                self.snipping_width = abs(self.final_x - self.original_x)
                self.snipping_height = abs(self.final_y - self.original_y)
                self.snip_x = min(self.final_x, self.original_x)
                self.snip_y = min(self.final_y, self.original_y)
                # UIWindow.select_area_x.setText(str(self.snip_x))
                # UIWindow.select_area_y.setText(str(self.snip_y))
                # UIWindow.select_area_width.setText(str(self.snipping_width))
                # UIWindow.select_area_height.setText(str(self.snipping_height))
                # UIWindow.select_area_radio_button.setChecked(True)
                # UIWindow.show()
                self.master.select_area_x.setText(str(self.snip_x))
                self.master.select_area_y.setText(str(self.snip_y))
                self.master.select_area_width.setText(str(self.snipping_width))
                self.master.select_area_height.setText(str(self.snipping_height))
                self.master.select_area_radio_button.setChecked(True)
                self.master.show()
            logger.info(
                "ending function to capture screen on defined area once mouse press is released"
            )
        except:
            logger.error(
                "exception in capture_screen_mouse_release_event()", exc_info=True
            )

# print(f"starting- {datetime.datetime.now()}")
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename=functions.resource_path("app.log"),
    filemode="w",
    format="%(asctime)s - %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger.info("starting")

form = functions.resource_path("version2.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(form)
responses = []


appname = "GG-Autoclicker"
appauthor = "GG"

dir_path = os.path.join(user_data_dir(appname, appauthor), "GG_autoclicker")
# dir_path = os.path.join(os.environ['APPDATA'], 'GG_autoclicker')

logger.info("before db init")
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    file_path = os.path.join(dir_path, "autoclicker.db")
    # generateKey.generate()
    initialise_db()
else:
    file_path = os.path.join(dir_path, "autoclicker.db")
    if not os.path.exists(file_path):
        # generateKey.generate()
        initialise_db()
logger.info("after db init")

file_path = os.path.join(dir_path, "autoclicker.db")
# below 7 lines gets the latest preferences of the user from the database
# logger.info(f"db file path is - {file_path}")
conn = sqlite3.connect(file_path)
cursor = conn.cursor()

logger.info("importing app_settings stored in database")
sql = """SELECT * FROM app_settings LIMIT 1"""
cursor.execute(sql)
app_settings = cursor.fetchone()
logger.info("getting app settings")
sql = """SELECT * FROM home_run_settings LIMIT 1"""
cursor.execute(sql)
home_settings = cursor.fetchone()
cursor.close()
conn.close()

logger.info("getting home run settings")

(
    show_tool_after,
    hide_system_tray,
    disable_cursor_location,
    disable_small_window,
    dark_theme,
    home_start_hotkey,
    add_record_line_hotkey,
    record_start_hotkey,
    record_recording_hotkey,
    mouse_location_hotkey,
) = app_settings

if home_settings is not None:
    logger.info("importing home_settings stored in database")
    (
        save_name,
        mouse_type,
        click_type,
        repeat_or_range,
        click_repeat,
        select_or_fixed,
        location_x,
        location_y,
        wait_interval_min,
        wait_interval_max,
        wait_type,
        area_width,
        area_height,
        saved_date,
    ) = home_settings

toaster = ToastNotifier()

stop_home_event = threading.Event()
stop_record_event = threading.Event()
wrong_key_event = threading.Event()
home_clicking_event = threading.Event()
record_recording_event = threading.Event()
record_playback_event = threading.Event()
app = QApplication(sys.argv)
UIWindow = UI()
logger.info("about to show UI")
UIWindow.show()
app.exec_()
