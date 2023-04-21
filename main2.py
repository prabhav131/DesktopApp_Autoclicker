_At='rundll32.exe powrprof.dll,SetSuspendState 0,1,0'
_As='shutdown.exe /h'
_Ar='shutdown -l'
_Aq='shutdown /s /t 1'
_Ap='error: set delay time for your choice'
_Ao='error: mouse location (and area width/height) is needed'
_An='error: number of repeat is needed to save'
_Am=' Action: '
_Al='QFrame {border-bottom: 1.5px solid;border-radius: none;border-color: #c8bab7}'
_Ak='Save File'
_Aj='error: this name exists'
_Ai='%Y-%m-%d %H:%M'
_Ah=' Save in App'
_Ag='images/app_logo'
_Af=' Save to PC'
_Ae='images/CPU'
_Ad='color: black;font-weight: bold'
_Ac='color: #bfcfb2;font-weight: bold'
_Ab='  Name your loop'
_Aa='background-color: rgb(239, 229, 220);border: 1px solid rgb(196, 177, 174);border-radius: none;'
_AZ='background-color: #10131b;;border: 1px solid #bfcfb2;border-radius: none;color: #bfcfb2'
_AY='border: 1px solid rgb(196, 174, 174);border-radius: 5px;'
_AX='border: 1px solid #bfcfb2;border-radius: 5px;'
_AW='background-color: #10131b;'
_AV='images/icons8-save-90'
_AU='images/icons8-ui-64.png'
_AT='background-color: #10131b'
_AS="SELECT * FROM user_info WHERE unique_device_id ='"
_AR=' Keyboard'
_AQ='images/red-circle'
_AP='images/GGicon'
_AO='images/LogOut'
_AN='images/Record'
_AM='images/home'
_AL='version2.ui'
_AK='QPushButton {background-color: rgb(239, 229, 220);border-radius: 3px;border: 1px solid;border-color: rgb(239, 229, 220);}'
_AJ='QPushButton {background-color: #10131b;border-radius: 3px;border: 1px solid;border-color: #10131b;}'
_AI='images/Red-Minus-PNG-File'
_AH='    ms'
_AG=' Delay:'
_AF=' Type:'
_AE='border: none;color: #3a5b41;'
_AD=' (saved from record)'
_AC=' (saved from home)'
_AB='CSV Files(*.csv)'
_AA='error: no actions available'
_A9='color: red;'
_A8='USERNAME'
_A7='background-color: rgb(239, 229, 220)'
_A6='images/run_dark'
_A5=' Standby'
_A4='Right'
_A3='Middle'
_A2='QComboBox {background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(218, 218, 218);padding-left: 2px;}QComboBox::drop-down {border: 1px;border-radius: 2px;border-color: rgb(218, 218, 218);}QComboBox::down-arrow {image: url(images/arrow1.png);width: 8px;height: 8px;}'
_A1='current'
_A0='fixed'
_z='range'
_y='error: name is needed'
_x='QPushButton::hover {border: 1px solid rgb(158, 143, 141);background-color: rgb(196, 177, 174);color: white;}QPushButton {background-color: rgb(249, 249, 245);border-radius: 3px;border: 1px solid rgb(158, 143, 141)}'
_w='QPushButton::hover {border: 1px solid #bfcfb2;background-color: rgb(196, 177, 174);color: white;}QPushButton {background-color: rgb(249, 249, 245);border-radius: 3px;border: 1px solid #bfcfb2;}'
_v=' + enter '
_u=' + '
_t='down)'
_s='QLabel {color: black;background-color: rgb(249, 249, 245);border: none;}QToolTip {background-color: #e0e0e0;border: none;}'
_r=' Hibernate'
_q=' Log off'
_p=' Turn off'
_o=' Lock'
_n=' Quit'
_m='No'
_l='Left'
_k='images/Hambuger'
_j='Key'
_i='APPKEY'
_h='APPID'
_g='border: none;background-color: rgb(239, 229, 220);'
_f='border: none;background-color: #10131b;'
_e='border: none;background-color: rgb(239, 229, 220)'
_d='border: none;background-color: #10131b'
_c='Release'
_b='images/ico_logo.ico'
_a='error: x and y location are needed'
_Z='images/check_icon'
_Y='images/check_icon_dark'
_X='images/empty_checkbox'
_W='images/empty_checkbox_dark'
_V='min'
_U='Yes'
_T='enter'
_S='color: black;border: 1px solid #bfcfb2;border-radius: 5px;background-color: rgb(249, 249, 245);'
_R='LOGGED_IN'
_Q="'"
_P='ms'
_O='Press'
_N='background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(218, 218, 218)'
_M='scroll'
_L=None
_K='1'
_J='char'
_I='mouse'
_H='keyboard'
_G='autoclicker.db'
_F='Single'
_E='100'
_D='border:none;'
_C='border: none;'
_B=False
_A=True
import csv
from device_id_file import device_id
import sqlite3
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QFrame,QWidget,QComboBox,QPushButton,QGroupBox,QLineEdit,QSpinBox,QRadioButton,QScrollArea,QHBoxLayout,QFormLayout,QFileDialog,QGridLayout,QListWidgetItem,QCheckBox,QDialog,QListWidget,QToolButton,QScrollBar,QSplashScreen
from PyQt5 import uic,QtGui,QtWidgets,QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt,QSettings
import sys,os,threading
from time import sleep
import time,mouse,keyboard,random
from functions_file import functions
import ctypes
from win10toast import ToastNotifier
import pynput,datetime
from datetime import timedelta
import webbrowser
from payment_dialog import Ui_Dialog
import hashlib
form=functions.resource_path(_AL)
Ui_MainWindow,QtBaseClass=uic.loadUiType(form)
def home_fixed_clicking(mouse_type,click_type,click_repeat,location_x,location_y,wait_interval):
        J=click_type;H=wait_interval;G=location_y;F=location_x;E=click_repeat;D=mouse_type;stop_home_event.clear()
        if H[0]==H[1]:
                if H[0]>2:A=int(H[0]/2);B=float(H[0]-A*2);C=2
                else:A=1;B=0;C=H[0]
                if E>0:
                        if J==_F:
                                for L in range(E):
                                        mouse.move(F,G);mouse.click(button=D)
                                        for I in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                        else:
                                for L in range(E):
                                        mouse.move(F,G);mouse.double_click(button=D)
                                        for I in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                elif E==0:0
                elif J==_F:
                        while _A:
                                mouse.move(F,G);mouse.click(button=D)
                                for I in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
                else:
                        while _A:
                                mouse.move(F,G);mouse.double_click(button=D)
                                for I in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
        else:
                K=round(random.uniform(H[0],H[1]),1)
                if K>2:A=int(K/2);B=float(K-A*2);C=2
                else:A=1;B=0;C=K
                if E>0:
                        if J==_F:
                                for L in range(E):
                                        mouse.move(F,G);mouse.click(button=D)
                                        for I in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                        else:
                                for L in range(E):
                                        mouse.move(F,G);mouse.double_click(button=D)
                                        for I in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                elif E==0:0
                elif J==_F:
                        while _A:
                                mouse.move(F,G);mouse.click(button=D)
                                for I in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
                else:
                        while _A:
                                mouse.move(F,G);mouse.double_click(button=D)
                                for I in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
        UIWindow.after_home_thread()
def home_current_clicking(mouse_type,click_type,click_repeat,waiting_interval):
        H=click_type;F=waiting_interval;E=click_repeat;D=mouse_type;stop_home_event.clear()
        if F[0]==F[1]:
                if F[0]>2:A=int(F[0]/2);B=float(F[0]-A*2);C=2
                else:A=1;B=0;C=F[0]
                if E>0:
                        if H==_F:
                                for J in range(E):
                                        mouse.click(button=D)
                                        for G in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                        else:
                                for J in range(E):
                                        mouse.double_click(button=D)
                                        for G in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                elif E==0:0
                elif H==_F:
                        while _A:
                                mouse.click(button=D)
                                for G in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
                else:
                        while _A:
                                mouse.double_click(button=D)
                                for G in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
        else:
                I=round(random.uniform(F[0],F[1]),1)
                if I>2:A=int(I/2);B=float(I-A*2);C=2
                else:A=1;B=0;C=I
                if E>0:
                        if H==_F:
                                for J in range(E):
                                        mouse.click(button=D)
                                        for G in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                        else:
                                for J in range(E):
                                        mouse.double_click(button=D)
                                        for G in range(A):
                                                sleep(C)
                                                if stop_home_event.is_set():break
                                        sleep(B)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                elif E==0:0
                elif H==_F:
                        while _A:
                                mouse.click(button=D)
                                for G in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
                else:
                        while _A:
                                mouse.double_click(button=D)
                                for G in range(A):
                                        sleep(C)
                                        if stop_home_event.is_set():break
                                sleep(B)
                                if stop_home_event.is_set():stop_home_event.clear();break
        UIWindow.after_home_thread()
def home_random_clicking(mouse_type,click_type,click_repeat,location_x,location_y,wait_interval,area_width,area_height):
        N=click_type;J=wait_interval;I=click_repeat;H=mouse_type;G=location_y;F=location_x;stop_home_event.clear();K=F+area_width;L=G+area_height
        if J[0]==J[1]:
                if J[0]>2:C=int(J[0]/2);D=float(J[0]-C*2);E=2
                else:C=1;D=0;E=J[0]
                if I>0:
                        if N==_F:
                                for P in range(I):
                                        A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.click(button=H)
                                        for M in range(C):
                                                sleep(E)
                                                if stop_home_event.is_set():break
                                        sleep(D)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                        else:
                                for P in range(I):
                                        A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.double_click(button=H)
                                        for M in range(C):
                                                sleep(E)
                                                if stop_home_event.is_set():break
                                        sleep(D)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                elif I==0:0
                elif N==_F:
                        while _A:
                                A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.click(button=H)
                                for M in range(C):
                                        sleep(E)
                                        if stop_home_event.is_set():break
                                sleep(D)
                                if stop_home_event.is_set():stop_home_event.clear();break
                else:
                        while _A:
                                A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.double_click(button=H)
                                for M in range(C):
                                        sleep(E)
                                        if stop_home_event.is_set():break
                                sleep(D)
                                if stop_home_event.is_set():stop_home_event.clear();break
        else:
                O=round(random.uniform(J[0],J[1]),1)
                if O>2:C=int(O/2);D=float(O-C*2);E=2
                else:C=1;D=0;E=O
                if I>0:
                        if N==_F:
                                for P in range(I):
                                        A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.click(button=H)
                                        for M in range(C):
                                                sleep(E)
                                                if stop_home_event.is_set():break
                                        sleep(D)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                        else:
                                for P in range(I):
                                        A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.double_click(button=H)
                                        for M in range(C):
                                                sleep(E)
                                                if stop_home_event.is_set():break
                                        sleep(D)
                                        if stop_home_event.is_set():stop_home_event.clear();break
                elif I==0:0
                elif N==_F:
                        while _A:
                                A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.click(button=H)
                                for M in range(C):
                                        sleep(E)
                                        if stop_home_event.is_set():break
                                sleep(D)
                                if stop_home_event.is_set():stop_home_event.clear();break
                else:
                        while _A:
                                A=random.randint(F,K);B=random.randint(G,L);mouse.move(A,B);mouse.double_click(button=H)
                                for M in range(C):
                                        sleep(E)
                                        if stop_home_event.is_set():break
                                sleep(D)
                                if stop_home_event.is_set():stop_home_event.clear();break
        UIWindow.after_home_thread()
def click_for_record(location_x,location_y,mouse_type,action_type,wait_interval):
        C=mouse_type;B=location_y;A=location_x;D=wait_interval/1000;E=mouse.get_position()
        if action_type==_O:
                sleep(D)
                if not E==(A,B):mouse.move(A,B,duration=0.01)
                mouse.press(button=C)
        else:
                sleep(D)
                if not E==(A,B):mouse.move(A,B,duration=0.1)
                mouse.release(button=C)
def scroll_for_record(location_x,location_y,scroll_type,click_repeat,waiting_interval):
        C=click_repeat;B=location_y;A=location_x;D=int(waiting_interval/C)/1000;E=mouse.get_position()
        if scroll_type=='Up':
                for F in range(C):
                        sleep(D)
                        if not E==(A,B):mouse.move(A,B)
                        mouse.wheel(1)
                        if stop_record_event.is_set():return
        else:
                for F in range(C):
                        sleep(D)
                        if not E==(A,B):mouse.move(A,B)
                        mouse.wheel(-1)
                        if stop_record_event.is_set():return
def type_for_record(key,key_type,action_type,waiting_interval):
        E=waiting_interval;D=action_type;A=key;B=pynput.keyboard.Controller()
        if key_type==_j:
                if str(A)[0]=='<':
                        try:C=pynput.keyboard.KeyCode(vk=int(str(A)[1:-1]))
                        except ValueError:stop_record_event.set();return
                        sleep(E/1000)
                        if D==_O:B.press(C)
                        else:B.release(C)
                else:
                        C=functions.key_converter(A.replace('Key.','').replace('_l','').replace('_r','').lower())
                        if C=='wrong':stop_record_event.set();wrong_key_event.set();return
                        else:
                                sleep(E/1000)
                                if D==_O:B.press(C)
                                else:B.release(C)
        else:
                F=len(A);H=int(E/F)/1000
                for G in range(F):
                        sleep(H)
                        if D==_O:B.press(A[G])
                        else:B.release(A[G])
                        if stop_record_event.is_set():return
def start_record_actions(actions_data,repeat_all,delay_time,i):
        C=delay_time;A=actions_data;F=0
        if C>2:D=int(C/2);G=float(C-D*2);H=2
        else:D=1;G=0;H=C
        for J in range(int(repeat_all)):
                for B in range(i-1):
                        F+=1
                        if A[B][0]==_I:
                                try:click_for_record(int(A[B][1]),int(A[B][2]),A[B][3].lower(),A[B][4],int(A[B][5]))
                                except:break
                        elif A[B][0]==_H:
                                try:type_for_record(A[B][1],A[B][2],A[B][3],int(A[B][4]))
                                except:break
                        else:
                                try:scroll_for_record(int(A[B][1]),int(A[B][2]),A[B][3],int(A[B][4]),int(A[B][5]))
                                except:break
                        if stop_record_event.is_set():break
                if stop_record_event.is_set():stop_record_event.clear();break
                for K in range(D):
                        sleep(H)
                        if stop_record_event.is_set():break
                sleep(G)
                if stop_record_event.is_set():stop_record_event.clear();break
        for E in range(i-1):
                if A[E][0]==_H:
                        I=A[E][1].replace('Key.','').replace('_l','').replace('_r','').lower()
                        if keyboard.is_pressed(I):type_for_record(I,A[E][2],_c,0)
        UIWindow.after_record_thread(F)
