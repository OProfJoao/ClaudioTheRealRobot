from machine import Pin
import time

sensor = Pin(25, Pin.IN,Pin.PULL_UP)  # Ativa resistor interno

while True:
    if sensor.value() == 0:  # Barreira interrompida (depende do sensor)
        print("Objeto detectado!")
    else:
        print("Nada detectado")
    time.sleep(0.2)
