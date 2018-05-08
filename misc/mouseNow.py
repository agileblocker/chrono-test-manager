#! python3

# mouseNow.py - Displays the mouse's current position.

import pyautogui

print('Welcome to Mouse Now. This will locate the coordinates of your mouse cursor on the screen.')
print('Point your mouse cursor to the location of the coordinates you want to identify.')
print('Then press Ctrl+C to retrieve the coordinates and exit.')

try:
	while True:
		#TODO: Get and print the mouse coordinates.
		x, y = pyautogui.position()
		positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
except KeyboardInterrupt:
	print('\nDone.')

print('Coordinates: ', positionStr, end=' ')
print('\b' * len(positionStr), end=' ', flush=True)
