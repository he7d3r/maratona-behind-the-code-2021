from src.main import main


def test_main_has_alerts():
    result = main({})
    assert "alerts" in result


def test_main_accepts_json_fields():
    data = {
        "room": "bathroom-main",
        "values": {
            "co2": 400,
            "temperature": 22,
            "humidity": 70,
            "sound": 30,
            "illumination": 150,
        },
    }
    result = main(data)
    assert "alerts" in result
