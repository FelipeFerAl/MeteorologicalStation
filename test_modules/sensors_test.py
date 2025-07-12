import json
import os
import time
import sys
from sensors_modules import dhtDevice, bmp, RAIN_PIN, lcd
from sensors_modules import dht_temperature, dht_humidity

def test_dht11():
    try:
        path="/tmp/sensor_data.json"
        if not os.path.exists(path):
            print("No hay archivo con datos\n")
            return
            
        with open(path, "r") as f:
            data = json.load(f)
            temp = data.get("dht_temperature")
            hum = data.get("dht_humidity")
    finally: 
        try:
            while True:
                if temp is not None and hum is not None:
                    print(f"✅ DHT11 OK - Temp: {temp}, Hum: {hum}")
                else:
                    print("⚠️  DHT11 data not available yet.")

                time.sleep(5)

        except KeyboardInterrupt:
            print("\n[✔] Lectura de DHT11 interrumpida por el usuario.")


def test_bmp280():
    try:
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
        lluvia = "SI" if state == 0 else "NO"
        print(f"\n✅ Estado: R: {lluvia}\n")
        time.sleep(2)
        GPIO.cleanup()
       
        time.sleep(1)
    except Exception as e:
        print(f"\n❌ Error con sensor de lluvia: {e}\n")


def test_lcd():
    try:
        if lcd != None:
            print("\n✅ LCD OK - LCD FUNCIONANDO.\n")
        else:
            print("\nError con LCD.\n")
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
