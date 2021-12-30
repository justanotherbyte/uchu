# MangaDex related HTTP operations
import requests


SESSION = requests.Session()
BASE = "https://api.mangadex.org"

def _request(method: str, endpoint: str, **kwargs) -> requests.Response:
    url = BASE + endpoint
    response = SESSION.request(method, url, **kwargs)
    return response

def _create_user_account():
    response = _request("POST", "/account/create")
    print(response.json())
