"""
>> Tested on a PORTRAIT orientation 1080p monitor (HS on window-mode)
>> PERSONAL_USE
>> Adding/Using locateOnScreen instead of hard-coding coordinates avoids any possible timing issues
"""


import pyautogui
import time
import datetime


def click_at_percentage(x, y):
    target_x = screen_width * (x / 100)
    target_y = screen_height * (y / 100)
    pyautogui.moveTo(target_x, target_y)
    pyautogui.click()


def click_play_button():
    play_location = None
    while play_location is None:
        play_location = pyautogui.locateOnScreen('img/play_button.png', grayscale=True, confidence=0.8)
        time.sleep(0.5)
    x, y = play_location[0], play_location[1]
    pyautogui.moveTo(x, y)
    pyautogui.click()


def click_confirm_button():
    confirm_location = None
    while confirm_location is None:
        confirm_location = pyautogui.locateOnScreen('img/confirm_button.png', grayscale=True, confidence=0.8)
        time.sleep(0.5)
    x, y = confirm_location[0], confirm_location[1]
    pyautogui.moveTo(x, y)
    pyautogui.click()


def click_leave_button():
    leave_location = None
    while leave_location is None:
        leave_location = pyautogui.locateOnScreen('img/leave_button.png', grayscale=True, confidence=0.8)
        time.sleep(0.5)
    x, y = leave_location[0], leave_location[1]
    pyautogui.moveTo(x, y)
    pyautogui.click()


def click_left_board():
    click_at_percentage(12, 22)


def click_opp_portrait():
    click_at_percentage(50, 12)


def press_esc_key():
    pyautogui.press('esc')


def get_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")

    return formatted_time


###########################################
print("--> Script running... [Portrait LocateOnScreen]\n")

# Some timer
time.sleep(2)

# Get screen_size
screen_width, screen_height = pyautogui.size()

game_counter = 1

# Assuming one is inside "The Boomsday Project" dungeon
while True:
    # Step 1: Click Play button
    click_play_button()
    time.sleep(18)

    # Step 2: Click Play button
    click_confirm_button()
    print(f"Game {game_counter} started -- {get_time()}")

    time.sleep(300)
    click_left_board()
    time.sleep(300)
    click_opp_portrait()
    print(f"10 minutes has passed. -- {get_time()}")

    time.sleep(300)
    click_opp_portrait()
    time.sleep(300)
    click_opp_portrait()
    print(f"20 minutes has passed. -- {get_time()}")

    time.sleep(300)
    click_left_board()
    time.sleep(320)
    print("30 minutes has passed.")

    # Step 3-A: Keypress "ESC" key
    press_esc_key()
    time.sleep(1)

    # Step 3-B: Click Leave button
    click_leave_button()
    time.sleep(8)

    # Step 4: Click Defeat button
    click_left_board()
    print(f"Game {game_counter} complete! -- {get_time()}")
    print("**********************************\n")
    time.sleep(8)

    game_counter += 1
