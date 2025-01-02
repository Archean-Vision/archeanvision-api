# ArcheanVision API

Python wrapper for the Archean Vision API.

## Installation

```bash
pip install archeanvision-api
```
## Usage

from archeanvision import ArcheanVisionAPI

api = ArcheanVisionAPI("username", "password")
active_markets = api.get_active_markets()
print("Active Markets:", active_markets)