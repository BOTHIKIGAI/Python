import pywhatkit

x = 10
z = 17

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+573105505221", "Hola ma", x, z)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+573105505221", "Hola como estas?", 1, 11, 7, True, 2)

# Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")

# pywhatkit.sendwhatmsg_to_group("SENA - A.D de Software  💻", "Hey All!", 10, 9)