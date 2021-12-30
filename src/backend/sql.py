import sqlite3
import os
from typing import Callable, Any


HTTP_CACHE_ABS_PATH = os.path.abspath("../src/settings/http.cache") # relative paths are weird on some systems sometimes
HTTP_CACHE = sqlite3.connect(HTTP_CACHE_ABS_PATH)
HTTP_CACHE_CURSOR = HTTP_CACHE.cursor()

# init operations

def _setup_http_cache():
    # we want a seperate cursor for setup operations
    cursor = HTTP_CACHE.cursor()
    query = """CREATE TABLE IF NOT EXISTS requestkeys(
        key STRING,
        value STRING
    )"""
    cursor.execute(query)
    cursor.close()

# general operations

def execute_query(cursor: sqlite3.Cursor, query: str, args: tuple, operation_callable: Callable = "fetchone") -> Any:
    cursor.execute(query, args)
    r_method = getattr(HTTP_CACHE_CURSOR, operation_callable)
    return r_method()