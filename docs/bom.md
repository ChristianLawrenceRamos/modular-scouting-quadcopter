# Bill of Materials

This bill of materials documents the current major hardware, electronics, sensors, tools, and prototype components used in the Modular Scouting Quadcopter Prototype.

Status labels:
- `Installed` = physically mounted or connected
- `Testing` = connected or being validated
- `Planned` = intended for future integration
- `To Verify` = part is known, but exact connection/status should be confirmed in the current build
- `In Revision` = being redesigned, reprinted, or mechanically revised

---

## Core Flight Hardware

| Subsystem | Component | Model / Notes | Interface / Connection | Status |
|---|---|---|---|---|
| Flight Controller | Flight Controller | SpeedyBee F405 V4 | USB, UART, motor outputs, INAV configurator | Installed |
| ESC | 4-in-1 ESC | SpeedyBee 55A 4-in-1 ESC / SpeedyBee stack | Battery input, motor phase wires, FC stack connection | Installed |
| Motors | Brushless Motors | T-Motor F60 Pro V 1950KV | ESC motor outputs | Installed |
| Propulsion | Propellers | 5-inch propellers; tri-blade configuration planned/used in earlier build plan | Motor shafts | To Verify |
| Radio Control | Transmitter | Radiomaster Pocket | 2.4 GHz control link | Active |
| Radio Control | Receiver | Radiomaster-compatible receiver / CRSF workflow | FC UART2 RX from prior wiring notes | Installed / Bound |
| Firmware | Flight Firmware | INAV 9.1.0 | SpeedyBee F405 V4 | Installed |
| Battery | Main Flight Battery | 4S 1550 mAh LiPo | Main power input | Testing |
| Power | Power Regulation | Matek UBEC Duo and/or PDB-HEX; 5V/5A rail under evaluation | Battery/FC power to Raspberry Pi and sensors | Testing |
| Power | Power Distribution | SpeedyBee ESC stack + auxiliary regulator/PDB workflow | Battery input, ESC, FC, Pi/sensor power | Testing |

---

## Onboard Compute and Sensors

| Subsystem | Component | Model / Notes | Interface / Connection | Status |
|---|---|---|---|---|
| Compute | Onboard Computer | Raspberry Pi 5 | USB, GPIO, UART, I2C, CSI | Installed |
| Range Sensor | LiDAR / Rangefinder | TF-Luna LiDAR | UART to Raspberry Pi | Testing |
| Optical Flow | Optical-Flow Sensor | MSP optical-flow module / MTF-01-class sensor | UART/MSP to flight controller | Testing |
| Camera | Monochrome Camera | IMX296 monochrome camera, 1456×1088, 10-bit | Raspberry Pi camera interface / CSI workflow | Testing |
| Camera | NoIR / RGB Camera | Pi NoIR or RGB camera option | CSI ribbon cable | Planned |
| Thermal Sensor | Thermal Camera | MLX90640 32×24 thermal sensor | I2C | Planned |
| IMU | Payload IMU | BNO085 or similar | I2C / UART | Planned |
| Environmental Sensor | Barometer / Temp / Humidity | BME280 | I2C | Planned |
| Lighting | LED / IR Module | Dimmable LED / IR illumination concept | GPIO / PWM / MOSFET driver | Planned |

---

## Interfaces and Communication

| Subsystem | Component | Model / Notes | Interface / Connection | Status |
|---|---|---|---|---|
| Flight Controller UART | Receiver Port | Receiver connected to FC UART2 RX in prior wiring notes | UART / CRSF workflow | Installed / To Verify |
| Flight Controller UART | Optical Flow Port | Optical flow connected to FC UART3 RX in prior wiring notes | UART/MSP | Testing |
| Raspberry Pi UART | LiDAR Serial | TF-Luna serial data observed from Pi | `/dev/serial0`, `/dev/ttyAMA0`, or mapped UART | Testing |
| Raspberry Pi UART | External Radio Test | Radio/serial test device used in prior testing | `/dev/ttyAMA3` or mapped UART | Testing |
| Raspberry Pi I2C | Sensor Bus | MLX90640, BNO085, BME280 planned sensor bus | GPIO I2C | Planned |
| USB | Configuration / Debug | FC USB and Pi USB access | USB-C / USB | Active |
| CSI | Camera Ribbon Cable | Pi camera connection | Raspberry Pi CSI port | Testing |
| Ground Link | Telemetry / Radio Pair | 915 MHz communication concept / radio pair | UART or USB serial | Testing / To Verify |

---

## Structure, Mounts, and Rapid Prototyping

