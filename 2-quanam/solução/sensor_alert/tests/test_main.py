from src.main import (
    main,
    get_acceptable_co2_levels,
    get_acceptable_temperature_levels,
    get_acceptable_humidity_levels,
)


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
    assert "alerts" in result
    assert "co2" not in result["alerts"]

    data["values"]["co2"] = 500
    result = main(data)
    assert "co2" not in result["alerts"]

    data["values"]["co2"] = 501
    result = main(data)
    assert "co2" in result["alerts"]


def test_co2_settings():
    result = get_acceptable_co2_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        assert "min" in result[key]
        assert "max" in result[key]


def test_temperature_settings():
    result = get_acceptable_temperature_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        assert "min" in result[key]
        assert "max" in result[key]


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
    assert "alerts" in result
    assert "temperature" in result["alerts"]

    data["values"]["temperature"] = 20
    result = main(data)
    assert "temperature" not in result["alerts"]

    data["values"]["temperature"] = 23
    result = main(data)
    assert "temperature" not in result["alerts"]

    data["values"]["temperature"] = 24
    result = main(data)
    assert "temperature" in result["alerts"]


def test_humidity_settings():
    result = get_acceptable_humidity_levels()
    keys = ["activity-room", "refectory", "room-1", "bathroom-main", "garden"]
    for key in keys:
        assert key in result
        assert "min" in result[key]
        assert "max" in result[key]


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
    assert "alerts" in result
    assert "humidity" in result["alerts"]

    data["values"]["humidity"] = 50
    result = main(data)
    assert "humidity" not in result["alerts"]

    data["values"]["humidity"] = 60
    result = main(data)
    assert "humidity" not in result["alerts"]

    data["values"]["humidity"] = 61
    result = main(data)
    assert "humidity" in result["alerts"]
