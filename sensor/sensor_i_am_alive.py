import sensor.patron_sensor as spS

class sensor_i_am_alive:
    def get_uptime(self):
        with open('/proc/uptime', 'r') as f:
            second = float(f.readline().split()[0])
            if second == 0:
                second = 0.1
            self.uptime_seconds = second

    def pipe_lauch_alive(self, address, password):
        spS.patron_sensor.request(address, password,"I'm alive !",f"Dearest creator, this message is to let you know that I have been running for {(round(self.uptime_seconds/60)/60)} hours now!")
    def __init__(self):
        self.get_uptime()