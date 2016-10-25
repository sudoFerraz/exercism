"""class Clock(object):
    
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

"""

def Clock(hour, minute):
    if hour >= 24:
        hour = hour % 24
    if hour < 0:
        hour = hour % 24

    if minute > 59 or minute < 0:
        divide = minute / 60
        hour = hour + divide
        hour = hour % 24

    if hour < 10:
        hour = format(hour, "02")


    if minute < 10 or minute > 59:
        minute = minute % 60
        minute = format(minute, "02")
    
    relogio = str(hour) + ':' + str(minute)
    return relogio

def add(minute):
    pass
