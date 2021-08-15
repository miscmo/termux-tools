import os
import json

def get_battery_status():
    request = os.popen("termux-battery-status")

    request_json = request.read()

    if not request_json:
        return None

    status = json.loads(request_json)

    return status

def get_battery_percentage():
    battery_status = get_battery_status()

    return battery_status['percentage']

def is_battery_plugged():
    battery_status = get_battery_status()

    unplugged = battery_status['plugged'] == 'UNPLUGGED'

    return not unplugged

if __name__ == "__main__":
    battery_status = get_battery_status()

    print(battery_status)

    is_plugged = is_battery_plugged()

    print(f'battery plugged: {is_plugged}')

    battery_percentage = get_battery_percentage()

    print(battery_percentage)
