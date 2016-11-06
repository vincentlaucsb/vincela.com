from time import sleep

battery_level = 100

while battery_level > 0:
    sleep(1)
    battery_level -= 10
    
    if battery_level > 20:
        print("The battery is currently at {0} percent.".format(battery_level))
    elif battery_level > 0:
        print("The battery is currently at {0} percent. Consider connecting a charger.".format(battery_level))
    else:
        print("The battery is currently at {0} percent. Goodbye.".format(battery_level))
    