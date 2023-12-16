from rpi_lcd import LCD
import requests
import threading
import time
import RPi.GPIO as GPIO

# Define GPIO pin for the button
BUTTON_PIN = 17  # Change this to your actual GPIO pin

# List of cryptocurrencies to cycle through
cryptos = ['BTC', 'ETH', 'XRP', 'LTC', 'ADA', 'DOT', 'BCH', 'LINK', 'XLM', 'DOGE']
current_crypto_index = 0

# Variable to track the current price
current_price = 0
price_update_interval = 10  # Update interval in seconds

# Function to get cryptocurrency price from Coinbase API
def get_crypto_price(crypto):
    url = f'https://api.coinbase.com/v2/prices/{crypto}-USD/spot'
    response = requests.get(url)
    data = response.json()
    return data['data']['amount']

# Function to display cryptocurrency price on LCD
def display_on_lcd(lcd, crypto, price):
    lcd.text(f"{crypto} Price:", 1)
    lcd.text(f"${price}", 2)

# Function to continuously fetch and update the price in the background
def update_price():
    global current_price
    while True:
        try:
            crypto = cryptos[current_crypto_index]
            price = get_crypto_price(crypto)
            current_price = price
            time.sleep(price_update_interval)
        except Exception as e:
            print(f"Error fetching price: {e}")
            time.sleep(2)  # Wait for two seconds before retrying if an error occurs

# Callback function for button press
def button_callback(channel):
    global current_crypto_index
    current_crypto_index = (current_crypto_index + 1) % len(cryptos)
    print(current_crypto_index)

# Set up LCD with specified GPIO ports for SDA and SCL
lcd = LCD()

# Set up GPIO for button input
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)

# Fetch initial BTC price before entering the main loop
initial_btc_price = get_crypto_price('BTC')
display_on_lcd(lcd, 'BTC', initial_btc_price)

# Start the background thread for continuous price updates
price_thread = threading.Thread(target=update_price)
price_thread.start()

# Main loop to handle LCD updates
try:
    while True:
        crypto = cryptos[current_crypto_index]
        display_on_lcd(lcd, crypto, current_price)
        time.sleep(5)  # Adjust the sleep duration as needed

except KeyboardInterrupt:
    GPIO.cleanup()
