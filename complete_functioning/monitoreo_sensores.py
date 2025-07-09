import time
import board
import adafruit_dht
import adafruit_bmp280
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

def run_all_sensors():
    try:
        # Inicializa sensores
        dhtDevice = adafruit_dht.DHT11(board.D23)
        i2c = board.I2C()
        bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)

        # Sensor de lluvia
        RAIN_PIN = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RAIN_PIN, GPIO.IN)

        # LCD
        lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
                      cols=16, rows=2, dotsize=8,
                      charmap='A00', auto_linebreaks=True)

        print("\n[✔] Monitoreo activo. Presiona Ctrl+C para detener.\n")

        while True:
            try:
                # DHT11
                temp_dht = dhtDevice.temperature
                humedad = dhtDevice.humidity

                # BMP280
                temp_bmp = bmp.temperature
                presion = bmp.pressure

                # Sensor de lluvia
                lluvia = "SI" if GPIO.input(RAIN_PIN) == 0 else "NO"

                # Consola
                print(f"DHT11  → T:{temp_dht:.1f}C  H:{humedad}%")
                print(f"BMP280 → T:{temp_bmp:.1f}C  P:{int(presion)}hPa")
                print(f"Lluvia → R:{lluvia}")
                print("-" * 35)

                # LCD rotativa
                lcd.clear()
                lcd.cursor_pos=(0,0)
                lcd.write_string(f"T:{temp_bmp:.1f}  P:{int(presion)}hPa")
                lcd.cursor_pos=(1,0)
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