class UI(QMainWindow):
        def __init__(A):
                X='Put the  PC to Hibernate mode';W='Put the PC to Standby mode';V='Sign out of the PC with all the apps closed';U='Shut down the PC';T='Sign out of PC with apps still running';S='Close the tool (PC keeps running)';R='No changes to PC';Q=' Idle';P='images/liliajohn';O='QComboBox {background-color: rgb(249, 249, 245);border: 2px solid;border-radius: 7px;border-color: rgb(217, 217, 217);}QComboBox QAbstractItemView {background-color: rgb(249, 249, 245);border: none;color: black;}QComboBox::drop-down {border: 2px;border-radius: 5px;border-color: rgb(249, 249, 245);}QComboBox::down-arrow {image: url(images/arrow1);width: 8px;height: 8px;}';N='hotkey_settings_frame';M='images/app_logo.png';E='no valid key';D='hr';C='QComboBox {background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(218, 218, 218);}QComboBox QAbstractItemView {background-color: rgb(249, 249, 245);border: none;color: black;}QComboBox::drop-down {border: 1px;border-radius: 2px;border-color: rgb(218, 218, 218);}QComboBox::down-arrow {image: url(images/arrow1.png);width: 8px;height: 8px;}';super(UI,A).__init__();uic.loadUi(_AL,A);A.login_signup_button_3.clicked.connect(A.gotologin_signup);A.settings=QSettings('GG','autoclicker');A.MainWindow=A.findChild(QMainWindow,'MainWindow');A.setWindowIcon(QtGui.QIcon(M));A.setFixedWidth(662);A.setFixedHeight(533);A.buy_button.clicked.connect(A.open_payment_dialog);A.buy_button_3.clicked.connect(A.open_payment_dialog);A.central_widget=A.findChild(QWidget,'central_widget');A.central_widget_2=A.findChild(QFrame,'central_widget_2');A.integer=QIntValidator();A.main_frame=A.findChild(QFrame,'main_frame');A.home_frame=A.findChild(QFrame,'home_frame');A.snipping_push_button=A.findChild(QPushButton,'snipping_push_button');A.snipping_push_button.clicked.connect(A.screenCapture);A.tmpDimScreen=CaptureScreen();A.snipping_radio_button=A.findChild(QRadioButton,'snipping_radio_button');A.fixed_location_radio_button=A.findChild(QRadioButton,'fixed_location_radio_button');A.current_location_radio_button=A.findChild(QRadioButton,'current_location_radio_button');A.fixed_location_x=A.findChild(QLineEdit,'fixed_location_x');A.fixed_location_y=A.findChild(QLineEdit,'fixed_location_y');A.height_label=A.findChild(QLabel,'height_label');A.select_area_height=A.findChild(QLineEdit,'select_area_height');A.select_area_radio_button=A.findChild(QRadioButton,'select_area_radio_button');A.select_area_width=A.findChild(QLineEdit,'select_area_width');A.select_area_x=A.findChild(QLineEdit,'select_area_x');A.select_area_y=A.findChild(QLineEdit,'select_area_y');A.short_cut_label=A.findChild(QLabel,'short_cut_label');A.width_label=A.findChild(QLabel,'width_label');A.x_left_label=A.findChild(QLabel,'x_left_label');A.x_right_label=A.findChild(QLabel,'x_right_label');A.y_left_label=A.findChild(QLabel,'y_left_label');A.y_right_label=A.findChild(QLabel,'y_right_label');A.click_options_groupbox=A.findChild(QGroupBox,'click_options_groupbox');A.click_type_combobox=A.findChild(QComboBox,'click_type_combobox');A.click_type_combobox.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(218, 218, 218);}QComboBox QAbstractItemView {background-color: rgb(249, 249, 245);border: none;color: black;}QComboBox::drop-down {border: 1px;border-radius: 2px;border-color: rgb(249, 249, 245);}QComboBox::down-arrow {image: url(images/arrow1.png);width: 8px;height: 8px;}');A.click_type_label=A.findChild(QLabel,'click_type_label');A.mouse_button_combobox=A.findChild(QComboBox,'mouse_button_combobox');A.mouse_button_combobox.setStyleSheet(C);A.mouse_button_label=A.findChild(QLabel,'mouse_button_label');A.click_repeat_groupbox=A.findChild(QGroupBox,'click_repeat_groupbox');A.never_stop_combobox=A.findChild(QComboBox,'never_stop_combobox');A.never_stop_combobox.setStyleSheet(C);A.never_stop_label=A.findChild(QLabel,'never_stop_label');A.repeat_for_label=A.findChild(QLabel,'repeat_for_label');A.repeat_for_number=A.findChild(QLineEdit,'repeat_for_number');A.delay_groupbox=A.findChild(QGroupBox,'delay_groupbox');A.delay_time_combobox=A.findChild(QComboBox,'delay_time_combobox');A.delay_time_combobox.setStyleSheet(C);A.delay_time_combobox_2=A.findChild(QComboBox,'delay_time_combobox_2');A.delay_time_combobox_2.setStyleSheet(C);A.delay_time_entrybox=A.findChild(QLineEdit,'delay_time_entrybox');A.line_label=A.findChild(QLabel,'line_label');A.range_max=A.findChild(QLineEdit,'range_max');A.range_min=A.findChild(QLineEdit,'range_min');A.range_radio_button=A.findChild(QRadioButton,'range_radio_button');A.repeat_radio_button=A.findChild(QRadioButton,'repeat_radio_button');A.play_button=A.findChild(QPushButton,'play_button');A.reset_settings_button=A.findChild(QPushButton,'reset_settings_button');A.save_settings_button=A.findChild(QPushButton,'save_settings_button');A.hotkey_settings_frame=A.findChild(QFrame,N);A.left_frame=A.findChild(QFrame,'left_frame');A.home_button=A.findChild(QToolButton,'home_button');A.home_button.setIcon(QtGui.QIcon(_AM));A.record_button=A.findChild(QToolButton,'record_button');A.record_button.setIcon(QtGui.QIcon(_AN));A.theme_button=A.findChild(QToolButton,'theme_button');A.theme_button.setIcon(QtGui.QIcon('images/Mode'));A.view_settings_button=A.findChild(QToolButton,'view_settings_button');A.view_settings_button.setIcon(QtGui.QIcon('images/Settings'));A.navigation_frame=A.findChild(QFrame,'navigation_frame');A.record_frame=A.findChild(QFrame,'record_frame');A.view_settings_frame=A.findChild(QFrame,'view_settings_frame');A.hotkey_settings_button=A.findChild(QToolButton,'hotkey_settings_button');A.hotkey_settings_button.setIcon(QtGui.QIcon('images/HotkeyBlack'));A.hotkey_settings_frame=A.findChild(QFrame,N);A.top_frame=A.findChild(QFrame,'top_frame');A.top_frame_logged_out=A.findChild(QFrame,'top_frame_logged_out');A.app_icon=A.findChild(QLabel,'app_icon');A.complete_combobox=A.findChild(QComboBox,'complete_combobox');A.complete_combobox.setStyleSheet(O);A.complete_combobox_3=A.findChild(QComboBox,'complete_combobox_3');A.complete_combobox_3.setStyleSheet(O);A.log_out_button=A.findChild(QPushButton,'log_out_button');A.log_out_button.setIcon(QtGui.QIcon(_AO));A.GG_icon=A.findChild(QPushButton,'GG_icon');A.GG_icon.setIcon(QtGui.QIcon(_AP));A.navigate_button=A.findChild(QPushButton,'navigate_button');A.navigate_button.setIcon(QtGui.QIcon(_k));A.navigate_button_3=A.findChild(QPushButton,'navigate_button_3');A.navigate_button_3.setIcon(QtGui.QIcon(_k));A.profile_button=A.findChild(QPushButton,'profile_button');A.profile_button.setIcon(QtGui.QIcon(P));A.profile_button_3=A.findChild(QPushButton,'profile_button_3');A.profile_button_3.setIcon(QtGui.QIcon(P));A.record_add_button=A.findChild(QPushButton,'record_add_button');A.record_add_button.setIcon(QtGui.QIcon('images/icons8-ui-64'));A.record_add_items=A.findChild(QComboBox,'record_add_items');A.record_load_button=A.findChild(QPushButton,'record_load_button');A.record_load_button.setIcon(QtGui.QIcon('images/icons8-upload-96'));A.record_play_button=A.findChild(QPushButton,'record_play_button');A.record_play_button.setIcon(QtGui.QIcon('images/Run'));A.record_record_button=A.findChild(QPushButton,'record_record_button');A.record_record_button.setIcon(QtGui.QIcon(_AQ));A.repeat_for_label_2=A.findChild(QLabel,'repeat_for_label_2');A.repeat_for_number_2=A.findChild(QLineEdit,'repeat_for_number_2');A.repeat_for_number_2.setValidator(A.integer);A.repeat_for_label_2.hide();A.repeat_for_number_2.hide();A.repeat_for_number_2.setText(_K);A.delay_label_2=A.findChild(QLabel,'delay_label_2');A.delay_2=A.findChild(QLineEdit,'delay_2');A.delay_time_combobox_record=A.findChild(QComboBox,'delay_time_combobox_record');A.delay_label_2.hide();A.delay_2.hide();A.delay_time_combobox_record.hide();A.delay_2.setText(_E);A.delay_time_combobox_record.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(249, 249, 245);}QComboBox QAbstractItemView {background-color: rgb(249, 249, 245);border: none;color: black;}QComboBox::drop-down {border: 1px;border-radius: 2px;border-color: rgb(249, 249, 245);background-color: rgb(249, 249, 245);}QComboBox::down-arrow {background-color: rgb(249, 249, 245);image: url(images/arrow1.png);width: 8px;height: 8px;}');A.delay_time_combobox_record.addItem(_P);A.delay_time_combobox_record.addItem('s');A.delay_time_combobox_record.addItem(_V);A.delay_time_combobox_record.addItem(D);A.record_remove_all_button=A.findChild(QPushButton,'record_remove_all_button');A.record_save_button=A.findChild(QPushButton,'record_save_button');A.record_scroll_area=A.findChild(QScrollArea,'record_scroll_area');A.scroll_bar=A.record_scroll_area.findChildren(QWidget)[5];A.scrollAreaWidgetContents=A.findChild(QWidget,'scrollAreaWidgetContents');A.scrollAreaWidgetContents.setFixedWidth(518);A.scrollAreaWidgetContents.setStyleSheet(_C);A.form_layout=QFormLayout(A.scrollAreaWidgetContents);A.foot_note_label=A.findChild(QLabel,'foot_note_label');A.live_mouse_label=A.findChild(QLabel,'live_mouse_label');A.home_start_stop_hotkey_label=A.findChild(QLabel,'home_start_stop_hotkey');A.mouse_location_hotkey_label=A.findChild(QLabel,'mouse_location_hotkey');A.record_start_stop_hotkey_label=A.findChild(QLabel,'record_start_stop_hotkey');A.playback_start_stop_hotkey_label=A.findChild(QLabel,'playback_start_stop_hotkey');A.set_new_hotkey_button_1=A.findChild(QPushButton,'set_new_hotkey_1');A.set_new_hotkey_button_2=A.findChild(QPushButton,'set_new_hotkey_2');A.set_new_hotkey_button_3=A.findChild(QPushButton,'set_new_hotkey_3');A.set_new_hotkey_button_4=A.findChild(QPushButton,'set_new_hotkey_4');A.on_click_complete_label=A.findChild(QLabel,'on_click_label');A.on_click_complete_label_3=A.findChild(QLabel,'on_click_label_3');A.username_box=A.findChild(QLabel,'name');A.label=A.findChild(QPushButton,'label');A.frame=A.findChild(QFrame,'frame');A.frame_2=A.findChild(QFrame,'frame_2');A.frame_3=A.findChild(QFrame,'frame_3');A.frame_4=A.findChild(QFrame,'frame_4');A.frame_10=A.findChild(QFrame,'frame_10');A.frame_11=A.findChild(QFrame,'frame_11');A.frame_12=A.findChild(QFrame,'frame_12');A.frame_13=A.findChild(QFrame,'frame_13');A.frame_14=A.findChild(QFrame,'frame_14');A.frame_6=A.findChild(QFrame,'frame_6');A.frame_7=A.findChild(QFrame,'frame_7');A.frame_8=A.findChild(QFrame,'frame_8');A.frame_9=A.findChild(QFrame,'frame_9');A.line_list=[];A.i=1;A.j=0;A.dark_theme_activated=_B;app.aboutToQuit.connect(A.exit_app);A.mouse_button_combobox.addItem(_l);A.mouse_button_combobox.addItem(_A3);A.mouse_button_combobox.addItem(_A4);A.click_type_combobox.addItem(_F);A.click_type_combobox.addItem('Double');A.never_stop_combobox.addItem(_m);A.never_stop_combobox.addItem(_U);A.delay_time_combobox.addItem(_P);A.delay_time_combobox.addItem('s');A.delay_time_combobox.addItem(_V);A.delay_time_combobox.addItem(D);A.complete_combobox.addItem(Q);A.complete_combobox.addItem(_n);A.complete_combobox.addItem(_o);A.complete_combobox.addItem(_p);A.complete_combobox.addItem(_q);A.complete_combobox.addItem(_A5);A.complete_combobox.addItem(_r);A.complete_combobox_3.addItem(Q);A.complete_combobox_3.addItem(_n);A.complete_combobox_3.addItem(_o);A.complete_combobox_3.addItem(_p);A.complete_combobox_3.addItem(_q);A.complete_combobox_3.addItem(_A5);A.complete_combobox_3.addItem(_r);A.delay_time_combobox_2.addItem(_P);A.delay_time_combobox_2.addItem('s');A.delay_time_combobox_2.addItem(_V);A.delay_time_combobox_2.addItem(D);A.record_add_items.addItem(' Mouse');A.record_add_items.addItem(_AR);A.record_add_items.addItem(' Scroll');A.repeat_radio_button.setChecked(_A);A.current_location_radio_button.setChecked(_A);A.record_remove_all_button.setEnabled(_B);A.repeat_for_number.setText(_K);A.delay_time_entrybox.setText(_E)
                for Y in A.home_frame.findChildren(QLineEdit):Y.setValidator(A.integer)
                A.log_out_button.clicked.connect(A.logout);A.record_button.clicked.connect(A.get_record_screen);A.home_button.clicked.connect(A.get_home_screen);A.view_settings_button.clicked.connect(A.get_view_screen);A.hotkey_settings_button.clicked.connect(A.get_hotkey_screen);A.navigate_button.clicked.connect(A.open_menu);A.navigate_button_3.clicked.connect(A.open_menu);A.play_button.clicked.connect(A.home_start_process);A.reset_settings_button.clicked.connect(A.home_reset_settings);A.record_add_button.clicked.connect(A.add_new_line);A.record_load_button.clicked.connect(A.window_load);A.record_save_button.clicked.connect(A.window_record_save);A.save_settings_button.clicked.connect(A.window_home_save);A.record_play_button.clicked.connect(A.record_start_process);A.theme_button.clicked.connect(A.get_dark_theme);A.record_remove_all_button.clicked.connect(A.remove_all_lines);A.never_stop_combobox.currentIndexChanged.connect(A.check_repeat_style);A.complete_combobox.activated.connect(lambda:A.on_click_complete_label.hide());A.complete_combobox_3.activated.connect(lambda:A.on_click_complete_label_3.hide());A.label_21=A.findChild(QLabel,'label_21');A.label_22=A.findChild(QLabel,'label_22');A.label_23=A.findChild(QLabel,'label_23');A.label_24=A.findChild(QLabel,'label_24');A.label_21.hide();A.label_22.hide();A.label_23.hide();A.label_24.hide();A.set_new_hotkey_button_1.clicked.connect(A.start_thread_hotkey_1);A.set_new_hotkey_button_2.clicked.connect(A.start_thread_hotkey_4);A.set_new_hotkey_button_3.clicked.connect(A.start_thread_hotkey_3);A.set_new_hotkey_button_4.clicked.connect(A.start_thread_hotkey_2);A.record_record_button.clicked.connect(A.thread_for_live_record);A.minimized_icon=QtGui.QIcon(M);A.tray=QtWidgets.QSystemTrayIcon();A.tray.setIcon(A.minimized_icon);A.tray.setVisible(_A);A.minimized_menu=QtWidgets.QMenu();A.menu_option_1=QtWidgets.QAction('Open');A.menu_option_1.triggered.connect(A.show);A.minimized_menu.addAction(A.menu_option_1);A.menu_option_2=QtWidgets.QAction('Quit');A.menu_option_2.triggered.connect(app.exit);A.minimized_menu.addAction(A.menu_option_2);A.tray.setContextMenu(A.minimized_menu);A.setStyleSheet('QToolTip {background-color: #e0e0e0;border: none;}QRadioButton::indicator {height: 15px;width: 15px;}QRadioButton::indicator::unchecked {image: url(images/radio_unchecked.png);margin-top: 2px;}QRadioButton::indicator::checked {image: url(images/radio_checked.png);margin-top: 2px;}');A.central_widget_2.setStyleSheet('QToolTip {background-color: #e0e0e0;border: none;color: black;}QFrame {color: rgb(30, 30, 30);background-color: rgb(239, 229, 220); }');A.record_add_items.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(249, 249, 245);}QComboBox::drop-down {background-color: rgb(249, 249, 245);border: 0px;border-color: rgb(249, 249, 245);}QComboBox::down-arrow {background-color: rgb(249, 249, 245);image: url(images/arrow1.png);width: 8px;height: 8px;}QToolTip {background-color: #e0e0e0;border: none;color: black;}QFrame {color: rgb(30, 30, 30);background-color: rgb(239, 229, 220); }');A.complete_combobox.setItemData(0,R,QtCore.Qt.ToolTipRole);A.complete_combobox.setItemData(1,S,QtCore.Qt.ToolTipRole);A.complete_combobox.setItemData(2,T,QtCore.Qt.ToolTipRole);A.complete_combobox.setItemData(3,U,QtCore.Qt.ToolTipRole);A.complete_combobox.setItemData(4,V,QtCore.Qt.ToolTipRole);A.complete_combobox.setItemData(5,W,QtCore.Qt.ToolTipRole);A.complete_combobox.setItemData(6,X,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(0,R,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(1,S,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(2,T,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(3,U,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(4,V,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(5,W,QtCore.Qt.ToolTipRole);A.complete_combobox_3.setItemData(6,X,QtCore.Qt.ToolTipRole);A.hide_to_tray_checkbox2=A.findChild(QPushButton,'hide_to_tray_checkbox2');A.show_after_complete_checkbox2=A.findChild(QPushButton,'hide_while_click_checkbox2');A.mouse_location_checkbox2=A.findChild(QPushButton,'mouse_location_checkbox2');A.hide_to_tray_checkbox=A.findChild(QCheckBox,'hide_to_tray_checkbox');A.show_after_complete_checkbox=A.findChild(QCheckBox,'hide_while_click_checkbox');A.mouse_location_checkbox=A.findChild(QCheckBox,'mouse_location_checkbox');A.hide_to_tray_checkbox.hide();A.show_after_complete_checkbox.hide();A.mouse_location_checkbox.hide();A.hide_to_tray_checkbox2.clicked.connect(A.trigger_tray_checkbox);A.mouse_location_checkbox2.clicked.connect(A.trigger_live_mouse);A.show_after_complete_checkbox2.clicked.connect(A.trigger_show_tool);A.check_live_mouse()
                if show_tool_after==1:A.show_after_complete_checkbox2.click()
                if hide_system_tray==1:A.hide_to_tray_checkbox2.click()
                if disable_cursor_location==1:A.mouse_location_checkbox2.click()
                if dark_theme==1:A.get_dark_theme()
                A.home_start_stop_hotkey=home_start_hotkey;A.record_start_stop_hotkey=record_start_hotkey;A.record_recording_hotkey=record_recording_hotkey;A.mouse_location_hotkey=mouse_location_hotkey;keyboard.add_hotkey(A.mouse_location_hotkey,A.get_mouse_location);keyboard.add_hotkey(A.home_start_stop_hotkey,lambda:A.play_button.click());keyboard.add_hotkey(A.record_start_stop_hotkey,lambda:A.record_play_button.click());keyboard.add_hotkey(A.record_recording_hotkey,lambda:A.record_record_button.click());A.home_start_stop_hotkey_label.setText(str(home_start_hotkey));A.playback_start_stop_hotkey_label.setText(str(record_start_hotkey));A.record_start_stop_hotkey_label.setText(str(record_recording_hotkey));A.mouse_location_hotkey_label.setText(str(mouse_location_hotkey));A.label_10=A.findChild(QLabel,'label_10');A.label_2=A.findChild(QLabel,'label_2');A.label_3=A.findChild(QLabel,'label_3');A.label_4=A.findChild(QLabel,'label_4');A.label_6=A.findChild(QLabel,'label_6');A.label_7=A.findChild(QLabel,'label_7');A.font=QtGui.QFont();A.font.setPixelSize(13)
                for B in A.findChildren(QLabel):B.setFont(A.font)
                for B in A.findChildren(QComboBox):B.setFont(A.font)
                for B in A.findChildren(QRadioButton):B.setFont(A.font)
                for B in A.findChildren(QLineEdit):B.setFont(A.font)
                for B in A.home_frame.findChildren(QPushButton):B.setFont(A.font)
                for B in A.record_frame.findChildren(QPushButton):B.setFont(A.font)
                for B in A.findChildren(QToolButton):B.setFont(A.font)
                A.font.setPixelSize(11);A.on_click_complete_label.setFont(A.font);A.on_click_complete_label_3.setFont(A.font);A.font.setPixelSize(10);A.label_10.setFont(A.font);A.font.setPixelSize(11);A.font.setBold(_B);A.username_box.setFont(A.font);A.font.setBold(_A);A.label_2.setFont(A.font);A.label_3.setFont(A.font);A.label_4.setFont(A.font);A.label_6.setFont(A.font);A.label_7.setFont(A.font);A.label_9=A.findChild(QLabel,'label_9');A.label_14=A.findChild(QLabel,'label_14');A.label_15=A.findChild(QLabel,'label_15');A.label_16=A.findChild(QLabel,'label_16');A.label_17=A.findChild(QLabel,'label_17');A.label_9.setFont(A.font);A.label_14.setFont(A.font);A.label_15.setFont(A.font);A.label_16.setFont(A.font);A.label_17.setFont(A.font);A.font.setBold(_B);A.foot_note_label.setFont(A.font);A.live_mouse_label.setFont(A.font);A.font.setPixelSize(12);A.record_add_items.setFont(A.font);A.delay_time_combobox.setFont(A.font);A.delay_time_combobox_2.setFont(A.font);A.delay_time_combobox_record.setFont(A.font);Z=A.findChild(QPushButton,'pushButton');Z.clicked.connect(lambda:webbrowser.open('https://autoclicker.gg/'));a=A.findChild(QPushButton,'pushButton_2');a.clicked.connect(lambda:webbrowser.open('https://autoclicker.gg/windows'));b=A.findChild(QPushButton,'pushButton_3');b.clicked.connect(lambda:webbrowser.open('https://autoclicker.gg/contact'));c=A.findChild(QPushButton,'pushButton_4');c.clicked.connect(lambda:webbrowser.open('https://autoclicker.gg/FAQs'));d=A.findChild(QPushButton,'pushButton_5');d.clicked.connect(lambda:webbrowser.open('https://autoclicker.gg/privacy-policy/'));e,F,f=A.getAppIdKey();G=str(device_id.get_windows_uuid())
                if e==G:
                        g=G;H=sqlite3.connect(_G);I=H.cursor();h="SELECT * FROM session_details WHERE application_id ='"+g+_Q;I.execute(h);J=I.fetchone();H.close()
                        if J is not _L:
                                K=J[2]
                                if F!=''and K==F:
                                        print('kokos');L=A.checkAppKey(K);print(L)
                                        if L==1:A.top_frame_logged_out.hide();A.top_frame.show();A.settings.setValue(_R,1);print('key validated');A.name.setText(str(f))
                                        else:print(E);A.logout()
                                else:print(E);A.logout()
                        else:print(E);A.logout()
        def open_payment_dialog(A):A.dialog=QtWidgets.QDialog();A.ui=Ui_Dialog();A.ui.setupUi(A.dialog);A.dialog.show()
        def gotologin_signup(A):A.get_login_signup_screen();A.login_Button.clicked.connect(A.gotologin);A.signup_Button.clicked.connect(A.gotosignup)
        def gotosignup(A):A.get_signup_screen();A.password_signup.setEchoMode(QtWidgets.QLineEdit.Password);A.signup_Butt.clicked.connect(A.signupfunction);A.message_2.setText('');A.username_signup.setText('');A.password_signup.setText('')
        def signupfunction(A):
                D=A.username_signup.text();E=A.password_signup.text();F=str(device_id.get_windows_uuid());H=hashlib.sha256(E.encode());I=H.hexdigest();J=1
                if len(D)==0 or len(E)==0:A.message_2.setText('Please fill in all inputs.')
                else:
                        B=sqlite3.connect(_G);C=B.cursor();K="SELECT * FROM user_info WHERE username ='"+D+_Q;C.execute(K);L=C.fetchone();M=_AS+F+_Q;C.execute(M);G=C.fetchone();B.close()
                        if G is not _L:print(G);A.message_2.setText('This device is already registered. Log in to continue!')
                        elif L is not _L:A.message_2.setText('username already exists. Choose a different username!')
                        else:B=sqlite3.connect(_G);C=B.cursor();N=[D,I,J,F];C.execute('INSERT INTO user_info (username, password, whether_subscribed, unique_device_id) VALUES (?,?,?,?)',N);B.commit();B.close();A.message_2.setText('Account Created!');A.top_frame_logged_out.hide();A.top_frame.show();A.settings.setValue(_R,1);A.name.setText(str(D));time.sleep(1);A.get_home_screen()
        def whether_logged_in(A):return A.settings.value(_R)
        def gotologin(A):A.get_login_screen();A.password_login.setEchoMode(QtWidgets.QLineEdit.Password);A.login_Butt.clicked.connect(A.loginfunction);A.message.setText('');A.username_login.setText('');A.password_login.setText('')
        def loginfunction(A):
                B=A.username_login.text();L=A.password_login.text();M=hashlib.sha256(L.encode());C=M.hexdigest();E=str(device_id.get_windows_uuid())
                if len(B)==0 or len(C)==0:A.message.setText('Please input all fields.')
                else:
                        D=sqlite3.connect(_G);G=D.cursor();N=_AS+E+_Q;G.execute(N);F=G.fetchone();D.close()
                        if F is _L:A.message.setText('Device is not registered!');B=A.username_login.setText('');C=A.password_login.setText('')
                        else:
                                H=F[0];I=F[1];U=F[2];O=F[3]
                                if I==C and O==E and H==B:A.message.setText('Successfully logged in!');J=functions.randomword(12);A.createNewAppKey(E,J,B);time.sleep(1);A.get_home_screen();A.settings.setValue(_R,1);A.top_frame_logged_out.hide();A.top_frame.show();A.name.setText(str(B));P=datetime.datetime.now();Q=P+timedelta(days=1);R=str(Q);D=sqlite3.connect(_G);K=D.cursor();S="DELETE FROM session_details WHERE application_id = '"+E+_Q;K.execute(S);print('deleted app_id row if already present in session_details');T=f"""INSERT INTO session_details VALUES (
                            '{B}',
                            '{E}',
                            '{J}',
                            '{R}'
                            )""";K.execute(T);D.commit();D.close();print('added row in session_details')
                                elif H!=B:A.message.setText('Invalid username for this device');time.sleep(2);A.message.setText('');B=A.username_login.setText('');C=A.password_login.setText('')
                                elif I!=C:A.message.setText('Invalid password!');time.sleep(2);A.message.setText('');C=A.password_login.setText('')
                A.login_Butt.clicked.connect(A.loginfunction);A.password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        def screenCapture(A):'Show the dim Splashscreen';A.hide();A.tmpDimScreen.show();A.original_x=A.tmpDimScreen.getOriginal_x();A.original_y=A.tmpDimScreen.getOriginal_y();A.final_x=A.tmpDimScreen.getFinal_x();A.final_y=A.tmpDimScreen.getFinal_y();A.snipping_width=abs(A.final_x-A.original_x);A.snipping_height=abs(A.final_y-A.original_y);A.snip_x=min(A.final_x,A.original_x);A.snip_y=min(A.final_y,A.original_y)
        def trigger_show_tool(A):
                if A.show_after_complete_checkbox.isChecked():
                        A.show_after_complete_checkbox.setChecked(_B)
                        if A.dark_theme_activated:A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_W));A.show_after_complete_checkbox2.setStyleSheet(_d)
                        else:A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_X));A.show_after_complete_checkbox2.setStyleSheet(_e)
                else:
                        A.show_after_complete_checkbox.setChecked(_A)
                        if A.dark_theme_activated:A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_Y));A.show_after_complete_checkbox2.setStyleSheet(_d)
                        else:A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_Z));A.show_after_complete_checkbox2.setStyleSheet(_e)
        def exit_app(A):
                if A.show_after_complete_checkbox.isChecked():C=1
                else:C=0
                if A.hide_to_tray_checkbox.isChecked():D=1
                else:D=0
                if A.mouse_location_checkbox.isChecked():E=1
                else:E=0
                if A.dark_theme_activated:F=1
                else:F=0
                H=A.home_start_stop_hotkey;I=A.record_start_stop_hotkey;J=A.record_recording_hotkey;K=A.mouse_location_hotkey;B=sqlite3.connect(_G);G=B.cursor();L='DELETE FROM app_settings';G.execute(L);M=f"""INSERT INTO app_settings VALUES (
                '{C}',
                '{D}',
                '{E}',
                '{F}',
                '{H}',
                '{I}',
                '{J}',
                '{K}'
                )""";G.execute(M);B.commit();B.close();app.exit()
        def get_dark_theme(A):
                K='images/Profile-Picture_dark';J='images/Menu_dark.png';I='QPushButton {color: #1ecd97;border: 2px solid #1ecd97;border-radius: 5px;color: #1ecd97;}QPushButton::hover {color:white;background-color: #1ecd97;}';H='QPushButton {color: #c98860;border: 2px solid #c98860;border-radius: 5px;color: #c98860;}QPushButton::hover {color:white;background-color: #c98860;}';G='QPushButton {color: #ffa94d;border: 2px solid #ffa94d;border-radius: 5px;color: #ffa94d;}QPushButton::hover {color:white;background-color: #ffa94d;}';F='QFrame {background-color: #10131b;color: #bfcfb2;border: none;}QComboBox {color: black;background-color: rgb(249, 249, 245);border: none}QLineEdit {color: black;background-color: rgb(249, 249, 245);border: none}';E='QFrame {background-color: #10131b;color: #bfcfb2;border: none;}QComboBox {color: black;background-color: rgb(249, 249, 245);border: none}QLineEdit {color: black;background-color: rgb(249, 249, 245);border: none}QRadioButton {color: #bfcfb2;}';D='color: black;background-color: #e0e0e0;';C='border: 2px solid #bfcfb2;border-radius: 10px;';B='border: 1.5px solid #bfcfb2;border-radius: 10px;';A.setStyleSheet('QComboBox {color: black;background-color: rgb(249, 249, 245);border: none}QComboBox::drop-down {background-color: rgb(249, 249, 245);border-color: rgb(249, 249, 245);}QToolTip {background-color: #e0e0e0;border: none;}QRadioButton::indicator {height: 15px;width: 15px;}QRadioButton::indicator::unchecked {image: url(images/dark_unchecked.png);margin-top: 2px;}QRadioButton::indicator::checked {image: url(images/dark_checked.png);margin-top: 2px;}');A.dark_theme_activated=_A;A.left_frame.setStyleSheet('background-color: #10131b;color: #bfcfb2;border: 2px solid #bfcfb2;border-radius: 10px;');A.GG_icon.setStyleSheet(_D);A.GG_icon.setIcon(QtGui.QIcon('images/GG_dark'));A.home_button.setStyleSheet(_D);A.home_button.setIcon(QtGui.QIcon('images/Home_dark'));A.record_button.setStyleSheet(_D);A.record_button.setIcon(QtGui.QIcon('images/Record_dark'));A.theme_button.setStyleSheet(_D);A.theme_button.setIcon(QtGui.QIcon('images/Mode_dark.png'));A.view_settings_button.setStyleSheet(_D);A.view_settings_button.setIcon(QtGui.QIcon('images/Setting_dark.png'));A.hotkey_settings_button.setStyleSheet(_D);A.hotkey_settings_button.setIcon(QtGui.QIcon('images/HotKey_dark.png'));A.central_widget_2.setStyleSheet(E);A.main_frame.setStyleSheet(E);A.top_frame.setStyleSheet(F);A.top_frame_logged_out.setStyleSheet(F);A.home_frame.setStyleSheet(E);A.reset_settings_button.setStyleSheet(G);A.play_button.setStyleSheet(H);A.play_button.setIcon(QtGui.QIcon(_A6));A.save_settings_button.setStyleSheet(I);A.foot_note_label.setStyleSheet(_D);A.navigate_button.setStyleSheet(_D);A.navigate_button.setIcon(QtGui.QIcon(J));A.navigation_frame.setStyleSheet('QPushButton {background-color: #10131b;border: 1px solid #bfcfb2;color: #bfcfb2;}');A.navigate_button_3.setStyleSheet(_D);A.navigate_button_3.setIcon(QtGui.QIcon(J));A.on_click_complete_label.setStyleSheet(_s);A.on_click_complete_label_3.setStyleSheet(_s);A.profile_button.setStyleSheet(_C);A.profile_button.setIcon(QtGui.QIcon(K));A.profile_button_3.setStyleSheet(_C);A.profile_button_3.setIcon(QtGui.QIcon(K));A.username_box.setStyleSheet('QLineEdit {background-color: #10131b;color: #bfcfb2;}QToolTip {background-color: #e0e0e0;}');A.log_out_button.setStyleSheet(_C);A.log_out_button.setIcon(QtGui.QIcon('images/LogOut_dark'));A.home_start_stop_hotkey_label.setStyleSheet(_S);A.playback_start_stop_hotkey_label.setStyleSheet(_S);A.record_start_stop_hotkey_label.setStyleSheet(_S);A.mouse_location_hotkey_label.setStyleSheet(_S);A.frame.setStyleSheet('QFrame {border: 1.5px solid #bfcfb2;border-radius: 10px;}QComboBox::drop-down {background-color: rgb(249, 249, 245);border-color: rgb(249, 249, 245);}');A.frame_2.setStyleSheet(B);A.frame_3.setStyleSheet(B);A.frame_4.setStyleSheet(B);A.frame_10.setStyleSheet(C);A.frame_11.setStyleSheet(C);A.frame_12.setStyleSheet(C);A.frame_13.setStyleSheet(C);A.frame_14.setStyleSheet(C);A.view_settings_frame.setStyleSheet('QFrame {background-color: #10131b;color: #bfcfb2;border: none;}');A.frame_6.setStyleSheet(B);A.frame_7.setStyleSheet(B);A.frame_8.setStyleSheet(B);A.frame_9.setStyleSheet(B);A.record_scroll_area.setStyleSheet('QScrollArea {border: 1.5px solid #bfcfb2;background-color: #10131b;border-radius: 5px;}');A.scrollAreaWidgetContents.setStyleSheet(_d);A.scroll_bar.setStyleSheet('QScrollBar:vertical {\n                                        border-color: #10131b;\n                                        border-width: 1px;\n                                        border-style: solid;\n                                        border-radius: 10px;\n                                        background-color: #10131b;\n                                        width:18px;\n                                        margin: 10px 4px 10px 0;}\n                                    QScrollBar::handle:vertical {\n                                        background-color: #bfcfb2;\n                                        min-height: 25px;\n                                        border: 1px solid #bfcfb2;\n                                        border-radius: 5px;}\n                                    QScrollBar::add-line:vertical {\n                                        border: 1px solid #10131b;\n                                        background-color: #10131b;\n                                        height: 0px;\n                                        subcontrol-position: bottom;\n                                        subcontrol-origin: margin;}\n                                    QScrollBar::sub-line:vertical {\n                                        border: 1px solid #10131b;\n                                        background-color: #10131b;\n                                        height: 0px;\n                                        subcontrol-position: top;\n                                        subcontrol-origin: margin;}\n                                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n                                        background: none;}\n                                    QScrollBar::up-arrow:vertical {\n                                      background-color: #10131b;}\n                                    QScrollBar::down-arrow:vertical {\n                                      background-color: #10131b;}')
                for L in A.scrollAreaWidgetContents.children():
                        for M in L.findChildren(QPushButton):M.setStyleSheet(_AT)
                A.record_record_button.setStyleSheet('QPushButton {color: white;border: 2px solid white;border-radius: 5px;color: white;}QPushButton::hover {color:black;background-color: white;}');A.record_play_button.setStyleSheet(H);A.record_play_button.setIcon(QtGui.QIcon(_A6));A.record_save_button.setStyleSheet(I);A.record_remove_all_button.setStyleSheet(G);A.record_load_button.setStyleSheet('QPushButton {color: black;background-color: #bfcfb2;border 1px solid #bfcfb2;border-radius: 3px;}QToolTip {background-color: #e0e0e0;border: none;}');A.record_load_button.setIcon(QtGui.QIcon('images/uplode_dark.png'));A.record_add_button.setStyleSheet('QPushButton {border: 1px solid rgb(196, 177, 174);border-radius: 10;background-color: #bfcfb2;}QToolTip {background-color: #e0e0e0;border: none;}');A.record_add_button.setIcon(QtGui.QIcon(_AU));A.label_21.setStyleSheet(D);A.label_22.setStyleSheet(D);A.label_23.setStyleSheet(D);A.label_24.setStyleSheet(D);A.theme_button.disconnect();A.theme_button.clicked.connect(A.get_normal_theme)
                if A.hide_to_tray_checkbox.isChecked():A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_Y))
                else:A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_W))
                A.hide_to_tray_checkbox2.setStyleSheet(_f)
                if A.show_after_complete_checkbox.isChecked():A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_Y))
                else:A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_W))
                A.show_after_complete_checkbox2.setStyleSheet(_f)
                if A.mouse_location_checkbox.isChecked():A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_Y))
                else:A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_W))
                A.mouse_location_checkbox2.setStyleSheet(_f)
        def get_normal_theme(A):
                F='images/liliajohn.png';E='QPushButton {color: #3A5A40;border: 2px solid #3A5A40;border-radius: 5px;color: #3A5A40;}QPushButton::hover {color:white;background-color: #3A5A40;}';D='border: 2px solid rgb(196, 177, 174);border-radius: 10px;';C='QFrame {background-color: rgb(239, 229, 220);color: rgb(30, 30, 30);border: none;}QComboBox {color: rgb(30, 30, 30);background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;}QLineEdit {color: rgb(30, 30, 30);background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px solid;}QRadioButton {color: rgb(30, 30, 30);border: none;}';B='border: 1.5px solid rgb(196, 177, 174);border-radius: 10px;';A.setStyleSheet('QComboBox::drop-down {background-color: rgb(249, 249, 245);border-color: rgb(249, 249, 245);}QToolTip {background-color: #e0e0e0;border: none;}QRadioButton::indicator {height: 15px;width: 15px;}QRadioButton::indicator::unchecked {image: url(images/radio_unchecked.png);margin-top: 2px;}QRadioButton::indicator::checked {image: url(images/radio_checked.png);margin-top: 2px;}');A.dark_theme_activated=_B;A.left_frame.setStyleSheet('background-color: rgb(196, 177, 174);color: black;border: 2px solid rgb(196, 177, 174);border-radius: 10px;');A.GG_icon.setStyleSheet(_D);A.GG_icon.setIcon(QtGui.QIcon(_AP));A.home_button.setStyleSheet(_D);A.home_button.setIcon(QtGui.QIcon(_AM));A.record_button.setStyleSheet(_D);A.record_button.setIcon(QtGui.QIcon(_AN));A.theme_button.setStyleSheet(_D);A.theme_button.setIcon(QtGui.QIcon('images/Mode.png'));A.view_settings_button.setStyleSheet(_D);A.view_settings_button.setIcon(QtGui.QIcon('images/Settings.png'));A.hotkey_settings_button.setStyleSheet(_D);A.hotkey_settings_button.setIcon(QtGui.QIcon('images/HotkeyBlack.png'));A.central_widget_2.setStyleSheet(C);A.main_frame.setStyleSheet(C);A.top_frame.setStyleSheet(C);A.top_frame_logged_out.setStyleSheet(C);A.home_frame.setStyleSheet(C);A.reset_settings_button.setStyleSheet('QPushButton {color: rgb(255, 162, 0);border: 2px solid rgb(255, 162, 0);border-radius: 5px;color: #ffa94d;}QPushButton::hover {color:white;background-color: rgb(255, 162, 0);}');A.play_button.setStyleSheet(E);A.play_button.setIcon(QtGui.QIcon('images/run'));A.save_settings_button.setStyleSheet('QPushButton {color: rgb(3, 199, 26);border: 2px solid rgb(3, 199, 26);border-radius:5px; color: rgb(3, 199, 26);}QPushButton::hover {color:white;background-color: rgb(3, 199, 26);}');A.foot_note_label.setStyleSheet(_D);A.navigate_button.setStyleSheet(_D);A.navigate_button.setIcon(QtGui.QIcon(_k));A.navigate_button_3.setStyleSheet(_D);A.navigate_button_3.setIcon(QtGui.QIcon(_k));A.navigation_frame.setStyleSheet('QPushButton {background-color: rgb(242,242,242);border: 1px solid rgb(204, 204, 204);color: rgb(30, 30, 30);}');A.on_click_complete_label.setStyleSheet(_s);A.on_click_complete_label_3.setStyleSheet(_s);A.profile_button.setStyleSheet(_C);A.profile_button.setIcon(QtGui.QIcon(F));A.profile_button_3.setStyleSheet(_C);A.profile_button_3.setIcon(QtGui.QIcon(F));A.username_box.setStyleSheet('QLabel {background-color: rgb(239, 229, 220);color: rgb(30, 30, 30);border: none;}QToolTip {background-color: #e0e0e0;}');A.log_out_button.setStyleSheet(_C);A.log_out_button.setIcon(QtGui.QIcon(_AO));A.home_start_stop_hotkey_label.setStyleSheet(_S);A.playback_start_stop_hotkey_label.setStyleSheet(_S);A.record_start_stop_hotkey_label.setStyleSheet(_S);A.mouse_location_hotkey_label.setStyleSheet(_S);A.frame.setStyleSheet(B);A.frame_2.setStyleSheet(B);A.frame_3.setStyleSheet(B);A.frame_4.setStyleSheet(B);A.frame_10.setStyleSheet(D);A.frame_11.setStyleSheet(D);A.frame_12.setStyleSheet(D);A.frame_13.setStyleSheet(D);A.frame_14.setStyleSheet(D);A.view_settings_frame.setStyleSheet('QFrame {background-color: rgb(239, 229, 220);color: rgb(30, 30, 30);border: none;}');A.frame_6.setStyleSheet(B);A.frame_7.setStyleSheet(B);A.frame_8.setStyleSheet(B);A.frame_9.setStyleSheet(B);A.record_scroll_area.setStyleSheet('QScrollArea {border: 1.5px solid #c8bab7;background-color: rgb(239, 229, 220);border-radius: 5px;}');A.scrollAreaWidgetContents.setStyleSheet(_e);A.scroll_bar.setStyleSheet('QScrollBar:vertical {\n                                        border-color: rgb(239, 229, 220);\n                                        border-width: 1px;\n                                        border-style: solid;\n                                        border-radius: 10px;\n                                        background-color: rgb(239, 229, 220);\n                                        width:18px;\n                                        margin: 10px 4px 10px 0;}\n                                    QScrollBar::handle:vertical {\n                                        background-color: #c4b1ad;\n                                        min-height: 25px;\n                                        border: 1px solid #c4b1ad;\n                                        border-radius: 5px;}\n                                    QScrollBar::add-line:vertical {\n                                        border: 1px solid rgb(239, 229, 220);\n                                        background-color: rgb(239, 229, 220);\n                                        height: 0px;\n                                        subcontrol-position: bottom;\n                                        subcontrol-origin: margin;}\n                                    QScrollBar::sub-line:vertical {\n                                        border: 1px solid rgb(239, 229, 220);\n                                        background-color: rgb(241, 241, 241);\n                                        height: 0px;\n                                        subcontrol-position: top;\n                                        subcontrol-origin: margin;}\n                                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n                                        background: none;}\n                                    QScrollBar::up-arrow:vertical {\n                                      background-color: rgb(239, 229, 220);}\n                                    QScrollBar::down-arrow:vertical {\n                                      background-color: rgb(239, 229, 220);}')
                for G in A.scrollAreaWidgetContents.children():
                        for H in G.findChildren(QPushButton):H.setStyleSheet(_A7)
                A.record_record_button.setStyleSheet('QPushButton {color: black;border: 2px solid black;border-radius: 5px;color: black;}QPushButton::hover {color: white;background-color: black;}');A.record_play_button.setStyleSheet(E);A.record_play_button.setIcon(QtGui.QIcon(_A6));A.record_save_button.setStyleSheet('QPushButton {color: rgb(3, 199, 26);border: 2px solid rgb(3, 199, 26);border-radius: 5px;color: rgb(3, 199, 26);}QPushButton::hover {color:white;background-color: rgb(3, 199, 26);}');A.record_remove_all_button.setStyleSheet('QPushButton {color: rgb(255, 162, 0);border-radius: 5px;border: 2px solid rgb(255, 162, 0);color: rgb(255, 162, 0);}QPushButton::hover {color:white;background-color: rgb(255, 162, 0);}');A.record_load_button.setStyleSheet('QPushButton {color: white;background-color: #5579c7;border 1px solid #5579c7;border-radius: 3px;}QToolTip {background-color: #e0e0e0;border: none;}');A.record_load_button.setIcon(QtGui.QIcon('images/icons8-upload-96.png'));A.record_add_button.setStyleSheet('QPushButton {border: 1px solid rgb(196, 177, 174);border-radius: 10;background-color:  #c1b3b0;}QToolTip {background-color: #e0e0e0;border: none;}');A.record_add_button.setIcon(QtGui.QIcon(_AU));A.theme_button.clicked.disconnect();A.theme_button.clicked.connect(A.get_dark_theme)
                if A.hide_to_tray_checkbox.isChecked():A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_Z))
                else:A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_X))
                A.hide_to_tray_checkbox2.setStyleSheet(_g)
                if A.show_after_complete_checkbox.isChecked():A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_Z))
                else:A.show_after_complete_checkbox2.setIcon(QtGui.QIcon(_X))
                A.show_after_complete_checkbox2.setStyleSheet(_g)
                if A.mouse_location_checkbox.isChecked():A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_Z))
                else:A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_X))
                A.mouse_location_checkbox2.setStyleSheet(_g)
        def get_home_screen(A):A.navigation_frame.lower();A.home_frame.show();A.login_signup_frame.show();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.subscription_check_frame.hide();A.access_denied_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('')
        def get_login_signup_screen(A):A.login_signup_frame.show();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.home_frame.hide();A.subscription_check_frame.hide();A.access_denied_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('')
        def get_login_screen(A):A.login_signup_frame.hide();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.home_frame.hide();A.subscription_check_frame.hide();A.access_denied_frame.hide();A.login_frame.show();A.signup_frame.hide();A.foot_note_label.setText('')
        def get_signup_screen(A):A.login_signup_frame.hide();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.home_frame.hide();A.subscription_check_frame.hide();A.access_denied_frame.hide();A.login_frame.hide();A.signup_frame.show();A.foot_note_label.setText('')
        def get_subscription_check_screen(A):A.subscription_check_frame.show();A.login_signup_frame.hide();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.home_frame.hide();A.access_denied_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('')
        def get_access_denied_screen(A):A.access_denied_frame.show();A.subscription_check_frame.hide();A.login_signup_frame.hide();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.home_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('')
        def createNewAppKey(A,id,key,username):B='^^^^^^';A.settings.setValue(_h,id);A.settings.setValue(_i,key);A.settings.setValue(_A8,username);A.settings.setValue(_R,0);print(B);print(A.settings.value(_h));print(A.settings.value(_i));print(A.settings.value(_A8));print(A.settings.value(_R));print(B)
        def getAppIdKey(A):id=A.settings.value(_h);B=A.settings.value(_i);C=A.settings.value(_A8);return id,B,C
        def logout(A):B=sqlite3.connect(_G);C=B.cursor();D="UPDATE session_details SET application_key = '', key_expiration_date = '' WHERE application_id ='"+A.settings.value(_h)+_Q;C.execute(D);B.close();A.settings.setValue(_i,'');A.settings.setValue(_R,0);print('logging out!');A.username_box.setText('');A.top_frame.hide();A.top_frame_logged_out.show();A.get_home_screen()
        def checkAppKey(H,key):
                A=sqlite3.connect(_G);B=A.cursor();E="SELECT * FROM session_details WHERE application_key ='"+key+_Q;B.execute(E);C=B.fetchone();A.close()
                if C is not _L:
                        D=C[3]
                        if D=='':return 0
                        F=datetime.datetime.now();G=datetime.datetime.strptime(D,'%Y-%m-%d %H:%M:%S.%f')
                        if G>F:return 1
                return 0
        def get_record_screen(A):
                A.navigation_frame.lower();id=A.settings.value(_h);H=A.settings.value(_i);B=A.settings.value(_R)
                if B==0:A.get_subscription_check_screen();print('logged out state mein hu')
                else:
                        print(B);print('logged in mein hu');C=sqlite3.connect(_G);D=C.cursor();F="SELECT whether_subscribed FROM user_info WHERE unique_device_id ='"+id+_Q;D.execute(F);E=D.fetchone();C.close()
                        if E is _L:A.get_subscription_check_screen();print('heree')
                        else:
                                G=E[0]
                                if G==1:A.access_denied_frame.hide();A.subscription_check_frame.hide();A.login_signup_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.hide();A.home_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('');A.record_frame.show()
                                else:A.get_access_denied_screen()
        def get_view_screen(A):A.navigation_frame.lower();A.access_denied_frame.hide();A.subscription_check_frame.hide();A.login_signup_frame.hide();A.record_frame.hide();A.view_settings_frame.show();A.hotkey_settings_frame.hide();A.home_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('')
        def get_hotkey_screen(A):A.navigation_frame.lower();A.access_denied_frame.hide();A.subscription_check_frame.hide();A.login_signup_frame.hide();A.record_frame.hide();A.view_settings_frame.hide();A.hotkey_settings_frame.show();A.home_frame.hide();A.login_frame.hide();A.signup_frame.hide();A.foot_note_label.setText('')
        def change_home_start_hotkey(A):
                A.label_21.show();keyboard.remove_hotkey(A.home_start_stop_hotkey);A.home_start_stop_hotkey_label.setText('');A.set_new_hotkey_button_1.setEnabled(_B);A.set_new_hotkey_button_2.setEnabled(_B);A.set_new_hotkey_button_3.setEnabled(_B);A.set_new_hotkey_button_4.setEnabled(_B);B='';keyboard.start_recording();keyboard.wait(_T);D=keyboard.stop_recording()
                for C in D:
                        if str(C)[-11:-6]==_T:continue
                        if str(C)[-5:]==_t:
                                if B!='':B+=_u
                                B+=str(C)[14:-6]
                B=B.replace(_v,'')
                if B=='':keyboard.add_hotkey(A.home_start_stop_hotkey,lambda:A.play_button.click());A.home_start_stop_hotkey_label.setText(str(A.home_start_stop_hotkey))
                else:
                        try:A.home_start_stop_hotkey=B;keyboard.add_hotkey(A.home_start_stop_hotkey,lambda:A.play_button.click());A.home_start_stop_hotkey_label.setText(B)
                        except ValueError:keyboard.add_hotkey(A.home_start_stop_hotkey,lambda:A.play_button.click());A.home_start_stop_hotkey_label.setText(str(A.home_start_stop_hotkey))
                A.set_new_hotkey_button_1.setEnabled(_A);A.set_new_hotkey_button_2.setEnabled(_A);A.set_new_hotkey_button_3.setEnabled(_A);A.set_new_hotkey_button_4.setEnabled(_A);A.label_21.hide()
        def change_record_start_hotkey(A):
                A.label_23.show();keyboard.remove_hotkey(A.record_start_stop_hotkey);A.playback_start_stop_hotkey_label.setText('');A.set_new_hotkey_button_1.setEnabled(_B);A.set_new_hotkey_button_2.setEnabled(_B);A.set_new_hotkey_button_3.setEnabled(_B);A.set_new_hotkey_button_4.setEnabled(_B);B='';keyboard.start_recording();keyboard.wait(_T);D=keyboard.stop_recording()
                for C in D:
                        if str(C)[-11:-6]==_T:continue
                        if str(C)[-5:]==_t:
                                if B!='':B+=_u
                                B+=str(C)[14:-6]
                B=B.replace(_v,'')
                if B=='':keyboard.add_hotkey(A.record_start_stop_hotkey,lambda:A.record_play_button.click());A.playback_start_stop_hotkey_label.setText(str(A.record_start_stop_hotkey))
                else:
                        try:A.record_start_stop_hotkey=B;keyboard.add_hotkey(A.record_start_stop_hotkey,lambda:A.record_play_button.click());A.playback_start_stop_hotkey_label.setText(B)
                        except ValueError:keyboard.add_hotkey(A.record_start_stop_hotkey,lambda:A.record_play_button.click());A.playback_start_stop_hotkey_label.setText(str(A.record_start_stop_hotkey))
                A.set_new_hotkey_button_1.setEnabled(_A);A.set_new_hotkey_button_2.setEnabled(_A);A.set_new_hotkey_button_3.setEnabled(_A);A.set_new_hotkey_button_4.setEnabled(_A);A.label_23.hide()
        def change_mouse_location_hotkey(A):
                A.label_22.show();keyboard.remove_hotkey(A.mouse_location_hotkey);A.mouse_location_hotkey_label.setText('');A.set_new_hotkey_button_1.setEnabled(_B);A.set_new_hotkey_button_2.setEnabled(_B);A.set_new_hotkey_button_3.setEnabled(_B);A.set_new_hotkey_button_4.setEnabled(_B);B='';keyboard.start_recording();keyboard.wait(_T);D=keyboard.stop_recording()
                for C in D:
                        if str(C)[-11:-6]==_T:continue
                        if str(C)[-5:]==_t:
                                if B!='':B+=_u
                                B+=str(C)[14:-6]
                B=B.replace(_v,'')
                if B=='':keyboard.add_hotkey(A.mouse_location_hotkey,A.get_mouse_location);A.mouse_location_hotkey_label.setText(str(A.mouse_location_hotkey))
                else:
                        try:A.mouse_location_hotkey=B;keyboard.add_hotkey(A.mouse_location_hotkey,A.get_mouse_location);A.mouse_location_hotkey_label.setText(B)
                        except ValueError:keyboard.add_hotkey(A.mouse_location_hotkey,A.get_mouse_location);A.mouse_location_hotkey_label.setText(str(A.mouse_location_hotkey))
                A.set_new_hotkey_button_1.setEnabled(_A);A.set_new_hotkey_button_2.setEnabled(_A);A.set_new_hotkey_button_3.setEnabled(_A);A.set_new_hotkey_button_4.setEnabled(_A);A.label_22.hide()
        def change_recording_hotkey(A):
                A.label_24.show();keyboard.remove_hotkey(A.record_recording_hotkey);A.record_start_stop_hotkey_label.setText('');A.set_new_hotkey_button_1.setEnabled(_B);A.set_new_hotkey_button_2.setEnabled(_B);A.set_new_hotkey_button_3.setEnabled(_B);A.set_new_hotkey_button_4.setEnabled(_B);B='';keyboard.start_recording();keyboard.wait(_T);D=keyboard.stop_recording()
                for C in D:
                        if str(C)[-11:-6]==_T:continue
                        if str(C)[-5:]==_t:
                                if B!='':B+=_u
                                B+=str(C)[14:-6]
                B=B.replace(_v,'')
                if B=='':keyboard.add_hotkey(A.record_recording_hotkey,lambda:A.record_record_button.click());A.record_start_stop_hotkey_label.setText(str(A.record_recording_hotkey))
                else:
                        try:A.record_recording_hotkey=B;keyboard.add_hotkey(A.record_recording_hotkey,lambda:A.record_record_button.click());A.record_start_stop_hotkey_label.setText(B)
                        except ValueError:keyboard.add_hotkey(A.record_recording_hotkey,lambda:A.record_record_button.click());A.record_start_stop_hotkey_label.setText(str(A.record_recording_hotkey))
                A.set_new_hotkey_button_1.setEnabled(_A);A.set_new_hotkey_button_2.setEnabled(_A);A.set_new_hotkey_button_3.setEnabled(_A);A.set_new_hotkey_button_4.setEnabled(_A);A.label_24.hide()
        def start_thread_hotkey_1(A):B=threading.Thread(target=A.change_home_start_hotkey);B.start()
        def start_thread_hotkey_2(A):B=threading.Thread(target=A.change_record_start_hotkey);B.start()
        def start_thread_hotkey_3(A):B=threading.Thread(target=A.change_mouse_location_hotkey);B.start()
        def start_thread_hotkey_4(A):B=threading.Thread(target=A.change_recording_hotkey);B.start()
        def open_menu(A):A.navigation_frame.raise_();A.navigate_button.clicked.disconnect();A.navigate_button.clicked.connect(A.close_menu);A.navigate_button_3.clicked.disconnect();A.navigate_button_3.clicked.connect(A.close_menu)
        def close_menu(A):A.navigation_frame.lower();A.navigate_button.clicked.disconnect();A.navigate_button.clicked.connect(A.open_menu);A.navigate_button_3.clicked.disconnect();A.navigate_button_3.clicked.connect(A.open_menu)
        def window_record_save(A):
                A.font.setBold(_B);A.font.setPixelSize(11);A.record_save_window=QDialog(_L,Qt.WindowCloseButtonHint|Qt.WindowTitleHint);A.record_save_window.setWindowTitle('Save');A.record_save_window.setWindowIcon(QtGui.QIcon(_AV));A.record_save_window.setGeometry(827,520,300,115);A.record_save_window.setFixedWidth(300);A.record_save_window.setFixedHeight(115);A.invisible_widget_1=QWidget(A.record_save_window);A.record_save_layout=QGridLayout(A.invisible_widget_1);A.record_save_name_box=QLineEdit(A.invisible_widget_1);A.record_save_name_box.setAlignment(Qt.AlignRight);A.record_save_name_label=QLabel(A.invisible_widget_1);A.record_save_button_pc=QPushButton(A.invisible_widget_1);A.record_save_button_db=QPushButton(A.invisible_widget_1);A.record_save_footnote=QLabel(A.invisible_widget_1);A.invisible_widget_1.setGeometry(0,0,300,115)
                if A.dark_theme_activated:A.invisible_widget_1.setStyleSheet(_AW)
                else:A.invisible_widget_1.setStyleSheet('background-color: rgb(239, 229, 220);')
                A.record_save_name_box.clear();A.record_save_frame1=QFrame(A.invisible_widget_1);A.record_save_frame1.setGeometry(10,8,280,91)
                if A.dark_theme_activated:A.record_save_frame1.setStyleSheet(_AX)
                else:A.record_save_frame1.setStyleSheet(_AY)
                A.record_save_frame1.lower();A.record_save_name_box.setGeometry(20,22,260,30)
                if A.dark_theme_activated:A.record_save_name_box.setStyleSheet(_AZ)
                else:A.record_save_name_box.setStyleSheet(_Aa)
                A.record_save_name_box.setFont(A.font);A.record_save_name_label.setText(_Ab)
                if A.dark_theme_activated:A.record_save_name_label.setStyleSheet(_Ac)
                else:A.record_save_name_label.setStyleSheet(_Ad)
                A.record_save_name_label.setGeometry(26,14,98,15);A.record_save_name_label.setFont(A.font);A.record_save_button_pc.setIcon(QtGui.QIcon(_Ae));A.record_save_button_pc.setGeometry(30,60,115,30);A.record_save_button_pc.setText(_Af);A.record_save_button_pc.clicked.connect(A.record_save_settings_pc)
                if A.dark_theme_activated:A.record_save_button_pc.setStyleSheet(_w)
                else:A.record_save_button_pc.setStyleSheet(_x)
                A.record_save_button_pc.setFont(A.font);A.record_save_button_db.setIcon(QtGui.QIcon(_Ag));A.record_save_button_db.setGeometry(160,60,115,30);A.record_save_button_db.setText(_Ah);A.record_save_button_db.clicked.connect(A.record_save_settings)
                if A.dark_theme_activated:A.record_save_button_db.setStyleSheet(_w)
                else:A.record_save_button_db.setStyleSheet(_x)
                A.record_save_button_db.setFont(A.font);A.record_save_footnote.setGeometry(10,99,280,13);A.record_save_footnote.setText('');A.record_save_footnote.setStyleSheet(_A9);A.record_save_footnote.setFont(A.font);A.record_save_window.show()
        def record_save_settings(A):
                if A.i==1:A.foot_note_label.setText(_AA);return
                F=[];G=A.record_save_name_box.text()
                if G=='':A.record_save_footnote.setText(_y);return
                for E in range(A.i-1):
                        B=[];C=A.line_list[E][1].children()
                        if A.line_list[E][0]==_I:
                                B.append(_I)
                                for D in (3,5):
                                        if C[D].text()=='':A.foot_note_label.setText(_a);return
                                        else:B.append(C[D].text())
                                for D in (7,9):B.append(C[D].currentText())
                                if C[11].text()=='':B.append(_E)
                                else:B.append(C[11].text())
                        elif A.line_list[E][0]==_H:
                                B.append(_H);B.append(C[3].text());B.append(C[5].currentText());B.append(C[7].currentText())
                                if C[9].text()=='':B.append(_E)
                                else:B.append(C[9].text())
                        elif A.line_list[E][0]==_M:
                                B.append(_M)
                                for D in (3,5):
                                        if C[D].text()=='':A.foot_note_label.setText(_a);return
                                        else:B.append(C[D].text())
                                B.append(C[7].currentText());B.append(C[9].text())
                                if C[11].text()=='':B.append(_E)
                                else:B.append(C[11].text())
                        J=', '.join(B);F.append(J)
                K='---'.join(F);L=datetime.datetime.today().strftime(_Ai)
                if A.repeat_for_number_2.text()=='':H=_K
                else:H=A.repeat_for_number_2.text()
                if A.delay_2.text()=='':I=_E
                else:I=A.delay_2.text()
                M=A.delay_time_combobox_record.currentText()
                try:functions.add_run_record_db(G,K,L,H,I,M);A.record_save_window.close()
                except sqlite3.IntegrityError:A.record_save_footnote.setText(_Aj);return
        def record_save_settings_pc(A):
                if A.i==1:A.foot_note_label.setText(_AA);return
                G=[];H=A.record_save_name_box.text()
                if H=='':A.record_save_footnote.setText(_y);return
                for E in range(A.i-1):
                        B=[];C=A.line_list[E][1].children()
                        if A.line_list[E][0]==_I:
                                B.append(_I)
                                for D in (3,5):
                                        if C[D].text()=='':A.foot_note_label.setText(_a);return
                                        else:B.append(C[D].text())
                                for D in (7,9):B.append(C[D].currentText())
                                if C[11].text()=='':B.append(_E)
                                else:B.append(C[11].text())
                        elif A.line_list[E][0]==_H:
                                B.append(_H);B.append(C[3].text());B.append(C[5].currentText());B.append(C[7].currentText())
                                if C[9].text()=='':B.append(_E)
                                else:B.append(C[9].text())
                        elif A.line_list[E][0]==_M:
                                B.append(_M)
                                for D in (3,5):
                                        if C[D].text()=='':A.foot_note_label.setText(_a);return
                                        else:B.append(C[D].text())
                                B.append(C[7].currentText());B.append(C[9].text())
                                if C[11].text()=='':B.append(_E)
                                else:B.append(C[11].text())
                        G.append(B)
                if A.repeat_for_number_2.text()=='':I=_K
                else:I=A.repeat_for_number_2.text()
                if A.delay_2.text()=='':J=_E
                else:J=A.delay_2.text()
                M=A.delay_time_combobox_record.currentText();K,N=QFileDialog.getSaveFileName(A,_Ak,f"{H}",_AB)
                if K:
                        L=open(K,'w',newline='');F=csv.writer(L)
                        for E in range(A.i-1):F.writerow(G[E])
                        F.writerow(I);F.writerow(J);F.writerow(M);L.close();A.record_save_window.close()
        def window_load(A):
                D='QPushButton::hover {border: 1px solid #bfcfb2;background-color: rgb(196, 177, 174);color: white;}QPushButton {background-color: rgb(249, 249, 245);border-radius: 5px;border: 1px solid #bfcfb2;}';B='QPushButton::hover {border: 1px solid rgb(196, 177, 174);background-color: rgb(196, 177, 174);color: white;}QPushButton {background-color: rgb(249, 249, 245);border-radius: 5px;border: 1px solid rgb(196, 177, 174);}';A.font.setBold(_B);A.font.setPixelSize(11);A.load_window=QDialog(_L,Qt.WindowCloseButtonHint|Qt.WindowTitleHint);A.load_window.setWindowTitle('Load');A.load_window.setWindowIcon(QtGui.QIcon('images/uplode_dark'));A.load_window.setGeometry(575,250,400,400);A.load_window.setFixedWidth(400);A.load_window.setFixedHeight(400);A.invisible_widget_2=QWidget(A.load_window);A.load_layout=QGridLayout(A.invisible_widget_2);A.load_list=QListWidget(A.invisible_widget_2);A.load_from_pc=QPushButton(A.invisible_widget_2);A.load_from_list=QPushButton(A.invisible_widget_2);A.delete_selected=QPushButton(A.invisible_widget_2);A.invisible_widget_2.setGeometry(0,0,400,400)
                if A.dark_theme_activated:A.invisible_widget_2.setStyleSheet(_AW)
                else:A.invisible_widget_2.setStyleSheet(_A7)
                A.load_list.setGeometry(10,10,380,340);C=A.load_list.findChildren(QWidget)[4]
                if A.dark_theme_activated:C.setStyleSheet('QScrollBar:vertical {\n                                                       border-color: #10131b;\n                                                       border-width: 1px;\n                                                       border-style: solid;\n                                                       border-radius: 10px;\n                                                       background-color: #10131b;\n                                                       width:18px;\n                                                       margin: 10px 4px 10px 0;}\n                                                   QScrollBar::handle:vertical {\n                                                       background-color: #bfcfb2;\n                                                       min-height: 25px;\n                                                       border: 1px solid #bfcfb2;\n                                                       border-radius: 5px;}\n                                                   QScrollBar::add-line:vertical {\n                                                       border: 1px solid #10131b;\n                                                       background-color: #10131b;\n                                                       height: 0px;\n                                                       subcontrol-position: bottom;\n                                                       subcontrol-origin: margin;}\n                                                   QScrollBar::sub-line:vertical {\n                                                       border: 1px solid #10131b;\n                                                       background-color: #10131b;\n                                                       height: 0px;\n                                                       subcontrol-position: top;\n                                                       subcontrol-origin: margin;}\n                                                   QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n                                                       background: none;}\n                                                   QScrollBar::up-arrow:vertical {\n                                                     background-color: #10131b;}\n                                                   QScrollBar::down-arrow:vertical {\n                                                     background-color: #10131b;}')
                else:C.setStyleSheet('QScrollBar:vertical {\n                                               border-color: rgb(239, 229, 220);\n                                               border-width: 1px;\n                                               border-style: solid;\n                                               border-radius: 10px;\n                                               background: rgb(239, 229, 220);\n                                               width:18px;\n                                               margin: 10px 4px 10px 0;}\n                                           QScrollBar::handle:vertical {\n                                               background-color: #c4b1ad;\n                                               min-height: 25px;\n                                               border: 1px solid #c4b1ad;\n                                               border-radius: 5px;}\n                                           QScrollBar::add-line:vertical {\n                                               border: 1px solid rgb(239, 229, 220);\n                                               background-color: rgb(239, 229, 220);\n                                               height: 0px;\n                                               subcontrol-position: bottom;\n                                               subcontrol-origin: margin;}\n                                           QScrollBar::sub-line:vertical {\n                                               border: 1px solid rgb(239, 229, 220);\n                                               background-color: rgb(241, 241, 241);\n                                               height: 0px;\n                                               subcontrol-position: top;\n                                               subcontrol-origin: margin;}\n                                           QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n                                               background: none;}')
                if A.dark_theme_activated:A.load_list.setStyleSheet('QListWidget {border: 1px solid #bfcfb2;border-radius: 5px;color: #bfcfb2;}')
                else:A.load_list.setStyleSheet('QListWidget {border: 1px solid rgb(196, 177, 174);border-radius: 5px;}color: black;')
                A.load_list.setFont(A.font);A.load_from_pc.setIcon(QtGui.QIcon('images/icons8-monitor-96'));A.load_from_pc.setGeometry(10,360,120,30);A.load_from_pc.setText(' Load From PC');A.load_from_pc.clicked.connect(A.load_selected_from_pc)
                if A.dark_theme_activated:A.load_from_pc.setStyleSheet(D)
                else:A.load_from_pc.setStyleSheet(B)
                A.load_from_pc.setFont(A.font);A.load_from_list.setIcon(QtGui.QIcon('images/icons8-list-100'));A.load_from_list.setGeometry(270,360,120,30);A.load_from_list.setText(' Load Selected');A.load_from_list.clicked.connect(A.load_selected_from_db)
                if A.dark_theme_activated:A.load_from_list.setStyleSheet('QPushButton::hover {border: 1px solid #bfcfb2;background-color: rgb(196, 177, 174);color: white;}QPushButton {background-color: rgb(249, 249, 245);border-radius: 5px;border: 1px solid rgb(196, 177, 174)}')
                else:A.load_from_list.setStyleSheet(B)
                A.load_from_list.setFont(A.font);A.delete_selected.setIcon(QtGui.QIcon('images/icons8-delete-96'));A.delete_selected.setGeometry(140,360,120,30);A.delete_selected.setText(' Delete Selected');A.delete_selected.clicked.connect(A.delete_from_db)
                if A.dark_theme_activated:A.delete_selected.setStyleSheet(D)
                else:A.delete_selected.setStyleSheet(B)
                A.delete_selected.setFont(A.font);A.load_list.clear();A.update_db_view();A.load_list.setCurrentRow(A.j-1);A.load_window.show()
        def update_db_view(A):
                A.j=0;A.items_list=[];A.items_from_home=[];A.items_from_record=[];D=sqlite3.connect(_G);C=D.cursor();F='SELECT save_name, saved_date FROM home_run_settings';C.execute(F)
                for B in C.fetchall():A.items_list.append(str(B[0])+f" ({str(B[1])})"+_AC);A.items_from_home.append(B[0])
                G='SELECT save_name, saved_date FROM record_run_settings';C.execute(G)
                for B in C.fetchall():A.items_list.append(str(B[0])+f" ({str(B[1])})"+_AD);A.items_from_record.append(B[0])
                D.close()
                for B in A.items_list:E=QListWidgetItem(B);E.setTextAlignment(Qt.AlignHCenter);A.load_list.addItem(E);A.j+=1
        def read_csv(E,csv_file):
                C=[]
                with open(csv_file,'r')as D:
                        A=D.readlines();A=list(map(lambda x:x.strip(),A))
                        for B in A:B=B.split(',');C.append(B)
                return C
        def load_selected_from_pc(A):
                D=[];G,L=QFileDialog.getOpenFileName(A,'Choose File','',_AB)
                if G:B=A.read_csv(G)
                else:return
                try:
                        for I in range(12):D.append(B[0][I])
                        A.load_window.close();A.get_home_screen();H=D[9];A.mouse_button_combobox.setCurrentText(D[0]);A.click_type_combobox.setCurrentText(D[1])
                        if D[2]==_z:A.range_radio_button.setChecked(_A);A.delay_time_combobox_2.setCurrentText(str(H));J=D[7];K=D[8];A.range_min.setText(str(J));A.range_max.setText(str(K));A.delay_time_entrybox.setText('')
                        else:A.repeat_radio_button.setChecked(_A);A.delay_time_combobox.setCurrentText(str(H));A.delay_time_entrybox.setText(str(D[7]));A.range_min.setText('');A.range_max.setText('')
                        if D[3]==-1:A.never_stop_combobox.setCurrentText(_U);A.repeat_for_number.setText('')
                        else:A.never_stop_combobox.setCurrentText(_m);A.repeat_for_number.setText(str(D[3]))
                        if D[4]==_A0:A.fixed_location_radio_button.setChecked(_A);A.fixed_location_x.setText(str(D[5]));A.fixed_location_y.setText(str(D[6]));A.select_area_x.setText('');A.select_area_y.setText('');A.select_area_width.setText('');A.select_area_height.setText('')
                        elif D[4]==_A1:A.current_location_radio_button.setChecked(_A);A.fixed_location_x.setText('');A.fixed_location_y.setText('');A.select_area_x.setText('');A.select_area_y.setText('');A.select_area_width.setText('');A.select_area_height.setText('')
                        else:A.select_area_radio_button.setChecked(_A);A.select_area_x.setText(str(D[5]));A.select_area_y.setText(str(D[6]));A.select_area_width.setText(str(D[10]));A.select_area_height.setText(str(D[11]));A.fixed_location_x.setText('');A.fixed_location_y.setText('')
                except KeyError:
                        F=len(B);A.load_window.close();A.remove_all_lines()
                        for C in range(F-3):
                                if B[C][0]==_I:A.add_mouse_line();E=A.line_list[C][1].children();E[3].setText(str(int(B[C][1])));E[5].setText(str(int(B[C][2])));E[7].setCurrentText(B[C][3]);E[9].setCurrentText(B[C][4]);E[11].setText(str(int(B[C][5])))
                                if B[C][0]==_M:A.add_scroll_line();E=A.line_list[C][1].children();E[3].setText(str(int(B[C][1])));E[5].setText(str(int(B[C][2])));E[7].setCurrentText(B[C][3]);E[9].setText(B[C][4]);E[11].setText(str(int(B[C][5])))
                                if B[C][0]==_H:A.add_keyboard_line();E=A.line_list[C][1].children();E[3].setText(str(B[C][1]));E[5].setCurrentText(str(B[C][2]));E[7].setCurrentText(B[C][3]);E[9].setText(str(B[C][4]))
                        A.repeat_for_number_2.setText(B[F-3][0]);A.delay_2.setText(B[F-2][0]);A.delay_time_combobox_record.setCurrentText(B[F-1][0])
        def delete_from_db(A):
                try:B=A.load_list.currentItem().text()
                except AttributeError:return
                H=B[-5:];C=sqlite3.connect(_G);G=C.cursor()
                if H=='home)':D=B.find(_AC);E=B[:D][0:-19];F=f"DELETE FROM home_run_settings WHERE save_name = '{E}'";G.execute(F);C.commit();C.close();A.load_list.clear();A.update_db_view()
                else:D=B.find(_AD);E=B[:D][0:-19];F=f"DELETE FROM record_run_settings WHERE save_name = '{E}'";G.execute(F);C.commit();C.close();A.load_list.clear();A.update_db_view()
        def load_selected_from_db(A):
                try:E=A.load_list.currentItem().text()
                except AttributeError:return
                N=E[-5:];J=sqlite3.connect(_G);F=J.cursor()
                if N=='home)':
                        K=E.find(_AC);L=E[:K][0:-19];M=f"SELECT * FROM home_run_settings WHERE save_name = '{L}'";F.execute(M);B=F.fetchall()[0];J.close();A.load_window.close();A.get_home_screen();G=B[10];A.mouse_button_combobox.setCurrentText(B[1]);A.click_type_combobox.setCurrentText(B[2])
                        if B[3]==_z:A.range_radio_button.setChecked(_A);A.delay_time_combobox_2.setCurrentText(str(G));O=B[8];P=B[9];A.range_min.setText(str(O));A.range_max.setText(str(P));A.delay_time_entrybox.setText('')
                        else:A.repeat_radio_button.setChecked(_A);A.delay_time_combobox.setCurrentText(str(G));A.delay_time_entrybox.setText(str(B[8]));A.range_min.setText('');A.range_max.setText('')
                        if B[4]==-1:A.never_stop_combobox.setCurrentText(_U);A.repeat_for_number.setText('')
                        else:A.never_stop_combobox.setCurrentText(_m);A.repeat_for_number.setText(str(B[4]))
                        if B[5]==_A0:A.fixed_location_radio_button.setChecked(_A);A.fixed_location_x.setText(str(B[6]));A.fixed_location_y.setText(str(B[7]));A.select_area_x.setText('');A.select_area_y.setText('');A.select_area_width.setText('');A.select_area_height.setText('')
                        elif B[5]==_A1:A.current_location_radio_button.setChecked(_A);A.fixed_location_x.setText('');A.fixed_location_y.setText('');A.select_area_x.setText('');A.select_area_y.setText('');A.select_area_width.setText('');A.select_area_height.setText('')
                        else:A.select_area_radio_button.setChecked(_A);A.select_area_x.setText(str(B[6]));A.select_area_y.setText(str(B[7]));A.select_area_width.setText(str(B[11]));A.select_area_height.setText(str(B[12]));A.fixed_location_x.setText('');A.fixed_location_y.setText('')
                else:
                        K=E.find(_AD);L=E[:K][0:-19];M=f"SELECT * FROM record_run_settings WHERE save_name = '{L}'";F.execute(M);H=F.fetchall()[0];B=H[1].split('---');Q=H[3];R=H[4];G=H[5];J.close();A.load_window.close();S=len(B);A.remove_all_lines()
                        for I in range(S):
                                C=B[I].split(', ')
                                if C[0]==_I:A.add_mouse_line();D=A.line_list[I][1].children();D[3].setText(C[1]);D[5].setText(C[2]);D[7].setCurrentText(C[3]);D[9].setCurrentText(C[4]);D[11].setText(C[5])
                                elif C[0]==_H:A.add_keyboard_line();D=A.line_list[I][1].children();D[3].setText(C[1]);D[5].setCurrentText(C[2]);D[7].setCurrentText(C[3]);D[9].setText(C[4])
                                elif C[0]==_M:A.add_scroll_line();D=A.line_list[I][1].children();D[3].setText(C[1]);D[5].setText(C[2]);D[7].setCurrentText(C[3]);D[9].setText(C[4]);D[11].setText(C[5])
                        A.repeat_for_number_2.setText(str(Q));A.delay_2.setText(str(R));A.delay_time_combobox_record.setCurrentText(str(G))
        def add_new_line(A):
                B=A.record_add_items.currentText()
                if B==' Mouse':A.add_mouse_line()
                elif B==_AR:A.add_keyboard_line()
                elif B==' Scroll':A.add_scroll_line()
        def add_mouse_line(B):
                A=QFrame(B);C=QHBoxLayout(A);C.setContentsMargins(5,0,0,0);C.setSpacing(5);A.setFixedSize(500,30);A.setStyleSheet(_Al);H=QLabel(A);H.setStyleSheet(_AE);H.setText(str(B.i));H.setFixedSize(20,10);I=QLabel(A);I.setStyleSheet(_C);I.setText('X:');I.setFixedSize(10,20);O=QLineEdit(A);O.setFixedSize(40,20);O.setStyleSheet(_N);J=QLabel(A);J.setStyleSheet(_C);J.setText('Y:');J.setFixedSize(10,20);P=QLineEdit(A);P.setFixedSize(40,20);P.setStyleSheet(_N);K=QLabel(A);K.setStyleSheet(_C);K.setText(_AF);K.setFixedSize(30,20);D=QComboBox(A);D.addItem(_l);D.addItem(_A3);D.addItem(_A4);D.setFixedSize(55,20);D.setStyleSheet(_A2);L=QLabel(A);L.setStyleSheet(_C);L.setText(_Am);L.setFixedSize(40,20);F=QComboBox(A);F.addItem(_O);F.addItem(_c);F.setFixedSize(65,20);F.setStyleSheet('QComboBox {background-color: rgb(249, 249, 245);border: 1px solid;border-radius: 3px;border-color: rgb(218, 218, 218);padding-left: 2px;}QComboBox::drop-down {background-color: rgb(249, 249, 245);border: 1px;border-radius: 2px;border-color: rgb(218, 218, 218);}QComboBox::down-arrow {image: url(images/arrow1.png);width: 8px;height: 8px;}');M=QLabel(A);M.setStyleSheet(_C);M.setText(_AG);M.setFixedSize(40,20);N=QLineEdit(A);N.setPlaceholderText(_AH);N.setFixedSize(45,20);N.setStyleSheet(_N);E=QPushButton(A);E.setIcon(QtGui.QIcon(_AI));E.setFixedSize(25,20)
                if B.dark_theme_activated:E.setStyleSheet(_AJ)
                else:E.setStyleSheet(_AK)
                E.clicked.connect(B.remove_line)
                for Q in A.findChildren(QLineEdit):Q.setValidator(B.integer)
                C.addWidget(H);C.addWidget(I);C.addWidget(O);C.addWidget(J);C.addWidget(P);C.addWidget(K);C.addWidget(D);C.addWidget(L);C.addWidget(F);C.addWidget(M);C.addWidget(N);C.addWidget(E);B.form_layout.addWidget(A);B.line_list.append([_I,A]);B.i+=1;B.repeat_for_label_2.show();B.repeat_for_number_2.show();B.delay_label_2.show();B.delay_2.show();B.delay_time_combobox_record.show();B.record_remove_all_button.setEnabled(_A);B.font.setBold(_B);B.font.setPixelSize(11)
                for G in A.findChildren(QLabel):G.setFont(B.font)
                for G in A.findChildren(QComboBox):G.setFont(B.font)
                for G in A.findChildren(QLineEdit):G.setFont(B.font)
        def add_keyboard_line(A):
                B=QFrame(A);B.setStyleSheet(_Al);B.setFixedSize(500,30);C=QHBoxLayout(B);C.setContentsMargins(5,0,0,0);C.setSpacing(5);I=QLabel(B);I.setStyleSheet(_AE);I.setText(str(A.i));I.setFixedSize(20,10);J=QLabel(B);J.setStyleSheet(_C);J.setText('Input:');J.setFixedSize(35,20);N=QLineEdit(B);N.setFixedSize(77,20);N.setStyleSheet(_N);K=QLabel(B);K.setStyleSheet(_C);K.setText(_AF);K.setFixedSize(30,20);E=QComboBox(B);E.addItem('Char');E.addItem(_j);E.setFixedSize(55,20);E.setStyleSheet(_A2);L=QLabel(B);L.setStyleSheet(_C);L.setText(_Am);L.setFixedSize(40,20);F=QComboBox(B);F.addItem(_O);F.addItem(_c);F.setFixedSize(65,20);F.setStyleSheet(_A2);M=QLabel(B);M.setStyleSheet(_C);M.setText(_AG);M.setFixedSize(40,20);G=QLineEdit(B);G.setPlaceholderText(_AH);G.setValidator(A.integer);G.setFixedSize(45,20);G.setStyleSheet(_N);D=QPushButton(B);D.setIcon(QtGui.QIcon(_AI));D.setFixedSize(25,20)
                if A.dark_theme_activated:D.setStyleSheet(_AJ)
                else:D.setStyleSheet(_AK)
                D.clicked.connect(A.remove_line);C.addWidget(I);C.addWidget(J);C.addWidget(N);C.addWidget(K);C.addWidget(E);C.addWidget(L);C.addWidget(F);C.addWidget(M);C.addWidget(G);C.addWidget(D);A.form_layout.addWidget(B);A.line_list.append([_H,B]);A.i+=1;A.repeat_for_label_2.show();A.repeat_for_number_2.show();A.delay_label_2.show();A.delay_2.show();A.delay_time_combobox_record.show();A.record_remove_all_button.setEnabled(_A);A.font.setBold(_B);A.font.setPixelSize(11)
                for H in B.findChildren(QLabel):H.setFont(A.font)
                for H in B.findChildren(QComboBox):H.setFont(A.font)
                for H in B.findChildren(QLineEdit):H.setFont(A.font)
        def add_scroll_line(B):
                A=QFrame(B);A.setStyleSheet('QFrame {border-bottom: 1.5px solid;border-radius: none;border-color: #c8bab7;}');A.setFixedSize(500,30);C=QHBoxLayout(A);C.setContentsMargins(5,0,0,0);C.setSpacing(5);G=QLabel(A);G.setStyleSheet(_AE);G.setText(str(B.i));G.setFixedSize(20,10);H=QLabel(A);H.setStyleSheet(_C);H.setText('X:');H.setFixedSize(10,20);N=QLineEdit(A);N.setFixedSize(40,20);N.setStyleSheet(_N);I=QLabel(A);I.setStyleSheet(_C);I.setText('Y:');I.setFixedSize(10,20);O=QLineEdit(A);O.setFixedSize(40,20);O.setStyleSheet(_N);J=QLabel(A);J.setStyleSheet(_C);J.setText(_AF);J.setFixedSize(30,20);E=QComboBox(A);E.addItem('Up');E.addItem('Down');E.setFixedSize(55,20);E.setStyleSheet(_A2);K=QLabel(A);K.setStyleSheet(_C);K.setText(' Repeat:');K.setFixedSize(40,20);P=QLineEdit(A);P.setFixedSize(65,20);P.setStyleSheet(_N);L=QLabel(A);L.setStyleSheet(_C);L.setText(_AG);L.setFixedSize(40,20);M=QLineEdit(A);M.setPlaceholderText(_AH);M.setFixedSize(45,20);M.setStyleSheet(_N);D=QPushButton(A);D.setIcon(QtGui.QIcon(_AI));D.setFixedSize(25,20)
                if B.dark_theme_activated:D.setStyleSheet(_AJ)
                else:D.setStyleSheet(_AK)
                D.clicked.connect(B.remove_line)
                for Q in A.findChildren(QLineEdit):Q.setValidator(B.integer)
                C.addWidget(G);C.addWidget(H);C.addWidget(N);C.addWidget(I);C.addWidget(O);C.addWidget(J);C.addWidget(E);C.addWidget(K);C.addWidget(P);C.addWidget(L);C.addWidget(M);C.addWidget(D);B.form_layout.addWidget(A);B.line_list.append([_M,A]);B.i+=1;B.repeat_for_label_2.show();B.repeat_for_number_2.show();B.delay_label_2.show();B.delay_2.show();B.delay_time_combobox_record.show();B.record_remove_all_button.setEnabled(_A);B.font.setBold(_B);B.font.setPixelSize(11)
                for F in A.findChildren(QLabel):F.setFont(B.font)
                for F in A.findChildren(QComboBox):F.setFont(B.font)
                for F in A.findChildren(QLineEdit):F.setFont(B.font)
        def remove_line(A):
                D=A.sender();E=D.parentWidget();B=int(E.findChild(QLabel).text());A.form_layout.removeRow(B-1);del A.line_list[B-1];A.i-=1
                for C in range(B-1,A.i-1):F=A.line_list[C][1].findChild(QLabel);F.setText(str(C+1))
                if A.i==1:A.repeat_for_label_2.hide();A.repeat_for_number_2.hide();A.repeat_for_number_2.setText(_K);A.delay_label_2.hide();A.delay_2.hide();A.delay_time_combobox_record.hide();A.delay_2.setText(_E);A.record_remove_all_button.setEnabled(_B)
        def remove_all_lines(A):
                while A.i>1:A.form_layout.removeRow(A.i-2);del A.line_list[-1];A.i-=1
                A.record_remove_all_button.setEnabled(_B);A.repeat_for_label_2.hide();A.repeat_for_number_2.hide();A.repeat_for_number_2.setText(_K);A.delay_label_2.hide();A.delay_2.hide();A.delay_time_combobox_record.hide();A.delay_2.setText(_E)
        def check_repeat_style(A):
                if A.never_stop_combobox.currentText()==_U:A.repeat_for_number.setDisabled(_A);A.repeat_for_number.setStyleSheet('background-color: rgb(225, 225, 225);border: 1px solid;border-color: rgb(218, 218, 218);border-radius: 3px;')
                else:A.repeat_for_number.setDisabled(_B);A.repeat_for_number.setStyleSheet('background-color: rgb(249, 249, 245);border: 1px solid;border-color: rgb(218, 218, 218);border-radius: 3px;')
        def trigger_tray_checkbox(A):
                if A.hide_to_tray_checkbox.isChecked():
                        A.hide_to_tray_checkbox.setChecked(_B)
                        if A.dark_theme_activated:A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_W));A.hide_to_tray_checkbox2.setStyleSheet(_d)
                        else:A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_X));A.hide_to_tray_checkbox2.setStyleSheet(_e)
                else:
                        A.hide_to_tray_checkbox.setChecked(_A)
                        if A.dark_theme_activated:A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_Y));A.hide_to_tray_checkbox2.setStyleSheet(_d)
                        else:A.hide_to_tray_checkbox2.setIcon(QtGui.QIcon(_Z));A.hide_to_tray_checkbox2.setStyleSheet(_e)
                A.check_tray_checkbox()
        def check_tray_checkbox(A):
                if A.hide_to_tray_checkbox.isChecked():app.setQuitOnLastWindowClosed(_B)
                else:app.setQuitOnLastWindowClosed(_A)
        def get_mouse_location(A):
                for C in A.home_frame.findChildren(QLineEdit):C.clearFocus()
                B=mouse.get_position();D=B[0];E=B[1]
                if not A.home_frame.isHidden():A.fixed_location_x.setText(str(D));A.fixed_location_y.setText(str(E))
        def trigger_live_mouse(A):
                if A.mouse_location_checkbox.isChecked():
                        A.mouse_location_checkbox.setChecked(_B)
                        if A.dark_theme_activated:A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_W));A.mouse_location_checkbox2.setStyleSheet(_f)
                        else:A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_X));A.mouse_location_checkbox2.setStyleSheet(_g)
                else:
                        A.mouse_location_checkbox.setChecked(_A)
                        if A.dark_theme_activated:A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_Y));A.mouse_location_checkbox2.setStyleSheet(_f)
                        else:A.mouse_location_checkbox2.setIcon(QtGui.QIcon(_Z));A.mouse_location_checkbox2.setStyleSheet(_g)
                A.check_live_mouse()
        def check_live_mouse(B):A=threading.Thread(target=B.get_live_mouse);A.setDaemon(_A);A.start()
        def get_live_mouse(A):
                while 1:
                        if A.mouse_location_checkbox.isChecked():A.live_mouse_label.setText('');break
                        B=mouse.get_position();A.live_mouse_label.setText(f"X: {B[0]}, Y: {B[1]}");sleep(0.05)
        def home_reset_settings(A):A.mouse_button_combobox.setCurrentText(_l);A.click_type_combobox.setCurrentText(_F);A.never_stop_combobox.setCurrentText(_m);A.repeat_for_number.setText(_K);A.delay_time_entrybox.setText(_E);A.delay_time_combobox.setCurrentText(_P);A.repeat_radio_button.setChecked(_A);A.current_location_radio_button.setChecked(_A);A.range_min.setText('');A.range_max.setText('');A.select_area_x.setText('');A.select_area_y.setText('');A.select_area_width.setText('');A.select_area_height.setText('');A.fixed_location_x.setText('');A.fixed_location_y.setText('')
        def window_home_save(A):
                A.font.setBold(_B);A.font.setPixelSize(11);A.home_save_window=QDialog(_L,Qt.WindowCloseButtonHint|Qt.WindowTitleHint);A.home_save_window.setWindowTitle('Save');A.home_save_window.setWindowIcon(QtGui.QIcon(_AV));A.home_save_window.setGeometry(827,520,300,115);A.home_save_window.setFixedWidth(300);A.home_save_window.setFixedHeight(115);A.invisible_widget_3=QWidget(A.home_save_window);A.home_save_layout=QGridLayout(A.invisible_widget_3);A.save_name_box=QLineEdit(A.invisible_widget_3);A.save_name_box.setAlignment(Qt.AlignRight);A.save_name_label=QLabel(A.invisible_widget_3);A.home_save_button_pc=QPushButton(A.invisible_widget_3);A.home_save_button_db=QPushButton(A.invisible_widget_3);A.home_save_footnote=QLabel(A.invisible_widget_3)
                if A.dark_theme_activated:A.invisible_widget_3.setStyleSheet(_AT)
                else:A.invisible_widget_3.setStyleSheet(_A7)
                A.invisible_widget_3.setGeometry(0,0,300,115);A.save_name_box.clear();A.home_save_frame1=QFrame(A.invisible_widget_3);A.home_save_frame1.setGeometry(10,8,280,91)
                if A.dark_theme_activated:A.home_save_frame1.setStyleSheet(_AX)
                else:A.home_save_frame1.setStyleSheet(_AY)
                A.home_save_frame1.lower();A.save_name_box.setGeometry(20,22,260,30)
                if A.dark_theme_activated:A.save_name_box.setStyleSheet(_AZ)
                else:A.save_name_box.setStyleSheet(_Aa)
                A.save_name_box.setFont(A.font);A.save_name_label.setText(_Ab)
                if A.dark_theme_activated:A.save_name_label.setStyleSheet(_Ac)
                else:A.save_name_label.setStyleSheet(_Ad)
                A.save_name_label.setGeometry(26,14,98,15);A.save_name_label.setFont(A.font);A.home_save_button_pc.setIcon(QtGui.QIcon(_Ae));A.home_save_button_pc.setGeometry(30,60,115,30);A.home_save_button_pc.setText(_Af);A.home_save_button_pc.clicked.connect(A.home_save_settings_pc)
                if A.dark_theme_activated:A.home_save_button_pc.setStyleSheet(_w)
                else:A.home_save_button_pc.setStyleSheet(_x)
                A.home_save_button_pc.setFont(A.font);A.home_save_button_db.setIcon(QtGui.QIcon(_Ag));A.home_save_button_db.setGeometry(160,60,115,30);A.home_save_button_db.setText(_Ah);A.home_save_button_db.clicked.connect(A.home_save_settings)
                if A.dark_theme_activated:A.home_save_button_db.setStyleSheet(_w)
                else:A.home_save_button_db.setStyleSheet(_x)
                A.home_save_button_db.setFont(A.font);A.home_save_footnote.setGeometry(10,99,280,13);A.home_save_footnote.setText('')
                if A.dark_theme_activated:A.home_save_footnote.setStyleSheet(_A9)
                else:A.home_save_footnote.setStyleSheet(_A9)
                A.home_save_footnote.setFont(A.font);A.home_save_window.show()
        def home_save_settings(A):
                G=A.save_name_box.text()
                if G=='':A.home_save_footnote.setText(_y);return
                N=str(A.mouse_button_combobox.currentText());O=str(A.click_type_combobox.currentText())
                if A.repeat_radio_button.isChecked():H='repeat'
                else:H=_z
                if str(A.never_stop_combobox.currentText())==_U:I=-1
                else:
                        try:I=int(A.repeat_for_number.text())
                        except ValueError:A.home_save_footnote.setText(_An);return
                if A.select_area_radio_button.isChecked():B='select'
                elif A.current_location_radio_button.isChecked():B=_A1
                else:B=_A0
                try:
                        if A.select_area_radio_button.isChecked():C=int(A.select_area_x.text());D=int(A.select_area_y.text());E=int(A.select_area_width.text());F=int(A.select_area_height.text())
                        elif A.current_location_radio_button.isChecked():C=0;D=0;E=0;F=0
                        else:C=int(A.fixed_location_x.text());D=int(A.fixed_location_y.text());E=0;F=0
                except ValueError:A.home_save_footnote.setText(_Ao);return
                try:
                        if A.repeat_radio_button.isChecked():J=str(A.delay_time_combobox.currentText());K=int(A.delay_time_entrybox.text());L,M=K,K
                        else:J=str(A.delay_time_combobox_2.currentText());L=int(A.range_min.text());M=int(A.range_max.text())
                except ValueError:A.home_save_footnote.setText(_Ap);return
                P=datetime.today().strftime(_Ai)
                try:functions.add_run_home_db(G,N,O,H,I,B,C,D,L,M,J,E,F,P);A.home_save_window.close()
                except sqlite3.IntegrityError:A.home_save_footnote.setText(_Aj);return
        def home_save_settings_pc(A):
                J=A.save_name_box.text()
                if J=='':A.home_save_footnote.setText(_y);return
                O=str(A.mouse_button_combobox.currentText());P=str(A.click_type_combobox.currentText())
                if A.repeat_radio_button.isChecked():K='repeat'
                else:K=_z
                if str(A.never_stop_combobox.currentText())==_U:L=-1
                else:
                        try:L=int(A.repeat_for_number.text())
                        except ValueError:A.home_save_footnote.setText(_An);return
                if A.select_area_radio_button.isChecked():D='select'
                elif A.current_location_radio_button.isChecked():D=_A1
                else:D=_A0
                try:
                        if A.select_area_radio_button.isChecked():E=int(A.select_area_x.text());F=int(A.select_area_y.text());G=int(A.select_area_width.text());H=int(A.select_area_height.text())
                        elif A.current_location_radio_button.isChecked():E=0;F=0;G=0;H=0
                        else:E=int(A.fixed_location_x.text());F=int(A.fixed_location_y.text());G=0;H=0
                except ValueError:A.home_save_footnote.setText(_Ao);return
                try:
                        if A.repeat_radio_button.isChecked():
                                I=str(A.delay_time_combobox.currentText());B=int(A.delay_time_entrybox.text())
                                if I==_P:C=B,B
                                else:C=B,B
                        else:I=str(A.delay_time_combobox_2.currentText());Q=int(A.range_min.text());R=int(A.range_max.text());C=Q,R
                except ValueError:A.home_save_footnote.setText(_Ap);return
                S=[O,P,K,L,D,E,F,C[0],C[1],I,G,H];M,U=QFileDialog.getSaveFileName(A,_Ak,f"{J}",_AB)
                if M:
                        try:N=open(M,'w');T=csv.writer(N);T.writerow(S);N.close();A.home_save_window.close()
                        except PermissionError:A.home_save_footnote.setText('error: cannot overwrite because it is being used');return
        def home_start_process(A):
                A.get_home_screen();L=A.mouse_button_combobox.currentText().lower();M=A.click_type_combobox.currentText();P=A.never_stop_combobox.currentText()
                if P==_U:H=-1
                else:
                        try:H=int(A.repeat_for_number.text())
                        except ValueError:A.foot_note_label.setText('error: repeat number is missing');return
                try:
                        if A.repeat_radio_button.isChecked():
                                D=str(A.delay_time_combobox.currentText());C=int(A.delay_time_entrybox.text())
                                if D==_P:B=C/1000,C/1000
                                elif D=='s':B=C,C
                                elif D==_V:B=C*60,C*60
                                else:B=C*1440,C*1440
                        else:
                                D=str(A.delay_time_combobox_2.currentText())
                                if D==_P:E=int(A.range_min.text())/1000;F=int(A.range_max.text())/1000;B=E,F
                                elif D=='s':E=int(A.range_min.text());F=int(A.range_max.text());B=E,F
                                elif D==_V:E=int(A.range_min.text())*60;F=int(A.range_max.text())*60;B=E,F
                                else:E=int(A.range_min.text())*1440;F=int(A.range_max.text())*1440;B=E,F
                except ValueError:A.foot_note_label.setText('error: value is missing for your repeat or range choice');return
                if not A.current_location_radio_button.isChecked():
                        try:
                                if A.select_area_radio_button.isChecked():I=int(A.select_area_x.text());J=int(A.select_area_y.text())
                                else:I=int(A.fixed_location_x.text());J=int(A.fixed_location_y.text())
                        except ValueError:A.foot_note_label.setText('error: x and y location is missing');return
                else:I=0;J=0
                if A.select_area_width.text()=='':N=0
                else:N=int(A.select_area_width.text())
                if A.select_area_height.text()=='':O=0
                else:O=int(A.select_area_height.text())
                A.foot_note_label.setText('')
                if A.fixed_location_radio_button.isChecked():K=1
                elif A.current_location_radio_button.isChecked():K=2
                else:K=3
                A.showMinimized();keyboard.remove_hotkey(A.home_start_stop_hotkey);keyboard.add_hotkey(A.home_start_stop_hotkey,A.home_stop_process);A.foot_note_label.setText('');A.play_button.setEnabled(_B);toaster.show_toast(title='Clicking started',msg=f"Press {A.home_start_stop_hotkey.upper()} to stop",icon_path=_b,threaded=_A,duration=2)
                if K==1:G=threading.Thread(target=lambda:home_fixed_clicking(L,M,H,int(I),int(J),B));G.start()
                elif K==2:G=threading.Thread(target=lambda:home_current_clicking(L,M,H,B));G.start()
                else:G=threading.Thread(target=lambda:home_random_clicking(L,M,H,I,J,B,N,O));G.start()
        def after_home_thread(A):
                A.play_button.setEnabled(_A);keyboard.remove_hotkey(A.home_start_stop_hotkey);keyboard.add_hotkey(A.home_start_stop_hotkey,lambda:A.play_button.click())
                if A.show_after_complete_checkbox.isChecked():A.showNormal()
                toaster.show_toast('Clicking stopped',f"Press {A.home_start_stop_hotkey.upper()} to start again",icon_path=_b,threaded=_A,duration=2)
                if A.whether_logged_in()==1:B=A.complete_combobox.currentText()
                else:B=A.complete_combobox_3.currentText()
                if B==_p:os.system(_Aq)
                elif B==_q:os.system(_Ar)
                elif B==_r:os.system(_As)
                elif B==_o:ctypes.windll.user32.LockWorkStation()
                elif B==_n:app.exit()
                elif B=='Standby':os.system(_At)
        def home_stop_process(A):stop_home_event.set()
        def record_stop_process(A):stop_record_event.set()
        def record_start_process(A):
                A.get_record_screen()
                if A.i==1:A.foot_note_label.setText(_AA);return
                D=[]
                for G in range(A.i-1):
                        B=[];C=A.line_list[G][1].children()
                        if A.line_list[G][0]==_I:
                                B.append(_I)
                                for E in (3,5):
                                        if C[E].text()=='':A.foot_note_label.setText(_a);return
                                        else:B.append(C[E].text())
                                for E in (7,9):B.append(C[E].currentText())
                                if C[11].text()=='':B.append(_E)
                                else:B.append(C[11].text())
                                D.append(B)
                        elif A.line_list[G][0]==_H:
                                B.append(_H);B.append(C[3].text())
                                if C[3].text()=='':A.foot_note_label.setText('error: no input given');return
                                B.append(C[5].currentText());B.append(C[7].currentText())
                                if C[9].text()=='':B.append(_E)
                                else:B.append(C[9].text())
                                D.append(B)
                        elif A.line_list[G][0]==_M:
                                B.append(_M)
                                for E in (3,5):
                                        if C[E].text()=='':A.foot_note_label.setText(_a);return
                                        else:B.append(C[E].text())
                                B.append(C[7].currentText());B.append(C[9].text())
                                if C[11].text()=='':B.append(_E)
                                else:B.append(C[11].text())
                                D.append(B)
                if D[0][0]==_H:
                        if D[0][2]==_j:
                                J=functions.key_converter(D[0][1].replace('Key.','').lower())
                                if J=='wrong':A.foot_note_label.setText('error: wrong key input');return
                if A.repeat_for_number_2.text()=='':I=_K
                else:I=A.repeat_for_number_2.text()
                if A.delay_2.text()=='':F=0.1
                else:
                        H=A.delay_time_combobox_record.currentText()
                        if H==_P:F=int(A.delay_2.text())/1000
                        elif H=='s':F=int(A.delay_2.text())
                        elif H==_V:F=int(A.delay_2.text())*60
                        else:F=int(A.delay_2.text())*1440
                A.foot_note_label.setText('');A.showMinimized();keyboard.remove_hotkey(A.record_start_stop_hotkey);keyboard.add_hotkey(A.record_start_stop_hotkey,A.record_stop_process);A.record_play_button.setEnabled(_B);toaster.show_toast(title='Playback started',msg=f"Press {A.record_start_stop_hotkey.upper()} to stop playback",icon_path=_b,threaded=_A,duration=2);K=threading.Thread(target=lambda:start_record_actions(D,I,F,A.i));K.start()
        def after_record_thread(A,a):
                if wrong_key_event.is_set():A.foot_note_label.setText(f"error: wrong key input at line {a+1}");wrong_key_event.clear()
                A.record_play_button.setEnabled(_A);keyboard.remove_hotkey(A.record_start_stop_hotkey);keyboard.add_hotkey(A.record_start_stop_hotkey,lambda:A.record_play_button.click())
                if A.show_after_complete_checkbox.isChecked():A.showNormal()
                toaster.show_toast(title='Playback completed',msg=f"Press {A.record_start_stop_hotkey.upper()} to start again",icon_path=_b,threaded=_A,duration=2)
                if A.whether_logged_in()==1:B=A.complete_combobox.currentText()
                else:B=A.complete_combobox_3.currentText()
                if B==_p:os.system(_Aq)
                elif B==_q:os.system(_Ar)
                elif B==_r:os.system(_As)
                elif B==_o:ctypes.windll.user32.LockWorkStation()
                elif B==_n:app.exit()
                elif B==_A5:os.system(_At)
        def insert_recording_list(E,events):
                A=events;N=0;M=0
                while len(A[N])==6:
                        if A[0][3]=='release':del A[0];M+=1
                        else:break
                if M==0:del A[-1];del A[-1]
                else:del A[-1]
                E.remove_all_lines();H=len(A);B=0;I=0
                while B<H:
                        if len(A[B])==5:
                                E.add_mouse_line();C=E.line_list[I][1].children();C[3].setText(str(A[B][0]));C[5].setText(str(A[B][1]))
                                if str(A[B][2])=='Button.left':C[7].setCurrentText(_l)
                                elif str(A[B][2])=='Button.middle':C[7].setCurrentText(_A3)
                                else:C[7].setCurrentText(_A4)
                                if A[B][3]is _A:C[9].setCurrentText(_O)
                                else:C[9].setCurrentText(_c)
                                D=int(A[B][4]*1000);C[11].setText(str(D))
                        elif len(A[B])==4:
                                E.add_scroll_line();C=E.line_list[I][1].children();C[3].setText(str(A[B][0]));C[5].setText(str(A[B][1]));G=1;D=int(A[B][3]*1000)
                                if str(A[B][2])=='-1':
                                        C[7].setCurrentText('Down')
                                        for F in range(1,H-B):
                                                if len(A[B+F])==4:
                                                        if str(A[B+F][2])=='-1':G+=1;D+=int(A[B+F][3]*1000)
                                                        else:break
                                                else:break
                                        C[9].setText(str(G))
                                else:
                                        C[7].setCurrentText('Up')
                                        for F in range(1,H-B):
                                                if len(A[B+F])==4:
                                                        if str(A[B+F][2])==_K:G+=1;D+=int(A[B+F][3]*1000)
                                                        else:break
                                                else:break
                                        C[9].setText(str(G))
                                if G>1:B+=G-1
                                C[11].setText(str(D))
                        elif len(A[B])==6:
                                E.add_keyboard_line();C=E.line_list[I][1].children();K=A[B][0];L=1;D=int(A[B][2]*1000)
                                if A[B][1]==_J:
                                        C[5].setCurrentText('Char')
                                        for J in range(1,H-B):
                                                if len(A[B+J])==3:
                                                        if str(A[B+J][1])==_J:K+=A[B+J][0];D+=int(A[B+J][2]*1000);L+=1
                                                        else:break
                                        C[3].setText(str(K))
                                else:C[5].setCurrentText(_j);C[3].setText(str(K))
                                if L>1:B+=L-1
                                if A[B][3]=='press':C[7].setCurrentText(_O)
                                else:C[7].setCurrentText(_c)
                                C[9].setText(str(D))
                        B+=1;I+=1
        def thread_for_live_record(A):A.remove_all_lines();B=threading.Thread(target=A.live_record_process);B.setDaemon(_A);B.start()
        def live_record_process(A):
                H='key'
                def C(x,y,button,pressed):nonlocal B;C=B;B=time.time();D=round(B-C,2);E=[x,y,button,pressed,D];A.record_events.append(E)
                def D(x,y,dx,dy):nonlocal B;C=B;B=time.time();D=round(B-C,2);E=[x,y,dy,D];A.record_events.append(E)
                def E(key):
                        C=key;nonlocal B;I=B;B=time.time();E=round(B-I,2);F='press'
                        if hasattr(C,_J):
                                if str(C)[0]=='<':D=H;G=[C,D,E,F,0,0]
                                elif str(C)[0]=='[':D=_J;G=[str(C)[2:-2].lower(),D,E,F,0,0]
                                elif str(C)[1]=='\\':D=_J;J=functions.char_converter(str(C)[1:-1]);G=[J.lower(),D,E,F,0,0]
                                else:D=_J;G=[str(C)[1:-1].lower(),D,E,F,0,0]
                        else:D=H;G=[C,D,E,F,0,0]
                        A.record_events.append(G)
                def F(key):
                        C=key;nonlocal B;I=B;B=time.time();E=round(B-I,2);F='release'
                        if hasattr(C,_J):
                                if str(C)[0]=='<':D=H;G=[C,D,E,F,0,0]
                                elif str(C)[0]=='[':D=_J;G=[str(C)[2:-2].lower(),D,E,F,0,0]
                                elif str(C)[1]=='\\':D=_J;J=functions.char_converter(str(C)[1:-1]);G=[J.lower(),D,E,F,0,0]
                                else:D=_J;G=[str(C)[1:-1].lower(),D,E,F,0,0]
                        else:D=H;G=[C,D,E,F,0,0]
                        A.record_events.append(G)
                A.record_record_button.disconnect();A.record_record_button.clicked.connect(A.stop_live_record);A.record_record_button.setText('Stop');A.record_events=[];A.mouse_listener=pynput.mouse.Listener(on_click=C,on_scroll=D);A.keyboard_listener=pynput.keyboard.Listener(on_press=E,on_release=F);A.showMinimized();toaster.show_toast(title='Recording Started',msg=f"Press {A.record_recording_hotkey.upper()} to stop recording",icon_path=_b,threaded=_A,duration=2);A.record_play_button.setEnabled(_B);A.mouse_listener.start();A.keyboard_listener.start();B=time.time();A.mouse_listener.join();A.keyboard_listener.join()
        def stop_live_record(A):A.mouse_listener.stop();A.keyboard_listener.stop();toaster.show_toast(title='Recording completed',msg=f"Press {A.record_start_stop_hotkey.upper()} to start playback",icon_path=_b,threaded=_A,duration=2);A.record_record_button.setIcon(QtGui.QIcon(_AQ));A.record_record_button.disconnect();A.record_record_button.clicked.connect(A.thread_for_live_record);A.record_record_button.setText('Record');A.insert_recording_list(A.record_events);A.showNormal();A.record_play_button.setEnabled(_A)
