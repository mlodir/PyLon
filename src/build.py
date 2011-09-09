import os

commands = ("pyuic4 -o ui_PyLonGui.py ui/PyLonGui.ui",)

for command in commands:
	print(command)
	os.system(command)
