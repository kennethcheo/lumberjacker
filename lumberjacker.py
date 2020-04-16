import pyautogui as pygi
import time

'''
todo: find a way to improve speed

'''

class lumberjacker():

    def start():
        play_x, play_y = pygi.locateCenterOnScreen('play_button.png') # replace with screenshot?
        pygi.click(x=play_x, y=play_y, clicks=1, button='left')


    def play():
        
        while True:
            player_right = pygi.pixelMatchesColor(1020, 740, (207,70,59))
            player_left = pygi.pixelMatchesColor(900, 740, (207,70,59))

            branch_right = pygi.pixelMatchesColor(1020, 650, (126,173,79))
            branch_left = pygi.pixelMatchesColor(850, 650, (126,173,79))

            sky_right = pygi.pixelMatchesColor(1020, 650, (211, 247, 255)) 
            sky_left = pygi.pixelMatchesColor(850, 650, (211, 247, 255)) 

            # game_over = pygi.pixelMatchesColor(958,490, (255, 255, 255))

            if player_right and sky_right:
                pygi.press('right')
                # print('Right')

            elif player_left and sky_left:
                pygi.press('left')
                # print('Left')

            if player_right and branch_right:
                pygi.press('left')
                # print('Left')

            elif player_left and branch_left:
                pygi.press('right')
                # print('Right')

            # elif player_right and sky_left: 
            #     pygi.press('left')

            # elif player_right and branch_left:
            #     pygi.press('right')

            # elif player_left and branch_right:
            #     pygi.press('left')

            # elif game_over:
            #     break

        print('Game Over!')
    

print('Lumberjack starting in...')

for i in range(3,0,-1):
    time.sleep(1)
    print(i)

lumberjacker.start()
lumberjacker.play()
