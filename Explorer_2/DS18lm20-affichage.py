import machine, onewire, ds18x20, time
import utime
import picoexplorer

# Initialise Picoexplorer with a bytearray display buffer
buf = bytearray(picoexplorer.get_width() * picoexplorer.get_height() * 2)
picoexplorer.init(buf)

picoexplorer.set_pen(0, 0, 0)                      # Set a red pen
picoexplorer.clear()                                 # Fill the screen in red
picoexplorer.set_pen(255, 255, 255)                  # Set a white pen
picoexplorer.text("Temperature", 10, 10, 240, 3)   # Add some text
picoexplorer.update()                                # Update the display with our changes
utime.sleep(1)

ds_pin = machine.Pin(6)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
utime.sleep(1)
#print('Found a ds18x20 device')
picoexplorer.set_pen(255, 255, 255)
picoexplorer.text("Found a ds18x20 device", 10, 80, 240, 2)   # Add some text
picoexplorer.update()
utime.sleep(1)

 
while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    picoexplorer.set_pen(0, 255, 0)                      # Set a green pen
    picoexplorer.clear()                                 # Fill the screen in green
    picoexplorer.set_pen(0, 0, 0)                        # Set a black pen
    picoexplorer.text("temperature", 60, 60, 240, 2)
    picoexplorer.text(str(ds_sensor.read_temp(rom))+" C", 10, 80, 240, 4) # Add some text
    picoexplorer.update()                                # Update the display with our changes
    #print(ds_sensor.read_temp(rom))
  time.sleep(1)
