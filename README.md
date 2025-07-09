# Final Project Embedded Linux Systems Programming: Metheorological Station 

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

## Project Structure: 

### Hardware Connections (GPIO and I2C)

DHT11 (Temperature & Humidity)
  VCC → 3.3V
  DATA → GPIO 23 (board.D23)
  GND → GND

BMP280 (Temperature & Pressure, I2C mode)
  VIN → 3.3V
  GND → GND
  SCL → GPIO 3 (I2C SCL)
  SDA → GPIO 2 (I2C SDA)

  Default I2C address used: 0x77

YL-38 Rain Sensor
  DO (Digital Output) → GPIO 24
  VCC → 3.3V or 5V
  GND → GND

The sensor sends LOW when it detects rain. No need for analog input.

I2C LCD 16x2 Display
  SDA → GPIO 2
  SCL → GPIO 3
  VCC → 5V
  GND → GND

  I2C address: 0x27

### Software Configuration: 

** Libraries Used: **

