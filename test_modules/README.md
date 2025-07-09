## This carpet contains the files associated to the testing of each one of the sensors and the correct installation of the libraries:

### Function for testing the DHT11 sensor: 

`test_dht11()`: 

- Initializes the sensor using GPIO 23.

- Reads temperature (°C) and humidity (%).

- Displays the values on the terminal and on the I2C LCD.

- Handles read errors (which are common with DHT sensors).

- Updates every 5 seconds in a loop until interrupted.

### Function for testing the BMP2280 sensor: 

`test_bmp280()`:

- Initializes communication over I2C (default address 0x77).

- Reads the ambient temperature (°C) and atmospheric pressure (hPa).

- Shows results on the terminal and on the LCD (two-line display).

- Updates values every 5 seconds in a loop until interrupted by the user.

### Function for testing the YL - 38 rain sensor:

`test_rain_sensor()`:

- Uses GPIO 24 to read the digital output.

- Prints “R: SI” if rain is detected (i.e., signal is LOW), “R: NO” otherwise.

- Shows the result on the LCD screen.

- Cleans up GPIO pins after reading.

### Function for testing the LCD 16x2: 

`test_lcd()`:

- Initializes the LCD using I2C (address 0x27).

### To check if the libraries are correct installed:

`check_module(name)`: 
A helper function to check if a given Python module is installed on the system.

- Input: A string with the module name (e.g., 'adafruit_dht')

**Process:**

- Tries to import the module using __import__()

- If successful, prints a checkmark and returns True

- If not installed, prints a red and returns False

- Purpose: Quickly validate critical modules without crashing the main script.

- Displays a simple test message across two lines.
