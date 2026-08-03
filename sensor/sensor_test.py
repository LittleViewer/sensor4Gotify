import sensor.patron_sensor as spS

class sensor_test:

    def pipe_lauch_test(self, address, password):
        spS.patron_sensor.request(address, password,"TEST","TEST")
        
    def __init__(self):
        pass