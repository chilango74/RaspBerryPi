from gpiozero import DistanceSensor

from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)
# d = round(sensor.distance * 100, 2)
# print('Distance: ', d)
def get_distance():
    return round(sensor.distance * 100, 2)

