import time
import pyautogui
import keyboard
def get_pixel_colour(i_x, i_y):
	import win32gui
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)
time.sleep(3) 
pyautogui.click(650, 0, button='right') 
try:
	while True:
				
		if get_pixel_colour(850, 100)[0] ==0:
			pyautogui.click(850, 100, button='left')
		
		
		if get_pixel_colour(850, 100)[0] ==0:
			pyautogui.click(850, 100, button='left')
	
		if get_pixel_colour(850, 100)[0] ==0:
			pyautogui.click(850, 100, button='left')
		
		
		if get_pixel_colour(850, 100)[0] ==0:
			pyautogui.click(850, 100, button='left')
			
		if get_pixel_colour(550, 300)[0] ==0:
			pyautogui.click(550, 300, button='left')


		if get_pixel_colour(650, 300)[0] ==0:
			pyautogui.click(650, 300, button='left')


		if get_pixel_colour(740, 300)[0] ==0:
			pyautogui.click(740, 300, button='left')


		if get_pixel_colour(850, 300)[0] ==0:
			pyautogui.click(850, 300, button='left')

			
	
except:
	pass