# Test Plan

This test plan documents the bench, integration, and flight-readiness checks for the Modular Scouting Quadcopter Prototype. The goal is to verify hardware safety, sensor communication, flight-controller configuration, wiring reliability, and prototype readiness before powered flight testing.

## Test Philosophy

Testing is performed in stages to reduce risk:

1. Mechanical inspection
2. Wiring and continuity checks
3. Power verification
4. Receiver and failsafe verification
5. Sensor communication checks
6. Motor output and direction checks
7. Vibration and fitment checks
8. Tethered hover preparation
9. Controlled hover testing

Propellers should remain removed during all bench, wiring, receiver, sensor, and motor-direction checks unless a hover or thrust test specifically requires them.

---

## Test 1 — Mechanical Inspection

### Purpose

Verify that the prototype is mechanically safe before power is applied.

### Checklist

- Frame hardware is secure
- No loose screws or standoffs
- Battery mount or battery strap is secure
- Flight controller is mounted securely
- Raspberry Pi is mounted securely
- LiDAR/range sensor mount is secure
- Optical-flow sensor mount is secure
- Camera mount is secure
- Wires are clear of propeller paths
- No wires are pinched between frame plates
- No exposed conductors are touching the frame
- Printed parts show no major cracks, warping, or delamination
- Motor screws do not contact motor windings

### Pass Criteria

The airframe, electronics, and printed components are physically secure with no visible interference, loose hardware, or unsafe wiring.

---

## Test 2 — Dimensional and Fitment Check

### Purpose

Verify printed-part fitment, mounting-hole alignment, sensor orientation, and component clearances.

### Tools

- Digital calipers
- Screwdriver/hex drivers
- Printed part revisions
- Mounting hardware

### Checklist

- Mounting holes align with frame or component holes
- Sensor faces are not blocked by frame or printed parts
- Camera field of view is not blocked
- LiDAR/range sensor has clear downward or intended line of sight
- Optical-flow sensor has clear downward view
- Raspberry Pi clearance is acceptable
- Flight controller USB port remains accessible
- Wires can be routed without sharp bends
- Battery clearance is acceptable
- Printed parts do not interfere with propellers or motor wires

### Pass Criteria

All major components fit correctly, mounting locations are usable, and no critical clearance or alignment issues are found.

---

## Test 3 — Continuity and Polarity Check

### Purpose

Verify wiring before applying battery power.

### Tools

- Multimeter
- Wiring diagram
- Continuity mode
- Visual inspection

### Checklist

- Battery positive and negative verified
- Power input polarity verified
- 5V regulator polarity verified
- Raspberry Pi power input checked
- Flight controller power input checked
- Sensor power wiring checked
- No short between battery positive and ground
- No short between 5V and ground
- No short between signal wires and power wires
- Connector pinouts verified before plugging into electronics
- Heat-shrink or insulation applied where needed

### Pass Criteria

No shorts are detected, all power connections have correct polarity, and connector pinouts match the wiring diagram.

---

## Test 4 — Initial Power-On Check

### Purpose

Safely verify that the electronics power on correctly.

### Tools

- Smoke stopper or current-limited power source if available
- Multimeter
- Battery checker
- INAV Configurator
- Raspberry Pi terminal

### Checklist

- Propellers removed
- Battery voltage checked before connection
- Smoke stopper used if available
- Flight controller powers on
- ESC stack powers on without overheating
- Receiver powers on
- Raspberry Pi powers on
- 5V rail verified
- No smoke, smell, excessive heat, or abnormal LED behavior
- USB connection to flight controller works
- Raspberry Pi can be accessed through terminal/SSH if applicable

### Pass Criteria

All electronics power on normally with stable voltage and no signs of electrical fault.

---

## Test 5 — Receiver and Failsafe Check

### Purpose

Verify radio control input and failsafe behavior before any motor or flight testing.

### Tools

- Transmitter
- Receiver
- INAV Configurator
- Flight controller USB connection

### Checklist

- Receiver is bound to transmitter
- Receiver protocol is configured correctly
- Stick inputs are visible in INAV Configurator
- Channel mapping is correct
- Arm switch is recognized
- Flight mode switch is recognized
- Throttle low value is verified
- Failsafe activates when transmitter is turned off
- Failsafe behavior is confirmed before propellers are installed

