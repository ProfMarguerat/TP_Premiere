import machine 
import utime

servo = machine.PWM(machine.Pin(15))  # signal PWM à la broche GP 15
servo.freq(50) # réglage de la fréquence

while True:
    servo.duty_u16(2500)    # rapport cyclique 3500/65535
    utime.sleep(1)          # temps d'arrêt
    servo.duty_u16(5000)    # rapport cyclique 3500/65535
    utime.sleep(1)          # temps d'arrêt
    servo.duty_u16(7500)    # rapport cyclique 6000/65535
    utime.sleep(1)          # temps d'arrêt