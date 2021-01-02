import win32api             # for mouse_event
import win32con             # Windows constants

# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event


def moveRelative(xx=0, yy=2):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, xx, yy, 0)


def PressButton(down, button='left'):
    # Put the mouse_event flags in a convenient dictionary by button
    flags = {
        'left':   (win32con.MOUSEEVENTF_LEFTUP,   win32con.MOUSEEVENTF_LEFTDOWN),
        'middle': (win32con.MOUSEEVENTF_MIDDLEUP, win32con.MOUSEEVENTF_MIDDLEDOWN),
        'right':  (win32con.MOUSEEVENTF_RIGHTUP,  win32con.MOUSEEVENTF_RIGHTDOWN)
    }
    # hit the button
    win32api.mouse_event(flags[button][down], 0, 0)