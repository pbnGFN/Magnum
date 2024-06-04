import win32gui
import win32con
from pywinauto import mouse
from time import sleep


def foreground(window_title):
    hwnd = win32gui.FindWindow(None, window_title)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    foreground("Document - Wordpad")
    sleep(1)
    #if you comment the next line you will get a 'Access is denied.' error
    mouse.move(coords=(-10000, 500))
    foreground("Geronimo")


      
      