| Subsystem | Component | Material / Notes | Manufacturing Method | Status |
|---|---|---|---|---|
| Frame | Quadcopter Frame | Current test frame with future carbon-fiber frame concept | Purchased / prototype | Installed |
| Mounts | Sensor Mounts | PLA/PETG LiDAR, optical-flow, camera mounts | Bambu Lab P1S 3D printing | In Revision |
| Mounts | Raspberry Pi Mount | Pi 5 electronics tray / mount | Bambu Lab P1S 3D printing | In Revision |
| Mounts | Antenna Mount | Antenna support bracket | Bambu Lab P1S 3D printing | Planned / In Revision |
| Mounts | LED / IR Mount | Lighting mount for future scouting/security use | Bambu Lab P1S 3D printing | Planned |
| Wire Management | Cable Guides / Clips | PLA/PETG routing clips | 3D printed | In Revision |
| Vibration Isolation | Rubber Rings / Dampers | Anti-vibration isolation for electronics/sensors | Purchased / installed | Testing |
| Composite Tooling | Prototype Molds | PLA/PETG molds for carbon fiber layup | 3D printed tooling | Testing |
| Composite Structure | Carbon Fiber Components | Carbon fiber layup, vacuum bagging, fitment checks | Hand layup / prototype tooling | Testing |

---

## Tools and Lab Equipment

| Category | Tool / Equipment | Model / Notes | Use | Status |
|---|---|---|---|---|
| 3D Printing | 3D Printer | Bambu Lab P1S with AMS | PLA/PETG prototype parts | Active |
| Measurement | Digital Calipers | Caliper-based fitment checks | Hole spacing, clearance, printed-part dimensions | Active |
| Soldering | Soldering Station | Standard electronics soldering tools | Wiring and connector assembly | Active |
| Wiring | Crimpers / Wire Strippers | Connector and harness assembly | Signal/power wiring | Active |
| Electrical Test | Multimeter | Continuity, polarity, voltage checks | Bench testing | Active |
| Serial Debug | USB-UART Adapter | CP2102 / USB serial adapter | UART testing | Active |
| Software | INAV Configurator | FC configuration and CLI | Flight controller setup | Active |
| Software | Linux Terminal | Raspberry Pi hardware testing | UART/I2C/USB debugging | Active |
| Software | Python | Sensor test scripts / serial reads | Data logging and debugging | Active |
| Software | MATLAB | Analysis / simulation | Engineering analysis | Active |
| CAD | Fusion 360 / SolidWorks | CAD layouts and printed part design | Mechanical design | Active |

---

## Consumables and Hardware

| Category | Item | Notes | Status |
|---|---|---|---|
| Fasteners | M2 / M2.5 / M3 screws | Drone assembly and mounts | Active |
| Fasteners | Standoffs and spacers | Electronics mounting | Active |
| Wiring | Silicone wire | Power and signal wiring | Active |
| Wiring | Heat-shrink tubing | Insulation and strain relief | Active |
| Connectors | JST / Dupont / servo leads | Sensor and signal connections | Active |
| Connectors | XT30 / XT60 | Battery and power connections | Testing |
| Adhesives | Epoxy | Carbon fiber layup and bonding | Active |
| Composite | Carbon fiber cloth / tow | Prototype composite components | Active |
| Printing | PLA filament | Fit-check parts and prototypes | Active |
| Printing | PETG filament | Functional prototype mounts and molds | Active |

---

## Current Integration Status

| System | Current Status | Notes |
|---|---|---|
| Flight Controller | Installed | SpeedyBee F405 V4 configured through INAV 9.1.0 |
| ESC | Installed | SpeedyBee 55A 4-in-1 ESC / SpeedyBee stack |
| Motors | Installed | T-Motor F60 Pro V 1950KV |
| Propellers | To Verify | 5-inch propellers; confirm exact pitch/blade count/brand |
| Battery | Testing | 4S 1550 mAh LiPo |
| Receiver | Bound | Radiomaster Pocket link verified |
| Failsafe | Verified / Testing | Radio-off failsafe behavior tested |
| Raspberry Pi 5 | Installed / Testing | Linux terminal and serial testing active |
| TF-Luna LiDAR | Testing | UART frames observed from Pi serial testing |
| Optical Flow | Testing | Connected to FC through MSP/serial workflow |
| Camera System | Testing | IMX296 monochrome camera known; mounting/integration in progress |
| 3D Printed Mounts | In Revision | PLA/PETG parts being iterated for fitment and packaging |
| Composite Parts | Prototype Stage | PETG/PLA molds and carbon fiber layup workflow under development |
| Home Security Ecosystem | Concept Stage | Future fixed-camera + PC hub + scouting drone demo |

---

## Remaining Items to Verify

| Item | Needed Information | Why It Matters |
|---|---|---|
| Propellers | Exact brand, diameter, pitch, blade count, and CW/CCW set | Needed for thrust estimate, current draw, noise, and motor compatibility |
| Receiver | Exact receiver model and protocol settings | Needed for wiring diagram and INAV documentation |
| Optical Flow Sensor | Exact module model and protocol | Needed for INAV setup and wiring documentation |
| 5V Regulator / PDB | Final choice between Matek UBEC Duo, PDB-HEX, or both | Needed to safely power Raspberry Pi 5 and sensors |
| Camera Mount | Final IMX296 camera mounting geometry | Needed for printed mount revision and field-of-view planning |
| Telemetry Radio | Exact model, frequency, and interface | Needed for communication range and wiring documentation |
| GPS Module | Selected model, GNSS support, compass status, and interface | Needed for future outdoor/global-coordinate experiments |
| Printed Mounts | Revision numbers, material, dimensions, infill/settings | Needed for repeatable manufacturing and GitHub documentation |
