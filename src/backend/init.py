# the master initialization operation
import importlib
import os

import eel

from src.backend import sql
from src.backend import links

def _application_initialize():
    # first we expose the functions we want to expose to eel
    eel.expose(links.github)

    # we run basic application initialization operations
    # most plugins will need these operations to be successful to even
    # operate
    sql._setup_http_cache()

    # next we run the initialization operations on all the plugins
    plugins_directory = os.path.abspath("../src/plugins")
    for plugin_folder in os.listdir(plugins_directory):
        print(plugin_folder)