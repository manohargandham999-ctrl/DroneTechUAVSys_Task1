import collections

# This is the "fix" for Python 3.10+ compatibility
if not hasattr(collections, 'MutableMapping'):
    import collections.abc
    collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect

# Connect to the Vehicle (SITL)
print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Print information from Screenshot 2026-05-04 150725.png
print("Drone is connected")
print("GPS: %s" % vehicle.gps_0)
print("Battery: %s" % vehicle.battery)
print("Last Heartbeat: %s" % vehicle.last_heartbeat)

vehicle.close()
print("Connection closed")
