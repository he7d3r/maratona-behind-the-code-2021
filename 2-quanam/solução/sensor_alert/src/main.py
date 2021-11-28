class ClosedInterval:
    def __init__(self, min=None, max=None):
        self.min = min
        self.max = max


def get_acceptable_co2_levels():
    return {
        "activity-room": ClosedInterval(min=None, max=500),
        "refectory": ClosedInterval(min=None, max=400),
        "room-1": ClosedInterval(min=None, max=300),
        "bathroom-main": ClosedInterval(min=None, max=500),
        "garden": ClosedInterval(min=None, max=500),
    }


def get_acceptable_temperature_levels():
    return {
        "activity-room": ClosedInterval(min=19, max=22),
        "refectory": ClosedInterval(min=20, max=23),
        "room-1": ClosedInterval(min=21, max=23),
        "bathroom-main": ClosedInterval(min=22, max=25),
        "garden": ClosedInterval(min=15, max=22),
    }


def get_acceptable_humidity_levels():
    return {
        "activity-room": ClosedInterval(min=50, max=60),
        "refectory": ClosedInterval(min=50, max=70),
        "room-1": ClosedInterval(min=50, max=60),
        "bathroom-main": ClosedInterval(min=60, max=75),
        "garden": ClosedInterval(min=50, max=80),
    }


def get_acceptable_sound_levels():
    return {
        "activity-room": ClosedInterval(min=0, max=40),
        "refectory": ClosedInterval(min=20, max=35),
        "room-1": ClosedInterval(min=10, max=30),
        "bathroom-main": ClosedInterval(min=20, max=35),
        "garden": ClosedInterval(min=10, max=35),
    }


def get_acceptable_illumination_levels():
    return {
        "activity-room": ClosedInterval(min=300, max=750),
        "refectory": ClosedInterval(min=200, max=500),
        "room-1": ClosedInterval(min=100, max=200),
        "bathroom-main": ClosedInterval(min=100, max=200),
        "garden": ClosedInterval(min=None, max=None),
    }


def main(sensor_data):
    result = {"alerts": []}
    if "room" not in sensor_data or "values" not in sensor_data:
        return result

    room = sensor_data["room"]
    acceptable_levels = {
        "co2": get_acceptable_co2_levels(),
        "temperature": get_acceptable_temperature_levels(),
        "humidity": get_acceptable_humidity_levels(),
        "sound": get_acceptable_sound_levels(),
        "illumination": get_acceptable_illumination_levels(),
    }
    for sensor_name, levels in acceptable_levels.items():
        acceptable = levels[room]
        sensor_level = sensor_data["values"][sensor_name]

        if (acceptable.min is not None and sensor_level < acceptable.min) or (
            acceptable.max is not None and sensor_level > acceptable.max
        ):
            result["alerts"].append(sensor_name)

    return result
