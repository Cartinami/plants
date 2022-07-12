import time
import threading

class Plant(object):
    # how often passtime method gets called (seconds)
    TIMER = 5
    # max plant stats values
    MAX_VALUES = 10

    # gets time of when plant was created and starts passtime method
    def __init__(self, name, size = 0, thirst = 0, light = 0, isInSun = False):
        self.isInSun = isInSun
        self.name = name
        self.size = size
        self.thirst = thirst
        self.light = light
        self.value = 0
        self.startTime = time.perf_counter()
        self.passTime()

    # returns plant specs
    def __str__(self):
        if self.isInSun == True:
            sun = 'yes'
        else:
            sun = 'no'
        return 'plant {} , size = {} , thirst = {} , light = {} , time = {} , value = ${} , in sun = {}'.format(self.name, self.size, self.thirst, self.light, self.age(), self.get_value(), sun)

    # Gets price value for plant
    def get_value(self):
        # x makes max plant value == 145 instead of 144
        x = 0
        if self.size == 4:
            x = 1
        self.value = (((self.size + 1) * 11) + ((((Plant.MAX_VALUES + 1) - self.thirst) + ((Plant.MAX_VALUES + 1) - self.light)) * 2)) + 5 + x
        return self.value

    # determines age by subtracting start time from current time
    def age(self):
        age = time.perf_counter() - self.startTime
        return age

    # Determines size of plant and adds value to plants needs over time
    def passTime(self):
        # timer to call passtime every x (plant.timer) seconds
        self.timer = threading.Timer(Plant.TIMER, self.passTime)
        self.timer.start()

        incriment = (self.size / 2) + 0.5
        self.thirst += incriment
        self.light += incriment

        # if plant is in sun then light needs decrease
        if self.isInSun == True:
            self.light -= (self.size / 2) + 1

        # stops values from going up during initialization (if plant age less than timer incriment)
        if self.age() < Plant.TIMER:
            self.thirst = 0
            self.light = 0

        # doesnt let values get below - max value or above max value
        if self.thirst > Plant.MAX_VALUES or self.thirst < -(Plant.MAX_VALUES):
            if self.thirst > 0:
                self.thirst = Plant.MAX_VALUES
            else:
                self.thirst = -(Plant.MAX_VALUES)
        if self.light > Plant.MAX_VALUES or self.light < -(Plant.MAX_VALUES):
            if self.light > 0:
                self.light = Plant.MAX_VALUES
            else:
                self.light = -(Plant.MAX_VALUES)

        # determines size based on age
        if self.age() >= 60 and self.age() < 120:
            self.size = 1
        elif self.age() >= 120 and self.age() < 180:
            self.size = 2
        elif self.age() >= 180 and self.age() < 240:
            self.size = 3
        elif self.age() >= 240:
            self.size = 4
        else:
            self.size = 0

        self.get_value()

    # lowers plants water needs
    def water(self):
        self.thirst -= 2
        if self.thirst < -(Plant.MAX_VALUES):
            self.thirst = -(Plant.MAX_VALUES)
        return 'Watered plant!\n'

    # stops timer on plant (neccessary for closing app Successfully)
    def stop_timer(self):
        self.timer.cancel()


class Inventory(object):
    # seperate lists based on if plant is in the sun or not
    def __init__(self):
        self.plants = []

    # return plant data when called
    def __str__(self):
        list = []
        for plant in self.plants:
            list.append(str(plant))
        return str(list)

    # add a new plant to inventory (default not in sun (plants) list)
    def add(self, plant):
        plant.isInSun = False
        self.plants.append(plant)

    # move from shade to sun or vice versa
    def move(self, plant):
        plant.isInSun = not plant.isInSun
