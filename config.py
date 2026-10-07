"""Configuration constants for the Met Museum API tests."""

BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"
BASE_URL_V1_1 = "https://collectionapi.metmuseum.org/public/collection/v1.1"

REQUEST_TIMEOUT = 20

# Well-documented object from the official docs
SMOKE_OBJECT_ID = 45734
SMOKE_OBJECT_TITLE = "Quail and Millet"
SMOKE_OBJECT_ARTIST = "Kiyohara Yukinobu"
SMOKE_OBJECT_DEPARTMENT = "Asian Art"

VALID_OBJECT_ID = SMOKE_OBJECT_ID
INVALID_OBJECT_ID = 999999999

DEFAULT_PAGE_LIMIT = 100
MAX_PAGE_LIMIT = 500
MAX_REACHABLE_RESULTS = 10_000

# Department ids (note: no id=2, no id=20)
KNOWN_DEPARTMENT_IDS = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]
