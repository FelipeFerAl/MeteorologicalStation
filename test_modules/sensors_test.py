import time
import sys
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

def test_dht11():
    # Initial the dht device, with data pin connected to:
    dhtDevice = adafruit_dht.DHT11(board.D23)
    #Inicializa LCD
    lcd = CharLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=16, 
                  dotsize=8, charmap='A00',auto_linebreaks=True)
    
    try:
        while True:
            try:
                temperature_c = dhtDevice.temperature
                humidity = dhtDevice.humidity
                print(f"Temp: {temperature_c:.1f} C    Humidity: {humidity}% ")
                #muestra en pantalla LCD
                lcd.clear()
                lcd.write_string(f"T:{temperature_c:.1f}C H:{humidity}%")
                lcd.crlf()

            except RuntimeError as error:
                print(error.args[0])
            time.sleep(5.0)

    except KeyboardInterrupt:
        print("\n[✔] Lectura de DHT11 interrumpida por el usuario.")


def test_bmp280():
    try:
        import board
        import adafruit_bmp280

        # Initialize I2C bus
        i2c = board.I2C()

        # Create BMP280 object
        bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,address=0x77)

        while True:
            temp = bmp.temperature
            pressure = bmp.pressure
            print(f"Temp: {temp:.1f} C    Pressure: {pressure:.1f}hPa")
            time.sleep(5.0)

    except KeyboardInterrupt:
        print("\n[✔] Lectura de BMP280 interrumpida por el usuario.")


def test_rain_sensor():
    try:
        import RPi.GPIO as GPIO

        RAIN_PIN = 24
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
        lcd.write_string("LCD Funcionando")
        lcd.crlf()
        lcd.write_string("Test exitoso :D")
        print("\n✅ LCD OK - LCD FUNCIONANDO.\n")
        time.sleep(3)
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
