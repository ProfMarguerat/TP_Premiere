from machine import Pin, PWM
analogvalue = machine.ADC(28)
pwm = PWM(Pin(15))
pwm.freq(50)
while True:
    reading = analogvalue.read_u16()
    print (reading)
    pwm.duty_u16(int(reading/8))
