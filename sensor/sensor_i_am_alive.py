import requests

class sensor_i_am_alive:

    def pipe_lauch_alive(self, address, password):
        resp = requests.post(address, headers={"X-Gotify-Key": password}, json={
            "message": "Well hello there.",
            "priority": 2,
            "title": "I'm alive !"})
    def __init__(self):
        pass