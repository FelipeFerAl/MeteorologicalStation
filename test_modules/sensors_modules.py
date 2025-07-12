import board
import adafruit_dht
import adafruit_bmp280
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD

# Shared sensor objects (not initialized immediately)
dhtDevice = None
i2c = board.I2C()
bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True)

# Shared data placeholders
dht_temperature = None
dht_humidity = None

RAIN_PIN = 24

def init_all_sensors():
    global dhtDevice, bmp, lcd

    # Initialize DHT11 (GPIO23)
    dhtDevice = adafruit_dht.DHT11(board.D23)
    
    # GPIO Rain sensor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RAIN_PIN, GPIO.IN)
