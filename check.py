try:
    import Adafruit_DHT
    print("✅ Adafruit_DHT imported successfully")
except ImportError as e:
    print("❌ Adafruit_DHT failed:", e)

try:
    import RPi.GPIO as GPIO
    print("✅ RPi.GPIO imported successfully")
except ImportError as e:
    print("❌ RPi.GPIO failed:", e)

try:
    import smbus2
    print("✅ smbus2 imported successfully")
except ImportError as e:
    print("❌ smbus2 failed:", e)

try:
    from RPLCD.i2c import CharLCD
    print("✅ RPLCD (LCD library) imported successfully")
except ImportError as e:
    print("❌ RPLCD failed:", e)

try:
    import board
    import busio
    import adafruit_bmp280
    print("✅ adafruit_bmp280 and I2C dependencies imported successfully")
except ImportError as e:
    print("❌ adafruit_bmp280 or I2C dependencies failed:", e)
