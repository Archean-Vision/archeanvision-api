# archeanvision/api.py

import requests

class ArcheanVisionAPI:
    """
    Python wrapper for the Archean Vision API.
    """

    BASE_URL = "https://archeanvision.com/api/"

    def __init__(self, username, password):
        """
        Initialize the API client and authenticate.

        :param username: API username.
        :param password: API password.
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        self._authenticate()

    def _authenticate(self):
        """
        Authenticate and store the session cookie.
        """
        endpoint = f"{self.BASE_URL}auth/login"
        payload = {"login": self.username, "password": self.password}

        response = self.session.post(endpoint, json=payload)
        if response.status_code == 200:
            print("Authentication successful.")
        else:
            raise Exception(f"Authentication failed: {response.json()} ")

    def get_active_markets(self):
        """
        Retrieve a list of active and analyzed markets.

        :return: List of active markets.
        """
        endpoint = f"{self.BASE_URL}signals/available"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

    def get_inactive_markets(self):
        """
        Retrieve a list of inactive markets.

        :return: List of inactive markets.
        """
        endpoint = f"{self.BASE_URL}signals/inactive"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

    def get_market_info(self, market):
        """
        Retrieve detailed information about a specific market.

        :param market: Market identifier.
        :return: Market information.
        """
        endpoint = f"{self.BASE_URL}signals/{market}/info"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

    def get_all_signals(self):
        """
        Retrieve all historical signals from all markets.

        :return: List of signals.
        """
        endpoint = f"{self.BASE_URL}signals/all/signals"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

    def get_market_signals(self, market):
        """
        Retrieve historical signals for a specific market.

        :param market: Market identifier.
        :return: List of signals for the specified market.
        """
        endpoint = f"{self.BASE_URL}signals/{market}/signals"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

    def get_realtime_signals(self):
        """
        Retrieve live signals using Server-Sent Events (SSE).

        :return: Generator for live signals.
        """
        endpoint = f"{self.BASE_URL}signals/realtime/signals"
        with self.session.get(endpoint, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    yield line.decode("utf-8")

    def get_realtime_data(self):
        """
        Retrieve live market data using Server-Sent Events (SSE).

        :return: Generator for live data.
        """
        endpoint = f"{self.BASE_URL}signals/realtime/data"
        with self.session.get(endpoint, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    yield line.decode("utf-8")

    def get_market_data(self, market):
        """
        Retrieve historical data for a specific market.

        :param market: Market identifier.
        :return: List of data points for the specified market.
        """
        endpoint = f"{self.BASE_URL}signals/{market}/data"
        response = self.session.get(endpoint)
        response.raise_for_status()
        return response.json()

# Example Usage
if __name__ == "__main__":
    api = ArcheanVisionAPI("***", "***********")
    active_markets = api.get_active_markets()
    print("Active Markets:", active_markets)

    market_info = api.get_market_info("BTC")
    print("Market Info for BTC:", market_info)