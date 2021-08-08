import cv2 as cv
import pyautogui as pag
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

mouse = Controller()

def find(what):
    if what == "1":
        img = cv.imread("a.jpg", 0)
    if what == "2":
        img = cv.imread("b.jpg", 0)
    if what == "3":
        img = cv.imread("c.jpg", 0)
    if what == "r":
        img = cv.imread("send.jpg", 0)
    ss = pag.screenshot()
    ss.save("temp.jpg")
    template = cv.imread("temp.jpg", 0)
    w,h = template.shape[::-1]

    method = cv.TM_CCOEFF_NORMED
    res = cv.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    top_left = max_loc

    mouse.position = (top_left[0] +20, top_left[1] +20)
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def on_press(key):
    if key.char == "1":
        find("1")
    if key.char == "2":
        find("2")
    if key.char == "3":
        find("3")
    if key.char == "r":
        find("r")

with Listener(on_press = on_press) as listener:
    listener.join()
