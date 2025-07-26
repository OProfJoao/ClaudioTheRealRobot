from machine import Pin
import time


rightCounter = 0
leftCounter = 0
leftLastDetection = time.ticks_ms()
rightLastDetection = time.ticks_ms()


rightEncoderPin = Pin(32, Pin.IN, Pin.PULL_UP)
leftEncoderPin = Pin(33, Pin.IN, Pin.PULL_UP)


def encoderHandler(pin):
    global rightCounter, leftCounter
    global leftLastDetection, rightLastDetection
    current_ms = time.ticks_ms()

    if pin is rightEncoderPin and current_ms > (rightLastDetection + 0):
        rightCounter += 1
        print(f'right: {rightCounter}')
        rightLastDetection = current_ms
    elif pin is leftEncoderPin and current_ms > (leftLastDetection + 0):
        leftCounter += 1
        leftLastDetection = current_ms
        print(f'left: {leftCounter}')


rightEncoderPin.irq(trigger=Pin.IRQ_FALLING, handler=encoderHandler)
leftEncoderPin.irq(trigger=Pin.IRQ_FALLING, handler=encoderHandler)

while True:

    # print(f"Right: {rightCounter} / Left: {leftCounter}")
    time.sleep(0.1)
