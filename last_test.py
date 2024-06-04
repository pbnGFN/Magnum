import ctypes
import pydirectinput
import time

from time import sleep, time
import math
import brain
import win32gui
import win32con
from pywinauto import mouse
import pydirectinput


SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
    
class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]
    
class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]
    
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )



class WindowNotFoundError(Exception):
    """Error to be raised if window name is not found"""
    pass

def focus_on_window(window_name):
    """Will bring all windows with a specific name to the top. The last one to be brought up will be in focus.

    Todo:
        * I feel like I could do more with this. Might make it its own module

    Examples:
        >>> focus_on_window("Untitled - Notepad")

    Args:
        window_name: (str) The name of the target window that you want to bring into focus

    Returns: None

    Raises:
        WindowNotFoundError(Exception) if window_name is not in the list

    """

    def window_dict_handler(hwnd, top_windows):
        """Adapted from: https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

        """

        if win32gui.IsWindowVisible(hwnd) and len(win32gui.GetWindowText(hwnd)) > 0:
            top_windows[hwnd] = win32gui.GetWindowText(hwnd)

    tw = {}
    win32gui.EnumWindows(window_dict_handler, tw)
    for handle in tw:
        if tw[handle] == window_name:
            win32gui.ShowWindow(handle, win32con.SW_NORMAL)
            win32gui.BringWindowToTop(handle)
            try:
                win32gui.SetForegroundWindow(handle)
            except Exception as e:
                if e.__str__() == "(0, 'SetForegroundWindow', 'No error message is available')":
                    pass
                else:
                    raise e

            return None
    raise WindowNotFoundError(f"WindowNotFoundError : The window name '{window_name}' does not appear to be an item in: {tw}")




def rotate(name):
    
    focus_on_window(name)
    pydirectinput.press('a')
    sleep(1)
    


if __name__ == '__main__':
    rotate('Geronimo')