### Pass Criteria

Receiver inputs respond correctly, arming controls are recognized, and failsafe behavior works reliably.

---

## Test 6 — Flight Controller Configuration Check

### Purpose

Verify INAV configuration and flight-readiness settings.

### Tools

- INAV Configurator
- CLI
- Saved CLI dump
- UART assignment notes

### Checklist

- Board target and firmware version recorded
- Accelerometer detected
- Gyroscope detected
- Barometer detected, if installed
- Magnetometer status noted
- Receiver input working
- UART assignments documented
- Optical-flow input status checked
- Rangefinder input status checked
- Motor mixer verified
- Board orientation verified
- Arming flags reviewed
- CLI dump saved to `firmware_config/inav_cli_dump.txt`

### Pass Criteria

Flight controller sensors and configuration are documented, major arming blockers are understood, and the configuration is saved for revision control.

---

## Test 7 — Sensor Communication Check

### Purpose

Verify sensor status and communication between onboard sensors, flight controller, and Raspberry Pi.

### Tools

- INAV Configurator
- Raspberry Pi terminal
- Python/serial tools
- I2C tools, if applicable
- Wiring diagram

### Checklist

- LiDAR/range sensor wiring checked
- Optical-flow sensor wiring checked
- Camera ribbon cable seated correctly
- UART device path identified on Raspberry Pi
- Serial baud rate verified
- Sensor data read successfully, if available
- I2C devices detected, if applicable
- USB devices detected, if applicable
- Sensor failure status documented
- Sensor readings or raw data saved to `results/sensor_logs/`

### Pass Criteria

Sensor communication is verified or failure modes are documented for troubleshooting.

---

## Test 8 — Motor Output and Direction Check

### Purpose

Verify motor order, motor direction, and ESC response before flight.

### Safety Requirement

Propellers must be removed for this test.

### Tools

- INAV Configurator
- Motor tab
- Battery
- Safety glasses

### Checklist

- Propellers removed
- Drone secured on bench
- Motor order verified
- Motor direction verified
- ESC response verified
- No abnormal grinding, clicking, or overheating
- Motor wires clear of frame and rotating parts
- Motor screws checked after spin test

### Pass Criteria

All motors spin in the correct order and direction with normal sound and response.

---

## Test 9 — Vibration and Mounting Check

### Purpose

Evaluate vibration sources and component security during motor operation.

### Safety Requirement

Propellers removed unless performing a controlled thrust/hover test.

### Checklist

- Motors spin smoothly
- Frame does not show excessive vibration
- Flight controller mount remains secure
- Raspberry Pi mount remains secure
- Camera mount remains secure
- LiDAR/range sensor mount remains secure
- Optical-flow sensor mount remains secure
- Wires do not move into unsafe areas
- Loose fasteners are retightened after testing

### Pass Criteria

No major vibration-related movement, loose hardware, or unsafe wire movement is observed.

---

## Test 10 — Tethered Hover Preparation

### Purpose

Prepare for first controlled hover test.

### Checklist

- Previous tests completed
- Battery charged and inspected
- Propellers installed in correct orientation
- Motor direction verified
- Receiver/failsafe verified
- Flight mode selected
- Arming procedure understood
- Emergency disarm procedure understood
- Test area clear
- Drone tethered or restrained safely if using tethered hover method
- Observer present if possible
- Video recording started for review

### Pass Criteria

Drone is ready for a low-risk hover test with emergency shutdown procedure confirmed.

---

## Test 11 — Controlled Hover Test

### Purpose

Validate basic flight readiness and stability.

### Checklist

- Takeoff area clear
- Low hover attempted
- Throttle response observed
- Roll/pitch/yaw response observed
- Excessive drift noted
- Abnormal vibration noted
- Battery voltage monitored
- Landing completed safely
- Motors checked after landing
- Frame and mounts inspected after landing
- Notes recorded in build log

### Pass Criteria

Drone completes a short, controlled hover without major instability, unsafe vibration, or hardware failure.

---

## Test Results Template

Use this format for each test entry:

```text
Date:
Test Number:
Configuration / Revision:
Battery:
Propellers Installed: Yes / No
Result: Pass / Fail / Partial
Observations:
Issues Found:
Corrective Actions:
Next Steps:
