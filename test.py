from sense_hat import SenseHat
import time
from datetime import datetime

# Initialize the Sense HAT
sense = SenseHat()
sense.clear()  # Clear the LED matrix

print("Raspberry Pi Sense HAT Sensor Test")
print("==================================")

try:
    while True:
        # Get current timestamp
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Environmental sensors
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        
        # Motion sensors
        orientation = sense.get_orientation()
        acceleration = sense.get_accelerometer_raw()
        
        # Display readings
        print(f"\n[{current_time}] Sensor Readings:")
        print("-------------------------")
        print(f"Temperature: {temp:.1f}°C")
        print(f"Humidity: {humidity:.1f}%")
        print(f"Pressure: {pressure:.1f} millibars")
        print(f"Pitch: {orientation['pitch']:.1f}°")
        print(f"Roll: {orientation['roll']:.1f}°")
        print(f"Yaw: {orientation['yaw']:.1f}°")
        print(f"Acceleration: x={acceleration['x']:.2f}g, y={acceleration['y']:.2f}g, z={acceleration['z']:.2f}g")
        
        # Display temperature on the LED matrix
        temp_color = [min(255, int(temp * 8)), max(0, 255 - int(temp * 8)), 0]  # Hotter = more red, less green
        sense.show_message(f"{temp:.1f}C", text_colour=temp_color, scroll_speed=0.05)
        
        # Wait before taking the next reading
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nTest terminated by user")
    sense.clear()  # Clear the LED matrix on exit