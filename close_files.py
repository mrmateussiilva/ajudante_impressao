from time import sleep

import pyautogui as pytg

# print(pytg.position())
# desbloquear = 1881, 651
# pytg.click(desbloquear,button='left', clicks=3, interval=0.25)
# pytg.hotkey("enter")


def close_ficha_shopee(n):
    for n in range(n):
        pytg.hotkey("ctrl","shift","q")
        sleep(0.1)
        pytg.hotkey("ctrl","shift","s")
        sleep(0.1)
        pytg.hotkey("enter")
        sleep(0.1)
        pytg.hotkey("enter")
        sleep(0.1)
        pytg.hotkey("ctrl","w")




def close_cangas(n):
    for n in range(n):
        pytg.hotkey("ctrl","shift","q")
        sleep(0.1)
        pytg.hotkey("ctrl","s")
        sleep(0.1)
        pytg.hotkey("ctrl","w")
        sleep(0.1)


def close_cangas_corte_laser(n):
    for n in range(n):
        pytg.hotkey("ctrl","shift","q")
        sleep(0.5)
        pytg.hotkey("ctrl","j")
        sleep(0.5)
        pytg.hotkey("ctrl","shift","1")
        sleep(0.5)
        pytg.hotkey("enter")
        sleep(0.5)
        pytg.hotkey("ctrl","shift","q")
        sleep(0.5)
        pytg.hotkey("ctrl","s")
        sleep(0.9)
        pytg.hotkey("ctrl","shift","tab")
        # sleep(0.1)
    pytg.hotkey("ctrl","alt","w")







if __name__ == "__main__":
    pytg.FAILFALSE  = True
    # pytg.PAUSE = 2.5
    sleep(3)
    # close_cangas(30)
    close_cangas_corte_laser(32)
    