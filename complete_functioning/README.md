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
* Continuously loops until the user presses `Ctrl+C`.

---

#### **Key Components**

| Sensor/Device | Description                       | Connection            |
| ------------- | --------------------------------- | --------------------- |
| `DHT11`       | Temperature and humidity via GPIO | `board.D23` (GPIO 23) |
| `BMP280`      | Pressure and temperature via I2C  | Address `0x77`        |
| `YL-38`       | Rain sensor (digital read)        | GPIO `24`             |
| `CharLCD`     | I2C 16x2 LCD display              | I2C Address `0x27`    |

---

#### 🛠**Flow Description**

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
    temp_dht = dhtDevice.temperature
    humedad = dhtDevice.humidity
    temp_bmp = bmp.temperature
    presion = bmp.pressure
    lluvia = "SI" if GPIO.input(RAIN_PIN) == 0 else "NO"
```

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


