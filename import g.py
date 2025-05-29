import time
import random

def get_distance():
    # Simulates distance from an ultrasonic sensor in cm
    return random.randint(5, 100)

def detect_obstacle():
    distance = get_distance()
    print(f"Distance from object: {distance} cm")
    if distance < 20:
        print("Obstacle detected! Stopping vehicle.")
    else:
        print("Path is clear. Moving forward.")

# Simulate the vehicle checking for obstacles every second
for _ in range(5):
    detect_obstacle()
    time.sleep(1)