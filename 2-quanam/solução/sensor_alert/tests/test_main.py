import pytest
from src.main import (
    ClosedInterval,
    Location,
    Sensor,
    get_location_sensors,
    main,
)


def test_closed_interval_both_min_and_max():
    interval = ClosedInterval(min=10, max=20)
    assert not interval.contains(9.99)
    assert interval.contains(10)
    assert interval.contains(15)
    assert interval.contains(20)
    assert not interval.contains(20.01)


def test_closed_interval_min_only():
    interval = ClosedInterval(min=10)
    assert not interval.contains(9.99)
    assert interval.contains(10)
    assert interval.contains(15)
    assert interval.contains(9999)


def test_closed_interval_max_only():
    interval = ClosedInterval(max=20)
    assert interval.contains(-9999)
    assert interval.contains(15)
    assert interval.contains(20)
    assert not interval.contains(20.01)


def test_closed_interval_none():
    interval = ClosedInterval()
    assert interval.contains(-9999)
    assert interval.contains(15)
    assert interval.contains(9999)


def test_sensor_has_acceptable_value():
    sensor = Sensor(ClosedInterval(min=111, max=333))

    with pytest.raises(ValueError):
        sensor.has_acceptable_value()

    sensor.value = 222
    assert sensor.has_acceptable_value()

    sensor.value = 444
    assert not sensor.has_acceptable_value()


def test_location_get_alerts():
    room = Location(
        {
            "foo": Sensor(ClosedInterval(min=10, max=20)),
            "bar": Sensor(ClosedInterval(min=None, max=20), value=42),
        },
    )

    room.sensors["foo"].value = 15
    assert room.get_alerts() == ["bar"]

    room.sensors["foo"].value = 21
    assert room.get_alerts() == ["foo", "bar"]

    room.sensors["foo"].value = 9
    assert room.get_alerts() == ["foo", "bar"]


def test_get_location_sensors():
    result = get_location_sensors()
    all_rooms = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]

    assert set(result.keys()) == set(all_rooms)

    all_sensor_kinds = ["humidity", "illumination", "temperature", "sound", "co2"]
    for room in all_rooms:
        assert isinstance(result[room], Location)
        assert set(result[room].sensors.keys()) == set(all_sensor_kinds)


def test_main_invalid_data():
    no_alerts = {"alerts": []}

    assert main({}) == no_alerts
    assert main({"room": "bathroom-main"}) == no_alerts
    assert main({"room": "bathroom-main", "values": {}}) == no_alerts
    assert main({"foo": "bar", "baz": 42}) == no_alerts


def test_main_valid_data():
    data = {
        "room": "refectory",
        "values": {
            "co2": 999,
            "temperature": -2,
            "humidity": -3,
            "sound": -4,
            "illumination": -5,
        },
    }
    result = main(data)
    all_sensors = ["co2", "temperature", "humidity", "sound", "illumination"]
    assert set(result["alerts"]) == set(all_sensors)
