from framework.utils.nav_config import Nav

CONFIG = {
    "en": {},
    "ru": {}
}

def get_label(key):
    return CONFIG[Nav.LANG][key]