def get_acceptable_co2_levels():
    return {
        "activity-room": {"min": None, "max": 500},
        "refectory": {"min": None, "max": 400},
        "room-1": {"min": None, "max": 300},
        "bathroom-main": {"min": None, "max": 500},
        "garden": {"min": None, "max": 500},
    }


def main(sensor_data):
    result = {"alerts": []}
    room = sensor_data["room"]
    acceptable_co2_levels = get_acceptable_co2_levels()
    acceptable_range = acceptable_co2_levels[room]
    co2_level = sensor_data["values"]["co2"]

    if (
        acceptable_range["min"] is not None and co2_level < acceptable_range["min"]
    ) or (acceptable_range["max"] is not None and co2_level > acceptable_range["max"]):
        result["alerts"].append("co2")

    return result
