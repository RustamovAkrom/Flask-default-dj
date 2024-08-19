from flask import Flask

from string import ascii_lowercase, digits
import logging
import random
import sys


def generate_secret_key(max_length: int = 30, rounds: int = 12, prefix: str = "2b"):
    secret_key: str = r""

    for _ in range(1, max_length + 1):
        secret_key += random.choice([i for i in  ascii_lowercase + digits])

    return secret_key


def import_string(import_name: str):
    import_name = import_name.replace(":", ".")
    try:
        try:
            __import__(import_name)
            
        except ImportError:
            if "." not in import_name:
                raise
        else:
            return sys.modules[import_name]
        
        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])

        try:
            return getattr(module, obj_name)
        
        except AttributeError as e:
            raise ImportError(e) from None
        
    except ImportError as e:
        raise ImportError(e) from None



def check_installed_apps(app: Flask) -> list | None: 
    INSTALLED_APPS = None
    
    try:
        INSTALLED_APPS = app.config['INSTALLED_APPS']

    except Exception as e:
        logging.error(f"INSTALLED_APPS not found from {app.import_name}/settings.py")


    if INSTALLED_APPS is not None:
        if type(INSTALLED_APPS) == list:
            return INSTALLED_APPS
        
        else:
            raise TypeError(
                f"Type `{type(app.config['INSTALLED_APPS'])}` not allowed INSTALLED_APPS ."
                f"From {app.import_name}/settings.py"
            )
    else:
        logging.error(f"INSTALLED_APPS not found from {app.import_name}/settings.py")
