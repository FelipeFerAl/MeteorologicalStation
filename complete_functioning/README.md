### `run_all_sensors()` – Full Sensor Monitoring Function

```python
def run_all_sensors():
```

This function continuously reads and displays data from all connected sensors and prints it both on the terminal and a 16x2 I2C LCD.

---

#### **Functionality Summary**

* Reads data from:

  * **DHT11**: Temperature and Humidity
  * **BMP280**: Barometric Pressure and Temperature
  * **YL-38**: Rain detection via digital GPIO
* Displays results on:

  * Terminal (for debugging)
  * I2C LCD (rotating data every 5 seconds)


---

#### **Flow Description**

```python
# Initialize all devices
dhtDevice = adafruit_dht.DHT11(board.D23)
i2c = board.I2C()
bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)
```

* Initializes all sensors using proper libraries.
* Sets up GPIO pin 24 for digital rain input.
* Sets up the LCD using I2C on default address `0x27`.

---

#### **Main Loop**

```python
while True: 
        # DHT11
         temp_dht = dhtDevice.temperature
         humedad = dhtDevice.humidity
         data = {
             "dht_temperature": temp_dht,
             "dht_humidity": humedad
         }
         with open("/tmp/sensor_data.json", "w") as f:
             json.dump(data, f)

         # BMP280
         temp_bmp = bmp.temperature
         presion = bmp.pressure

         # Rain Sensor
         lluvia = "SI" if GPIO.input(RAIN_PIN) == 0 else "NO"
```
Note: To avoid conflicts between the readings of the sensor DHT11 and the display of the parameters in console for the testing it was used the json library, that access to the data and allows to show it in the console. 

* Continuously reads:

  * DHT11 data: `temperature`, `humidity`
  * BMP280 data: `temperature`, `pressure`
  * Rain sensor: digital status (LOW = rain)

```python
# Display in terminal
print(f"DHT11  → T:{temp_dht:.1f}C  H:{humedad}%")
print(f"BMP280 → T:{temp_bmp:.1f}C  P:{int(presion)}hPa")
print(f"Lluvia → R:{lluvia}")
```

* Displays readable data in the console for monitoring.

```python
# Display in LCD
lcd.clear()
lcd.cursor_pos=(0,0)
lcd.write_string(f"T:{temp_bmp:.1f}  P:{int(presion)}hPa")
lcd.cursor_pos=(1,0)
lcd.write_string(f"R:{lluvia:>2}  H:{humedad}%")
```

* LCD shows rotating sensor values on two lines:

  * Line 1: Temperature and pressure
  * Line 2: Rain detection and humidity

---

#### **Graceful Exit**

```python
except KeyboardInterrupt:
    print("Monitoreo detenido por el usuario.")
    lcd.clear()
    lcd.write_string("Monitoreo stop")
    GPIO.cleanup()
```

* Handles `Ctrl+C` to safely stop the program and clear the LCD.
* Ensures GPIO resources are released properly.


