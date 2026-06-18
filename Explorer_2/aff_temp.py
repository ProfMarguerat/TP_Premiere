import machine, onewire, ds18x20, time
import utime
import picoexplorer
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4

# Initialise Picoexplorer with a bytearray display buffer
#buf = bytearray(picoexplorer.get_width() * picoexplorer.get_height() * 2)
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P4)

#picoexplorer.init(buf)

#picoexplorer.set_pen(0, 0, 0)                      # Set a red pen
#picoexplorer.clear()                                 # Fill the screen in red
#picoexplorer.set_pen(255, 255, 255)                  # Set a white pen
#picoexplorer.text("temperature", 10, 10, 240, 3)   # Add some text
#picoexplorer.update()                                # Update the display with our changes
#utime.sleep(1)

WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(GREEN)
    display.clear()
    display.update()


# set up
clear()
display.set_font("bitmap8")

display.set_pen(BLACK)
display.clear()
display.update()
display.set_pen(GREEN)
display.text("Temperature", 10, 10, 240, 4)
display.update()

ds_pin = machine.Pin(6)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
utime.sleep(1)
#print('Found a ds18x20 device')
display.set_pen(CYAN)
display.text("Found a ds18x20 device", 10, 80, 240, 2)   # Add some text
display.update()
utime.sleep(1)

 
while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    display.set_pen(WHITE)                      # Set a green pen
    display.clear()                                 # Fill the screen in green
    display.set_pen(BLACK)                        # Set a black pen
    display.text("temperature", 60, 60, 240, 2)
    display.text(str(ds_sensor.read_temp(rom))+" C", 10, 80, 240, 4) # Add some text
    display.update()                                # Update the display with our changes
    #print(ds_sensor.read_temp(rom))
  time.sleep(0.5)
