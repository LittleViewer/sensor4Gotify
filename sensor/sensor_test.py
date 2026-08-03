import requests

class sensor_test:

    def pipe_lauch_test(self, address, password):
        requests.post(address, headers={"X-Gotify-Key": password}, json={
            "message": "TEST",
            "priority": 2,
            "title": "This is a test !"})
        
    def __init__(self):
        pass