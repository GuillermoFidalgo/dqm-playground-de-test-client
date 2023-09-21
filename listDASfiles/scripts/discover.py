import requests

DEVLOP_API_TOKEN= "871450223ff7d809acdf6ffe8d11ef4a18a724c6"
MLP_DEVELOP_URL = "https://ml4dqm-playground-develop.web.cern.ch"

# Manually do the request for now
r = requests.get(
    f"{MLP_DEVELOP_URL}/api/histogram_data_files/discover/",
    headers={"Content-Type": "application/json", "Authorization": f"Token {DEVLOP_API_TOKEN}"},
)
