# water_flow_sensor.py
import random
import time

def read_water_flow():
    # Simulate reading from a water flow sensor
    return random.uniform(0.0, 10.0)  # Flow rate in liters per minute

def detect_leak(flow_rate):
    # Simple leak detection logic
    if flow_rate > 8.0:
        return True
    return False

while True:
    flow_rate = read_water_flow()
    leak_detected = detect_leak(flow_rate)
    print(f"Flow Rate: {flow_rate:.2f} L/min | Leak Detected: {leak_detected}")
    time.sleep(5)  # Wait for 5 seconds before next reading
