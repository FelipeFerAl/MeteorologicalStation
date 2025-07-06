import sys

def check_module(name):
    try:
        __import__(name)
        print(f"[✓] {name} is installed")
        return True
    except ImportError:
        print(f"[✗] {name} is NOT installed")
        return False

print("🔍 Checking Adafruit DHT dependencies...\n")

all_ok = True
modules = ['adafruit_dht', 'board', 'digitalio']

for module in modules:
    if not check_module(module):
        all_ok = False

# Additional check: is this running on a Raspberry Pi (via Blinka)?
try:
    import adafruit_platformdetect
    from adafruit_platformdetect import Detector
    d = Detector()
    print(f"\n🧠 Platform detected: {d.board.id}")
except Exception:
    print("\n[!] Could not detect platform. Blinka may not be installed correctly.")
    all_ok = False

# GPIO functionality check
try:
    import board
    import digitalio
    pin = digitalio.DigitalInOut(board.D4)
    pin.direction = digitalio.Direction.INPUT
    print("[✓] GPIO access via Blinka is working")
    pin.deinit()
except Exception as e:
    print(f"[✗] GPIO test failed: {e}")
    all_ok = False

print("\n✅ All dependencies OK!" if all_ok else "\n❌ One or more dependencies are missing or broken.")
