"""Define constants for the Growatt Server component."""
from homeassistant.const import Platform

CONF_PLANT_ID = "plant_id"

DEFAULT_PLANT_ID = "0"

DEFAULT_NAME = "Growatt fixed"

SERVER_URLS = [
    "https://server-api.growatt.com/",
    "https://server-us.growatt.com/",
    "http://server.smten.com/",
    "https://server.growatt.com/",
]

DEPRECATED_URLS = [
]

DEFAULT_URL = SERVER_URLS[0]

DOMAIN = "growatt_server_fixed"

PLATFORMS = [Platform.SENSOR]

LOGIN_INVALID_AUTH_CODE = "502"
