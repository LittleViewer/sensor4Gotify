import requests
class patron_sensor:

    def request(address, password, title, message, priority = 2):
        requests.post(address, headers={"X-Gotify-Key": password}, json={
                "message": message,
                "priority": priority,
                "title": title})