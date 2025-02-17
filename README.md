# ArcheanVision API

A **Python wrapper** for the [ArcheanVision](https://archeanvision.com/) API.  
This project allows you to retrieve information on active/inactive markets, real-time or historical signals, and much more — all secured via a **Bearer Token**.

---

## Table of Contents

1. [Key Features](#key-features)  
2. [Installation](#installation)  
   - [From PyPI](#from-pypi)  
   - [Manual Installation](#manual-installation)  
3. [Configuration](#configuration)  
4. [Usage](#usage)  
5. [Code Example](#code-example)  
6. [Contributing](#contributing)  
7. [License](#license)

---

## Key Features

- **Fetch** active and inactive markets.  
- **Access** historical or real-time signals (via SSE).  
- **Retrieve** market data (historical and real-time).  
- **Easy Integration** through an object-oriented interface.

---

## Installation

### From PyPI

```bash
pip install archeanvision-api

    Requirement: Python 3.6 or later.

Manual Installation

    Clone or download this repository:

git clone https://github.com/Archean-Vision/archeanvision-api.git

Navigate into the folder:

cd archeanvision-api

Install dependencies:

pip install -r requirements.txt

(Optional) Install in editable mode:

    pip install -e .

Configuration
Obtain a Bearer Token

    Go to your ArcheanVision profile.
    Create or retrieve your API key (a token typically starting with pypi-... or another alphanumeric string).
    Keep this token in a safe place (you will need it as your Bearer Token).

Usage

Once you have your API key, you can call the protected endpoints of the ArcheanVision API as follows:

from archeanvision import ArcheanVisionAPI

# Replace "YOUR_API_KEY" with your Bearer token
api = ArcheanVisionAPI(api_key="YOUR_API_KEY")

# Fetch the list of active markets
active_markets = api.get_active_markets()
print("Active Markets:", active_markets)

# Retrieve market info for BTC (if present)
if "BTC" in active_markets:
    market_info = api.get_market_info("BTC")
    print("Market Info for BTC:", market_info)

Code Example

"""
Full example of how to use the ArcheanVision API library.
Save this file as 'example.py' and run it with:
    python example.py
"""

from archeanvision import ArcheanVisionAPI

def main():
    # Initialize the API with your Bearer Token
    api_key = "YOUR_API_KEY"  # Replace with your actual key
    api = ArcheanVisionAPI(api_key)

    # 1. Fetch active markets
    active = api.get_active_markets()
    print("Active Markets:", active)

    # 2. Fetch inactive markets
    inactive = api.get_inactive_markets()
    print("Inactive Markets:", inactive)

    # 3. Retrieve info for a specific market (e.g., BTC)
    if "BTC" in active:
        btc_info = api.get_market_info("BTC")
        print("BTC Info:", btc_info)

    # 4. Retrieve all historical signals
    all_signals = api.get_all_signals()
    print("All Signals (preview):", all_signals[:5])

    # 5. Retrieve historical signals for a specific market (e.g., BTC)
    btc_signals = api.get_market_signals("BTC")
    print("BTC Signals (preview):", btc_signals[:5])

    # 6. Retrieve the last 24h of data (1,440 data points) for a market
    btc_data = api.get_market_data("BTC")
    print("BTC Data (preview):", btc_data[:5])

if __name__ == "__main__":
    main()

Contributing

    Fork the repository.
    Create a branch for your feature or fix:

git checkout -b feature/my-feature

Commit your changes:

git commit -m "Add feature X or fix Y"

Push the branch:

    git push origin feature/my-feature

    Open a Pull Request on GitHub.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Thanks for using ArcheanVision API!
If you have any questions or need assistance, please contact us at support@archeanvision.com.

Last update: January 2025
