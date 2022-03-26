"""
    * Created by PyCharm
    * User: Abhinav Bhardwaj
    * Date: 26/03/22
    * Time: 21:56
    """

import pyautogui as pg
import time

text = "Text to be typped multiple times"

time.sleep(5)               # Time to place cursor on the desired location
for i in range(10):
    pg.write(text)
    pg.press('enter')