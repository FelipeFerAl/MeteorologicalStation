import time
import sys
import os
import RPi.GPIO as GPIO
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_modules')))
import sensors_modules

def run_all_sensors():
    try:
        # ✅ Initialize all sensors once
        sensors_modules.init_all_sensors()

        # ✅ Access the initialized objects
        dhtDevice = sensors_modules.dhtDevice
        bmp = sensors_modules.bmp
        lcd = sensors_modules.lcd
        RAIN_PIN = sensors_modules.RAIN_PIN

        while True:
            try:
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

                # Display on LCD
                lcd.clear()
                lcd.cursor_pos = (0, 0)
                lcd.write_string(f"T:{temp_bmp:.1f}  P:{int(presion)}hPa")
                lcd.cursor_pos = (1, 0)
                lcd.write_string(f"R:{lluvia:>2}  H:{humedad}%")

                time.sleep(5)

            except RuntimeError as e:
                print(f"[!] Error lectura DHT11: {e}")
                time.sleep(2)

    except KeyboardInterrupt:
        print("\n[✔] Monitoreo detenido por el usuario.")
        lcd.clear()
        lcd.write_string("Monitoreo stop")
        time.sleep(2)
        lcd.clear()
        GPIO.cleanup()


if __name__ == "__main__":
    run_all_sensors()
