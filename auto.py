from time import sleep
from pyautogui import locateOnScreen, press, KEYBOARD_KEYS
from playsound import playsound
from multiprocessing import Process, Pipe, Value
from keyboard import is_pressed
from dotenv import load_dotenv
import ctypes, os, signal, psutil

load_dotenv(dotenv_path='settings.env')

if os.getenv('exit_key') not in KEYBOARD_KEYS or os.getenv('pause_key') not in KEYBOARD_KEYS:
    print(f'Invalid key! \nList of valid keys: {KEYBOARD_KEYS}')
    quit()

def quit_(pipe, pipe2, pause):
    p2_pid = pipe.recv()
    p1_pid = pipe2.recv()
    psutil.Process(p1_pid).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS) # Lowers process priority
    psutil.Process(p2_pid).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    while True:
        if is_pressed(os.getenv('exit_key')):
            print('Exiting program')
            os.kill(p1_pid, signal.SIGTERM)
            os.kill(p2_pid, signal.SIGTERM)
        if is_pressed(os.getenv('pause_key')):
            if pause.value == 0:
                pause.value = 1
                print('Stopped looking for notes on the screen')
                sleep(1)
            else:
                pause.value = 0
                print('Started looking for notes on the screen')
                sleep(1)

def sound():
    playsound('Ding.wav')

def no_sound():
    pass

def check(pause):
    while True:
        sleep(5)
        if os.getenv('sound') == 'False':
            p = Process(target=no_sound)
        else:
            p = Process(target=sound)

        if pause.value == 0:
            # You can probably tinker with this to get better results
            dream = locateOnScreen('img/greate_dream.png', confidence=.6) # .6 because water and dream are very similar and sometimes it miss match them
            beastly = locateOnScreen('img/beastly.png', confidence=.5)
            sprout = locateOnScreen('img/sprout.png', confidence=.5)
            water = locateOnScreen('img/water.png', confidence=.6) # .6 because water and dream are very similar and sometimes it miss match them
            gloomy = locateOnScreen('img/gloomy.png', confidence=.5)
            revival = locateOnScreen('img/revival.png', confidence=.5)
            vamadha = locateOnScreen('img/vamadha.png', confidence=.5)
        else:
            dream = None
            beastly = None
            sprout = None
            water = None
            gloomy = None
            revival = None
            vamadha = None
        
        if dream != None:
            print('Rhythm Of The Great Dream')
            p.start()
            press('r')
            sleep(0.4)
            press('e')
            sleep(0.4)
            press('t')
            sleep(0.4)
            press('r')
            sleep(0.4)
            press('q')
            sleep(10)
        elif beastly != None:
            print('Rhythm Of The Beastly Trail')
            p.start()
            press('z')
            sleep(0.4)
            press('b')
            sleep(0.4)
            press('n')
            sleep(0.4)
            press('c')
            sleep(0.4)
            press('z')
            sleep(10)
        elif sprout != None:
            print('Rhythm Of The Sprout')
            p.start()
            press('z')
            sleep(0.4)
            press('b')
            sleep(0.4)
            press('b')
            sleep(0.4)
            press('n')
            sleep(0.4)
            press('m')
            sleep(10)
        elif water != None:
            print('Rhythm Of The Source Water')
            p.start()
            press('r')
            sleep(0.4)
            press('e')
            sleep(0.4)
            press('u')
            sleep(0.4)
            press('r')
            sleep(0.4)
            press('j')
            sleep(10)
        elif gloomy != None:
            print('Rhythm Of the Gloomy Path')
            p.start()
            press('e')
            sleep(0.4)
            press('w')
            sleep(0.4)
            press('e')
            sleep(0.4)
            press('w')
            sleep(0.4)
            press('y')
            sleep(10)
        elif revival != None:
            print('Rhythm Of Revival')
            p.start()
            press('s')
            sleep(0.4)
            press('a')
            sleep(0.4)
            press('m')
            sleep(0.4)
            press('b')
            sleep(0.4)
            press('z')
            sleep(10)
        elif vamadha != None:
            print('Rhythm Of Vamadha')
            p.start()
            press('r')
            sleep(0.4)
            press('e')
            sleep(0.4)
            press('e')
            sleep(0.4)
            press('w')
            sleep(0.4)
            press('q')
            sleep(10)

   
if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        value = Value("i", 0)
        conn1, conn2 = Pipe()
        p1 = Process(target=check, args=(value,))
        p2 = Process(target=quit_, args=(conn2, conn1, value))
        
        print(f'Script is running! \nPress {os.getenv("exit_key")} to exit \nPress {os.getenv("pause_key")} to pause')
        p1.start()
        p2.start()
        conn1.send(p2.pid)
        conn2.send(p1.pid)
        
    else:
        print("Admin mode is required! Please run as administrator and try again.")
        quit()