#!/usr/bin/env python3

import requests
import redis
import time
from functools import wraps
from typing import Callable


def get_page(url: str) -> str:
    cache = redis.Redis()
    count_key = f"count:{url}"
    page_key = f"page:{url}"

    # Check if the page is already cached
    cached_page = cache.get(page_key)
    if cached_page is not None:
        return cached_page.decode()

    # Increment the count of URL accesses
    cache.incr(count_key)

    # Fetch the page content
    response = requests.get(url)
    page_content = response.text

    # Cache the page content with an expiration time of 10 seconds
    cache.setex(page_key, 10, page_content)

    return page_content
