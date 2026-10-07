"""Thin HTTP client wrapper around the Met Museum API with logging."""

from typing import Any, Dict, Optional

import requests

from config import BASE_URL, BASE_URL_V1_1, REQUEST_TIMEOUT
from utils.logger import get_logger

logger = get_logger(__name__)


class MetMuseumClient:
    """Client for the Metropolitan Museum of Art Collection API."""

    def __init__(self, base_url: str = BASE_URL) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        base_url: Optional[str] = None,
    ) -> requests.Response:
        url = f"{(base_url or self.base_url).rstrip('/')}/{path.lstrip('/')}"
        logger.info("HTTP %s %s params=%s", method, url, params)
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as exc:
            logger.error("Request to %s failed: %s", url, exc)
            raise

        logger.info(
            "Response %s %s (%d bytes)",
            response.status_code,
            url,
            len(response.content),
        )
        if not response.ok:
            logger.warning(
                "Non-OK response body (truncated): %s", response.text[:500]
            )
        return response

    def _get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        base_url: Optional[str] = None,
    ) -> requests.Response:
        return self._request("GET", path, params=params, base_url=base_url)

    # -------- endpoints --------
    def get_object(self, object_id: int) -> requests.Response:
        return self._get(f"objects/{object_id}")

    def get_objects(
        self,
        metadata_date: Optional[str] = None,
        department_ids: Optional[str] = None,
    ) -> requests.Response:
        params: Dict[str, Any] = {}
        if metadata_date:
            params["metadataDate"] = metadata_date
        if department_ids:
            params["departmentIds"] = department_ids
        return self._get("objects", params=params or None)

    def search(self, **params: Any) -> requests.Response:
        return self._get("search", params=params or None)

    def search_v1_1(self, **params: Any) -> requests.Response:
        return self._get("search", params=params or None, base_url=BASE_URL_V1_1)

    def get_departments(self) -> requests.Response:
        return self._get("departments")

    # -------- lifecycle --------
    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> "MetMuseumClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()
