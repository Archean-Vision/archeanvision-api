import requests

class ArcheanVisionAPI:
	"""
	Python wrapper for the Archean Vision API (version utilisant un Bearer Token).
	"""

	BASE_URL = "https://archeanvision.com/api/"

	def __init__(self, api_key: str):
		"""
		Initialise le client API avec un Bearer Token.

		:param api_key: Votre clé API Archean Vision
		"""
		self.api_key = api_key
		self.session = requests.Session()
		
		# Ajout de l'en-tête Authorization à chaque requête
		self.session.headers.update({
			"Authorization": f"Bearer {self.api_key}"
		})

	def get_active_markets(self):
		"""
		Récupère la liste des marchés actifs et analysés.

		:return: Liste des marchés actifs (format JSON).
		"""
		endpoint = f"{self.BASE_URL}signals/available"
		response = self.session.get(endpoint)
		response.raise_for_status()
		return response.json()

	def get_inactive_markets(self):
		"""
		Récupère la liste des marchés inactifs (auparavant analysés).

		:return: Liste des marchés inactifs (format JSON).
		"""
		endpoint = f"{self.BASE_URL}signals/inactive"
		response = self.session.get(endpoint)
		response.raise_for_status()
		return response.json()

	def get_market_info(self, market: str):
		"""
		Récupère des informations détaillées sur un marché spécifique.

		:param market: Identifiant du marché (ex: "BTC").
		:return: Informations du marché (format JSON).
		"""
		endpoint = f"{self.BASE_URL}signals/{market}/info"
		response = self.session.get(endpoint)
		response.raise_for_status()
		return response.json()

	def get_all_signals(self):
		"""
		Récupère tous les signaux historiques de tous les marchés.

		:return: Liste de tous les signaux (format JSON).
		"""
		endpoint = f"{self.BASE_URL}signals/all/signals"
		response = self.session.get(endpoint)
		response.raise_for_status()
		return response.json()

	def get_market_signals(self, market: str):
		"""
		Récupère les signaux historiques pour un marché spécifique.

		:param market: Identifiant du marché (actif ou inactif).
		:return: Liste des signaux pour ce marché (format JSON).
		"""
		endpoint = f"{self.BASE_URL}signals/{market}/signals"
		response = self.session.get(endpoint)
		response.raise_for_status()
		return response.json()

	def get_realtime_signals(self):
		"""
		Récupère les signaux en temps réel via Server-Sent Events (SSE).

		:yield: Les événements SSE en temps réel (format brut).
		"""
		endpoint = f"{self.BASE_URL}signals/realtime/signals"
		with self.session.get(endpoint, stream=True) as response:
			response.raise_for_status()
			for line in response.iter_lines():
				if line:
					yield line.decode("utf-8")

	def get_realtime_data(self):
		"""
		Récupère les données de marché en temps réel via Server-Sent Events (SSE).

		:yield: Les événements SSE en temps réel (format brut).
		"""
		endpoint = f"{self.BASE_URL}signals/realtime/data"
		with self.session.get(endpoint, stream=True) as response:
			response.raise_for_status()
			for line in response.iter_lines():
				if line:
					yield line.decode("utf-8")

	def get_market_data(self, market: str):
		"""
		Récupère les 1440 dernières données (historique 24h) pour un marché spécifique.

		:param market: Identifiant du marché (ex: "BTC").
		:return: Liste des données (format JSON).
		"""
		endpoint = f"{self.BASE_URL}signals/{market}/data"
		response = self.session.get(endpoint)
		response.raise_for_status()
		return response.json()


if __name__ == "__main__":
	# Exemple d’utilisation :
	# Remplacez 'YOUR_API_KEY' par la clé générée sur votre profil Archean Vision.
	api = ArcheanVisionAPI(api_key="*****")
	
	# Récupération des marchés actifs
	active_markets = api.get_active_markets()
	print("Active Markets:", active_markets)
	
	# Récupération des infos pour le marché BTC (si présent dans la liste)
	if "BTC" in active_markets:
		market_info = api.get_market_info("BTC")
		print("Market Info for BTC:", market_info)