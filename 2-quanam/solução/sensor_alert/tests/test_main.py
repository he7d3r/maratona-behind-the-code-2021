from src.main import main, get_acceptable_co2_levels


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
