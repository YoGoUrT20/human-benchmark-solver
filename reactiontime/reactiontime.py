import pyautogui
from screeninfo import get_monitors

m = get_monitors()[0]
width, height = int(m.width*0.5), int(m.height*0.3)
green_tuple = (75, 219, 106)
blue_tuple = (43, 135, 209)
def main():
    count = 0
    while True:
        if count == 5:
            break
        if pyautogui.pixelMatchesColor(width, height, green_tuple):
            count+=1
            click()
        if pyautogui.pixelMatchesColor(width, height, blue_tuple):
            click()
        
def click():
    pyautogui.click(width, height)

if __name__ == '__main__':
    main()