class CaptureScreen(QtWidgets.QSplashScreen):
        'QSplashScreen, that track mouse event for capturing screenshot.'
        def __init__(A):super(CaptureScreen,A).__init__();A.origin=QtCore.QPoint(0,0);A.end=QtCore.QPoint(0,0);A.signal=0;A.rubberBand=QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle,A);A.createDimScreenEffect()
        def createDimScreenEffect(A):'Fill splashScreen with black color and reduce the widget opacity to create dim screen effect';B=QtGui.QGuiApplication.primaryScreen().geometry();C=QtGui.QPixmap(B.width(),B.height());C.fill(QtGui.QColor(0,0,0));A.setPixmap(C);A.setWindowState(QtCore.Qt.WindowFullScreen);A.setWindowOpacity(0.4)
        def mousePressEvent(A,event):
                'Show rectangle at mouse position when left-clicked';B=event
                if B.button()==QtCore.Qt.LeftButton:A.origin=B.pos();print('origin_x: '+str(A.origin.x()));print('origin_y: '+str(A.origin.y()));A.rubberBand.setGeometry(QtCore.QRect(A.origin,QtCore.QSize()));A.rubberBand.show()
        def getOriginal_x(A):return A.origin.x()
        def getOriginal_y(A):return A.origin.y()
        def getFinal_x(A):return A.end.x()
        def getFinal_y(A):return A.end.y()
        def mouseMoveEvent(A,event):'Resize rectangle as we move mouse, after left-clicked.';A.rubberBand.setGeometry(QtCore.QRect(A.origin,event.pos()).normalized())
        def indicator(A):return A.signal
        def mouseReleaseEvent(A,event):
                "Upon mouse released, ask the main desktop's QScreen to capture screen on defined area.";C=event
                if C.button()==QtCore.Qt.LeftButton:A.end=C.pos();print('end_x: '+str(A.end.x()));print('end_y: '+str(A.end.y()));A.rubberBand.hide();A.hide();A.signal=1;D=QtGui.QGuiApplication.primaryScreen();E=D.grabWindow(0,A.origin.x(),A.origin.y(),A.end.x()-A.origin.x(),A.end.y()-A.origin.y());B=UI();A.original_x=A.getOriginal_x();A.original_y=A.getOriginal_y();A.final_x=A.getFinal_x();A.final_y=A.getFinal_y();A.snipping_width=abs(A.final_x-A.original_x);A.snipping_height=abs(A.final_y-A.original_y);A.snip_x=min(A.final_x,A.original_x);A.snip_y=min(A.final_y,A.original_y);B.select_area_x.setText(str(A.snip_x));B.select_area_y.setText(str(A.snip_y));B.select_area_width.setText(str(A.snipping_width));B.select_area_height.setText(str(A.snipping_height));B.select_area_radio_button.setChecked(_A);B.show()
conn=sqlite3.connect(_G)
cursor=conn.cursor()
sql='SELECT * FROM app_settings LIMIT 1'
cursor.execute(sql)
app_settings=cursor.fetchone()
conn.close()
show_tool_after,hide_system_tray,disable_cursor_location,dark_theme,home_start_hotkey,record_start_hotkey,record_recording_hotkey,mouse_location_hotkey=app_settings
toaster=ToastNotifier()
stop_home_event=threading.Event()
stop_record_event=threading.Event()
wrong_key_event=threading.Event()
app=QApplication(sys.argv)
UIWindow=UI()
UIWindow.show()
app.exec_()
