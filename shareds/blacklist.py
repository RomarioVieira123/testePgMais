import requests
import json

from core.settings import WS_URL


class BlackList:

    def tochange(self):
        try:
            response = requests.get(WS_URL)
            if response.status_code != 200:
                return None

            blacklist = json.loads(response.text)
            return blacklist

        except ConnectionError:
            return None
