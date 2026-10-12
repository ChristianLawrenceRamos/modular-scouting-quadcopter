# Modular Scouting Quadcopter Prototype

A compact scouting quadcopter prototype focused on UAV hardware integration, embedded sensor testing, rapid prototyping, flight-controller configuration, and hardware test validation.

## Project Purpose

This project is being developed as a modular UAV platform for scouting, inspection, and future autonomous sensing applications. The goal is to integrate a flight controller, Raspberry Pi compute, onboard sensing, camera systems, telemetry, and 3D printed hardware into a compact quadcopter prototype.

The project emphasizes practical aerospace hardware skills including:

- UAV hardware integration
- Flight-controller setup and troubleshooting
- INAV configuration
- Raspberry Pi/Linux hardware testing
- UART and I2C sensor communication
- Soldering, wiring, and connector verification
- 3D printed prototype parts
- Dimensional fit checks using calipers
- Bench testing and flight-readiness validation

## Current Hardware

- SpeedyBee F405 flight controller / ESC stack
- Brushless motors
- Receiver and telemetry hardware
- Raspberry Pi 5 onboard compute
- LiDAR/range sensing
- Optical-flow sensing
- Camera modules
- Power distribution and voltage regulation
- 3D printed PLA/PETG mounts and electronics packaging

## Flight Controller Work

The flight controller is configured using INAV. Current work includes:

- Receiver binding
- Failsafe testing
- UART assignment checks
- Optical-flow and rangefinder sensor status verification
- Motor output checks
- CLI-based configuration review
- Flight-readiness troubleshooting

## Raspberry Pi / Embedded Systems Work

The Raspberry Pi 5 is used for onboard compute and sensor testing. Current work includes:

- Linux terminal setup and hardware debugging
- UART serial communication testing
- Sensor data reads
- GPIO/I2C/USB troubleshooting
- Camera ribbon-cable integration
- Python-based sensor test scripts

## Rapid Prototyping

A Bambu Lab P1S with AMS is used to rapidly prototype:

- Sensor mounts
- Electronics trays
- Camera brackets
- Wire-routing features
- Fit-check parts
- Vibration-isolation concepts
- Prototype tooling concepts

Parts are iterated using caliper-based fit checks, mounting-hole alignment checks, component-clearance checks, and assembly review.

## Testing

Testing includes:

- Bench power checks
- Wiring verification
- Continuity checks
- Receiver/failsafe checks
- Motor spin testing
- Sensor status checks
- UART/I2C communication checks
- Vibration checks
- Tethered hover preparation
- Prototype troubleshooting

## Next Steps

- Complete system wiring diagram
- Create full bill of materials
- Document INAV CLI configuration
- Write Python sensor logging scripts
- Complete controlled hover testing
- Add sensor test data and flight-readiness checklist
- Create Rev 2 printed parts in PETG
