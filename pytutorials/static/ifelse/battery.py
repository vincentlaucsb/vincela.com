from time import sleep

battery_level = 100

while battery_level > 0:
    sleep(1)
    battery_level -= 10
    print("The battery is currently at {0} percent.".format(battery_level))