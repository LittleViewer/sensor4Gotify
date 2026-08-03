import sensor.patron_sensor as spS
import config_tool_class as ctC
import psutil

class sensor_cpu_ram:

    def pipe_alert_usage(self, address, password):
        title = "Alert usage of "
        message = "This is an alert regarding "
        if self.ctC_.key_return("parameter","ram","alert_level") >= self.ram_usage_percent :
            title += "RAM"
            message += f"{self.ram_usage_percent}% RAM usage"
        if self.ctC_.key_return("parameter","cpu","alert_level") >= self.cpu_usage:
            title += "CPU"
            message += f"{self.cpu_usage}% CPU usage"
        spS.patron_sensor.request(address, password,f"{title} !",f"{message}!")

    def __init__(self):
        self.ctC_ = ctC.config_toml_tool()
        self.ram = psutil.virtual_memory()
        self.ram_usage_percent = self.ram.percent
        self.cpu_usage = self.cpu_usage(interval=1)
