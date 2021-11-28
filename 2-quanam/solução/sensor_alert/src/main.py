class ClosedInterval:
    def __init__(self, min=None, max=None) -> None:
        self.min = min
        self.max = max

    def contains(self, value):
        return (self.min is None or self.min <= value) and (
            self.max is None or self.max >= value
        )

    def __repr__(self) -> str:
        return f"ClosedInterval({self.min}, {self.max})"


class Sensor:
    def __init__(self, interval, value=None) -> None:
        self.interval = interval
        self.value = value

    def has_acceptable_value(self):
        if self.value is None:
            raise ValueError(f"Sensor value missing")
        return self.interval.contains(self.value)

    def __repr__(self) -> str:
        return f"Sensor({self.interval}, {self.value})"


class Location:
    def __init__(self, sensors) -> None:
        self.sensors = sensors

    def get_alerts(self):
        result = []
        for kind, sensor in self.sensors.items():
            if not sensor.has_acceptable_value():
                result.append(kind)
        return result


def get_location_sensors():
    return {
        "activity-room": Location(
            {
                "co2": Sensor(ClosedInterval(min=None, max=500)),
                "temperature": Sensor(ClosedInterval(min=19, max=22)),
                "humidity": Sensor(ClosedInterval(min=50, max=60)),
                "sound": Sensor(ClosedInterval(min=0, max=40)),
                "illumination": Sensor(ClosedInterval(min=300, max=750)),
            },
        ),
        "refectory": Location(
            {
                "co2": Sensor(ClosedInterval(min=None, max=400)),
                "temperature": Sensor(ClosedInterval(min=20, max=23)),
                "humidity": Sensor(ClosedInterval(min=50, max=70)),
                "sound": Sensor(ClosedInterval(min=20, max=35)),
                "illumination": Sensor(ClosedInterval(min=200, max=500)),
            },
        ),
        "room-1": Location(
            {
                "co2": Sensor(ClosedInterval(min=None, max=300)),
                "temperature": Sensor(ClosedInterval(min=21, max=23)),
                "humidity": Sensor(ClosedInterval(min=50, max=60)),
                "sound": Sensor(ClosedInterval(min=10, max=30)),
                "illumination": Sensor(ClosedInterval(min=100, max=200)),
            },
        ),
        "bathroom-main": Location(
            {
                "co2": Sensor(ClosedInterval(min=None, max=500)),
                "temperature": Sensor(ClosedInterval(min=22, max=25)),
                "humidity": Sensor(ClosedInterval(min=60, max=75)),
                "sound": Sensor(ClosedInterval(min=20, max=35)),
                "illumination": Sensor(ClosedInterval(min=100, max=200)),
            },
        ),
        "garden": Location(
            {
                "co2": Sensor(ClosedInterval(min=None, max=500)),
                "temperature": Sensor(ClosedInterval(min=15, max=22)),
                "humidity": Sensor(ClosedInterval(min=50, max=80)),
                "sound": Sensor(ClosedInterval(min=10, max=35)),
                "illumination": Sensor(ClosedInterval(min=None, max=None)),
            },
        ),
    }


def main(data):
    try:
        location = get_location_sensors()[data["room"]]
        for sensor_name, value in data["values"].items():
            location.sensors[sensor_name].value = value

        return {"alerts": location.get_alerts()}
    except Exception as e:
        return {"alerts": []}
