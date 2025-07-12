## This space contains the files associated to the testing of each one of the sensors, the module to create each sensor object and the correct installation of the libraries:

### How the sensors_modules work:
It basically initializes the objects each sensor needs so the Raspberry can take the information provided via GPIO pins or I2C channel. This module is called by the sensors_test and monitoreo_sensores files as they work at the same time with the same sensors, so we just avoid overwriting or problems with GPIO activations (especially the one connected with the DHT11 sensor)

### Function for testing the DHT11 sensor: 

`test_dht11()`: 

- It looks for the temporary file with the values read by the meteorological station service

- Reads temperature (°C) and humidity (%).

- Displays the values on the terminal.

- Handles read errors (In case there is no json temporary file).

- Updates every 5 seconds in a loop until interrupted.

### Function for testing the BMP2280 sensor: 

`test_bmp280()`:

- Reads the ambient temperature (°C) and atmospheric pressure (hPa).
  
- Shows results on the terminal.

- Updates values every 5 seconds in a loop until interrupted by the user.

### Function for testing the YL - 38 rain sensor:

`test_rain_sensor()`:

- Uses GPIO 24 to read the digital output.

- Prints “R: SI” if rain is detected (i.e., signal is LOW), “R: NO” otherwise.

- Shows the result on the LCD screen.

- Cleans up GPIO pins after reading.

### Function for testing the LCD 16x2: 

`test_lcd()`:

- Checks if the LCD object was created correctly with the service activation

### Testing:

`main_menu`:

- We clear the terminal to print the menu the user will have access to while the service is running and wait for its input
<img width="364" height="152" alt="Screenshot 2025-07-11 214006" src="https://github.com/user-attachments/assets/a5ce5512-23a0-450b-bd96-02073b59c1f9" />

Once there is a valid input, we call the functions to test each sensor on a loop stopped via Ctrl+C, its error is controlled to show on terminal a correct termination

- DHT11:
<img width="493" height="184" alt="Screenshot 2025-07-11 214059" src="https://github.com/user-attachments/assets/93bcbaef-5609-44ea-bd8f-de4029e486be" />

- BMP280:
<img width="502" height="164" alt="Screenshot 2025-07-11 214127" src="https://github.com/user-attachments/assets/db906aed-ddb8-469c-9c8a-f8a410f0e3e8" />

- Rain Sensor:
<img width="377" height="104" alt="Screenshot 2025-07-11 214152" src="https://github.com/user-attachments/assets/63667178-afdb-4779-87d5-d6a6a7ff659f" />

- LCD:
<img width="376" height="103" alt="Screenshot 2025-07-11 214208" src="https://github.com/user-attachments/assets/de845428-9d02-4175-9782-4aeaaeedfb90" />

- Exiting the menu:
<img width="305" height="45" alt="Screenshot 2025-07-11 214224" src="https://github.com/user-attachments/assets/1a6f7e25-fd5c-4611-b66e-1aae93aedb3e" />




