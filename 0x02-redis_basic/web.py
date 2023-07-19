#!/usr/bin/env python3
import requests
import time

CACHE_DURATION = 10  # Cache duration in seconds
CACHE = {}  # Dictionary to store cached results


def cache_result(func):
    def wrapper(url):
        if url in CACHE and time.time() - CACHE[url]['timestamp'] < CACHE_DURATION:
            CACHE[url]['count'] += 1  # Increment the access count
            return CACHE[url]['content']

        content = func(url)  # Call the decorated function

        CACHE[url] = {
            'content': content,
            'timestamp': time.time(),
            'count': 1
        }

        return content

    return wrapper


@cache_result
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
