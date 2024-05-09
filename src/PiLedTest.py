import hal.hal_input_switch as sw
import hal.hal_led as led
import time
lastblink=00
sw.init()
led.init()
blink=True
ledState=False
while True:
    cur=time.time()*1000
    blink=sw.read_slide_switch()
    if blink:
        if cur>lastblink+200:
            lastblink=cur
            ledState=not ledState
            led.set_output(0,ledState)
    else:
        if cur>lastblink+100:
            lastblink=cur
            ledState=not ledState
            led.set_output(0,ledState)
        
        

