from src.main import (
    ClosedInterval,
    main,
    get_acceptable_co2_levels,
    get_acceptable_temperature_levels,
    get_acceptable_humidity_levels,
    get_acceptable_sound_levels,
    get_acceptable_illumination_levels,
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


def test_main_validates_co2():
    data = {
        "room": "bathroom-main",
        "values": {
            "co2": 0,
            "temperature": 0,
            "humidity": 0,
            "sound": 0,
            "illumination": 0,
        },
    }
    result = main(data)
    all_sensors = ["co2", "temperature", "humidity", "sound", "illumination"]
    assert set(result["alerts"]).issubset(set(all_sensors))


def test_co2_settings():
    result = get_acceptable_co2_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        isinstance(result[key], ClosedInterval)


def test_temperature_settings():
    result = get_acceptable_temperature_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        isinstance(result[key], ClosedInterval)


def test_main_validates_temperature():
    data = {
        "room": "refectory",
        "values": {
            "co2": 0,
            "temperature": 19,
            "humidity": 0,
            "sound": 0,
            "illumination": 0,
        },
    }
    result = main(data)
    all_sensors = ["co2", "temperature", "humidity", "sound", "illumination"]
    assert set(result["alerts"]).issubset(set(all_sensors))


def test_humidity_settings():
    result = get_acceptable_humidity_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        isinstance(result[key], ClosedInterval)


def test_main_validates_humidity():
    data = {
        "room": "room-1",
        "values": {
            "co2": 0,
            "temperature": 0,
            "humidity": 49,
            "sound": 0,
            "illumination": 0,
        },
    }
    result = main(data)
    all_sensors = ["co2", "temperature", "humidity", "sound", "illumination"]
    assert set(result["alerts"]).issubset(set(all_sensors))


def test_sound_settings():
    result = get_acceptable_sound_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        isinstance(result[key], ClosedInterval)


def test_main_validates_sound():
    data = {
        "room": "garden",
        "values": {
            "co2": 0,
            "temperature": 0,
            "humidity": 0,
            "sound": 9,
            "illumination": 0,
        },
    }
    result = main(data)
    all_sensors = ["co2", "temperature", "humidity", "sound", "illumination"]
    assert set(result["alerts"]).issubset(set(all_sensors))


def test_illumination_settings():
    result = get_acceptable_illumination_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        isinstance(result[key], ClosedInterval)


def test_main_validates_illumination():
    data = {
        "room": "bathroom-main",
        "values": {
            "co2": 0,
            "temperature": 0,
            "humidity": 0,
            "sound": 0,
            "illumination": 99,
        },
    }
    result = main(data)
    all_sensors = ["co2", "temperature", "humidity", "sound", "illumination"]
    assert set(result["alerts"]).issubset(set(all_sensors))
