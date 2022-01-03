#libs
import keyboard
import time
import win32api, win32con
import pyautogui as pg

from pyautogui import FailSafeException


#main
is_turned = False
is_in_progress = False
is_clicking = False
monitor_num = 2
all_pos = {
	1: (1051, 900),
	2: (2653, 926)
}
all_det_pos = {
	1: (345, 970),
	2: (2240, 982),
}
red = (255, 0, 0)
gray = (229, 229, 229)
yellow = (255, 216, 0)
pos = all_pos[monitor_num]
det_pos = all_det_pos[monitor_num]

while True:
	if keyboard.is_pressed('+'):
		is_turned = not is_turned
		if not is_turned and is_in_progress:
			is_turned = True
			is_in_progress = False
			is_clicking = False
			continue
		print(is_turned)
		time.sleep(0.1)
	if is_turned:
		if not is_in_progress and not is_clicking:
			print('Started')
			pg.press('4')
			is_in_progress = True
		if pg.pixelMatchesColor(det_pos[0], det_pos[1], yellow):
			if pg.pixelMatchesColor(pos[0], pos[1], red):
				mouse_pos = pg.position()
				try:
					pg.click(mouse_pos[0], mouse_pos[1])
				except KeyboardInterrupt:
					sys.exit()
				except FailSafeException:
					pg.moveTo(500, 500)
				is_clicking = True
			elif pg.pixelMatchesColor(pos[0], pos[1], gray):
				continue
			else:
				if is_in_progress and is_clicking:
					is_in_progress = False
					is_clicking = False
					print('Finished')