import collections
import time

# ABSOLUTE FIRST: Fix for Python 3.10+ compatibility
if not hasattr(collections, 'MutableMapping'):
    import collections.abc
    collections.MutableMapping = collections.abc.MutableMapping

# NOW import dronekit
from dronekit import connect, VehicleMode

# Connect to the Vehicle
print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just before target altitude.
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Run the function from Part 4 of Screenshot 2026-05-04 171606.png
arm_and_takeoff(10)

print("Takeoff complete. Hovering for 5 seconds...")
time.sleep(5)

print("Setting Land mode...")
vehicle.mode = VehicleMode("LAND")

vehicle.close()
