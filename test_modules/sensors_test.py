import time
import sys

def test_dht11():
    try:
        import Adafruit_DHT
        DHT_SENSOR = Adafruit_DHT.DHT11
        DHT_PIN = 4

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f"\n✅ DHT11 - Temperatura: {temperature:.1f}°C | Humedad: {humidity:.1f}%\n")
        else:
            print("\n⚠️ No se pudo leer el sensor DHT11. Verifique la conexión.\n")
    except RuntimeError as e:
        print(f"\n❌ Error en plataforma DHT11: {e}\n")
    except ImportError as e:
        print(f"\n❌ Módulo Adafruit_DHT no encontrado: {e}\n")
    except Exception as e:
        print(f"\n❌ Error inesperado con DHT11: {e}\n")


def test_bmp280():
    try:
        import board
        import busio
        import adafruit_bmp280

        i2c = busio.I2C(board.SCL, board.SDA)
        bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

        temp = bmp.temperature
        pressure = bmp.pressure

        print(f"\n✅ BMP280 - Temp: {temp:.1f}°C | Presión: {pressure:.1f} hPa\n")
    except Exception as e:
        print(f"\n❌ Error con BMP280: {e}\n")


def test_rain_sensor():
    try:
        import RPi.GPIO as GPIO

        RAIN_PIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RAIN_PIN, GPIO.IN)

        state = GPIO.input(RAIN_PIN)
        status = "Lluvia detectada" if state == 0 else "Sin lluvia"
        print(f"\n✅ Sensor de lluvia: {status}\n")
        time.sleep(2)
        GPIO.cleanup()
    except Exception as e:
        print(f"\n❌ Error con sensor de lluvia: {e}\n")


def test_lcd():
    try:
        from RPLCD.i2c import CharLCD

        lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
                      cols=16, rows=2, dotsize=8,
                      charmap='A00', auto_linebreaks=True)

        lcd.clear()
        lcd.write_string("LCD funcionando")
        lcd.crlf()
        lcd.write_string("Test exitoso!")
        print("\n✅ LCD OK - Mensaje mostrado en pantalla.\n")
        time.sleep(3)
        lcd.clear()
    except Exception as e:
        print(f"\n❌ Error con LCD: {e}\n")


def main_menu():
    while True:
        print("=== Menú de Pruebas de Sensores ===")
        print("1. Probar DHT11 (Temp y Humedad)")
        print("2. Probar BMP280 (Temp y Presión)")
        print("3. Probar sensor de lluvia")
        print("4. Probar pantalla LCD")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == '1':
            test_dht11()
        elif choice == '2':
            test_bmp280()
        elif choice == '3':
            test_rain_sensor()
        elif choice == '4':
            test_lcd()
        elif choice == '5':
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("Opción inválida. Intente de nuevo.\n")

        input("Presione Enter para volver al menú...\n")


if __name__ == "__main__":
    main_menu()
