import logging
import time

import requests


logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url, timeout=5, retries=1):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        attempts = self.retries + 1

        for attempt in range(1, attempts + 1):
            started_at = time.perf_counter()

            try:
                logger.info("%s %s", method, endpoint)
                response = self.session.request(
                    method,
                    url,
                    timeout=self.timeout,
                    **kwargs,
                )
                elapsed_ms = round((time.perf_counter() - started_at) * 1000)
                logger.info(
                    "%s %s -> %s in %sms",
                    method,
                    endpoint,
                    response.status_code,
                    elapsed_ms,
                )
                return response
            except requests.RequestException as error:
                if attempt == attempts:
                    logger.error("%s %s failed: %s", method, endpoint, error)
                    raise

                logger.warning(
                    "%s %s failed on attempt %s/%s: %s",
                    method,
                    endpoint,
                    attempt,
                    attempts,
                    error,
                )

    def get_users(self):
        return self._request("GET", "/users")

    def get_user(self, user_id):
        return self._request("GET", f"/users/{user_id}")

    def get_posts(self):
        return self._request("GET", "/posts")

    def create_post(self, payload):
        return self._request("POST", "/posts", json=payload)

    def update_post(self, post_id, payload):
        return self._request("PUT", f"/posts/{post_id}", json=payload)

    def patch_post(self, post_id, payload):
        return self._request("PATCH", f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self._request("DELETE", f"/posts/{post_id}")

    def get_comments_by_post_id(self, post_id):
        return self._request("GET", f"/posts/{post_id}/comments")
