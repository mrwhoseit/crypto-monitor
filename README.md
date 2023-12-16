# Cryptocurrency Price Ticker with Raspberry Pi and LCD

## Overview

This Python script enables a Raspberry Pi to display real-time cryptocurrency prices on an LCD screen. It utilizes the RPi LCD library for the display and fetches cryptocurrency prices from the Coinbase API.

## Components Used

- **RPi LCD Library:** A Python library for interfacing with LCD screens on Raspberry Pi.
- **Coinbase API:** Provides real-time cryptocurrency prices.
- **Button:** Connected to a GPIO pin for cycling through different cryptocurrencies.

## How It Works

1. **Import Necessary Libraries:**
   - `rpi_lcd` for LCD functionality.
   - `requests` for making API requests.
   - `threading` for running background tasks.
   - `RPi.GPIO` for handling GPIO operations.

2. **Define Constants:**
   - `BUTTON_PIN` is set to the GPIO pin number for the button.
   - `cryptos` is a list of cryptocurrencies to cycle through.
   - `price_update_interval` is the update interval for cryptocurrency prices.

3. **Define Functions:**
   - `get_crypto_price(crypto)`: Fetches cryptocurrency price from the Coinbase API.
   - `display_on_lcd(lcd, crypto, price)`: Displays cryptocurrency price on the LCD.
   - `update_price()`: Runs in the background, continuously fetching and updating cryptocurrency prices.
   - `button_callback(channel)`: Callback function for button press.

4. **Set Up Hardware:**
   - LCD is initialized using the `rpi_lcd` library.
   - GPIO is set up for the button.

5. **Initial Display and Background Thread:**
   - Initial cryptocurrency price is displayed on the LCD.
   - Background thread is started for continuous price updates.

6. **Main Loop:**
   - The main loop handles LCD updates for the selected cryptocurrency.
   - The script can be interrupted using a KeyboardInterrupt.

## How to Use

1. **Clone Repository:**
   - Clone the repository to your Raspberry Pi.
   - Navigate to the repository folder.

2. **Install Dependencies:**
   - Install the required Python libraries: `rpi_lcd` and `requests`.

3. **Run the Script:**
   - Execute the Python script.

4. **Interact with the LCD:**
   - The LCD will display the current price of the selected cryptocurrency.
   - Press the button to cycle through different cryptocurrencies.

5. **Exit the Program:**
   - To stop the script, use a KeyboardInterrupt (Ctrl+C).

## Configuration
- Adjust `BUTTON_PIN` in the code to match your button's GPIO pin.

## Cryptocurrencies Supported
- BTC
- ETH
- XRP
- LTC
- ADA
- DOT
- BCH
- LINK
- XLM
- DOGE
## Acknowledgments
- Thanks to [Coinbase API](https://developers.coinbase.com/api/v2) for providing real time data.
## Author
Syler J.
