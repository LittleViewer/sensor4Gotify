import sensor.patron_sensor as spS

class sensor_i_am_alive:

    def pipe_lauch_alive(self, address, password):
        spS.patron_sensor.request(address, password,"I'm alive !","Dearest creator, this message is to let you know that I am still up and running!")
    def __init__(self):
        pass