import hal.hal_input_switch as sw
import hal.hal_led as led
import time

lastblink = 00
blink = True
ledstate = False

sw.init()
led.init()


while True:
    cur=time.time() * 1000
    blink=sw.read_slide_switch()
    if blink:
        if cur > lastblink + 200:
            lastblink = cur
            ledstate = not ledstate
            led.set_output(0,ledstate)
    else:
        if cur>lastblink + 100:
            lastblink = cur
            ledstate = not ledstate
            led.set_output(0,ledstate)
        
        

