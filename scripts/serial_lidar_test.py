"""
serial_lidar_test.py

Basic serial test script for reading bytes from a UART-based LiDAR/range sensor.
Update SERIAL_PORT and BAUD_RATE for your Raspberry Pi configuration.
"""

import serial
import time

SERIAL_PORT = "/dev/serial0"
BAUD_RATE = 115200

def main():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
            print("Reading serial data. Press Ctrl+C to stop.")

            while True:
                data = ser.read(18)
                if data:
                    timestamp = time.time()
                    print(f"{timestamp:.3f}: {data.hex()}")
                time.sleep(0.05)

    except serial.SerialException as error:
        print(f"Serial error: {error}")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
