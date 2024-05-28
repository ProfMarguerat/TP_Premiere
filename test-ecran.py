import utime
import picoexplorer

# Initialise Picoexplorer with a bytearray display buffer
buf = bytearray(picoexplorer.get_width() * picoexplorer.get_height() * 2)
picoexplorer.init(buf)

picoexplorer.set_pen(255, 0, 0)                      # Set a red pen
picoexplorer.clear()                                 # Fill the screen in red
picoexplorer.set_pen(255, 255, 255)                  # Set a white pen
picoexplorer.text("pico explorer", 10, 10, 240, 5)   # Add some text
picoexplorer.update()                                # Update the display with our changes

while picoexplorer.is_pressed(picoexplorer.BUTTON_A) == True:
#    pass
    picoexplorer.set_pen(0, 255, 0)                      # Set a green pen
    picoexplorer.clear()                                 # Fill the screen in green
    picoexplorer.set_pen(0, 0, 0)                        # Set a black pen
    picoexplorer.text("button a pushed", 10, 10, 240, 5) # Add some text
    picoexplorer.update()                                # Update the display with our changes

picoexplorer.set_pen(255, 0, 0)                      # Set a red pen
picoexplorer.clear()                                 # Fill the screen in red
picoexplorer.set_pen(255, 255, 255)                  # Set a white pen
picoexplorer.text("Bonjour !", 10, 10, 240, 3)   # Add some text
picoexplorer.update()                                # Update the display with our changes