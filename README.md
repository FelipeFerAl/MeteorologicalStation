# Embedded Linux Systems Programming Final Project : Metheorological Station 

## Authors: 
- Felipe Fernández Alzate - C.C.1056120378
- Paulina Ruiz Bonilla - C.C.1002609493

## Description: 

This project is a compact and affordable weather station built using a Raspberry Pi Zero, designed to monitor basic environmental conditions in real time. It integrates multiple sensors and displays the data both on the console and an I2C LCD screen.

## Learning Objectives:

- Apply all the knowledgment learned during the semester, like the configuration of the environment for the raspberry pi using Linux and implementation of servers and functions.
- Programming a functional Weather Station using several sensors occupied to measure temperature, atmospheric prssure, humidity and presence of rain. 

## Features: 

- DHT11: Measures temperature and humidity.

- BMP280: Measures atmospheric pressure and temperature.

- YL-38 Rain Sensor: Detects presence of rain.

- I2C LCD 16x2: Displays live data from the sensors.

- The system starts right when the raspberry is on and the sensors asociated start to measure the desire variables.

## Project Structure: 

### Hardware Connections (GPIO and I2C)

**DHT11 (Temperature & Humidity)**
  
- VCC → 3.3V
  
- DATA → GPIO 23 (board.D23)
  
- GND → GND

**BMP280 (Temperature & Pressure, I2C mode)**
  
- VIN → 5V
  
- GND → GND
  
- SCL → GPIO 3 (I2C SCL)
  
- SDA → GPIO 2 (I2C SDA)

- DO → 5V

- Default I2C address used: 0x77

**YL-38 Rain Sensor**
  
- DO (Digital Output) → GPIO 24
  
- VCC → 3.3V or 5V
  
- GND → GND

The sensor sends LOW when it detects rain. No need for analog input.

**I2C LCD 16x2 Display**

- SDA → GPIO 2

- SCL → GPIO 3
  
- VCC → 5V
  
- GND → GND

- I2C address: 0x27

### Hardware Implementation:

![esquemático proyecto_bb](https://github.com/user-attachments/assets/1af8894a-34fd-43fd-b133-a3bef7abf41c)

<img width="1574" height="890" alt="image" src="https://github.com/user-attachments/assets/6a5d72c3-7f6f-4ca4-abde-f0d4773da60f" />

<img width="1600" height="820" alt="image" src="https://github.com/user-attachments/assets/3aad08ec-2301-4216-999d-7c9500a12603" />

### Software Configuration: 

**Libraries Used:**

- `adafruit-circuitpython-dht` – for reading DHT11 temperature/humidity sensor

- `adafruit-circuitpython-bmp280` – for BMP280 pressure/temperature sensor

- `RPLCD` – for controlling the I2C LCD display

- `RPi.GPIO` – for reading the rain sensor (YL-38)

- `board` – for identifying GPIO pin numbers in a hardware-friendly way

- `time, sys` – for delays, user inputs, and graceful exits

**Files:**

- *test_modules:* It contains the corresponding code to probe each one of the sensors and its correct functioning along with the visualization of the parameters sensed.
- *complete_functioning:* It contains the main program for the complete system functioning, where all the sensors work together to measure the variables mentioned above. The results are shown in the LCD and are updated every 5 seconds.

## Compilation and results: 

Inmediately, the raspberry pi is going to start the system and it can be seen in the LCD the weather variables desired. 

<img width="1484" height="676" alt="image" src="https://github.com/user-attachments/assets/8c5ed0ef-6b2b-4d41-9f66-1c25ca26e068" />

While the LCD shows the parameteres measure by the sensors, it is possible to test each one of the sensors through the console. For that, the code counts with a menu option and the possibility of verify the results, as it can be seen in the next image: 

**Image of the menu and each one of the results**






