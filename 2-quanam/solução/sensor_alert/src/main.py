def get_acceptable_co2_levels():
    return {
        "activity-room": {"min": None, "max": 500},
        "refectory": {"min": None, "max": 400},
        "room-1": {"min": None, "max": 300},
        "bathroom-main": {"min": None, "max": 500},
        "garden": {"min": None, "max": 500},
    }


def get_acceptable_temperature_levels():
    return {
        "activity-room": {"min": 19, "max": 22},
        "refectory": {"min": 20, "max": 23},
        "room-1": {"min": 21, "max": 23},
        "bathroom-main": {"min": 22, "max": 25},
        "garden": {"min": 15, "max": 22},
    }


def get_acceptable_humidity_levels():
    return {
        "activity-room": {"min": 50, "max": 60},
        "refectory": {"min": 50, "max": 70},
        "room-1": {"min": 50, "max": 60},
        "bathroom-main": {"min": 60, "max": 75},
        "garden": {"min": 50, "max": 80},
    }


def get_acceptable_sound_levels():
    return {
        "activity-room": {"min": 0, "max": 40},
        "refectory": {"min": 20, "max": 35},
        "room-1": {"min": 10, "max": 30},
        "bathroom-main": {"min": 20, "max": 35},
        "garden": {"min": 10, "max": 35},
    }


def main(sensor_data):
    result = {"alerts": []}
    room = sensor_data["room"]
    acceptable_levels = {
        "co2": get_acceptable_co2_levels(),
        "temperature": get_acceptable_temperature_levels(),
        "humidity": get_acceptable_humidity_levels(),
        "sound": get_acceptable_sound_levels(),
    }
    for sensor_name, levels in acceptable_levels.items():
        acceptable = levels[room]
        sensor_level = sensor_data["values"][sensor_name]

        if (acceptable["min"] is not None and sensor_level < acceptable["min"]) or (
            acceptable["max"] is not None and sensor_level > acceptable["max"]
        ):
            result["alerts"].append(sensor_name)

    return result
