## ArcheanVision API

Un wrapper Python pour consommer l’API Archean Vision.
Ce projet permet de récupérer des informations sur les marchés actifs, les signaux en temps réel/historiques, et bien plus encore — le tout via un Bearer Token.
Sommaire

    Fonctionnalités Principales
    Installation
    Configuration
    Utilisation
    Exemple de Code
    Contribuer
    Licence

## Fonctionnalités Principales

    Récupération de la liste des marchés actifs et inactifs.
    Accès aux signaux historiques ou en temps réel (SSE).
    Récupération de données de marché pour chaque actif (historique et temps réel).
    Facilité d’intégration grâce à une interface orientée objet.

## Installation
## Depuis PyPI

pip install archeanvision-api

    Assurez-vous d’avoir Python 3.6 ou une version ultérieure.

## Installation Manuelle

    Clonez ce dépôt ou téléchargez-le :

git clone https://github.com/Archean-Vision/archeanvision-api.git

Placez-vous dans le dossier :

cd archeanvision-api

## Installez les dépendances :

pip install -r requirements.txt

## (Optionnel) Installez-le en mode développement :

    pip install -e .

## Configuration
Obtenir une Clé API (Bearer Token)

    Rendez-vous sur votre profil Archean Vision.
    Créez ou récupérez votre clé API (un token commençant souvent par ...).
    Conservez-le précieusement (vous devrez l’utiliser comme Bearer Token).

## Utilisation

Une fois la clé API obtenue, vous pouvez l’utiliser pour appeler les endpoints protégés de l’API Archean Vision :

from archeanvision import ArcheanVisionAPI

# Remplacez "YOUR_API_KEY" par votre token Bearer
api = ArcheanVisionAPI(api_key="YOUR_API_KEY")

# Récupérer la liste des marchés actifs
active_markets = api.get_active_markets()
print("Active Markets:", active_markets)

# Récupérer les infos du marché BTC (si présent)
if "BTC" in active_markets:
    market_info = api.get_market_info("BTC")
    print("Market Info for BTC:", market_info)

## Exemple de Code

"""
Exemple complet d'utilisation de la librairie ArcheanVision API.
Sauvegardez ce fichier sous 'example.py' puis exécutez-le avec : 
    python example.py
"""

from archeanvision import ArcheanVisionAPI

def main():
    # Initialiser l'API avec votre Bearer Token
    api_key = "YOUR_API_KEY"  # Remplacez par votre clé
    api = ArcheanVisionAPI(api_key)

    # 1. Marchés actifs
    active = api.get_active_markets()
    print("Active Markets:", active)

    # 2. Marchés inactifs
    inactive = api.get_inactive_markets()
    print("Inactive Markets:", inactive)

    # 3. Infos d’un marché précis
    if "BTC" in active:
        btc_info = api.get_market_info("BTC")
        print("BTC Info:", btc_info)

    # 4. Signaux historiques globaux
    all_signals = api.get_all_signals()
    print("All Signals (preview):", all_signals[:5])

    # 5. Signaux historiques pour un marché
    btc_signals = api.get_market_signals("BTC")
    print("BTC Signals (preview):", btc_signals[:5])

    # 6. Données historiques (24h) d’un marché
    btc_data = api.get_market_data("BTC")
    print("BTC Data (preview):", btc_data[:5])

if __name__ == "__main__":
    main()

## Contribuer

    Forkez le dépôt.
    Créez une branche pour vos modifications : git checkout -b feature/ma-feature.
    Commitez vos modifications : git commit -m "Ajout de X ou correction de Y".
    Poussez la branche : git push origin feature/ma-feature.
    Ouvrez une Pull Request sur GitHub.

Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.

Merci d’utiliser ArcheanVision API !
Pour toute question ou assistance, contactez-nous à support@archeanvision.com.

Dernière mise à jour :jan 2025