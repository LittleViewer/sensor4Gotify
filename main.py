import config_tool_class
import sensor.sensor_i_am_alive
import sensor.sensor_test
import argparse


ctC_ = config_tool_class.config_toml_tool()

address = f"http://{ctC_.key_return("parameter","ip","server")}:{ctC_.key_return("parameter","port","server")}/message"
password = ctC_.key_return("parameter","password_app","server")
parser = argparse.ArgumentParser()
argument_run = ctC_.key_return("parameter","list_flag","flag")

for one_argument in argument_run:
    parser.add_argument(f"-{one_argument}", action="store_true")
args = parser.parse_args()

if args.i_am_alive:
    sensor.sensor_i_am_alive.sensor_i_am_alive().pipe_lauch_alive(address, password)
elif args.test:
    sensor.sensor_test.sensor_test().pipe_lauch_test(address, password)