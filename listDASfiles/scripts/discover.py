import requests

#DEVELOP_API_TOKEN= "871450223ff7d809acdf6ffe8d11ef4a18a724c6"
DEVELOP_API_TOKEN= "5ebc661c6358fb9b1ad4cb064f98d86a1910240e"
MLP_DEVELOP_URL = "https://ml4dqm-playground-develop.web.cern.ch"

# Manually do the request for now
r = requests.get(
    f"{MLP_DEVELOP_URL}/api/histogram_data_files/discover/",
    headers={"Content-Type": "application/json", "Authorization": f"Token {DEVELOP_API_TOKEN}"},
)
