import RPi.GPIO as g
import time

servo_pin = 12

g.setmode(g.BCM)
#g.setup(26, g.OUT)
g.output(servo_pin, g.OUT)

pwm = g.PWM(servo_pin,50)
pwm.start(3.0)

pwm.changeDutyCycle(0.0)

for i in range(10):
  pwm.stop()
  g.cleanup()

