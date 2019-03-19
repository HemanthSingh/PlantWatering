from microbit import *

REFRESH = 500


def get_data():
    moisture = pin0.read_analog() #moisture level 0 to 1023 based on conductvity
    level = pin1.read_analog()    #level of the tank 0 if empty
    print(moisture,level)                    #print to transmit this using UART
    if level >500:       #tank has water
        display.show(Image.HAPPY)
        sleep(REFRESH)
        display.scroll(str(moisture))        #display on LED
        if moisture<500:
            pin2.write_digital(1)
        else:
            pin2.write_digital(0)

    else:           #tank is empty
        display.show(Image.SAD)
        sleep(REFRESH)

def run():
    while True:
        sleep(REFRESH)
        get_data()

run()
